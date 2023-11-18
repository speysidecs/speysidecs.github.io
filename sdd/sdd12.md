# SDD 1.2 Input & Output
* Computer programs take data in from their users (known as input).
* Computer programs then display results to their users (known as output).

---
## Learning Intentions
  1. Getting user input into a program and storing it
  2. Displaying an output to the user
## Success Criteria
1. I have used the `input()` function to store user input in a variable
2. I have used the `input()` function to store user input of different types
3.  I have used the `print()` function to to display an output to the user
---
# Examples

Input and output are two important building blocks in computer programming and all of your programs will use these functions. 

## Getting user input

In order to get user input we need to use the `input()` function.

The `input()` function is used to ask the user to type in a value which will be stored as a variable as part of a variable assignment.

Inside the brackets of the `input()` function, you can type a hint, or prompt for the user, telling them what to do. 


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
