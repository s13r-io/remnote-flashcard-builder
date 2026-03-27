---
name: remnote-flashcard-builder
description: >
  Generates RemNote-importable flashcards from a markdown notes file.
  Use this skill whenever the user wants to convert notes, study material,
  or any markdown content into RemNote flashcards for spaced repetition,
  or wants to import their notes into RemNote. Perfect for exam preparation,
  learning from lecture notes, or turning research into study decks. Always use
  this skill when the user mentions notes, markdown files, RemNote, flashcards,
  spaced repetition, or wanting to create study material from existing content.
compatibility:
  - Read tool (to read markdown files)
  - Write tool (to output flashcard files)
---

# RemNote Flashcard Builder

This skill converts any markdown notes file into a collection of RemNote-importable flashcards, automatically selecting the best card type for each piece of information.

## Workflow

### 1. Read and Parse the Input File

When the user provides a markdown file path:
- Read the entire file content
- Identify the structure and all textual content
- Preserve the original meaning and context

### 2. Extract Atomic Information Units

Break down the markdown content into every learnable, atomic piece of information:
- **Definitions** — Named things with clear definitions (concepts, terms, entities)
- **Attributes** — Specific properties or facts about those things
- **Facts** — Specific information embedded in sentences (dates, names, formulae, events)
- **Lists** — Enumerated items that form a complete set
- **Relationships** — Paired associations (vocabulary, symbol↔meaning, abbreviation↔expansion)
- **Processes** — Sequential steps or cause-effect relationships
- **Questions** — Direct Q&A that could form multiple-choice or basic cards

Be exhaustive. Extract information that might seem minor or obvious — every fact is a potential flashcard.

### 3. Classify Using the Decision Tree

For each atomic unit, apply the decision tree from `references/flashcard-guide.md` to determine the best card type. Reference the tree in order:

#### Is the knowledge **VISUAL or SPATIAL**?
→ **Skip Image Occlusion** (not in scope). If visual content references exist, note them as context but don't create image cards.

#### Is this for **DISTINGUISHING BETWEEN OPTIONS**?
(E.g., comparing related terms, identifying the correct choice among plausible alternatives, exam-style distinction)
→ **Use MULTIPLE-CHOICE** (`>>A) ... B) ... C) ...`)

#### Is this a **NAMED THING with a DEFINITION**?
(Term, concept, entity, theory, condition, technology)
→ **Use CONCEPT** (`::`)

#### Is this an **ATTRIBUTE or PROPERTY** of a concept?
(A fact about that thing: its origin, creator, date, key feature, etc.)
→ **Use DESCRIPTOR** (`;;`)
*Note: Descriptors work best when you have a parent concept to attach to. If there's no clear parent concept, convert to a Basic or Cloze card instead.*

#### Is this a **SPECIFIC FACT within a SENTENCE** where context is how you'd naturally encounter it?
(Date, name, formula, term, or fact embedded in a natural sentence)
→ **Use CLOZE** (`{{ }}`)
*Check: Does the surrounding sentence give away the answer? If yes, rewrite to avoid answer leakage. Cloze blanks must have exactly one correct answer.*

#### Is this a **SHORT LIST** (3–8 items) in response to a single question?
(A well-defined, canonical list)
→ **Use MULTI-LINE** (`>>>`)

#### Is this **SIMPLE Q&A**?
(A factual question where you need to recall an answer)
→ **Use BASIC CARD**, but pick the direction carefully:
- **Reverse** (`<<`) if you'll encounter the ANSWER in practice and need to identify what it represents (e.g., given property/symptom/characteristic, name it). Examples: "Which is immutable? << Tuple", "What causes this? << Meningitis"
- **Bidirectional** (`<>`) if you need recall in BOTH directions (vocab pairs, symbol↔name, abbreviation↔expansion, paired associations)
- **Forward** (`>>`) by default (question→answer, the most common direction)

**Direction Selection Tips:**
- If phrased as "What/When/Where/Who/How is...", likely Forward (`>>`)
- If asking to identify/name something from its property or characteristic, use Reverse (`<<`)
- If it's a paired association with equal importance both ways, use Bidirectional (`<>`)

#### Still unsure?
→ Default to **FORWARD BASIC** (`>>`). You can always adjust later.

