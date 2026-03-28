# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**remnote-flashcard-builder** is a production-ready Claude Code skill that converts markdown notes into RemNote-importable flashcards. **Latest version (v1.1)** includes bold emphasis on prompts, preserved markdown headers for organization, and bullet points for proper RemNote import. Complete and stable.

## Architecture

The skill uses a 7-question decision tree to classify each atomic fact into optimal RemNote card types:

1. **Distinguishing options?** → Multiple-Choice (`- **Q?** >>A) X B) Y...`)
2. **Named with definition?** → Concept (`- **Term** ::`)
3. **Attribute/property?** → Descriptor (`- **attribute** ;;`)
4. **Fact in sentence?** → Cloze (`- Text with {{blank}}` — no bold)
5. **Short list?** → Multi-Line (`- **Q** >>>`)
6. **Simple Q&A?** → Basic Forward/Reverse/Bidirectional (`- **Q** >>`, `- **D** <<`, `- **A** <>`)

**Output Features:**
- ✅ Bullet points on every card (` - `)
- ✅ Bold emphasis on questions/terms (except cloze)
- ✅ Preserved markdown headers for organization

See `remnote-flashcard-builder-skill/SKILL.md` for complete decision tree and syntax reference.

## Evaluation Workflow

Evaluations use a two-step process. **Do NOT use an Anthropic API key or external scripts** — everything runs through Claude Code directly.

### Step 1: Generate flashcards

Spawn Claude Code agents that read `remnote-flashcard-builder-skill/SKILL.md` as instructions and an input notes file, then write flashcard output. Example agent prompt:

> "You are a RemNote flashcard builder. Read the skill specification at `remnote-flashcard-builder-skill/SKILL.md` and the input notes at `evals/samples/<domain>-notes.md`. Follow the SKILL.md instructions EXACTLY. Write the output to `workspace/iteration-N/eval-X-<domain>/<domain>-notes-flashcards.md`."

Run up to 3 agents in parallel for different domains.

### Step 2: Evaluate outputs

**`workspace/quality_analysis.py`** validates skill outputs across 9 dimensions:

**Programmatic (1-6):** completeness (% facts covered), type distribution (entropy), duplication, syntax correctness, atomicity (one idea/card), clean output (no metadata).

**LLM-Judge (7-9):** answer unambiguity (cloze/MC), directionality appropriateness (>> vs << vs <>), pedagogical depth (cognitive levels).

```bash
# Single domain evaluation
python workspace/quality_analysis.py <notes_file> <flashcards_file> [--llm-judge]

# Compare two iterations
python workspace/quality_analysis.py <notes_file> <new_flashcards> <old_flashcards> --labels "New" "Old" [--llm-judge]
```

## Key Files

- **`remnote-flashcard-builder.skill`** — Production skill file (install in Claude Code)
- **`remnote-flashcard-builder-skill/SKILL.md`** — Skill source definition
- **`workspace/quality_analysis.py`** — Validation tool (9 dimensions)
- **`workspace/iteration-5/`** — Latest test results (8 domains)
- **`evals/samples/`** — Test data (8 domains: cell biology, Python, WWII, physics, calculus, economics, organic chemistry, Shakespeare)

## Status

Tested across 8 domains with iteration 5. Averages: 96.9% completeness, 0.89 evenness, 100% syntax, 93.5 directionality, 86.4 unambiguity, 98.8 pedagogical depth.
