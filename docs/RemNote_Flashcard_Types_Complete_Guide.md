# The Complete Guide to RemNote Flashcard Types

## Purpose, Examples, Non-Examples, and a Decision Tree for Choosing the Right Card

---

## Why Card Type Matters

Not all knowledge is shaped the same way. A vocabulary word, an anatomy diagram, and a multi-step process each demand a different kind of recall. RemNote offers seven distinct card types precisely because choosing the right container for your knowledge dramatically affects how deeply and durably you learn it. Research on spaced repetition consistently shows that active recall — being forced to retrieve an answer rather than passively re-reading it — is one of the strongest evidence-based learning strategies available. But active recall only works well when the *prompt* matches the *shape* of what you need to remember. A poorly chosen card type can lead to shallow pattern-matching, where you recognise the card rather than truly remembering the concept.

This guide walks through every RemNote card type, explains when and why to use it, and — just as importantly — explains when *not* to use it. At the end, you'll find a decision-tree cheat sheet you can reference whenever you sit down to make new cards.

---

## 1. Basic Cards

### What They Are

Basic cards are the classic two-sided flashcard: a **prompt** (front) and an **answer** (back). You type the prompt, then `>>` or `==`, then the answer. They are the bread-and-butter of any spaced-repetition system.

What makes RemNote's Basic cards powerful is that they come in **three directional variants**, and picking the right direction is just as important as writing a good prompt.

---

### 1A. Forward Basic Card (`>>`)

**How it works:** You see the prompt (front), and you must recall the answer (back).