### 4. Generate RemNote Syntax

Write each flashcard using the correct RemNote syntax:

- **Concept**: `Term :: Full definition and explanation`
- **Descriptor**: `attribute ;; Specific value or fact about the parent concept`
- **Forward Basic**: `Question >> Answer`
- **Reverse Basic**: `Answer << Question`
- **Bidirectional Basic**: `Item <> Associated item`
- **Cloze**: `Sentence with {{hidden word}} and more context.`
- **Multi-Line**: `Question >>>` followed by list items on separate lines
- **Multiple-Choice**: `Question >>A) Correct answer B) Wrong option C) Wrong option D) Wrong option`

### 5. Output

- Write a clean markdown file (no metadata, no comments, just syntax)
- Name it `[input-filename]-flashcards.md`
- Place it in the same directory as the input file
- File should contain ONLY flashcard syntax, one flashcard per line (or multi-line for Multi-Line and Multiple-Choice cards)

## Important Principles

**Exhaustiveness**: Extract every learnable fact. Break down all concepts into atomic units. Don't skip information just because it seems minor, obvious, or redundant to you—the user will see all these facts when studying and needs flashcards for them all.

**Atomic Units**: One flashcard per idea. Don't combine multiple concepts into one card. If you write the same fact twice slightly differently, that's OK—it serves different learning angles.

**Minimize True Redundancy**: Avoid creating nearly identical flashcards with the same answer. If you find two Q&A pairs that are too similar, consider using different card types or angles (e.g., turn one into Multiple-Choice or Reverse format).

**Clarity**: Ensure every flashcard is clear, unambiguous, and has exactly one intended answer (especially for cloze and multiple-choice).

**Type Variety**: Aim for a good mix of card types—at least 5-6 different types per document. A deck of all Basic cards (`>>`) is monotonous and less effective than mixing Concepts, Descriptors, Cloze, Multiple-Choice, Bidirectional, and Multi-Line cards.

**Answer Unambiguity**: For cloze and multiple-choice, ensure the correct answer is unambiguous. If multiple answers are valid, reframe the card or break it into multiple cards.

**Exam Prep Emphasis**: Since these flashcards are for examination preparation, lean toward Multiple-Choice cards whenever content allows distinguishing between plausible options. These directly prepare learners for test conditions.

## Example Transformation

**Input (markdown):**
```markdown
# Photosynthesis

Photosynthesis is the process by which green plants convert sunlight,
water, and carbon dioxide into glucose and oxygen. It occurs in two main
stages: the light-dependent reactions and the light-independent reactions
(Calvin cycle). The light-dependent reactions occur in the thylakoid
membrane and produce ATP and NADPH. The Calvin cycle occurs in the stroma.
```

**Output (flashcards):**
```
Photosynthesis :: The process by which green plants convert sunlight, water, and carbon dioxide into glucose and oxygen
light-dependent reactions ;; Occur in the thylakoid membrane and produce ATP and NADPH
Calvin cycle ;; Also called light-independent reactions, occurs in the stroma
Photosynthesis occurs in how many main stages? >> Two: light-dependent reactions and light-independent reactions (Calvin cycle)
The {{thylakoid membrane}} is where the light-dependent reactions of photosynthesis occur.
The {{stroma}} is where the Calvin cycle occurs in plant cells.
```

## Tips for Best Results

1. **Read the whole source first** before classifying. Understand the context and relationships.
2. **Look for explicit definitions** — these are almost always Concept cards.
3. **Look for lists** — enumerated items or "X, Y, and Z" often become Multi-Line cards.
4. **Look for comparisons** — these often become Bidirectional or **Multiple-Choice cards**. If the content involves distinguishing between similar items, properties, or concepts (e.g., "String vs List vs Tuple mutability", "Which battle happened first"), strongly consider Multiple-Choice cards for exam prep.
5. **Look for processes** — sequential steps might be Cloze cards if embedded in a sentence, or Basic cards if meant as Q&A.
6. **Reuse context** — if you've created a Concept card for "Photosynthesis," subsequent facts about it become Descriptor cards nested under it conceptually (though you won't explicitly nest them since output is flat).
7. **Check cloze answers** — ensure the blank has exactly one right answer, not multiple valid options.
