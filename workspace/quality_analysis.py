#!/usr/bin/env python3
"""
Quality analysis for RemNote flashcard builder skill outputs.

Measures 9 dimensions across programmatic and LLM-based evaluation:

Programmatic (dimensions 1-6):
  1. Completeness — fact-level coverage of source material
  2. Type Distribution — evenness of card type usage (Shannon entropy)
  3. Duplication — near-duplicate detection within card types
  4. Syntactic Correctness — valid RemNote syntax for each card type
  5. Atomicity — one idea per card (flags overly long/compound cards)
  6. Clean Output — no metadata, headers, or non-flashcard content

LLM-Judge (dimensions 7-9, requires --llm-judge flag):
  7. Answer Unambiguity — cloze/MC cards have exactly one correct answer
  8. Directionality Appropriateness — card direction matches knowledge type
  9. Pedagogical Depth — deck tests recall at multiple cognitive levels

Usage:
    python quality_analysis.py <notes_file> <flashcards_file> [--label LABEL]
    python quality_analysis.py <notes_file> <new> <old> --labels "New" "Old"
    python quality_analysis.py <notes_file> <flashcards_file> --llm-judge
"""

import argparse
import json
import math
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict


# ---------------------------------------------------------------------------
# Fact extraction
# ---------------------------------------------------------------------------

def extract_key_facts(notes_path):
    """Extract key facts from each section of source notes."""
    with open(notes_path) as f:
        content = f.read()

    sections = []
    current_section = None
    current_text = []

    for line in content.split('\n'):
        if line.startswith('## '):
            if current_section:
                sections.append((current_section, '\n'.join(current_text)))
            current_section = line.replace('## ', '').strip().rstrip('?')
            current_text = []
        elif current_section and line.strip():
            current_text.append(line.strip())
    if current_section:
        sections.append((current_section, '\n'.join(current_text)))

    result = []
    for section_name, text in sections:
        facts = set()

        # Dates
        for m in re.finditer(r'\b(1[0-9]{3}|20[0-9]{2})\b', text):
            facts.add(m.group())
        for m in re.finditer(
            r'(?:January|February|March|April|May|June|July|August|'
            r'September|October|November|December)\s+\d{1,2},?\s+\d{4}', text
        ):
            facts.add(m.group())

        # Multi-word proper nouns
        for m in re.finditer(r'[A-Z][a-z]+(?:\s+[A-Z][a-z]+)+', text):
            phrase = m.group()
            if phrase.split()[0] not in ('The', 'This', 'These', 'That', 'There',
                                         'Each', 'Both', 'When', 'Unlike', 'Common',
                                         'An', 'Its', 'Inside'):
                facts.add(phrase)

        # Single capitalized terms (not at sentence start)
        for m in re.finditer(r'\b([A-Z][a-z]{2,})\b', text):
            word = m.group()
            if word not in ('The', 'This', 'These', 'That', 'There', 'Each',
                           'Both', 'When', 'Unlike', 'Common', 'Additionally',
                           'Major', 'Several', 'Britain', 'France'):
                idx = m.start()
                if idx > 0 and text[idx - 1] not in '.!?\n':
                    facts.add(word)

        # Numbers
        for m in re.finditer(r'\b(\d[\d,.-]+)\b', text):
            num = m.group()
            if len(num) >= 2 and num not in ('10', '11', '12'):
                facts.add(num)

        # Parenthesized / quoted terms
        for m in re.finditer(r'[("](.*?)[)"]', text):
            term = m.group(1).strip()
            if 2 < len(term) < 50:
                facts.add(term)

        result.append((section_name, list(facts)))
    return result


# ---------------------------------------------------------------------------
# Card classification
# ---------------------------------------------------------------------------

