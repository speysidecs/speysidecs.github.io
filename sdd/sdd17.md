[<- Return Home](https://speysidecs.github.io/)
# SDD 1.7 If and elif (else if) 

Our first condition in our program must start with `if`, but we can have as many conditions as we want underneath the first condition using `elif` which stands for *else if*. An `elif` is only run when the condition before it is `False` - it is like how an `else` only happens when the `if` condition is `False`.

  ## Learning Intentions
  1. Making decisions in programs
  2. Checking multiple conditions in programs

## Success Criteria
1. Use at least one `elif` statement to make a decision

---
## Examples

In English-like code (psuedocode) an if statement runs like this:

```
if  condition is True then:
	Code to run if condition above is true. 
elif condition is True then: 
	Code to run if condition above is true.
elif condition is True then:
	Code to run if condition above is true.
else then:
	Code to run when the if and the elifs are not true
```
The `elifs` will only be run when the `if` is not true, and the second `elif` will only run if the first `elif` is false. The `else` is only run when all other conditions are false.

### Python Example

```python
num1 = int(input("Enter a number"))
num2 = int(input("Enter another number"))
 
if num1 > num2:
	print (str(num1) + " is bigger.")
elif num1 < num2:
	print (str(num2) + " is bigger")
else:
	print("The numbers are the same")
```
In your code journal, copy the example above and answer the question:

	Why do we not need to use another `elif` to figure out if the numbers are the same?

 ## Task
 Look in the `main.py` file and follow the comment to complete the code.

Add to the program so that if the user inputs 'Music' they get a message saying 'Not bad, but Computing is better'.  For all other subjects the user should get a message saying 'How wrong can you be? Computing is waay better than that!'