# Python Basics

## What is Python?

- **Python** :: A high-level, interpreted programming language known for its simple and readable syntax
- **Guido van Rossum** :: Creator of the Python programming language
- **Python release year** >> 1991
- **What year was Python first released?** >> 1991
- {{Python}} emphasizes code readability and allows programmers to express concepts in fewer lines of code than C++ or Java.
- **Which language emphasizes code readability and conciseness?** >>A) Python B) Assembly C) Fortran D) COBOL
- **Which of these was created by Guido van Rossum?** >>A) Python B) Java C) Go D) Rust

## Variables and Data Types

- **Variable** :: A named location used to store data in memory
- **Dynamic typing** :: A type system where you don't need to declare a variable's type before using it
- **Python is dynamically typed.** >> True
- The {{type}} of a variable in Python can be determined at runtime.
- **Integer** :: A whole number (positive, negative, or zero) data type in Python
- **Float** :: A decimal number data type in Python
- **String** :: A text data type in Python, sequences of characters enclosed in quotes
- **Boolean** :: A data type in Python that can be either True or False
- **List** :: An ordered collection data type in Python, enclosed in square brackets
- **Dictionary** :: A key-value pair collection data type in Python, enclosed in curly braces
- **Tuple** :: An immutable sequence data type in Python, enclosed in parentheses
- **Main data types in Python** >>>
  Integers
  Floats
  Strings
  Booleans
  Lists
  Dictionaries
  Tuples

## Strings vs Lists vs Tuples

- **Strings** ;; Sequences of characters enclosed in quotes
- **Lists** ;; Mutable sequences of items enclosed in square brackets
- **Tuples** ;; Immutable sequences of items enclosed in parentheses
- **What is the key difference between lists and tuples?** >> Lists are mutable (can be modified), while tuples are immutable (cannot be changed after creation)
- {{Lists}} are mutable sequences that can be modified after creation.
- {{Tuples}} are immutable sequences that cannot be changed once created.
- **Can you add items to a list after creation?** >>A) Yes B) No
- **Can you add items to a tuple after creation?** >>A) Yes B) No
- **When should you use a list instead of a tuple?** >> When you need to modify the data
- **When should you use a tuple instead of a list?** >> When you need a collection that cannot be changed
- **List vs Tuple: Which should you use for constant data?** << Tuple
- **List vs Tuple: Which should you use when modifying data is required?** << List

## Dictionaries

- **Dictionary** :: An unordered collection of key-value pairs enclosed in curly braces
- **Key (in dictionary)** :: A unique identifier used to retrieve its associated value in a dictionary
- **Dictionaries are unordered collections of {{key-value}} pairs.**
- **Dictionaries are mutable.** >> True
- **Access method in dictionaries** ;; By key (not by index like lists)
- **Can you modify a dictionary after creation?** >>A) Yes B) No
- **How are dictionaries accessed, compared to lists?** >> Dictionaries are accessed by key, while lists are accessed by index
- **Dictionary vs List: Which uses keys for access?** << Dictionary
- **What must be true about all keys in a dictionary?** >> Each key must be unique

## Functions

- **Function** :: A reusable block of code that performs a specific task
- **def keyword** ;; Used to define a function in Python
- {{Function}} structure includes the def keyword, name, parentheses, and a colon.
- **Parameter** :: An input to a function
- **Return value** :: An output sent back from a function using the return statement
- **What keyword is used to send a value back from a function?** >> return
- **How many times can a function be reused?** >> Multiple times
- **The structure of a function definition** >>>
  def keyword
  Function name
  Parentheses
  Colon
- **What do parameters allow functions to do?** >> Accept inputs
- **What do return statements allow functions to do?** >> Send values back to the calling code

## Loops

