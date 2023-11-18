[<- Return Home](/index.md)
# SDD 5.2 Standard Algorithms - Traversing an array

### Learning Intentions
1. Define standard algorithms
2. Illustrate the traversing an array standard algorithm
3. Implement an traversing an array algorithm

### Success Criteria
1. I can explain the use of a standard algorithm
2. I can illustrate the traversing an array standard algorithm in Pseudocode and Python
3. I can design and implement a solution using the traversing an array algorithm

*What is a standard algorithm?*

A standard algorithm is a step-by-step solution for solving a common problem. These are problems that most programmers will encounter.

## Algorithm - Pseudocode
We use the Traversing an array algorithm to access each element in the array from first to last. This algorithm counts the number of A grades.
```
1. Define the array as 'grades' = ["A","B","D","A","C","B"]
2. Set total to 0
3. for each value in the array
	2.1 If the grade is equal to "A"
	2.2 Add 1 to total
4. end for loop
 ```

## Algorithm - Python - with len() function

We will now change the above algorithm into Python. 

```python
grades = ["A","B","D","A","C","B"]
total = 0
for x in range(len(grades)):
	if grades[x] == "A":
		total = total + 1
 ```
We use the len() function to generate the length of the array, and then loop for that number. 

We then access each value in the array as x increases in value, starting from 0 to the end of the array (e.g. first time round the loop we check grades[0], then grades[1] and so on until grades[5].)

If the current value of grades is "A" then we add 1 on to the variable total.

## Task 

Alan needs to check the values entered for the CO2 levels in the school

```
The levels of CO2 in the air and potential health problems are: 
400 ppm: average outdoor air level. 
400–1,000 ppm: typical level found in occupied spaces with good air exchange. 
1,000–2,000 ppm: level associated with complaints of drowsiness and poor air.
```

Alan has recorded CO2 values on average for all rooms in the English corridor, in order of room from 1-7.

co2Values = [700, 229, 1370, 1004, 1708, 2001, 2643]

Alan needs you to total the number of rooms with CO2 emissions higher than 1000, and rooms higher than 2000 using your array traversal algorithm.