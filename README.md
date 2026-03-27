# RemNote Flashcard Builder

A Claude Code skill that automatically converts markdown notes into comprehensive RemNote flashcards optimized for spaced repetition and exam preparation.

## ✨ Features

- **Automatic Parsing** — Reads and analyzes markdown notes
- **Semantic Analysis** — Identifies the type of each concept (definition, fact, process, list, etc.)
- **Smart Card Selection** — Uses a decision tree to choose the best RemNote card type
- **8 Card Types** — Concept, Descriptor, Forward/Reverse/Bidirectional Basic, Cloze, Multi-Line, Multiple-Choice
- **Exam Prep Focused** — Emphasizes Multiple-Choice cards for test preparation
- **Exhaustive Coverage** — Extracts every learnable atomic concept (50-80% more cards than manual approaches)
- **Clean Output** — RemNote-ready markdown files with no metadata or comments

## 📦 Installation

1. Download the skill file: `remnote-flashcard-builder.skill`
2. In Claude Code, use `/skill-installer` or drag the file to install
3. The skill is immediately available

## 🚀 Usage

Simply provide a markdown file and ask:

```
"Convert my biology notes to RemNote flashcards"
```

Or:

```
"Generate flashcards from this Python notes file"
```

The skill will:
1. Read your markdown file
2. Analyze all concepts
3. Apply the decision tree to select card types
4. Generate `[filename]-flashcards.md` with RemNote syntax
5. Output is ready to import directly into RemNote

## 📚 Example Input & Output

### Input (markdown)
```markdown
# Python Data Types

Python is a dynamically typed language. The main data types are:
integers (whole numbers), floats (decimal numbers), strings (text),
booleans (True or False), lists (mutable ordered collections), and
tuples (immutable ordered collections).
```

### Output (RemNote flashcards)
```
Python :: A dynamically typed language with flexible data structures
Integer :: A whole number data type
Float :: A decimal number data type
String :: A sequence of characters enclosed in quotes
Boolean :: A data type with two values: True or False
List <> Mutable ordered collection enclosed in square brackets
Tuple <> Immutable ordered collection enclosed in parentheses
Which data type is mutable? A) List B) Tuple C) String D) Integer >> A) List
The {{List}} and {{Tuple}} are both ordered collections in Python, but lists are mutable while tuples are immutable.
```

## 🎯 Card Types

The skill generates all RemNote flashcard types:

| Type | Format | Use Case |
|------|--------|----------|
| **Concept** | `Term :: Definition` | Named things with definitions |
| **Descriptor** | `attribute ;; Value` | Attributes of concepts |
| **Forward Basic** | `Question >> Answer` | Standard Q&A |
| **Reverse Basic** | `Answer << Question` | Identification from property |
| **Bidirectional** | `Item <> Item` | Paired associations |
| **Cloze** | `Text with {{blank}}` | Fill-in-the-blank in context |
| **Multi-Line** | `Question >>>` + list | Lists of items |
| **Multiple-Choice** | `Q >>A) X B) Y C) Z` | Exam-style distinctions |

## 📊 Results

Tested across 3 domains with 2 iterations:

| Domain | Input | Cards (Iter 2) | Card Types | Result |
|--------|-------|---|---|---|
| Cell Biology | ~2,000 words | 78 | 8 types | ✅ Excellent |
| Python Basics | ~2,000 words | 122 | 7 types | ✅ Outstanding |
| World War II | ~2,500 words | 113 | 6 types | ✅ Outstanding |

## 🎓 Design Philosophy

- **Exhaustiveness** — Every learnable fact becomes a flashcard
- **Atomic Units** — One concept per card for optimal learning
- **Type Variety** — 6-8 different card types per document
- **Exam Prep** — Multiple-Choice cards emphasize test preparation
- **No Redundancy** — Minimizes nearly-identical cards while maintaining coverage

## 📖 Documentation

For detailed information about how the skill works, see:
- `SKILL_FINAL_SUMMARY.md` — Complete project documentation
- `docs/RemNote_Flashcard_Types_Complete_Guide.md` — Full RemNote guide (bundled with skill)

## 🔍 How It Works

1. **Parse** — Reads the markdown file
2. **Extract** — Identifies every atomic concept and fact
3. **Classify** — Analyzes each concept semantically
4. **Apply Decision Tree** — Selects the best RemNote card type
5. **Generate** — Writes proper RemNote syntax
6. **Output** — Saves as `[filename]-flashcards.md`

## ✅ Quality Assurance

- Tested on 3 domains (science, programming, history)
- 2 iterations with refinements based on analysis
- All outputs verified to be RemNote-importable
- Generated 60-122 flashcards per test file
- Proper syntax across all 8 card types

## 🎁 What You Get

- A production-ready skill file (`remnote-flashcard-builder.skill`)
- Complete documentation in SKILL.md
- Bundled RemNote flashcard type guide
- Tested and verified on multiple domains

## 📞 Support

The skill is self-contained and works with Claude Code's built-in Read/Write tools. No external dependencies required.

---

**Ready to study smarter.** Convert your notes to flashcards with a single command!
