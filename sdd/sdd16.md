[<- Return Home](/index.md)
# SDD 1.6 if using else

## Learning Intentions
  1. Describe the purpose of an else statement
  2. Implement else statements within your computer programs
## Success Criteria
1. I can use an else statement to make a decision in a Python program
---

# If statements 
If statements are used to make decisions in a computer program. They check the value of a variable and then do a line of code if the condition is true. If it is NOT true, we can use the `else:` keyword to direct the program


## Else Statement Examples

```python
age = int(input("Enter your age: "))
if age < 17:
	print("You can't get a provisional driving license")
else:
	print ("You can get a provisional driving license")
```

In the above example, the code checks to see whether the value of age is less than 17 - if it is less than seventeen, it displays the string `You can't get a provisional license`. 

If the value of age is greater than or equal to 17, it prints the string `You can get a provisional driving license`.

```python
age = int(input("Enter your age: "))
if age > 16:
	print ("You can get a provisional driving license")
else:
	print("You can't get a provisional driving license")
```
In the above example, the code checks to see whether the value of age is greater than 16. If it is, it prints the string: `You can get a provisional driving license`.

If it is not greater than 16, it prints the string `You can't get a provisional driving license`.

---

# Task
In the `main.py` file follow the comments to complete the if statements required using the examples above to help you. 