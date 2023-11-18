[<- Return Home](/index.md)
# SDD 2.2 - Conditional Loops  

We can use a conditional loop to loop lines of code for a *unknown* amount of times until a condition is or is not met. It's a bit like combining an `if` and a `for`. 

  ## Learning Intention
  1. Repeat code using a conditional loop

## Success Criteria
1. Implement a conditional loop in Python using the `while` command
2. Explain the purpose of a conditional loop

## Examples
The following example has a variable at the top which sets the correct password. Initially, `correct` - a boolean value is set to `False`.

The conditional loop will run until the value of correct is `False`. It will keep asking for the user to enter a password until they correctly guess the password of `goodbrand123`.

```python
password = "goodbrand123"
correct = False
while correct == False:
	passwordEntry = input("What is the password?")
	if passwordEntry == password:
		correct = True
	else:
			 print ("incorrect! you can try again...")
print ("Correct! Welcome to Speyside High")
```

## Example 2
This code could be made simpler by taking out the `if` entirely

```python
password = "goodbrand123"
passwordEntry = input("What is the password?")
while passwordEntry != password:
	print ("Incorrect! Enter the password again.")
	passwordEntry = input("What is the password?")
print ("Correct! Welcome to Speyside High")
```
In this example, the condition has been changed so that it does the job of comparing the value of `password` to whatever the user has typed as input for the variable `passwordEntry`.

The loop repeats while `passwordEntry` does not equal (`!=`) `password`.

## Task

1. Copy the code examples above into main.py one at a time and try them out.
2. Create a program that asks the user to enter a number lower than 20. While the number is greater than or equal to 20, it should ask them to re-enter a number. When they have entered a valid number, the program should output a message saying "CORRECT!"