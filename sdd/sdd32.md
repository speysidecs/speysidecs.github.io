[<- Return Home](https://speysidecs.github.io/)
# SDD 3.2 - Arrays - Recap

An array is a *data structure* which is a type of *variable* which holds more than one value at a time. This is really useful when we come to apply algorithms. 

  ## Learning Intention
  1. Create an empty array which can later be populated with a fixed loop.

## Success Criteria
1. Create an empty array of a single type.
2. Use a fixed loop (`for`) combined with `input()` to add values to the array

## Examples - Defining an empty Array of fixed size
If we need to create an array which contains values that we don't yet know we should use the following format:
```python
classNames = [str() for x in range(20)]
```
This creates an empty array variable called `classnames` which is of  type `str` (string) and is size `20`.

We could also use `bool()` for boolean, `int()` for integer and `float()` for real numbers. 

## Examples - Adding a number of item to the array using a fixed loop

Now we  again use `[index]` numbers to assign the place in the array that an item is going to be stored. 
```python
classNames = [str() for x in range(20)]
classNames[8] = "India"
```
This code would store `India` at index `8` or the 9th position in the array. 

This is a really inefficient method of storing the values - we are now going to use a loop and input to add values to the array.



## Further explanation
You can imagine your array like a table with one row.

|Array Name|[0]|[1]|[2]|
|---------|---------|---------|---------|
|classNames|Alexander|Struan|Connor McGregor from UFC

## Arrays can only hold one data type

In most programming languages, you cannot have an array of mixed data types. For example, all values in an array must be of type `string` or type `integer`. An array couldn't contain a mixture of `strings` and `integers`. 

In Python you *can* but should not. 

## Task 
In `main.py` create an array to store names of 3 of your friends.

Then create an array to store the ages of those three friends. 