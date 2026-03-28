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

## Testing & Quality Analysis

**`workspace/quality_analysis.py`** validates skill outputs across 9 dimensions:

**Programmatic (1-6):** completeness (% facts covered), type distribution (entropy), duplication, syntax correctness, atomicity (one idea/card), clean output (no metadata).

**LLM-Judge (7-9):** answer unambiguity (cloze/MC), directionality appropriateness (>> vs << vs <>), pedagogical depth (cognitive levels).

```bash
python workspace/quality_analysis.py <notes_file> <flashcards_file> [--llm-judge]
```

## Key Files

- **`remnote-flashcard-builder.skill`** — Production skill file v1.1 (install in Claude Code)
- **`remnote-flashcard-builder-skill/SKILL.md`** — Skill source definition (with bold + headers)
- **`workspace/quality_analysis.py`** — Validation tool (9 dimensions, updated for headers)
- **`workspace/iteration-4/`** — Latest test results (validated with bold + headers)
- **`RELEASE_NOTES.md`** — v1.1 release documentation and changes
- **`evals/samples/`** — Test data (cell biology, Python, WWII)

## Status

✅ **v1.1 Production Ready.** Tested across 3 domains with 205+ flashcards. All 9 quality dimensions validated (100% on syntax/completeness in iteration 4). See `RELEASE_NOTES.md` for iteration 4 changes.
