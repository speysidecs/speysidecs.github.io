# SDD 5.1 Standard Algorithms - Input Validation

### Learning Intentions
1. Define standard algorithms
2. Illustrate the input validation standard algorithm
3. Implement an input validation algorithm

### Success Criteria
1. I can explain the use of a standard algorithm
2. I can illustrate an input validation standard algorithm in Pseudocode and Python
3. I can design and implement a solution using an input validation algorithm



*What is a standard algorithm?*

A standard algorithm is a step-by-step solution for solving a common problem. These are problems that most programmers will encounter.

## Algorithm - Pseudocode
Pseudocode is a generic way of describing instructions that are not in a programming language, but more like English. They should be easy to translate into a programming language. They are broken down into steps.
```
1. Get input from the user
2. while the input is not valid
	2.1 Display error message
	2.2 Get input again
 ```

## Algorithm - Python - within a number range

We will now change the above algorithm into Python. The following algorithm makes sure user input is between 0 and 100.

```python
userValue = int(input("Enter number between 0-100: "))
while userValue < 0 or userValue > 100:
	print ("Error - enter value within 0-100")
	userValue = int(input("Enter number between 0-100: "))
 ```
The loop will repeat until such times as they enter a value within the acceptable range.
## Algorithm - Python - fixed value
```python
userValue = input("Enter either yes or no: ")
while userValue != "yes" or userValue != "no":
	print ("Error - enter value as either yes or no")
	userValue = input("Enter either yes or no: ")
 ```
The loop will repeat until such times as they enter one of the two accepted values.

## Task 

Alan requires users to enter the CO2 levels in classrooms.

```
The levels of CO2 in the air and potential health problems are: 
400 ppm: average outdoor air level. 
400–1,000 ppm: typical level found in occupied spaces with good air exchange. 
1,000–2,000 ppm: level associated with complaints of drowsiness and poor air.
```

Create a program that displays the above messages depending on the user's input. The user's input should be validated to be within an acceptable range (0-2500).