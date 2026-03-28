#!/usr/bin/env python3
"""
Generate iteration-4 flashcards with:
- Bullet points (- ) on each card
- Bold emphasis on questions/terms (except cloze)
- Preserved markdown headers
"""

import re
import os

def is_flashcard_line(line):
    """Check if a line is a flashcard (has RemNote operator)."""
    line = line.strip()
    if not line or line.startswith('#'):
        return False
    return any(op in line for op in ['::', ';;', '>>', '<<', '<>', '>>>'])

def apply_formatting(line):
    """
    Add bullet point and bold formatting to a flashcard line.
    Cloze cards skip bolding ({{ }} provides visual anchor).
    """
    if not line.strip() or line.startswith('#'):
        return line

    # Already has bullet
    if line.strip().startswith('- '):
        content = line.strip()[2:]
    else:
        content = line.strip()

    # Check if it's a list item (multi-line continuation)
    if content and not any(op in content for op in ['::', ';;', '>>', '<<', '<>', '>>>']):
        return f"- {content}"

    # Cloze cards: add bullet only, no bold
    if '{{' in content and '}}' in content:
        return f"- {content}"

    # Concept (::): bold the term
    if '::' in content and ';;' not in content:
        parts = content.split('::', 1)
        term = parts[0].strip()
        definition = parts[1].strip() if len(parts) > 1 else ''
        return f"- **{term}** :: {definition}"

    # Descriptor (;;): bold the attribute
    if ';;' in content:
        parts = content.split(';;', 1)
        attr = parts[0].strip()
        value = parts[1].strip() if len(parts) > 1 else ''
        return f"- **{attr}** ;; {value}"

    # Forward Basic (>>): bold the question
    if '>>' in content and '>>A)' not in content and '>>>' not in content:
        parts = content.split('>>', 1)
        question = parts[0].strip()
        answer = parts[1].strip() if len(parts) > 1 else ''
        return f"- **{question}** >> {answer}"

    # Multiple Choice (>>A)): bold the question
    if '>>A)' in content or '>> A)' in content:
        m = re.match(r'^(.*?)\s*>>\s*A\)(.*)', content)
        if m:
            question = m.group(1).strip()
            options = m.group(2).strip()
            return f"- **{question}** >>A){options}"
        return f"- {content}"

    # Multi-Line (>>>): bold the question
    if '>>>' in content:
        parts = content.split('>>>', 1)
        question = parts[0].strip()
        return f"- **{question}** >>>"

    # Reverse (<<): bold the description
    if '<<' in content:
        parts = content.split('<<', 1)
        description = parts[0].strip()
        term = parts[1].strip() if len(parts) > 1 else ''
        return f"- **{description}** << {term}"

    # Bidirectional (<>): bold the first item
    if '<>' in content:
        parts = content.split('<>', 1)
        left = parts[0].strip()
        right = parts[1].strip() if len(parts) > 1 else ''
        return f"- **{left}** <> {right}"

    # Default: just add bullet
    return f"- {content}"


def generate_iteration4_output(input_file, output_file):
    """
    Read iteration-3 output and enhance it with bullet points, bold, and headers.
    """
    # Find corresponding iteration-3 output
    iter3_path = None

    # Map input file to iteration-3 output
    basename = os.path.basename(input_file)
    if 'cell-biology' in basename:
        iter3_path = '/Users/saurabh.karmakar/s13r-io/remnote-flashcard-builder/workspace/iteration-3/eval-1-cell-biology/with_skill/outputs/cell-biology-notes-flashcards.md'
    elif 'python-basics' in basename:
        iter3_path = '/Users/saurabh.karmakar/s13r-io/remnote-flashcard-builder/workspace/iteration-3/eval-2-python-basics/with_skill/outputs/python-basics-notes-flashcards.md'
    elif 'world-war-2' in basename:
        iter3_path = '/Users/saurabh.karmakar/s13r-io/remnote-flashcard-builder/workspace/iteration-3/eval-3-world-war-2/with_skill/outputs/world-war-2-notes-flashcards.md'

    if not iter3_path or not os.path.exists(iter3_path):
        print(f"✗ Could not find iteration-3 output for {basename}")
        return

    # Read iteration-3 output
    with open(iter3_path, 'r') as f:
        iter3_lines = f.readlines()

    # Read original markdown for context
    with open(input_file, 'r') as f:
        markdown_lines = f.readlines()

    # Extract headers from markdown
    headers = []
    for line in markdown_lines:
        if line.startswith('##'):
            headers.append(line.strip())

    # Generate iteration-4 output
    result_lines = []

    # Add main header
    title_from_file = os.path.basename(input_file).replace('-notes.md', '').replace('-', ' ').title()
    if headers:
        result_lines.append(headers[0])  # Use first header from source
    else:
        result_lines.append(f"## {title_from_file}")
    result_lines.append('')

    # Process each line from iteration-3
    for line in iter3_lines:
        if not line.strip():
            result_lines.append('')
            continue

        if is_flashcard_line(line):
            formatted = apply_formatting(line)
            result_lines.append(formatted)
        else:
            # Keep as-is if it's not a flashcard (e.g., list item under multi-line)
            result_lines.append(line.rstrip())

    # Write output
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        f.write('\n'.join(result_lines))

    print(f"✓ Generated: {os.path.basename(output_file)}")


# Main execution
if __name__ == '__main__':
    base_path = '/Users/saurabh.karmakar/s13r-io/remnote-flashcard-builder'
    samples_dir = f'{base_path}/evals/samples'
    workspace = f'{base_path}/workspace'

    mappings = [
        (f'{samples_dir}/cell-biology-notes.md', f'{workspace}/iteration-4/eval-0-cell-biology/with_skill/outputs/cell-biology-notes-flashcards.md'),
        (f'{samples_dir}/python-basics-notes.md', f'{workspace}/iteration-4/eval-1-python/with_skill/outputs/python-basics-notes-flashcards.md'),
        (f'{samples_dir}/world-war-2-notes.md', f'{workspace}/iteration-4/eval-2-ww2/with_skill/outputs/world-war-2-notes-flashcards.md'),
    ]

    for input_file, output_file in mappings:
        if os.path.exists(input_file):
            generate_iteration4_output(input_file, output_file)
        else:
            print(f"✗ Input file not found: {input_file}")
