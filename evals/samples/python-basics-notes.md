# Python Basics

## What is Python?

Python is a high-level, interpreted programming language known for its simple and readable syntax. Guido van Rossum created Python and first released it in 1991. Python emphasizes code readability and allows programmers to express concepts in fewer lines of code than might be used in languages such as C++ or Java.

## Variables and Data Types

A variable is a named location used to store data in memory. Python is dynamically typed, meaning you don't need to declare a variable's type before using it. The main data types in Python are integers (whole numbers), floats (decimal numbers), strings (text), booleans (True or False), lists (ordered collections), dictionaries (key-value pairs), and tuples (immutable sequences).

## Strings vs Lists vs Tuples

Strings are sequences of characters enclosed in quotes. Lists are mutable sequences of items enclosed in square brackets, meaning you can add, remove, or modify items after creation. Tuples are immutable sequences of items enclosed in parentheses, meaning once created, you cannot change their contents. Both lists and tuples can contain any data type, but lists are preferred when you need to modify data, while tuples are useful when you need a collection that cannot be changed.

## Dictionaries

A dictionary is an unordered collection of key-value pairs enclosed in curly braces. Each key must be unique and is used to retrieve its associated value. Dictionaries are mutable, so you can add, remove, or modify key-value pairs after creation. Unlike lists, which are accessed by index, dictionaries are accessed by key.

## Functions

A function is a reusable block of code that performs a specific task. Functions are defined using the def keyword followed by a name, parentheses, and a colon. Functions can accept parameters (inputs) and return values (outputs). The return statement is used to send a value back from the function to the code that called it.

## Loops

A loop allows you to repeat a block of code multiple times. Python has two types of loops: for loops, which iterate over a sequence (like a list or string) a known number of times, and while loops, which repeat as long as a condition is true. The break statement stops a loop immediately, and the continue statement skips the current iteration and moves to the next one.

## Conditional Statements

Conditional statements allow you to run different code depending on whether a condition is true or false. Python uses if, elif (else if), and else keywords. An if statement executes code only if the condition is true. An elif statement provides an alternative condition to check if the previous if was false. An else statement executes code if all previous conditions were false.

## Lists and List Methods

A list is created by placing items inside square brackets separated by commas. Common list methods include append() to add an item, remove() to delete an item, pop() to remove an item by index, insert() to add an item at a specific position, sort() to arrange items in order, and len() to count the number of items. Lists are mutable, so you can modify them after creation.

## Object-Oriented Programming Basics

Object-oriented programming (OOP) is a programming paradigm based on the concept of objects, which can contain data and code. A class is a blueprint for creating objects. An instance is a specific object created from a class. Methods are functions defined inside a class that operate on the data within an object. Inheritance allows a class to inherit properties and methods from another class, promoting code reuse.

## What is an Exception?

An exception is an error that occurs during program execution. Common exceptions include NameError (variable not defined), TypeError (wrong data type), ValueError (wrong value for operation), and IndexError (trying to access an index that doesn't exist). The try-except block allows you to handle exceptions gracefully instead of letting the program crash.
