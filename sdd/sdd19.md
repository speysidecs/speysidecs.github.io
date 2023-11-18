[<- Return Home](/index.md)
# SDD 1.9 Complex Conditions (and, or, not)


## Learning intentions
  1. Using Boolean Operators to make complex decisions in a program
  2. Describe the Boolean operators used in programming

## Success Criteria

1. Implement and explain a condition using `and`
2. Implement and explain a condition using `or`
3. Implement and explain a condition using `not`
4. Implement and explain a condition using more than one boolean operator



 ## Examples

In this first example, we check to see if the value of `name` is equal to `Marc` and the value of `homeTown` is equal to `Paisley`. Both of these conditions must be `True` because we are using the `and` boolean operator.
```python
#Example 1 - and
name = input("Enter your name: ")
homeTown = input("Enter your hometown: ")
if name == "Marc" and homeTown == "Paisley":
  print("Oh, hi Marc from Paisley!")
else:
  print("You're not Marc from Paisley!")
```

In this second example, we check to see if the value of `name` is equal to `Marc` or the value of `homeTown` is equal to `Paisley`. Only one of these conditions must be `True` because we are using the `or` boolean operator. So if the value for name was `Mr Picksley` and the value of `homeTown` was Paisley, it would still be true, even though the name was not `Marc`.

```python
#Example 2 - or
name = input("Enter your name: ")
homeTown = input("Enter your hometown: ")
if name == "Marc" or homeTown == "Paisley":
  print("You're either called Marc or you're from Paisley!")
else:
  print("You're not Marc, and you aren't from Paisley!")
```
`not` is a little trickier here in example 3, i've simplified the code for this example. 

The code checks to see if the `name` is `not` `Marc` - and outputs a message to say so. This means the `else` is only triggered if the `name` is `Marc`. 

```python
#Example 3 - not
name = input("Enter your name: ")
if not name == "Marc":
	print ("You're not Marc!")
else:
	print ("You are Marc")

```

In this next example we've combined the `not` and the `and` to produce output when the `name` does not equal `Marc` and does not equal `Ed`.
```python
#Example 4 and not
name = input("Enter your name: ")
if not name == "Marc" and not name == "Ed":
	print ("You're not Marc and you're not Ed!")
elif name == "Marc":
	print ("You are Marc")
	print ("Hello boss!")
else:
	print ("You are Ed")
	print ("Nice to see you, Ed!")
```
---
## Task

Write a program that:

* Stores your eye colour, hair colour and the number of pets you have in three separate variables.

* Asks the user to guess them one by one and stores their answers in three more variables.

* Outputs 'You guessed them all' if the user gets all 3 correct.
* Outputs 'You got some, but not all correct' if the user gets one or two correct.
* Outputs 'You didn't get any right' if the user gets them all wrong.
