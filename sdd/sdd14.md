[<- Return Home](/index.md)
# SDD 1.4 String Concatenation
## Recap
A reminder - programs store data within *variables* so that it can be referenced and modified later. We don't need to know the value that is stored in a variable to write a program with it, we can use the `input()` command to get that value later.

One of the types of values in a program is a `string` value which contains letters, numbers and symbols - basically any text value. 

---
## Learning Intentions
  1. Describe and implement string concatenation in a program
## Success Criteria
1. I can describe the purpose of string concatenation
2. I can use the `,` or `+` operators to concatenate two or more strings.
---

# Concatenation
To concatenate means to join two or more things together. In programming we can join *strings* together. This is known as string concatenation. 

For example, if we had the following strings: `"Mr"` and `"McWhirter"` if we concatenated them the  result would be one string like: `"MrMcWhirter"`.

----
# Examples

## Joining two variables with `+`
We can use the `+` operator to concatenate two variables.
```python
firstName = "Marc"
secondName  = "McWhirter"
print (firstName + secondName)
```
```
MarcMcWhirter
```

## You might need to add a space
Concatenation using the `+` symbol doesn't take account of the fact that you might need to have a space between the bits of text. You can manually add this in as follows:
```python
firstName = "Marc"
secondName  = "McWhirter"
print (firstName + " " + secondName)

```
```
Marc McWhirter
```

## Using the `,` instead of `+`
We can use the `,` instead of the plus sign to concatenate strings, which will automatically put a space in. (Sometimes you might not want a space!)

```python
first="Marc"
middle= "Computing"
second= "McWhirter"
print (first,middle,second)
```
```
Marc Computing McWhirter
```

## You can't concatenate strings and other data types 
You cannot concatenate a string with an integer or other values

```python
name = "Marc"
age = 10
print (name + age)
```
```error
Traceback (most recent call last):
  File "main.py", line 4, in <module>
    print (name+age)
TypeError: can only concatenate str (not "int") to str
```
To fix this you can convert integer values to strings using the `str()` function:

```python
name = "Marc"
age = 10
print (name + str(age))
```
```
Marc 10
```
## Storing concatenation in a variable
You can store a concatenated string in a variable.
```Python
first = "Marc"
second = "McWhirter"
full = first + " " + second
print (full)
```
```
Marc McWhirter
```

---

# Task
In the `main.py` file follow the comments to complete the calculations required using the examples above to help you. 