[<- Return Home](https://speysidecs.github.io/)
# SDD 2.1 - Fixed Loops  

We can use a fixed loop to loop lines of code for a *fixed* amount of times, in other words, code will be repeated as many times as we need it to. 

  ## Learning Intention
  1. Repeat code using a fixed loop

## Success Criteria
1. Implement a fixed loop in Python using the `for` command
2. Explain the purpose of a fixed loop
3. Understand the use of the counter variable in a fixed loop

## Examples
The following example shows a chunk of code which would display the message 6 times.
```python
for counter in range(6):
	print ("I'll be displayed 6 times!")
```
 Would display:
```output
I'll be displayed 6 times!
I'll be displayed 6 times!
I'll be displayed 6 times!
I'll be displayed 6 times!
I'll be displayed 6 times!
I'll be displayed 6 times!
```

Lets break that example down bit by bit
* `for` is the command to start a fixed loop
*  `counter` is a special type of variable that counts the number of times a loop has been repeated. it doesn't need to be called *counter* we could name it anything.
*  `in range(6)` means repeat 6 times, this could be an integer value or a variable which contains an integer value e.g `in range(num)`
*  Don't forget the colon `:`
* Code inside the loop must be *indented* from the side of the page. That's how Python knows what to repeat.
  
## counter Variable

The counter variable counts the number of times we have repeated a loop. This is quite useful for many reasons which you will see later in the course. We can access the value of the counter variable as the loop repeats.

```python
for counter in range(5):
	print ("counter is " + str(counter))
```
Would display
```output
0
1
2
3
4
```
Notice how the value starts at 0 - that means even though the range is set to 5, it will never reach 5 because in programming we start counting from 0.

## Task

Create a program that asks for a user's name and how many times they would like to be greeted, and then says 'Hello *their name* as many times as they would like to be greeted.

For example, if I entered my name was Marc, and I wanted to be greeted 3 times, it would display:

```output
Hello Marc
Hello Marc
Hello Marc
```