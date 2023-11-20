# Using the INSERT INTO query

## Learning Intention
* Adding a new record to a database

## Success Criteria
* I will be successful if I can add a new record to the database using the `INSERT INTO` query.



## INSERT INTO queries

An `INSERT INTO` query takes the following form:

```sql
INSERT INTO tablename (field1, field2, field3...)
VALUES ("value1",2,3.0);
```
* Where tablename is the name of the table we want to add values to.
* Where (field1,field2,field3...) are the names and order of the fields we want to insert values into.
* Where the values in brackets after `VALUES` are the values of the fields, in the correct order.

We can leave out the fields after the table name, as long as we are sure our values are in the correct order, for example:

```sql
INSERT INTO tablename
VALUES ("value1",2,3.0);
```
This can cause errors if you put the data in the wrong order.

To view your changes, your `INSERT INTO` query must be followed by a `SELECT` query - otherwise the changes will be lost the next time you press run.

For example:

```sql
INSERT INTO staff (title, surname, subject, favouriteColour)
VALUES ("Mr","Harris","Business","Red");

SELECT * FROM staff;
```

## Tasks

1. Add and display a new record to the database for the following item:
8, Ice cream, 0.99, 300, 0