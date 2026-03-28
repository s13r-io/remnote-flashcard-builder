# Python Basics

## What is Python?

- **Python** :: A high-level, interpreted programming language known for its simple and readable syntax
- Python was created by {{Guido van Rossum}}.
- Python was first released in {{1991}}.
- **What does Python emphasize as a language design goal?** >> Code readability
- **Compared to C++ or Java, Python allows programmers to do what?** >> Express concepts in fewer lines of code
- **Which type of programming language does not need compilation before running?** >>A) Interpreted B) Compiled C) Assembled D) Linked

## Variables and Data Types

- **Variable** :: A named location used to store data in memory
- **What does it mean that Python is dynamically typed?** >> You don't need to declare a variable's type before using it
- **dynamically typed** ;; A language feature where variable types are determined at runtime, not declared beforehand
- **Main data types in Python** >>>
Integers (whole numbers)
Floats (decimal numbers)
Strings (text)
Booleans (True or False)
Lists (ordered collections)
Dictionaries (key-value pairs)
Tuples (immutable sequences)
- **Integer** ;; A data type representing whole numbers
- **Float** ;; A data type representing decimal numbers
- **String** ;; A data type representing text
- **Boolean** ;; A data type with only two possible values: True or False
- **Given a data type that stores ordered, mutable collections** << List
- **Given a data type that stores key-value pairs** << Dictionary

## Strings vs Lists vs Tuples

- **String (in Python)** :: A sequence of characters enclosed in quotes
- **List (in Python)** :: A mutable sequence of items enclosed in square brackets
- **Tuple (in Python)** :: An immutable sequence of items enclosed in parentheses
- **What does it mean that lists are mutable?** >> You can add, remove, or modify items after creation
- **What does it mean that tuples are immutable?** >> Once created, you cannot change their contents
- **Which sequence type should you use when you need to modify data: list or tuple?** >> List
- **Which sequence type should you use when you need a collection that cannot be changed?** >> Tuple
- Both lists and tuples can contain {{any data type}}.
- **Which Python type is mutable: list, tuple, or string?** >>A) List B) Tuple C) String D) All of these

## Dictionaries

- **Dictionary (in Python)** :: An unordered collection of key-value pairs enclosed in curly braces
- Each key in a Python dictionary must be {{unique}}.
- **How is a dictionary value retrieved?** >> By using its associated key
- **Are Python dictionaries mutable or immutable?** >> Mutable — you can add, remove, or modify key-value pairs after creation
- **How are lists accessed vs. how are dictionaries accessed?** >> Lists are accessed by index; dictionaries are accessed by key
- Dictionaries are enclosed in {{curly braces}}.
- **Given a collection accessed by key rather than by index** << Dictionary

## Functions

- **Function (in Python)** :: A reusable block of code that performs a specific task
- Functions in Python are defined using the {{def}} keyword.
- **What follows the def keyword when defining a function?** >> A name, parentheses, and a colon
- **parameters** ;; Inputs that a function can accept
- **return values** ;; Outputs that a function can send back
- **return statement** ;; Used to send a value back from a function to the code that called it
- **What keyword is used to define a function in Python?** >>A) def B) func C) function D) define

## Loops

- **Loop** :: A construct that allows you to repeat a block of code multiple times
- **Two types of loops in Python** >>>
for loops
while loops
- **for loop** ;; Iterates over a sequence (like a list or string) a known number of times
- **while loop** ;; Repeats as long as a condition is true
- **break statement** ;; Stops a loop immediately
- **continue statement** ;; Skips the current iteration and moves to the next one
- **Which loop type iterates over a sequence a known number of times?** >>A) for loop B) while loop C) do-while loop D) repeat-until loop
- **Given a statement that stops a loop immediately** << break
- **Which statement skips the current iteration: break or continue?** >> continue

## Conditional Statements

- **Conditional statement** :: A statement that allows you to run different code depending on whether a condition is true or false
- **Three keywords Python uses for conditional statements** >>>
if
elif (else if)
else
- **if statement** ;; Executes code only if the condition is true
- **elif statement** ;; Provides an alternative condition to check if the previous if was false
- **else statement** ;; Executes code if all previous conditions were false
- The keyword {{elif}} is short for "else if" in Python.
- **In what order does Python evaluate if/elif/else?** >> It checks if first, then each elif in order, and runs else only if all previous conditions were false
- **Given a block that executes when all previous conditions were false** << else

## Lists and List Methods

- A list is created by placing items inside {{square brackets}} separated by commas.
- **Common list methods in Python** >>>
append() — add an item
remove() — delete an item
pop() — remove an item by index
insert() — add an item at a specific position
sort() — arrange items in order
len() — count the number of items
- **append()** ;; Adds an item to a list
- **remove()** ;; Deletes an item from a list
- **pop()** ;; Removes an item from a list by index
- **insert()** ;; Adds an item to a list at a specific position
- **sort()** ;; Arranges list items in order
- **len()** ;; Returns the count of items in a list
- **Which list method adds an item at a specific position?** >>A) insert() B) append() C) add() D) push()
- **Given a method that removes a list item by index** << pop()

## Object-Oriented Programming Basics

- **Object-oriented programming (OOP)** :: A programming paradigm based on the concept of objects, which can contain data and code
- **Class** :: A blueprint for creating objects
- **Instance** :: A specific object created from a class
- **Methods (in OOP)** :: Functions defined inside a class that operate on the data within an object
- **Inheritance (in OOP)** :: A mechanism that allows a class to inherit properties and methods from another class, promoting code reuse
- **What does inheritance promote?** >> Code reuse
- **What can objects contain in OOP?** >> Data and code
- **OOP** <> Object-oriented programming
- **Given a blueprint for creating objects** << Class

## What is an Exception?

- **Exception** :: An error that occurs during program execution
- **NameError** ;; Raised when a variable is not defined
- **TypeError** ;; Raised when the wrong data type is used
- **ValueError** ;; Raised when the wrong value is used for an operation
- **IndexError** ;; Raised when trying to access an index that doesn't exist
- **try-except block** ;; Allows you to handle exceptions gracefully instead of letting the program crash
- **Which exception is raised when accessing a non-existent index?** >>A) IndexError B) KeyError C) ValueError D) TypeError
- **Given an error raised when a variable is not defined** << NameError
- **What does a try-except block prevent?** >> The program from crashing when an exception occurs
