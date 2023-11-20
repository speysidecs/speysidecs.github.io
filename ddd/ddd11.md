# DDD 1.1 SELECT Queries

## Learning Intention
* What is the purpose of SQL?
* How do I use SQL to retrieve information from a database?

## Success Criteria
* I can describe the purpose of SQL
* I can use a SELECT query to retrieve information from a table
a
## SQL
SQL stands for Structured Query Language. It is a special type of language used to create, read, update and delete information in databases.

Databases are structures which hold data within tables.

## Tables
In this example, we have created a table in ```main.sql``` which is called ```pupil```. At N5 level you do not need to create your own tables, but may need to modify them. 

The entire table looks like this:

![image](image.png)

Our table contains *records* (rows) of data about pupils at 
 a school. Each record (row) contains information about one student. 

 Our records contain *fields* which are individual pieces of data about each record. For example, each record has a ```firstname``` field.

## Repl.it set up
In each of your lessons, tables will always be created within ```main.sql```. If you need to modify the table structure, you should do so in this file. 

At the bottom of ```main.sql``` you will see a command called `.read queries.sql`. This command is used to launch other SQL query files, like `queries.sql`. This is useful for keeping track of tasks completed. You can have as many SQL files in your project as required but you should only `.read` one query file at a time from your `main.sql` file. 


## SELECT Queries
A ```SELECT``` query is the main query you will use. It is used to read and display data from your database.

A `SELECT` query is formatted as follows:

```sql
SELECT * FROM tablename;
```

In the above example, `*` means display all fields. The keyword `FROM` should be followed by the name of the table we are retrieving information from. 

If our table was called `staff` then we would write:

```sql
SELECT * FROM staff;
```

Queries must be ended by a semi-colon (;)

## SELECT Queries Displaying Only Required Fields
Whilst we sometimes want to display every field in our results, sometimes we only want to display certain fields. 

The staff table contains the following information about staff at Speyside High:

![image](image_2.png)

It has 5 fields:
```
* title
* surname
* subject
* favouriteColour
* job
```

If we only wished to display the title, surname and subject of the teachers we would use the following query.

```SQL 
SELECT title, surname, subject FROM staff;
```
This would display as:

![image](image_3.png) 

In the above query, we listed the fields required in the results after the `SELECT` keyword. 

### Tasks
1.  In ```queries.sql``` create a query to display all information in the pupil table. 

2. Create a new file called `queries2.sql` in the Files section.
3. In `queries2.sql` create a query to show only the `glowusername` and `surname` of the records.
4. Update `main.sql` to `.read queries2.sql` instead of the command to read `queries.sql`