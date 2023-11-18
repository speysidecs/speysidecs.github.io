[<- Return Home](https://speysidecs.github.io/)
# SDD 4.3 Pre-Defined Functions: Random Library

Sometimes the pre-defined functions we require are built into Python like `len()` and `round()`. Sometimes, however, we need to make use of additional functions from outside Pythons own library (collection) of function. 

In this lesson we will import a library filled with functions to introduce randomness to our code.

  ## Learning Intention
  1. Import a module library to add random number generation to a program
## Success Criteria
1. Import the `random` library
2. Implement the `randrange()` function to generate a number within a set range

## The random library

When we want to use any random functions in Python we need to place the following line at the top of our code:

```python
from random import *
```

This will allow us to use all the functions within the random library. Without this, Python will not be able to use any of the functions. You only need to do this once and should place it at the very beginning of your program.

### Using the randrange() function
We can use the `randrange()` function to generate a random integer between a certain range of numbers. 

Like the `round()` function, `randrange()` must be given two values - the starting value, and the end of the range. For example:

```python
start = 0
end = 10
print (randrange(start,end))
```
The above code would generate a number between 0 - 9. Even though the end value is 10, it will not be included as a number that can be generated. 

We don't have to use variables as the values for the `randrange()` function, we can just use integer values, for example:

```python
print (randrange(0,101))
```
Would generate a random number which could be any value between 0 and 100.


----
## Task
In `main.py` create a program which will generate 100 random numbers between 0 and 30 (including 30). You should write this program using a fixed loop. 