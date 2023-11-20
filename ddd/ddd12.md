# DDD 1.2 SELECT Queries using WHERE

## Learning Intention
* How do I use SQL to find specific results?

## Success Criteria
* I can use the WHERE clause to specify a condition for the results of my query

## Tables
In this example, we have created a table in ```main.sql``` which is called ```pupil```. At N5 level you do not need to create your own tables, but may need to modify them. 

You can view the entire table using the following query:

```sql
SELECT * FROM pupil;
```

## WHERE clause
A ```SELECT``` query can include a ```WHERE``` clause which is used to specify a condition for the records we wish to return. For example:

```sql
SELECT * FROM pupil WHERE house = "Sith";
```
The above query will return all pupils where their house is equal to the value `Sith`.

We can use the same logical operators we used in conditional statements in programming, like: 

| symbol |  purpose  |
|--------------| -------------|
| >|greater than (numbers)|
|< |less than (numbers)|
|>=|greater than or equal to (numbers)|
|<=|less than or equal to (numbers)|
|=|equal to|
|!=|does not equal|

## WHERE with Boolean Operators

Using Boolean logic we can create advanced conditions which meet one or more conditions using `AND` and `OR`.

With `AND` both parts of the condition must be true.

With `OR` only one part of the condition must be true. 

For example: 


```sql
SELECT * FROM pupil WHERE surname = "Skywalker" AND house = "Jedi";
```
The above query shows records where surname is equal to Skywalker and the house is equal to Jedi.

Output: 
![image](image.png)

```sql
SELECT * FROM pupil WHERE surname = "Skywalker" OR house = "Jedi";
```
The above query shows records where surname is equal to Skywalker or house is equal to Jedi.

Output: 
![image](image_2.png)

### Tasks
1.  Create a file for each of your queries below.
2.  Display all fields for pupils who's midichlorian count is higher than 500.
3.  Display only the house and glowusername for pupils who's midichlorian count is less than 710.
4.  Display all pupils with the surname Skywalker and house Jedi.
5.  Display all pupils with the surname Skywalker and surname Kenobi.
6.  Display all pupils who are not Sith and the surname Skywalker or surname Kenobi.