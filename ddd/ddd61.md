# DDD 6.1 Validation

# Learning Intention
* Limit the data which can be entered within a database

# Success Criteria
* I can implement validation within a database to prevent incorrect data from being entered
* I can describe five types of validation applied to a database

## Validation
Validation is applied at the table design stage. So far we have just worked with a database which has already been created. In this task, you will have to modify a database which has not yet been fully implemented.

## Types of validation
At National 5 level you must know 5 types of validation.
* Unique - only one of this value can appear in this column in a table
* Presence check - make sure there is a value in a field (Required value)
* Range check - make sure a value is within an acceptable range
* Length check - make sure a value has a specified number of characters and not less
* Restricted choice - value entered must be in a list of values

## Example implementation
In the following example, we will be working with a `CREATE TABLE` statement. It is not required at National 5 level that you create your own tables using this code, but you must understand it.

### Table Design
In this example, we will implement the following design: 

![erd - ships n5](erd%20-%20ships%20n5.png)

For the ship table we know the following information:
* Each model will have a unique name
* An engine type code made up of four alpha-numeric characters
* Nickname for the ship
* The name of the manufacturer
* A class, from one of the following: fighter, bomber, support or interceptor
* Firepower between 0 and 10
* Shields between 0 and 10

A `CREATE TABLE` statement makes a table, then defines the fields (columns) within it. 

The statement for this table is shown below, with *no validation*.

```sqlite
CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4),
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(15),
	firepower INTEGER,
	shields INTEGER);
 ```

 This creates the fields in the table `ship`, where `VARCHAR()` is a text field, with the maximum number of characters which can be stored in the field in brackets.

## Unique Check
We can implement a unique check on a field by using the keyword `UNIQUE` before the comma (which tells SQL we have finished defining a field).

In the example, this has been applied to the `engineType` field this would look like:
```sqlite
CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4) UNIQUE,
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(15),
	firepower INTEGER,
	shields INTEGER);
 ```
If a duplicate value was entered through an` INSERT` query the following error would be displayed:

```
Error: near line 19: UNIQUE constraint failed: ship.engineType
```

 ## Presence Check

 We can implement a presence check by using the keywords `NOT NULL` in the field definition.

 In the example below we have applied this to the `firepower` field.

 ```sqlite
 CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4) UNIQUE,
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(15),
	firepower INTEGER NOT NULL,
	shields INTEGER);
 ```
If a firepower field was left blank after the `NOT NULL` validation check was set then the following error would be displayed: 
```
Error: near line 13: NOT NULL constraint failed: ship.firepower
```
 ## Range Check

 We can implement a range check using the `CHECK` constraint.
 For example, for a field called `fieldname` we could check that its values are greater than 5 and less than 20 as follows:
```sqlite
 CHECK (fieldname >5 and fieldname < 20)
```
As the `CHECK` constraints can be long, it is good practice to take a new line after the type of the field, and before the comma, to write your `CHECK` constraint.

For example, lets apply a range check of greater than 10 and less than 100 on the firepower field:

 ```sqlite
  CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4) UNIQUE,
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(15),
	firepower INTEGER
		CHECK (firepower >10 and firepower <100),
	shields INTEGER);
 ```
 If the range check failed when a value was being inserted, we would get the following error:
 ```
 Error: near line 14: CHECK constraint failed: firepower >10 and firepower <100
 ```

 ## Length Check
 A length check will use the `CHECK()` constraint as well. Let's say we want the class to be exactly 15 characters in length, we would write the following code:
```sqlite
   CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4) UNIQUE,
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(15)
		 CHECK (length(class) = 15),
	firepower INTEGER,
	shields INTEGER);
 ```
 In this example, if we tried to add a record to the database with a class which wasn't exactly 15 characters it would produce the following message:
 ```
 Error: near line 14: CHECK constraint failed: length(class) = 15
 ```

 ## Restricted Choice
 A restricted choice validation restricts the value entered to one from a list within the `CHECK()` constraint.

 For example:
 ```sqlite
 CHECK(sauce = "ketchup" OR sauce = "brown" OR sauce = "chilli")
 ```
 The above code restricts a field called `sauce` to the three values in the check - ketchup, brown or chilli.
 
 In our ship example:
 ```sqlite
   CREATE TABLE ship (
	model VARCHAR(50) PRIMARY KEY,
	engineType VARCHAR(4) UNIQUE,
	nickname VARCHAR(20),
	manufacturer VARCHAR(50),
	class VARCHAR(20)
		CHECK (class = "Classy" OR class = "Not classy"),
	firepower INTEGER,
	shields INTEGER);
 ```

 If the value entered wasn't `Classy` or `Not Classy` then the following message would be displayed:
``` 
Error: near line 14: CHECK constraint failed: class = "Classy" OR class = "Not classy"
```

### Task
In `main.sql` you will find the `CREATE TABLE` statement with no validation. Implement the following validation checks, and then test them using INSERT statements which meet the required criteria for each constraint, then some which would generate errors.

Use the following data dictionary to implement the validation.

![image](image.png)