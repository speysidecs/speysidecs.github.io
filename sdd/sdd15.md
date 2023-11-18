[<- Return Home](https://speysidecs.github.io/)
# SDD 1.5 Basic IF statements

## Learning Intentions
  1. Describe the purpose of an if statement
  2. Implement a basic if statement in a computer program
## Success Criteria
1. I can use an if statement to make a decision in a Python program
---

# If statements 
If statements are used to make decisions in a computer program. They check the value of a variable and then do a line of code if the condition is true. 

## Conditional Operators

* `>` means greater than
* `<` means less than
* `>=` means greater than or equal to
* `<=` means less than or equal to
* `==` means equal to
* `!=` means not equal to


## If Statement Examples

```python
age = int(input("Enter your age: "))
if age < 17:
	print("You can't get a provisional driving license")
```

In the above example, the code checks to see whether the value of age is less than 17 - if it is less than seventeen, it displays the string `You can't get a provisional license`.

```python
age = int(input("Enter your age: "))
if age > 16:
	print ("You can get a provisional driving license")
```
In the above example, the code checks to see whether the value of age is greater than 16. If it is, it prints the string: `You can get a provisional driving license`.

```python
age = int(input("Enter your age: "))
if age >= 17:
	print ("You can get a provisional driving license")
```
In the above example, the code checks to see whether the value of age is greater than or equal to 17. If it is, then it prints the string `You can get a provisional driving license`.

---

# Task
In the `main.py` file follow the comments to complete the if statements required using the examples above to help you. 