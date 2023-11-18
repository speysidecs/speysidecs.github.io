# Coursework Practice 1:  Code only

This coursework example will have a coding problem at the required level. The coursework involves more than just coding, however, it does make up the bulk of the marks. This initial practice will allow us to assess your progress of coding at National 5 level.

### Program Analysis
Professor Dumbledore is overseeing this years Magical Tournament.

Teams of four players try to capture multiple eggs from a dragon. 

He wishes for you to create a program to get the inputs for the four players, calculate the total number of eggs captured by the players, and the average number of eggs captured by each player in the team. The program should then output the number of points scored by the team.

#### Inputs
*	a valid number of eggs gathered by each of the four witches or wizards (each witch or wizard is entered separately)

#### Processes
*	calculate the total eggs gathered by all players
*	calculate an average (mean) number of eggs
*	determine if the players have earned points

#### Outputs
*	The average number of eggs captured and total eggs captured should be displayed
*	a message is displayed if one point has been earned
*	a message is displayed if the additional point has been earned
*	a message is displayed if no points have been earned


#### Assumptions
*	the number of eggs a single player can gather is greater than or equal to 0 and less than or equal to 20
*	the average should be displayed to two decimal places
*	one point is earned if the total number of eggs is greater than 15. An additional point is earned if the average number of eggs is greater than or equal to 5.

## Program Design

```
1.0 Initialise variables and data structures as required
2.0 Calculate total and average eggs gathered
3.0 Calculate points earned
```
Refinements are shown below
```
2.1 For the four players
	2.1.1 Get the number of eggs captured
	2.1.2 Add on to total eggs captured
2.2 Calculate the average (total/4)
2.3 Round the average to two decimal places
```

```
3.1 Display average and total eggs caught
3.2 If one point is earned
	3.2.1 Display message saying "one point earned"
3.3 If condition for additional point is earned
	3.3.1 Display message "two points earned"
3.4 If no points were earned
	3.4.1 Display message "no points earned"
```

Implement this program given the analysis and design above.