[<- Return Home](https://speysidecs.github.io/)
# SDD 4.1 Pre-Defined Function - round()
# Pre-Defined Functions

Pre-Defined Functions are pre-written, pre-tested computer programs that perform common functions that programmers require. Using them saves the programmer time (they don't have to solve common problems ) and because they have been pre-tested, the programmer can use them with confidence knowing that will not produce unreliable results.

  ## Learning Intention
  1. Use a pre-defined function to round a number

## Success Criteria
1. Use the `round()` pre-defined function to roundreal  numbers to a required number of decimal places.

## The round() function

The `round()` function is used to round a real number to the closest whole number.

```python
example = 3.14159
rounded = round(example)
print (rounded)
```
Would display the value of `rounded` as `3`.

We can also specify the number of decimal places to round a value to within the brackets of the pre-defined function.

```python
example = 3.14159
rounded = round(example,2)
print (rounded)
```
Would display the value of `rounded` as `3.14`. 

When we round a number, we always round up, for example:

```python
example = 3.6337
rounded = round(example,3)
print (rounded)
```
Would display the value of `rounded` as `3.634`.

----
## Task
In `main.py` round each of the variables set to the required number of decimal places.