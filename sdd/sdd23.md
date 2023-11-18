[<- Return Home](https://speysidecs.github.io/)
# SDD 2.1 - Conditional Loops with Complex Conditions

We can use a conditional loop to loop lines of code for a *unknown* amount of times until a condition is or is not met. It's a bit like combining an `if` and a `for`. 

Just like with `if` statements, we can use a complex condition where we check more than one condition, using `and`/ `or`, sometimes including `not`.

  ## Learning Intention
  1. Repeat code using a conditional loop with a complex condition

## Success Criteria
1. Implement a conditional loop in Python using the `while` command using a complex condition

## Examples
The following example is a complex condition version of our previous password program. The correct username and password is now stored at the top of the example. The conditional loop then checks to see if the values entered by the user in `userEntry` and `passwordEntry` match the variables at the top of the code. 

The user will be stuck inside the conditional loop until they type the correct username and password.


```python
username = "p.goodbrand@speyside.com"
password = "goodbrand123"
userEntry=input("Enter your username: ")
passwordEntry =input("Enter your password:" )
while userEntry != username and passwordEntry != password:
	print ("Error! Details not accepted. Please try again.")
	userEntry=input("Enter your username: ")
	passwordEntry =input("Enter your password:" )
print ("Correct! Welcome to Speyside High")
```


## Tasks

1. Copy the code example above. What would happen if the condition was changed from `and` to `or`? Would the program still work?
2. Create a program that asks the user to enter a number lower than 20 but higher than 5. While the number is 5 or lower or the number is 20 or above, it should ask them to re-enter a number. When they have entered a valid number, the program should output a message saying "CORRECT!"