- **Loop** :: A control structure that allows you to repeat a block of code multiple times
- **for loop** :: A loop that iterates over a sequence a known number of times
- **while loop** :: A loop that repeats as long as a condition is true
- **break statement** :: A statement that stops a loop immediately
- **continue statement** :: A statement that skips the current iteration and moves to the next one
- **Python has {{two}} main types of loops.**
- **Which loop type iterates over a sequence a known number of times?** >>A) for loop B) while loop C) do-while loop D) foreach loop
- **Which loop type repeats as long as a condition is true?** >>A) for loop B) while loop C) do-while loop D) repeat loop
- **What does the break statement do?** >> Stops the loop immediately
- **What does the continue statement do?** >> Skips the current iteration and moves to the next one
- **for loops iterate over sequences like lists or strings.** << for loop
- **while loops repeat based on a condition.** << while loop

## Conditional Statements

- **Conditional statement** :: A control structure that allows different code to run based on whether a condition is true or false
- **if statement** :: Executes code only if the condition is true
- **elif statement** :: Provides an alternative condition to check if the previous if was false
- **else statement** :: Executes code if all previous conditions were false
- **Python uses {{if}}, {{elif}}, and {{else}} keywords for conditional logic.**
- **Which keyword provides an alternative condition if the previous if was false?** >>A) else B) elif C) if D) switch
- **The {{if}} statement executes code only when the condition is true.**
- **Conditional statements allow you to write code that responds to different conditions.** >> True
- **When does an else statement execute?** >> When all previous conditions were false

## Lists and List Methods

- **append()** :: A list method that adds an item to the end of a list
- **remove()** :: A list method that deletes an item from a list
- **pop()** :: A list method that removes an item by index
- **insert()** :: A list method that adds an item at a specific position
- **sort()** :: A list method that arranges items in order
- **len()** :: A function that counts the number of items in a list
- **List creation syntax** >> Items placed inside square brackets separated by commas
- **Which list method adds an item to the end?** >>A) insert() B) append() C) add() D) push()
- **Which list method removes an item by index?** >>A) remove() B) delete() C) pop() D) extract()
- **What does the insert() method do?** >> Adds an item at a specific position
- **What does the sort() method do?** >> Arranges items in order
- **The {{len()}} function returns the number of items in a list.**
- **Mutable** ;; Lists can be modified after creation

## Object-Oriented Programming Basics

- **Object-oriented programming (OOP)** :: A programming paradigm based on the concept of objects that contain data and code
- **Class** :: A blueprint for creating objects
- **Instance** :: A specific object created from a class
- **Method** :: A function defined inside a class that operates on the data within an object
- **Inheritance** :: A mechanism that allows a class to inherit properties and methods from another class
- **Objects contain {{data}} and {{code}}.**
- **A class is a {{blueprint}} for creating objects.**
- **What is an instance?** >> A specific object created from a class
- **Inheritance promotes {{code}} reuse.**
- **Which concept allows a class to inherit properties from another class?** >>A) Polymorphism B) Encapsulation C) Inheritance D) Abstraction

## What is an Exception?

- **Exception** :: An error that occurs during program execution
- **NameError** :: An exception that occurs when a variable is not defined
- **TypeError** :: An exception that occurs when the wrong data type is used
- **ValueError** :: An exception that occurs when the wrong value is used for an operation
- **IndexError** :: An exception that occurs when trying to access an index that doesn't exist
- **try-except block** :: A control structure that allows you to handle exceptions gracefully instead of letting the program crash
- {{An exception}} is an error that occurs during program execution.
- **Which exception occurs when a variable is not defined?** >>A) NameError B) TypeError C) ValueError D) IndexError
- **Which exception occurs due to wrong data type?** >>A) NameError B) TypeError C) ValueError D) IndexError
- **Which exception occurs when accessing a non-existent index?** >>A) NameError B) TypeError C) ValueError D) IndexError
- **What is the purpose of a try-except block?** >> To handle exceptions gracefully instead of letting the program crash
- **Common exceptions in Python** >>>
  NameError
  TypeError
  ValueError
  IndexError