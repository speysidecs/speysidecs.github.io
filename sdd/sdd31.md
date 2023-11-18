# SDD 3.1 - Arrays - Intro

A variable can only store one item of data at a time. When working with a large amount of data, that would mean we would need to create a separate variable for each piece of data. 

Imagine creating variables to store the name of each person in class - we would need 20 variables, each with their own variable assignment and identifier. 

This just isn't practical, and it means we would need to remember the names of all those variables, and our code would be really inefficient. That's where arrays come in.

  ## Learning Intention
  1. Use an array to store an access pieces of related data in Python

## Success Criteria
1. I can create an array to store multiple values
2. I can access data within an array using it's `[index]` value 
3. I understand that variable indexing begins from `[0]`

## Examples - Defining an Array
The following example defines an array of strings in Python.
```python
classNames = ["Alexander","Struan", "Connor McGregor from UFC"]
```
An array is a variable which stores multiple values. Python defines an array using the `[]` square brackets. Data are separated by commas. In the above example, the array knows that `Alexander` and `Struan` are separate values.

## Examples - Accessinng values in an array

We use `[index]` numbers to define the place in the array that an item is held, starting from 0. For example:
```python
classNames = ["Alexander","Struan", "Connor McGregor from UFC"]
print (classNames[0])
```
Would display `Alexander` and
```python
print (classNames[2])
```
Would display `Connor McGregor from UFC`.

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