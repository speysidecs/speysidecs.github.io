# DDD 3.1 UPDATE a table

## Learning Intention
* Modify the contents of an existing table

## Success Criteria
* Use the `UPDATE` query to change the contents of a target record within a table

## The UPDATE query
The `UPDATE` query is used to modify the contents of a table. Care must be taken when modifying a table by targetting a unique value within the table. 

The query is structured as follows:
```sql
UPDATE tablename
SET fieldName = "value"
WHERE uniqueField = "value"
```

## Worked example

For example, if we were modifying a table called `phonebook` which looked like this:

![image](image.png)

We would see that neither the fname or sname are unique. If we updated the table based on either one of these, we would update multiple phone numbers. 

So what if we want to update John Smith (078954321)'s name to John-Pierre Smith? We would have to target the only unique field in the table - the phone number.

```sql
UPDATE phonebook
SET fname = "John-Pierre"
WHERE phoneNumber = "078954321"
```

## Tasks
1. The price of vegan nuggets has changed to 2.99 due to supply chain issues.
2. The calories of cheeseburgers has increased to 800 due to a new cheddar being used.
3. The vegan cheeseburger is now using "Beyond" Burgers and the name must be changed to "beyond cheeseburger"