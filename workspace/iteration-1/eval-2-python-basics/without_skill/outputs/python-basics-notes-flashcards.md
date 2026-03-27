# Python Basics Flashcards

## What is Python?
**Q: What is Python and who created it?**
- Python is a high-level, interpreted programming language known for its simple and readable syntax. It was created by Guido van Rossum and first released in 1991.

**Q: What is a key characteristic of Python?**
- Python emphasizes code readability and allows programmers to express concepts in fewer lines of code compared to languages like C++ or Java.

## Variables and Data Types
**Q: What is a variable in Python?**
- A variable is a named location used to store data in memory.

**Q: What does it mean that Python is dynamically typed?**
- Python is dynamically typed, which means you don't need to declare a variable's type before using it. The type is determined at runtime.

**Q: List the main data types in Python.**
- The main data types are: integers (whole numbers), floats (decimal numbers), strings (text), booleans (True or False), lists (ordered collections), dictionaries (key-value pairs), and tuples (immutable sequences).

## Strings vs Lists vs Tuples
**Q: What are strings and how are they defined?**
- Strings are sequences of characters enclosed in quotes.

**Q: What is a list and what are its key characteristics?**
- A list is a mutable sequence of items enclosed in square brackets. You can add, remove, or modify items after creation.

**Q: What is a tuple and how does it differ from a list?**
- A tuple is an immutable sequence of items enclosed in parentheses. Once created, you cannot change its contents, unlike lists which are mutable.

**Q: When should you use tuples vs lists?**
- Use lists when you need to modify data. Use tuples when you need a collection that cannot be changed.

**Q: What types of data can be stored in lists and tuples?**
- Both lists and tuples can contain any data type.

## Dictionaries
**Q: What is a dictionary in Python?**
- A dictionary is an unordered collection of key-value pairs enclosed in curly braces.

**Q: How do you access values in a dictionary?**
- Unlike lists which are accessed by index, dictionaries are accessed by key.

**Q: What is a requirement for dictionary keys?**
- Each key must be unique.

**Q: Are dictionaries mutable?**
- Yes, dictionaries are mutable, so you can add, remove, or modify key-value pairs after creation.

## Functions
**Q: What is a function in Python?**
- A function is a reusable block of code that performs a specific task.

**Q: How is a function defined in Python?**
- Functions are defined using the def keyword followed by a name, parentheses, and a colon.

**Q: What can functions accept and return?**
- Functions can accept parameters (inputs) and return values (outputs).

**Q: What is the purpose of the return statement?**
- The return statement is used to send a value back from the function to the code that called it.

## Loops
**Q: What are the two types of loops in Python?**
- For loops iterate over a sequence (like a list or string) a known number of times. While loops repeat as long as a condition is true.

**Q: What does the break statement do in a loop?**
- The break statement stops a loop immediately.

**Q: What does the continue statement do in a loop?**
- The continue statement skips the current iteration and moves to the next one.

## Conditional Statements
**Q: What are conditional statements used for?**
- Conditional statements allow you to run different code depending on whether a condition is true or false.

**Q: What are the three main conditional keywords in Python?**
- Python uses if, elif (else if), and else keywords.

**Q: What does an if statement do?**
- An if statement executes code only if the condition is true.

**Q: What does an elif statement do?**
- An elif statement provides an alternative condition to check if the previous if was false.

**Q: What does an else statement do?**
- An else statement executes code if all previous conditions were false.

## Lists and List Methods
**Q: How is a list created in Python?**
- A list is created by placing items inside square brackets separated by commas.

**Q: What does the append() method do?**
- The append() method adds an item to the list.

**Q: What does the remove() method do?**
- The remove() method deletes an item from the list.

**Q: What does the pop() method do?**
- The pop() method removes an item by index.

**Q: What does the insert() method do?**
- The insert() method adds an item at a specific position in the list.

**Q: What does the sort() method do?**
- The sort() method arranges items in order.

**Q: What does the len() function do?**
- The len() function counts the number of items in a list.

**Q: Are lists mutable?**
- Yes, lists are mutable, so you can modify them after creation.

## Object-Oriented Programming Basics
**Q: What is Object-Oriented Programming (OOP)?**
- Object-Oriented Programming is a programming paradigm based on the concept of objects, which can contain data and code.

**Q: What is a class in OOP?**
- A class is a blueprint for creating objects.

**Q: What is an instance in OOP?**
- An instance is a specific object created from a class.

**Q: What are methods in a class?**
- Methods are functions defined inside a class that operate on the data within an object.

**Q: What is inheritance in OOP?**
- Inheritance allows a class to inherit properties and methods from another class, promoting code reuse.

## Exceptions
**Q: What is an exception in Python?**
- An exception is an error that occurs during program execution.

**Q: Give examples of common exceptions in Python.**
- Common exceptions include NameError (variable not defined), TypeError (wrong data type), ValueError (wrong value for operation), and IndexError (trying to access an index that doesn't exist).

**Q: What is a try-except block used for?**
- The try-except block allows you to handle exceptions gracefully instead of letting the program crash.
