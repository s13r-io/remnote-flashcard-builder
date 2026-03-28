---
name: remnote-flashcard-builder
description: >
  Converts markdown notes into RemNote-importable flashcards. Use when the user
  wants to create flashcards, study material, or import notes into RemNote.
---

# RemNote Flashcard Builder

Converts any markdown notes file into RemNote-importable flashcards, selecting the optimal card type for each piece of information.

## Workflow

### 1. Read and Parse Input

Read the entire markdown file. Identify structure, headings, and all textual content. Preserve original meaning and context. Note all markdown headers (`#`, `##`, `###`, etc.) and which content falls under each—this section map will be used to group output cards by source section.

### 2. Extract Atomic Information Units

Break down content into every learnable, atomic piece of information:
- Definitions (named things with clear definitions)
- Attributes (properties or facts about those things)
- Facts (dates, names, formulae, events embedded in sentences)
- Lists (enumerated items forming a complete set)
- Relationships (paired associations: vocab, symbol-meaning, abbreviation-expansion)
- Processes (sequential steps, cause-effect)
- Distinctions (comparisons between similar items suitable for exam questions)

**Be exhaustive.** Extract every fact, even minor or obvious ones. Every fact is a potential flashcard.

### 3. Classify Using Decision Tree

For each atomic unit, apply these questions in order. Stop at the first match:

**Is this for DISTINGUISHING BETWEEN OPTIONS?** (comparing related terms, exam-style distinction)
-> **MULTIPLE-CHOICE** (`>>A) correct B) wrong C) wrong D) wrong`)

**Is this a NAMED THING with a DEFINITION?** (term, concept, entity, theory, condition)
-> **CONCEPT** (`::`)

**Is this an ATTRIBUTE or PROPERTY of a concept?** (origin, creator, date, key feature)
-> **DESCRIPTOR** (`;;`) — needs a parent concept; if none, use Basic or Cloze instead

**Is this a SPECIFIC FACT within a SENTENCE where context aids recall?** (date, name, formula in natural sentence)
-> **CLOZE** (`{{ }}`) — blank must have exactly one correct answer; rewrite if sentence gives away the answer

**Is this a SHORT LIST (3-8 items) answering a single question?**
-> **MULTI-LINE** (`>>>`)

**Is this SIMPLE Q&A?** Pick direction:
- **Reverse** (`<<`) if you encounter the ANSWER in practice and need to identify what it represents (given symptoms -> name condition; given property -> name the thing)
- **Bidirectional** (`<>`) if recall needed BOTH directions (vocab pairs, symbol-name, abbreviation-expansion)
- **Forward** (`>>`) by default (question -> answer)

**Still unsure?** Default to **FORWARD BASIC** (`>>`).

### 3.5 Organize by Section

Before generating output, group your classified cards by their source markdown section. Preserve the original header hierarchy. Cards without a clear header belong in a general section at the top.

## Card Types: Syntax and Examples

- **Concept**: `- **Term** :: Definition` — `- **Mitochondria** :: Membrane-bound organelle that produces ATP via oxidative phosphorylation`
- **Descriptor**: `- **attribute** ;; value` — `- **origin** ;; Ancient endosymbiotic event with alpha-proteobacterium`
- **Forward**: `- **Q?** >> A` — `- **What year did WWII end?** >> 1945`
- **Reverse**: `- **description** << Term` — `- **Describe: fever, neck stiffness, photophobia** << Meningitis`
- **Bidirectional**: `- **A** <> B` — `- **Fe** <> Iron`
- **Cloze**: `- sentence with {{blank}}` — `- The {{thylakoid membrane}} is where light-dependent reactions occur.` (No bold—{{ }} is the visual anchor)
- **Multi-Line**: `- **Q** >>>` then list items on separate lines — `- **Three branches of US government** >>>` / `Executive` / `Legislative` / `Judicial`
- **Multiple-Choice**: `- **Q?** >>A) correct B) wrong C) wrong D) wrong` — `- **Which organelle produces ATP?** >>A) Mitochondria B) Ribosome C) Golgi apparatus D) Nucleus`

## Principles

1. **Exhaustiveness**: Extract EVERY learnable fact. Don't skip minor or obvious information.
2. **Atomic units**: One idea per flashcard. Don't combine multiple concepts.
3. **Type variety**: Use at least 5-6 different card types per document. Avoid all-Basic decks.
4. **Exam prep emphasis**: Lean toward Multiple-Choice whenever content allows distinguishing between plausible options.
5. **Unambiguity**: Cloze blanks and MC questions must have exactly one correct answer.
6. **Minimize redundancy**: If two cards test the same fact, use different types or angles.
7. **Read first**: Read the whole source before classifying to understand context and relationships.
8. **Bold the prompt**: Wrap the question, term, or identifying part of each card in `**bold**`. This makes cards scannable during review—the eye lands on what needs to be answered. Skip cloze cards (the {{ }} blank already serves this purpose).

## Example Transformation

**Input (markdown):**
```markdown
## Photosynthesis Overview

Photosynthesis is the process by which green plants convert sunlight,
water, and carbon dioxide into glucose and oxygen. It occurs in two main
stages: the light-dependent reactions and the light-independent reactions
(Calvin cycle). The light-dependent reactions occur in the thylakoid
membrane and produce ATP and NADPH. The Calvin cycle occurs in the stroma.
```

**Output (flashcards):**
```
## Photosynthesis Overview

- **Photosynthesis** :: The process by which green plants convert sunlight, water, and carbon dioxide into glucose and oxygen
- **light-dependent reactions** ;; Occur in the thylakoid membrane and produce ATP and NADPH
- **Calvin cycle** ;; Also called light-independent reactions, occurs in the stroma
- **Photosynthesis occurs in how many main stages?** >> Two: light-dependent reactions and light-independent reactions (Calvin cycle)
- The {{thylakoid membrane}} is where the light-dependent reactions of photosynthesis occur.
- The {{stroma}} is where the Calvin cycle occurs in plant cells.
```

## Output

- Write ONLY flashcard syntax to `[input-filename]-flashcards.md` in the same directory as the input
- **Preserve markdown headers** — Include the original source section headers (e.g., `## Historical Background`) before the flashcards that belong to that section
- **Each flashcard must start with a bullet point (`- `)** to ensure proper import into RemNote
- **Bold the prompt** — Wrap the question/term/identifying part in `**bold**` (except for cloze cards where {{ }} is the visual anchor)
- One flashcard per line (multi-line and MC cards may span multiple lines after the bullet)
- No metadata, comments, or explanatory text
