# RemNote Flashcard Builder

A Claude Code skill that converts markdown notes into RemNote-importable flashcards, selecting the optimal card type for each piece of information.

## Installation

Copy `SKILL.md` into your Claude Code skills directory:

**For all projects (personal):**
```bash
mkdir -p ~/.claude/skills/remnote-flashcard-builder
cp remnote-flashcard-builder-skill/SKILL.md ~/.claude/skills/remnote-flashcard-builder/SKILL.md
```

**For a specific project:**
```bash
mkdir -p <your-project>/.claude/skills/remnote-flashcard-builder
cp remnote-flashcard-builder-skill/SKILL.md <your-project>/.claude/skills/remnote-flashcard-builder/SKILL.md
```

The skill is automatically available once the file is in place.

## Usage

Provide a markdown file and ask Claude Code:

```
"Convert my biology notes to RemNote flashcards"
```

The skill reads the file, extracts every learnable fact, classifies it using a decision tree, and outputs a RemNote-ready markdown file.

## Card Types

| Type | Syntax | Use Case |
|------|--------|----------|
| Concept | `- **Term** :: Definition` | Named things with definitions |
| Descriptor | `- **attr** ;; value` | Attributes of concepts |
| Forward | `- **Q?** >> A` | Standard Q&A |
| Reverse | `- **desc** << Term` | Identification from description |
| Bidirectional | `- **A** <> B` | Symmetric pairs (abbreviations, symbols) |
| Cloze | `- Text with {{blank}}` | Fill-in-the-blank (proper nouns/terms only) |
| Multi-Line | `- **Q** >>>` + list | Short lists (3-8 items) |
| Multiple-Choice | `- **Q?** >>A) X B) Y` | Distinguishing between options |

## Quality Metrics (8 domains, iteration 5)

| Metric | Average |
|--------|---------|
| Completeness | 96.9% |
| Type evenness | 0.89 |
| Syntax correctness | 100% |
| Directionality | 93.5/100 |
| Unambiguity | 86.4/100 |
| Pedagogical depth | 98.8/100 |

Tested on: cell biology, Python, WWII, physics, calculus, economics, organic chemistry, Shakespeare.

## Project Structure

```
remnote-flashcard-builder-skill/SKILL.md  — Skill definition (decision tree + syntax)
evals/samples/                            — 8 test input files
workspace/iteration-5/                    — Current baseline outputs
workspace/quality_analysis.py             — 9-dimension eval tool
CLAUDE.md                                 — Dev instructions & eval workflow
```

See `CLAUDE.md` for the evaluation workflow.