**When to use it:** Use a Forward Basic card whenever you need to recall a specific piece of information in response to a question, and you do *not* need to work backwards (i.e., you won't be given the answer and asked to identify what question it answers). This is the most common direction for factual Q&A learning.

**Good Examples:**

- `What year did World War II end? >> 1945` — You'll encounter this as a question in exams and conversations. You need to go from the question to the year, not the other way around.
- `What is the chemical formula for water? >> H₂O` — Knowing "H₂O" and needing to name the compound is a separate skill (that would need a reverse card). Here you're going from name to formula.
- `What is the capital of Australia? >> Canberra` — Geography trivia almost always flows from "what is the capital of X?" You rarely need to go from "Canberra" to "which country's capital is this?"
- `What does the HTTP status code 404 mean? >> Not Found` — As a developer, you encounter the code and need to recall its meaning, not the other way around.
- `What enzyme breaks down starch in the mouth? >> Salivary amylase` — In a biology exam, the question will be phrased this way.

**Non-Examples (don't use Forward Basic for these):**

- *Learning French vocabulary (e.g., "dog >> chien")* — Language vocabulary almost always needs to work both ways. You need to recall "chien" when you see "dog," but you also need to recall "dog" when you hear "chien." A bidirectional card is better here.
- *Memorising a complex definition you need to understand from multiple angles* — If you're studying "Mitochondria >> The powerhouse of the cell, responsible for ATP production via oxidative phosphorylation," a Concept card would be better because it structures the knowledge and auto-generates both directions.
- *Learning the steps of a process* — "Steps of cellular respiration >> Glycolysis, Krebs cycle, Electron transport chain" is too much information for one side of a basic card. A multi-line card or cloze deletions within a paragraph would serve you better.
- *Studying anatomy from a labelled diagram* — The spatial relationship matters. An Image Occlusion card would be far more effective.

---

### 1B. Reverse Basic Card (`<<`)

**How it works:** You see the answer (back), and you must recall the prompt (front). The card is flipped — what was originally written as the answer is now shown as the question.

**When to use it:** Use a Reverse Basic card when the *answer* is what you'll encounter in practice, and you need to identify or name what it represents. This is common in diagnostic, classification, and recognition tasks.

**Good Examples:**

- `Describe the symptoms: fever, neck stiffness, photophobia << Meningitis` — In a clinical setting, you encounter the symptoms and need to name the condition. You see "Meningitis" on the front and must recall what symptoms it presents with.
- `What law states: for every action, there is an equal and opposite reaction? << Newton's Third Law` — You see "Newton's Third Law" and need to state what it says. Useful when you'll encounter the name in a textbook and need to explain it.
- `What programming paradigm treats computation as evaluation of mathematical functions? << Functional programming` — You'll see the term "functional programming" in job interviews and need to define it on the spot.
- `Reddish-brown gas with a pungent odour, commonly produced in combustion << Nitrogen dioxide (NO₂)` — In a chemistry lab, you might observe the gas and need to identify it from its physical properties.

**Non-Examples (don't use Reverse Basic for these):**

- *Standard factual Q&A like "What is the speed of light?"* — The natural direction is forward: you encounter the question and need the number. A reverse card would show you "3 × 10⁸ m/s" and ask you what that represents, which is rarely how you'd be tested.
- *Vocabulary where you need production, not just recognition* — If you're learning to speak Spanish and need to say "mesa" when you see a table, you need a forward card (English → Spanish), not a reverse one.
- *Anything where the "answer" side is too long or complex to serve as a useful prompt* — If the back of your card is a three-sentence explanation, showing that paragraph and asking "what concept is this?" creates an unfocused, frustrating card.

---

### 1C. Bidirectional Basic Card (`<>`)

**How it works:** Two separate cards are generated from one note — one forward, one reverse. Each is scheduled independently in the spaced-repetition queue.

**When to use it:** Use bidirectional cards whenever the knowledge genuinely needs to flow in both directions — you need to go from A to B *and* from B to A. This is the gold standard for paired associations where neither side is inherently the "question."

**Good Examples:**

- `Dog <> Perro` (English-Spanish vocabulary) — You need to produce "perro" when you see "dog" AND recognise "dog" when you hear "perro." Both directions are essential for language fluency.
- `Fe <> Iron` (Chemical symbols) — You need to know that Fe stands for Iron, and that Iron's symbol is Fe. Both directions appear in chemistry problems.
- `Mozart <> Composed "The Magic Flute"` — In a music history course, you might be asked "Who composed The Magic Flute?" or "What did Mozart compose?" Both directions are fair game.
- `TCP <> Transmission Control Protocol` — You encounter the abbreviation and need the full name, but you also read the full name and need to recall the abbreviation.
- `Hypotenuse <> The longest side of a right triangle, opposite the right angle` — In geometry, you need to go from the word to the definition and vice versa.

**Non-Examples (don't use Bidirectional Basic for these):**

- *One-directional factual questions* — "What year was the Eiffel Tower built? <> 1889" creates an unnecessary reverse card that asks "What happened in 1889?" which is absurdly broad and impossible to answer uniquely.
- *When the answer is a long explanation* — "Photosynthesis <> The process by which green plants convert sunlight, water, and CO₂ into glucose and oxygen using chlorophyll" creates a reverse card with a wall of text as the prompt. Use a Concept card instead.
- *Procedural knowledge* — "How do you tie a bowline knot? <> Make a loop, pass the end through, go around the standing part, and back through the loop" — the reverse card (showing the steps and asking "what knot?") is trivially easy because of the specific phrasing. This doesn't test anything useful in reverse.

---

## 2. Concept Cards

### What They Are

Concept cards are designed to define *things* — named entities, ideas, or terms. You type the concept name, then `::`, then its definition. The concept name appears in **bold**, and by default, flashcards are generated in **both directions** (bidirectional). Concepts can also be used as forward-only (`:>`) or reverse-only (`:<`).

The key difference from Basic cards is semantic: Concept cards tell RemNote that this item is a "thing" in your knowledge base. This enables features like cross-referencing, linking, and better note organisation. When studying, concept cards also hide the back side of the parent concept from child cards, preventing answer leakage.

### When to Use Concept Cards

Use Concept cards for any named thing that has a definition — technical terms, scientific entities, historical figures, theories, legal doctrines, medical conditions, programming concepts, or any noun-like idea that you need to both define and recognise.

**Good Examples:**

- `Mitochondria :: The membrane-bound organelle responsible for producing ATP through oxidative phosphorylation` — A named biological structure with a clear definition. You need to define it AND recognise the definition.
- `Habeas Corpus :: A legal principle requiring that a detained person be brought before a court to determine whether their detention is lawful` — A legal term you'll encounter by name and by description.
- `Kubernetes :: An open-source container orchestration platform that automates deployment, scaling, and management of containerised applications` — A technology you'll see referenced by name and by what it does.
- `Cognitive Dissonance :: The mental discomfort experienced when holding two contradictory beliefs, values, or attitudes simultaneously` — A psychology term with a precise definition.
- `Renaissance :: A cultural and intellectual movement originating in 14th-century Italy, characterised by renewed interest in classical Greek and Roman art, literature, and philosophy` — A historical period with a definable meaning.

**Non-Examples (don't use Concept cards for these):**

- *Questions that aren't about defining a "thing"* — "What year did the Renaissance begin?" is a factual question, not a concept definition. Use a Basic card.
- *Attributes or properties of a concept* — "The Renaissance → originated in Italy" describes a property of the Renaissance, not the Renaissance itself. Use a Descriptor card nested under the Renaissance concept.
- *Process steps or procedures* — "How does Kubernetes deploy a container?" is a process question, not a definition. Use a Basic card or Cloze.
- *Subjective or opinion-based content* — "Best programming language :: Python" is not a factual concept definition.
- *Very long, multi-paragraph definitions* — If the definition is so long it can't be recalled as a unit, break it into a Concept card for the core definition plus Descriptor cards for the details.

---

## 3. Descriptor Cards

### What They Are

Descriptor cards describe a specific **attribute or property** of a parent Concept. They are created by typing the attribute name, then `;;`, then its value. The attribute name appears in *italics*. By default, they generate a card only in the **forward direction**, though you can make them reverse (`;<`) or bidirectional (`;<>`).

Descriptors always live *underneath* a Concept in the outline hierarchy. When you study a Descriptor card, RemNote shows the parent Concept as context, so the question becomes: "For [Concept], what is [attribute]?"

### When to Use Descriptor Cards

Use Descriptor cards when you already have a Concept card and you need to memorise specific facts, attributes, or details about that concept. They are perfect for structured, hierarchical knowledge.

**Good Examples (all nested under their parent Concept):**

Under **Mitochondria ::**
- `origin ;; Thought to have originated from an ancient endosymbiotic event with an alpha-proteobacterium`
- `number of membranes ;; Two (outer and inner, with cristae on the inner membrane)`
- `key function ;; Produces ATP through oxidative phosphorylation`

Under **Python (programming language) ::**
- `creator ;; Guido van Rossum`
- `year first released ;; 1991`
- `typing system ;; Dynamically typed, strongly typed`

Under **French Revolution ::**
- `key trigger ;; Storming of the Bastille on July 14, 1789`
- `lasted until ;; 1799, when Napoleon seized power`
- `major document produced ;; Declaration of the Rights of Man and of the Citizen`

**Non-Examples (don't use Descriptor cards for these):**

- *Standalone facts without a parent concept* — "The Bastille was stormed in 1789" has no parent concept to attach to. Use a Basic card unless you first create a Concept card for the French Revolution.
- *The definition of the concept itself* — The definition belongs in the Concept card (`French Revolution :: ...`), not in a Descriptor.
- *Content that doesn't naturally fit as an "attribute: value" pair* — "Explain why the French Revolution was significant" is an essay question, not an attribute. Use a Basic card.
- *Isolated trivia not connected to a larger knowledge structure* — If you just want to remember one fact about Python and don't plan to build out a knowledge tree, a simple Basic card is less overhead.

---

## 4. Cloze (Fill-in-the-Blank) Cards

### What They Are

Cloze cards work completely differently from the card types above. Instead of defining two sides, you write a full sentence or paragraph and then **hide specific words or phrases** (called "occlusions" or "cloze deletions"). During practice, you see the sentence with blanks and must fill in the missing parts.

Create them by selecting text and pressing `{`, or by typing `{{` before the text to hide and `}}` after. You can have multiple occlusions in the same note, and choose whether all blanks are hidden at once or each is tested individually on separate cards.

### When to Use Cloze Cards

Cloze cards shine when the **context surrounding the answer** is what triggers your memory in real life. They are excellent for factual statements, formulae embedded in sentences, specific terminology within a sentence, and quotes you need to memorise.

**Good Examples:**

- `In {{1957}}, the {{Soviet Union}} launched the world's first artificial satellite, {{Sputnik 1}}.` — Three separate cards are generated, each testing one piece of information within a rich factual sentence.
- `The three states of matter are {{solid}}, {{liquid}}, and {{gas}}.` — You're drilling a list within its natural context sentence.
- `The powerhouse of the cell is the {{mitochondria}}.` — Quick drill of a key term embedded in its defining sentence.
- `In Python, a {{list}} is mutable while a {{tuple}} is immutable.` — Testing a comparison within its natural context, so you remember which is which.
- `The formula for the area of a circle is {{πr²}}.` — Mathematical formulae within a sentence are natural cloze candidates.

**Non-Examples (don't use Cloze cards for these):**

- *Defining a concept from scratch* — If you need to recall what mitochondria *are* without any sentence prompt, a cloze card won't test that skill. The surrounding sentence hands you too much context. Use a Concept card.
- *When the surrounding sentence gives away the answer* — "The process of {{photosynthesis}} converts sunlight into chemical energy in plants" is too easy because the description essentially is the definition. You'll pattern-match rather than truly recall.
- *Open-ended questions* — "Why did Rome fall? {{Because of economic instability, military overextension, and barbarian invasions}}" doesn't work because the answer is too long, there are many valid phrasings, and cloze cards expect a specific word or phrase.
- *When you're building a structured knowledge base* — Cloze cards don't create named concepts or searchable, cross-referenceable notes. If you're building notes you'll use for years, Concept/Descriptor cards make your notes more useful long-term.
- *When ambiguity is unavoidable* — "The {{president}} signed the bill" has dozens of valid answers. Cloze cards need unambiguous blanks with only one correct answer.

### A Word of Caution

Research by Andy Matuschak and others notes that cloze deletions can produce shallower understanding than well-crafted question-answer pairs. The specific wording of the sentence can make it artificially easy to recall the answer during review. In real life, you won't have that sentence as a cue. For best results, use cloze cards as a *supplement* to other card types, not as your sole method. They are, however, the fastest cards to create, which matters when you're covering a lot of material quickly.

---

## 5. Multi-Line Cards

### What They Are

Multi-line cards are a variant of Basic, Concept, or Descriptor cards where the **back side contains a short list of items** rather than a single answer. You create them by typing the trigger character three times (e.g., `>>>` for a forward multi-line Basic card) or by pressing Enter after typing it twice. You can reveal all items at once or flip through them one by one.

### When to Use Multi-Line Cards

Use them when you need to recall a small, bounded list of items associated with a single prompt — and the items are individually meaningful enough to be worth testing.

**Good Examples:**

- `What are the three branches of the US government? >>>` followed by: Executive, Legislative, Judicial — A well-defined list with a clear, finite number of items.
- `Symptoms of diabetes mellitus >>>` followed by: Polyuria, Polydipsia, Polyphagia, Unexplained weight loss — A clinical checklist where each item matters independently.
- `SOLID principles in software engineering >>>` followed by: Single Responsibility, Open/Closed, Liskov Substitution, Interface Segregation, Dependency Inversion — An acronym-based list that you need to enumerate completely.
- `Primary colours of light >>>` followed by: Red, Green, Blue — A short, definitive list.

**Non-Examples (don't use Multi-Line cards for these):**

- *Lists with 15+ items* — A multi-line card with the names of all US presidents would be overwhelmingly long. Break it into smaller groups or use a different strategy altogether.
- *Ordered processes where sequence matters as much as content* — The steps of CPR must be recalled in order and performed as a sequence. A cloze card embedding the steps in a procedural sentence, or a series of individual Basic cards for each step, would be better.
- *When each item needs its own detailed explanation* — If each list item has sub-details you also need to memorise, create separate Concept/Descriptor cards for each item instead.
- *Subjective or variable-length lists* — "Benefits of exercise" could include dozens of valid answers. Multi-line cards work best with canonical, closed lists.

---

## 6. Multiple-Choice Cards

### What They Are

Multiple-choice cards show a question and several possible answers, with one (or more) marked as correct. You create them by typing a question, then `>>A)`, followed by the answer options. Answer A is correct by default; the options are shuffled during review.

### When to Use Multiple-Choice Cards

RemNote explicitly warns that multiple-choice cards should **not** be your primary learning method. They are most valuable for targeted exam preparation when the exam itself will be multiple-choice. They help you practice the skill of *distinguishing* between plausible options under test conditions.

**Good Examples:**

- Preparing for a medical licensing exam (USMLE) with a bank of practice questions that mimic the actual test format.
- Studying for a multiple-choice certification exam (AWS, PMP, bar exam) using sample questions from practice tests.
- Practising distinction between easily confused terms: "Which of the following is a function of the liver? A) Produces bile, B) Produces insulin, C) Filters blood cells, D) Produces surfactant" — testing your ability to distinguish organs' functions.
- Reviewing common misconceptions: "Which planet is closest to the Sun? A) Mercury, B) Venus, C) Mars, D) Earth" — when you know students commonly confuse the answer.

**Non-Examples (don't use Multiple-Choice cards for these):**

- *General-purpose learning of new material* — Multiple-choice questions let you recognise the right answer among options, which is much easier than producing the answer from memory. This creates a false sense of mastery.
- *Deep understanding of concepts* — Recognising that "Mitochondria" is the correct answer from four options is nothing like being able to explain what mitochondria do and why they matter.
- *Material where the distractors are too obviously wrong* — If three of your four options are absurd and the answer is obvious by elimination, you're not learning anything.
- *Topics where you need free recall* — In a job interview, no one gives you four options. If you need to explain Kubernetes from scratch, multiple-choice practice won't prepare you.
- *As a replacement for all other card types* — These should be a small supplement, mixed with Basic, Concept, and Cloze cards for a well-rounded study strategy.

---

## 7. Image Occlusion Cards

### What They Are

Image Occlusion cards work like cloze deletions, but for images instead of text. You upload an image (a diagram, map, chart, or photo), then cover specific parts of it with opaque rectangles. During review, you see the image with the selected area hidden and must recall what's underneath.

RemNote offers two modes: **Hide All, Test One** (all labels are hidden; you're tested on one at a time) and **Hide One, Test One** (only the tested label is hidden; the rest remain visible as context).

### When to Use Image Occlusion Cards

Use them whenever **spatial relationships** or **visual recognition** are central to what you need to learn. They are overwhelmingly popular in medical and STEM education for good reason.

**Good Examples:**

- **Anatomy:** A diagram of the heart with labels for each chamber, valve, and vessel. You hide all labels and test yourself on each one. Knowing *where* the mitral valve is, not just what it's called, is the whole point.
- **Geography:** A map of Europe where country borders are visible but country names are hidden. You see the shape and location and must name the country.
- **Chemistry:** A diagram of the Krebs cycle where specific molecules or enzymes at each step are hidden. You need to recall what happens at each stage within its visual context.
- **Circuit diagrams:** An electronics schematic where component names or values are hidden. You need to identify components by their visual symbols and position.
- **Histology slides:** Microscope images where cell structures or tissue types are labelled. You hide the labels and identify structures by appearance.

**Non-Examples (don't use Image Occlusion for these):**

- *Text-only content with no visual or spatial component* — If the information is purely verbal (definitions, dates, names), a Basic or Concept card is simpler and more effective. Don't force an image where none is needed.
- *Images where the labels are too small or blurry to read* — Low-quality images create frustrating, unproductive cards. Always use clear, high-resolution source material.
- *Diagrams with 30+ labels crammed together* — Covering everything creates a chaotic, overwhelming review experience. Best practice is to start with 4–6 occlusions per card and work up to 8–10 max. Beyond that, split into multiple cards.
- *Conceptual understanding that doesn't depend on spatial location* — Knowing the *function* of the mitochondria doesn't require an image. Knowing *where it is inside a cell diagram* does. Match the card type to the skill being tested.
- *Photos of text or screenshots of paragraphs* — If the "image" is just a photo of text, convert it to actual text and use Cloze or Basic cards instead.

---

## Best Practices Across All Card Types

**1. One atomic idea per card.** Each card should test exactly one thing. Complex cards with multiple sub-items lead to frustration, repeated forgetting of the hardest sub-item, and artificially short review intervals.

**2. Understand before you memorise.** Never make a card for something you don't understand. The spaced-repetition algorithm can help you remember the words, but if you don't grasp the concept, you'll just be memorising meaningless strings.

**3. Keep it concise.** Shorter prompts and answers are easier to review and harder to pattern-match. Trim unnecessary words ruthlessly.

**4. Use personal connections.** The Self-Reference Effect means you remember things that relate to your own life better. If you can add a personal mnemonic or a relatable example (even a ridiculous one) to the back of a card, do it.

**5. Combine card types strategically.** The best study decks use a mix: Concept cards for definitions, Descriptors for attributes, Cloze cards for quick reinforcement of specific terms, and Image Occlusion for visual content. No single card type covers all learning needs.

**6. Review regularly.** Spaced repetition only works if you show up. Even 15 minutes daily is vastly more effective than a 3-hour cram session once a week.

---

## Decision Tree Cheat Sheet: Choosing the Right Card Type

Use the following questions in sequence. Stop at the first match.

```
START HERE
│
├─ Is the knowledge primarily VISUAL or SPATIAL?
│  (Diagrams, maps, anatomy, circuits, charts)
│  │
│  YES → Use IMAGE OCCLUSION
│  │     Hide All/Test One for pure labelling
│  │     Hide One/Test One for contextual recall
│  │
│  NO ↓
│
├─ Are you preparing for a MULTIPLE-CHOICE EXAM
│  using a specific question bank?
│  │
│  YES → Use MULTIPLE-CHOICE CARDS
│  │     (Supplement with other types; don't rely solely on MCQs)
│  │
│  NO ↓
│
├─ Is the knowledge a NAMED THING with a DEFINITION?
│  (A term, concept, entity, theory, condition, tool)
│  │
│  YES → Use a CONCEPT CARD (::)
│  │     Default: bidirectional (recognise AND define)
│  │     Then ask: does this concept have specific ATTRIBUTES?
│  │     │
│  │     YES → Add DESCRIPTOR CARDS (;;) as children
│  │           (origin, date, creator, key feature, etc.)
│  │     │
│  │     NO → The Concept card alone is sufficient
│  │
│  NO ↓
│
├─ Is the knowledge a specific FACT within a SENTENCE
│  where the surrounding context is how you'd naturally
│  encounter it?
│  (Dates, names, terms, formulae in context)
│  │
│  YES → Use a CLOZE CARD ({{ }})
│  │     Ensure the blank has exactly ONE correct answer
│  │     Check: does the sentence give away the answer? If yes, rewrite
│  │
│  NO ↓
│
├─ Is the knowledge a SHORT LIST of items in response
│  to a single question?
│  (3–8 items, well-defined, canonical list)
│  │
│  YES → Use a MULTI-LINE CARD (>>>)
│  │
│  NO ↓
│
├─ Is the knowledge a simple Q&A fact?
│  │
│  YES → Use a BASIC CARD, but choose the direction:
│        │
│        ├─ Do you need to recall in BOTH directions?
│        │  (e.g., vocab pairs, symbol ↔ name, abbreviation ↔ full form)
│        │  │
│        │  YES → Use BIDIRECTIONAL (<>)
│        │
│        ├─ Will you encounter the ANSWER in practice and
│        │  need to identify what it represents?
│        │  (e.g., see symptoms → name the disease)
│        │  │
│        │  YES → Use REVERSE (<<)
│        │
│        └─ Default: Use FORWARD (>>)
│           (Question → Answer, the most common direction)
│
└─ STILL UNSURE?
   Default to a FORWARD BASIC CARD.
   You can always change the direction later
   or convert it to a different type.
```

### Quick-Reference Summary Table

| Card Type | Best For | Direction Default | Create With |
|---|---|---|---|
| **Basic (Forward)** | Factual Q&A, one-directional recall | Forward only | `>>` or `==` |
| **Basic (Reverse)** | Recognition/identification from the answer side | Reverse only | `<<` |
| **Basic (Bidirectional)** | Paired associations (vocab, symbols, abbreviations) | Both directions | `<>` |
| **Concept** | Named things with definitions (terms, entities, theories) | Bidirectional (default) | `::` |
| **Descriptor** | Attributes/properties of a parent Concept | Forward only (default) | `;;` |
| **Cloze** | Facts embedded in context sentences | N/A (fill-in-the-blank) | `{{ }}` |
| **Multi-Line** | Short, bounded lists in response to a question | Same as parent type | `>>>` |
| **Multiple-Choice** | Exam prep with specific question banks | Forward | `>>A)` |
| **Image Occlusion** | Visual/spatial knowledge (diagrams, maps, charts) | N/A (label recall) | Ctrl+click image |

---

*Sources: RemNote Help Center (Creating Flashcards), Anki documentation, Med School Insiders (Anki Best Practices), Andy Matuschak's notes on spaced repetition, SuperMemo's 20 Rules of Knowledge Formulation, Cambridge English (Flash Cards & SRS), and Ness Labs (The Power of Spaced Repetition).*