def classify_card(line):
    """Classify a flashcard line by type. Returns (type, parts_dict)."""
    line = line.strip()
    if not line:
        return None, {}

    if '>>A)' in line.replace(' ', '') or '>> A)' in line:
        # Multiple choice: Q >>A) correct B) wrong C) wrong D) wrong
        m = re.match(r'^(.+?)\s*>>\s*A\)\s*(.+)', line)
        if m:
            return 'multiple_choice', {'question': m.group(1), 'options': m.group(2)}
        return 'multiple_choice', {'raw': line}

    if '>>>' in line:
        parts = line.split('>>>', 1)
        return 'multi_line', {'question': parts[0].strip(), 'items': parts[1].strip() if len(parts) > 1 else ''}

    if '::' in line and ';;' not in line:
        parts = line.split('::', 1)
        return 'concept', {'term': parts[0].strip(), 'definition': parts[1].strip() if len(parts) > 1 else ''}

    if ';;' in line:
        parts = line.split(';;', 1)
        return 'descriptor', {'attribute': parts[0].strip(), 'value': parts[1].strip() if len(parts) > 1 else ''}

    if '{{' in line and '}}' in line:
        return 'cloze', {'sentence': line}

    if '<>' in line:
        parts = line.split('<>', 1)
        return 'bidirectional', {'left': parts[0].strip(), 'right': parts[1].strip() if len(parts) > 1 else ''}

    if '<<' in line:
        parts = line.split('<<', 1)
        return 'reverse', {'answer': parts[0].strip(), 'question': parts[1].strip() if len(parts) > 1 else ''}

    if '>>' in line:
        parts = line.split('>>', 1)
        return 'forward', {'question': parts[0].strip(), 'answer': parts[1].strip() if len(parts) > 1 else ''}

    return 'other', {'raw': line}


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def normalize(text):
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()


def jaccard_similarity(a, b):
    wa = set(normalize(a).split())
    wb = set(normalize(b).split())
    if not wa or not wb:
        return 0
    return len(wa & wb) / len(wa | wb)


def word_count(text):
    return len(text.split())


# ---------------------------------------------------------------------------
# Dimension 4: Syntactic Correctness
# ---------------------------------------------------------------------------

