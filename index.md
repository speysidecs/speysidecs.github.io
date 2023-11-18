# Speyside High School National 5 Computing Science Course
Welcome to the GitHub page for the National 5 Computing Science course at Speyside High School. You are welcome to take a copy of this course and associated Python and SQL files. 

This page was created when repl.it discontinued teams and its purpose is to be an open course book for Scottish students studying National 5 Computing.

---
# Software Design and Development

The following Python course pages are linked below. Associated Python files can be found in the GitHub repo.

## Section SDD 1: Python Basics

### SDD 1.1 - Basic Variable Assignment.
Task Instructions: [click here](/sdd/sdd11.md)
GitHub: 
Repl:

```python
nameOfDog = input("Enter the name of the dog:")
```
This will show up on the screen as:

```python
Enter the name of the dog:
```
When the user enters a value, the program will continue to run, storing whatever they have typed in the variable `nameOfDog`.

## Getting user input of a different type
The input function defaults to storing **string** variables. This means by default all values will be stored as text, which means we cannot perform maths on them. If we want to store number variables we need to use two other functions: `int()` and `float()`. 

### Storing a user input integer value

Using the `int()` function we can store a whole number user input by putting the `input()` function inside the `int()` functions brackets like in the example below:

```python
ageOfDog = int(input(Enter the age of the dog:))
```

### Storing a user input real number value

Using the `float()` function we can store a number with a decimal place user input by putting the `input()` function inside the `float()` function brackets, just like the previous example. 
```python
ageOfDog = float(input(Enter the age of the dog:))
```
## Displaying output

To display anything on the screen we use the `print()` function. 

We can display text or numbers directly by enterining them into the brackets, for example:

```python
print("Hello") #Display text
print (10) #Display a number
```
Which would output as:
```
Hello
10
```
We can also display the values of variables by referencing the variable name inside the brackets of the print function, for example:

```python
nameOfDog = "Alfie"
print (nameOfDog)
```
This would display: 
```
Alfie
```

---
## Task
In the Python section you will see some boiler plate code (that is the name for code I have created for you).
1. Complete the comment section at the top to put your name at the top (firstname only) and today's date.
2. In the comments that follow you will see tasks to get user input and store it as a variable. Underneath this comment create a name and value pair to store the user input in a variable. This should use the `input()` command.
3. Under each input, create a line of code to display what the user entered using the `print()` command.
