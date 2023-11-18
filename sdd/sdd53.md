# SDD 5.3 Standard Algorithms - Running total within a loop

### Learning Intentions
1. Define standard algorithms
2. Illustrate the running total standard algorithm
3. Implement the running total algorithm

### Success Criteria
1. I can explain the use of a standard algorithm
2. I can illustrate the running totaly standard algorithm in Pseudocode and Python
3. I can design and implement a solution using the running total algorithm

*What is a standard algorithm?*

A standard algorithm is a step-by-step solution for solving a common problem. These are problems that most programmers will encounter.

## Algorithm - Pseudocode
We use the running total algorithm to keep the count of values entered within a loop. Note there are *two* versions of the running total algorithm, a fixed loop version and conditional loop version.

#### Fixed Loop Version
When you know how many values the user will enter, use the fixed loop algorithm.
```
1. Set total to 0
2. For 10 times
	2.1 Ask the user to enter a new value
	2.2 Add the new value to total
	2.3 end for
3. Display total
```
The above algorithm could be modified to ask the user how many numbers to add after line 1, and then use this value to run the fixed loop.

#### Conditional Loop Version
When you don't know how many times to loop, you can continiously loop and ask the user if they want to add another value.

```
1. Set total to 0
2. Set continue to "yes"
3. while continue is equal to yes:
	3.1 Ask the user to enter a new value
	3.2 Add the new value to total
	3.3 Ask the user if they want to continue
	3.4 End while
 4. Display total
 ```


### Algorithms - Python

We will now change the above algorithms into Python. 

#### Fixed Loop Version
```python
total = 0
for x in range(10):
	newValue = int(input("Enter value to add:"))
	total = total + newValue
print (total)
 ```
#### Conditional Loop Version
```python
total = 0
getAnotherValue = "yes"
while getAnotherValue == "yes":
	newValue = int(input("Enter value to add:"))
	total = total + newValue
	getAnotherValue = input("Continue? yes/no: ")
print (total)
```
## Task 

Alan needs to check the values entered for the CO2 levels in the school

```
The levels of CO2 in the air and potential health problems are: 
400 ppm: average outdoor air level. 
400–1,000 ppm: typical level found in occupied spaces with good air exchange. 
1,000–2,000 ppm: level associated with complaints of drowsiness and poor air.
```

Alan has recorded CO2 values in Room 1 specifically for the last 7 days, they are stored in the array below.
```python
co2Values = [690,1001,500,1900,1734,1103,1623]
```


Alan would like you to enter these into a program to generate the total, using the running total algorithm. You will not need to use an array for this and will enter each value to test your program. 

#### Extension
When the algorithm is complete, use the value generated to tell Alan the average (mean) value of the CO2 values for the week.