def check_syntax(lines):
    """Validate RemNote syntax for each card. Returns (issues, total_checked)."""
    issues = []

    # Pre-scan to find multi-line card ranges (>>> cards followed by list items)
    multiline_item_lines = set()
    for i, line in enumerate(lines):
        ctype, _ = classify_card(line)
        if ctype == 'multi_line':
            # Mark subsequent lines as list items until we hit another card type
            for j in range(i + 1, len(lines)):
                next_type, _ = classify_card(lines[j])
                if next_type == 'other':
                    multiline_item_lines.add(j)
                else:
                    break

    for i, line in enumerate(lines, 1):
        ctype, parts = classify_card(line)
        if ctype is None:
            continue

        if ctype == 'other':
            # Skip if this is a markdown header (intentional organizational output)
            if re.match(r'^#{1,6}\s', line.strip()):
                continue
            # Skip if this is a list item under a multi-line card
            if (i - 1) in multiline_item_lines:
                continue
            issues.append({
                'line': i,
                'type': 'unrecognized',
                'card': line[:80],
                'issue': 'No recognized RemNote syntax operator found'
            })
            continue

        if ctype == 'concept':
            if not parts.get('term'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing term before ::'})
            if not parts.get('definition'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing definition after ::'})

        elif ctype == 'descriptor':
            if not parts.get('attribute'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing attribute before ;;'})
            if not parts.get('value'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing value after ;;'})

        elif ctype == 'forward':
            if not parts.get('question'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing question before >>'})
            if not parts.get('answer'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing answer after >>'})

        elif ctype == 'reverse':
            if not parts.get('answer'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing answer/description before <<'})
            if not parts.get('question'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing term/identifier after <<'})

        elif ctype == 'bidirectional':
            if not parts.get('left'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing left side before <>'})
            if not parts.get('right'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing right side after <>'})

        elif ctype == 'cloze':
            blanks = re.findall(r'\{\{(.*?)\}\}', line)
            if not blanks:
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Cloze syntax detected but no {{blank}} found'})
            for blank in blanks:
                if not blank.strip():
                    issues.append({'line': i, 'type': ctype, 'card': line[:80],
                                   'issue': 'Empty cloze blank {{}}'})

        elif ctype == 'multiple_choice':
            raw = line
            # Check for at least A) and B) options
            if not re.search(r'A\)', raw):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing option A) (correct answer)'})
            if not re.search(r'B\)', raw):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing option B)'})
            # Check question exists before >>
            q_match = re.match(r'^(.+?)\s*>>', raw)
            if not q_match or not q_match.group(1).strip():
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing question before >>A)'})

        elif ctype == 'multi_line':
            if not parts.get('question'):
                issues.append({'line': i, 'type': ctype, 'card': line[:80],
                               'issue': 'Missing question before >>>'})

    return issues


# ---------------------------------------------------------------------------
# Dimension 5: Atomicity
# ---------------------------------------------------------------------------

def check_atomicity(lines):
    """Flag cards that likely contain multiple ideas.

    Heuristics:
    - Answer/definition side > 30 words (too much for one card)
    - Contains "and" joining two independent clauses in the answer
    - Contains semicolons separating multiple facts in non-list context
    """
    issues = []
    WORD_LIMIT = 30

    for i, line in enumerate(lines, 1):
        ctype, parts = classify_card(line)
        if ctype is None or ctype == 'other':
            continue

        # Determine the "answer" portion to check
        answer = ''
        if ctype == 'concept':
            answer = parts.get('definition', '')
        elif ctype == 'descriptor':
            answer = parts.get('value', '')
        elif ctype == 'forward':
            answer = parts.get('answer', '')
        elif ctype == 'reverse':
            answer = parts.get('answer', '')  # the description side
        elif ctype == 'bidirectional':
            answer = parts.get('right', '')
        elif ctype == 'cloze':
            answer = parts.get('sentence', '')
        elif ctype == 'multiple_choice':
            answer = parts.get('options', '')
        elif ctype == 'multi_line':
            continue  # multi-line cards are inherently multi-item

        wc = word_count(answer)
        if wc > WORD_LIMIT:
            issues.append({
                'line': i,
                'type': ctype,
                'card': line[:80],
                'word_count': wc,
                'issue': f'Answer side has {wc} words (>{WORD_LIMIT}) — may contain multiple ideas'
            })

        # Check for compound answers with "and" joining clauses
        # Pattern: "X and Y" where both X and Y are substantial (>5 words each)
        if ctype in ('concept', 'forward', 'descriptor'):
            and_parts = re.split(r'\band\b', answer)
            if len(and_parts) >= 2:
                substantial = [p for p in and_parts if word_count(p.strip()) >= 5]
                if len(substantial) >= 2:
                    issues.append({
                        'line': i,
                        'type': ctype,
                        'card': line[:80],
                        'issue': 'May combine multiple concepts joined by "and"'
                    })

    return issues


# ---------------------------------------------------------------------------
# Dimension 6: Clean Output
# ---------------------------------------------------------------------------

def check_clean_output(content, lines):
    """Check for metadata, headers, comments, or non-flashcard content."""
    issues = []

    # HTML comments
    html_comments = re.findall(r'<!--.*?-->', content, re.DOTALL)
    if html_comments:
        issues.append({'issue': f'Contains {len(html_comments)} HTML comment(s)',
                       'examples': [c[:60] for c in html_comments[:3]]})

    # NOTE: Markdown headers are now EXPECTED output for organization
    # They are intentional, not metadata, so we skip flagging them

    # Blank lines between cards (not a problem per se, but indicates possible metadata)
    # Pre-scan multi-line item ranges
    multiline_item_lines = set()
    for idx, ln in enumerate(lines):
        ct, _ = classify_card(ln)
        if ct == 'multi_line':
            for j in range(idx + 1, len(lines)):
                nt, _ = classify_card(lines[j])
                if nt == 'other':
                    multiline_item_lines.add(j)
                else:
                    break

    # Check for explanatory text (lines with no RemNote operator)
    for i, line in enumerate(lines, 1):
        ctype, _ = classify_card(line)
        if ctype == 'other' and (i - 1) not in multiline_item_lines:
            # Skip markdown headers (they are intentional organizational output)
            if re.match(r'^#{1,6}\s', line.strip()):
                continue
            issues.append({'issue': f'Line {i}: No RemNote syntax — possible metadata or stray text',
                           'examples': [line[:60]]})

    return issues


# ---------------------------------------------------------------------------
# Main analysis
# ---------------------------------------------------------------------------

def analyze(notes_path, flashcards_path, label=None):
    """Run full quality analysis on a flashcard output."""
    section_facts = extract_key_facts(notes_path)

    with open(flashcards_path) as f:
        content = f.read()
    lines = [l.strip() for l in content.strip().split('\n') if l.strip()]
    all_text = content.lower()

    # === 1. COMPLETENESS ===
    section_results = []
    total_facts = 0
    covered_facts = 0
    for section_name, facts in section_facts:
        section_covered = 0
        section_missing = []
        for fact in facts:
            if fact.lower() in all_text:
                section_covered += 1
            else:
                section_missing.append(fact)
        total_facts += len(facts)
        covered_facts += section_covered
        pct = (section_covered / len(facts) * 100) if facts else 100
        section_results.append({
            'name': section_name,
            'total_facts': len(facts),
            'covered': section_covered,
            'missing': section_missing,
            'coverage_pct': pct
        })
    overall_completeness = (covered_facts / total_facts * 100) if total_facts > 0 else 100

    # === 2. TYPE DISTRIBUTION ===
    type_counts = Counter()
    cards_by_type = defaultdict(list)
    for line in lines:
        ctype, _ = classify_card(line)
        if ctype and ctype != 'other':
            type_counts[ctype] += 1
            cards_by_type[ctype].append(line)

    total_cards = sum(type_counts.values())
    entropy = 0
    for count in type_counts.values():
        p = count / total_cards
        if p > 0:
            entropy -= p * math.log2(p)
    max_entropy = math.log2(len(type_counts)) if type_counts else 0
    evenness = entropy / max_entropy if max_entropy > 0 else 0
    dominant = type_counts.most_common(1)[0] if type_counts else ('none', 0)
    dominant_pct = (dominant[1] / total_cards * 100) if total_cards > 0 else 0

    # === 3. DUPLICATION ===
    duplicates = []
    for ctype, cards in cards_by_type.items():
        for i in range(len(cards)):
            for j in range(i + 1, len(cards)):
                sim = jaccard_similarity(cards[i], cards[j])
                if sim > 0.7:
                    duplicates.append({
                        'type': ctype,
                        'card_a': cards[i][:80],
                        'card_b': cards[j][:80],
                        'similarity': f'{sim:.0%}'
                    })

    # === 4. SYNTACTIC CORRECTNESS ===
    syntax_issues = check_syntax(lines)

    # === 5. ATOMICITY ===
    atomicity_issues = check_atomicity(lines)

    # === 6. CLEAN OUTPUT ===
    clean_issues = check_clean_output(content, lines)

    result = {
        'label': label or flashcards_path,
        'completeness': {
            'overall_pct': round(overall_completeness, 1),
            'total_facts': total_facts,
            'covered_facts': covered_facts,
            'sections': section_results
        },
        'distribution': {
            'total_cards': total_cards,
            'types_used': len(type_counts),
            'evenness': round(evenness, 3),
            'entropy': round(entropy, 2),
            'max_entropy': round(max_entropy, 2),
            'dominant_type': dominant[0],
            'dominant_pct': round(dominant_pct, 1),
            'type_counts': dict(type_counts.most_common())
        },
        'duplication': {
            'count': len(duplicates),
            'items': duplicates
        },
        'syntax': {
            'issues_count': len(syntax_issues),
            'total_checked': len(lines),
            'pass_rate': round((1 - len(syntax_issues) / max(len(lines), 1)) * 100, 1),
            'issues': syntax_issues
        },
        'atomicity': {
            'issues_count': len(atomicity_issues),
            'total_checked': total_cards,
            'pass_rate': round((1 - len(atomicity_issues) / max(total_cards, 1)) * 100, 1),
            'issues': atomicity_issues
        },
        'clean_output': {
            'issues_count': len(clean_issues),
            'is_clean': len(clean_issues) == 0,
            'issues': clean_issues
        }
    }

    return result


# ---------------------------------------------------------------------------
# LLM Judge (dimensions 7-9)
# ---------------------------------------------------------------------------

LLM_JUDGE_PROMPT = """You are a flashcard quality evaluator. Analyze these RemNote flashcards generated from source notes and evaluate three dimensions. Be strict but fair.

## SOURCE NOTES:
{notes}

## FLASHCARDS TO EVALUATE:
{flashcards}

## EVALUATION DIMENSIONS

### 7. Answer Unambiguity
For each cloze card ({{blank}}) and multiple-choice card (>>A)...):
- Does the blank have exactly ONE correct answer in context?
- For MC: is the correct answer clearly correct, and are distractors plausible but wrong?
Rate: count of problematic cards vs total cloze+MC cards.

### 8. Directionality Appropriateness
For each basic card (>>, <<, <>):
- Forward (>>) should be used for standard Q&A where you encounter the question naturally
- Reverse (<<) should be used when you encounter the answer/description and need to identify what it is
- Bidirectional (<>) should be used for paired associations where recall is needed both ways (vocab, symbols, abbreviations)
Rate: count of cards with wrong direction vs total basic cards.

### 9. Pedagogical Depth
Does the deck as a whole test knowledge at multiple cognitive levels?
- Surface recall (definitions, dates) — basic cards, concept cards
- Contextual recall (facts in sentences) — cloze cards
- Discrimination (choosing between similar options) — MC cards
- Identification (recognizing from description) — reverse cards
- Association (paired concepts) — bidirectional cards
Rate: how many cognitive levels are exercised (out of 5)?

## OUTPUT FORMAT (respond with ONLY this JSON, no other text):
{{
  "unambiguity": {{
    "score": <0-100>,
    "total_checked": <number of cloze+MC cards>,
    "problematic_count": <number with ambiguity issues>,
    "issues": [
      {{"card": "<card text truncated to 80 chars>", "issue": "<what's ambiguous>"}}
    ]
  }},
  "directionality": {{
    "score": <0-100>,
    "total_checked": <number of basic cards (>>, <<, <>)>,
    "wrong_direction_count": <number with wrong direction>,
    "issues": [
      {{"card": "<card text truncated to 80 chars>", "issue": "<why direction is wrong>"}}
    ]
  }},
  "pedagogical_depth": {{
    "score": <0-100>,
    "levels_present": ["<list of cognitive levels exercised>"],
    "levels_missing": ["<list of cognitive levels not exercised>"],
    "notes": "<brief assessment of pedagogical quality>"
  }}
}}"""


def run_llm_judge(notes_path, flashcards_path):
    """Run LLM-based evaluation using claude CLI."""
    with open(notes_path) as f:
        notes = f.read()
    with open(flashcards_path) as f:
        flashcards = f.read()

    prompt = LLM_JUDGE_PROMPT.format(notes=notes, flashcards=flashcards)

    try:
        result = subprocess.run(
            ['claude', '-p', prompt, '--output-format', 'text'],
            capture_output=True, text=True, timeout=120
        )
        if result.returncode != 0:
            return {'error': f'claude CLI failed: {result.stderr[:200]}'}

        output = result.stdout.strip()
        # Extract JSON from response
        json_match = re.search(r'\{[\s\S]*\}', output)
        if json_match:
            return json.loads(json_match.group())
        return {'error': f'Could not parse JSON from LLM response: {output[:200]}'}

    except FileNotFoundError:
        return {'error': 'claude CLI not found. Install Claude Code or use --no-llm-judge.'}
    except subprocess.TimeoutExpired:
        return {'error': 'LLM judge timed out (120s)'}
    except json.JSONDecodeError as e:
        return {'error': f'Invalid JSON from LLM: {e}'}


# ---------------------------------------------------------------------------
# Printing
# ---------------------------------------------------------------------------

def print_report(r, llm_result=None):
    """Print a human-readable report."""
    print(f'\n{"=" * 70}')
    print(f'  {r["label"]}')
    print(f'{"=" * 70}')

    # 1. Completeness
    c = r['completeness']
    print(f'\n--- 1. COMPLETENESS ({c["overall_pct"]:.0f}% — {c["covered_facts"]}/{c["total_facts"]} facts) ---')
    for s in c['sections']:
        icon = '+' if s['coverage_pct'] >= 80 else ('~' if s['coverage_pct'] >= 50 else 'X')
        print(f'  [{icon}] {s["name"]}: {s["covered"]}/{s["total_facts"]} facts ({s["coverage_pct"]:.0f}%)')
        if s['missing']:
            print(f'      Missing: {", ".join(s["missing"][:5])}{"..." if len(s["missing"]) > 5 else ""}')

    # 2. Distribution
    d = r['distribution']
    print(f'\n--- 2. TYPE DISTRIBUTION (evenness: {d["evenness"]:.2f}/1.00) ---')
    for ctype, count in sorted(d['type_counts'].items(), key=lambda x: -x[1]):
        pct = count / d['total_cards'] * 100
        bar = '#' * int(pct / 2)
        print(f'  {ctype:18s} {count:3d} ({pct:4.1f}%) {bar}')
    print(f'  Dominant: {d["dominant_type"]} at {d["dominant_pct"]:.0f}% | '
          f'Entropy: {d["entropy"]:.2f}/{d["max_entropy"]:.2f}')

    # 3. Duplication
    dup = r['duplication']
    print(f'\n--- 3. DUPLICATION ({dup["count"]} near-duplicates) ---')
    if dup['items']:
        for item in dup['items']:
            print(f'  [{item["type"]}] {item["similarity"]} overlap:')
            print(f'    A: {item["card_a"]}')
            print(f'    B: {item["card_b"]}')
    else:
        print('  None found (>70% word overlap threshold)')

    # 4. Syntax
    sx = r['syntax']
    print(f'\n--- 4. SYNTACTIC CORRECTNESS ({sx["pass_rate"]:.0f}% — {sx["issues_count"]} issues in {sx["total_checked"]} cards) ---')
    if sx['issues']:
        for issue in sx['issues'][:5]:
            print(f'  Line {issue["line"]} [{issue["type"]}]: {issue["issue"]}')
            print(f'    Card: {issue["card"]}')
        if len(sx['issues']) > 5:
            print(f'  ... and {len(sx["issues"]) - 5} more')
    else:
        print('  All cards have valid syntax')

    # 5. Atomicity
    at = r['atomicity']
    print(f'\n--- 5. ATOMICITY ({at["pass_rate"]:.0f}% — {at["issues_count"]} issues in {at["total_checked"]} cards) ---')
    if at['issues']:
        for issue in at['issues'][:5]:
            print(f'  Line {issue["line"]} [{issue["type"]}]: {issue["issue"]}')
            print(f'    Card: {issue["card"]}')
        if len(at['issues']) > 5:
            print(f'  ... and {len(at["issues"]) - 5} more')
    else:
        print('  All cards are atomic (single idea per card)')

    # 6. Clean output
    cl = r['clean_output']
    status = 'CLEAN' if cl['is_clean'] else f'{cl["issues_count"]} issues'
    print(f'\n--- 6. CLEAN OUTPUT ({status}) ---')
    if cl['issues']:
        for issue in cl['issues'][:5]:
            print(f'  {issue["issue"]}')
            if issue.get('examples'):
                for ex in issue['examples'][:2]:
                    print(f'    > {ex}')
    else:
        print('  No metadata, headers, or non-flashcard content')

    # LLM Judge dimensions (7-9)
    if llm_result and 'error' not in llm_result:
        # 7. Unambiguity
        ua = llm_result.get('unambiguity', {})
        print(f'\n--- 7. ANSWER UNAMBIGUITY (score: {ua.get("score", "N/A")}/100) ---')
        print(f'  Checked: {ua.get("total_checked", "?")} cloze+MC cards, '
              f'{ua.get("problematic_count", "?")} problematic')
        for issue in ua.get('issues', [])[:3]:
            print(f'  ! {issue.get("card", "")[:70]}')
            print(f'    {issue.get("issue", "")}')

        # 8. Directionality
        di = llm_result.get('directionality', {})
        print(f'\n--- 8. DIRECTIONALITY (score: {di.get("score", "N/A")}/100) ---')
        print(f'  Checked: {di.get("total_checked", "?")} basic cards, '
              f'{di.get("wrong_direction_count", "?")} wrong direction')
        for issue in di.get('issues', [])[:3]:
            print(f'  ! {issue.get("card", "")[:70]}')
            print(f'    {issue.get("issue", "")}')

        # 9. Pedagogical Depth
        pd = llm_result.get('pedagogical_depth', {})
        print(f'\n--- 9. PEDAGOGICAL DEPTH (score: {pd.get("score", "N/A")}/100) ---')
        print(f'  Levels present: {", ".join(pd.get("levels_present", []))}')
        if pd.get('levels_missing'):
            print(f'  Levels missing: {", ".join(pd.get("levels_missing", []))}')
        if pd.get('notes'):
            print(f'  Assessment: {pd["notes"]}')

    elif llm_result and 'error' in llm_result:
        print(f'\n--- LLM JUDGE: SKIPPED ({llm_result["error"]}) ---')


def print_comparison(results, llm_results=None):
    """Print side-by-side comparison."""
    print(f'\n\n{"=" * 70}')
    print('  COMPARISON SUMMARY')
    print(f'{"=" * 70}')

    col_width = 22
    print(f'\n{"Metric":<28}', end='')
    for r in results:
        print(f'{r["label"][:20]:>{col_width}}', end='')
    print()
    print('-' * (28 + col_width * len(results)))

    rows = [
        ('1. Completeness', lambda r: f'{r["completeness"]["overall_pct"]:.0f}%'),
        ('2. Evenness (0-1)', lambda r: f'{r["distribution"]["evenness"]:.2f}'),
        ('   Dominant type %', lambda r: f'{r["distribution"]["dominant_pct"]:.0f}%'),
        ('   Types used', lambda r: f'{r["distribution"]["types_used"]}'),
        ('3. Duplicates', lambda r: f'{r["duplication"]["count"]}'),
        ('4. Syntax pass rate', lambda r: f'{r["syntax"]["pass_rate"]:.0f}%'),
        ('5. Atomicity pass rate', lambda r: f'{r["atomicity"]["pass_rate"]:.0f}%'),
        ('6. Clean output', lambda r: 'Yes' if r["clean_output"]["is_clean"] else 'No'),
        ('   Total cards', lambda r: f'{r["distribution"]["total_cards"]}'),
    ]

    for label, fn in rows:
        print(f'{label:<28}', end='')
        for r in results:
            print(f'{fn(r):>{col_width}}', end='')
        print()

    # LLM scores if available
    if llm_results:
        llm_rows = [
            ('7. Unambiguity', lambda lr: f'{lr.get("unambiguity", {}).get("score", "N/A")}/100'),
            ('8. Directionality', lambda lr: f'{lr.get("directionality", {}).get("score", "N/A")}/100'),
            ('9. Pedagogical Depth', lambda lr: f'{lr.get("pedagogical_depth", {}).get("score", "N/A")}/100'),
        ]
        print()
        for label, fn in llm_rows:
            print(f'{label:<28}', end='')
            for lr in llm_results:
                if lr and 'error' not in lr:
                    print(f'{fn(lr):>{col_width}}', end='')
                else:
                    print(f'{"N/A":>{col_width}}', end='')
            print()


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description='Quality analysis for RemNote flashcards')
    parser.add_argument('notes', help='Path to source notes markdown file')
    parser.add_argument('flashcards', nargs='+', help='Path(s) to flashcard output file(s)')
    parser.add_argument('--labels', nargs='+', help='Labels for each flashcard file')
    parser.add_argument('--json', action='store_true', help='Output JSON instead of text')
    parser.add_argument('--llm-judge', action='store_true', help='Run LLM-based evaluation (dims 7-9)')
    args = parser.parse_args()

    labels = args.labels or [f'Output {i + 1}' for i in range(len(args.flashcards))]
    if len(labels) < len(args.flashcards):
        labels.extend([f'Output {i + 1}' for i in range(len(labels), len(args.flashcards))])

    results = []
    llm_results = []

    for path, label in zip(args.flashcards, labels):
        r = analyze(args.notes, path, label)
        results.append(r)

        if args.llm_judge:
            print(f'  Running LLM judge for {label}...', file=sys.stderr)
            lr = run_llm_judge(args.notes, path)
            llm_results.append(lr)
        else:
            llm_results.append(None)

    if args.json:
        output = []
        for r, lr in zip(results, llm_results):
            entry = dict(r)
            if lr:
                entry['llm_judge'] = lr
            output.append(entry)
        print(json.dumps(output, indent=2))
    else:
        for r, lr in zip(results, llm_results):
            print_report(r, lr)
        if len(results) > 1:
            valid_llm = [lr for lr in llm_results if lr] or None
            print_comparison(results, llm_results if valid_llm else None)


if __name__ == '__main__':
    main()
