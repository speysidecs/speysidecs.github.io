# DDD 5.3 Equi-joins and foreign keys

# Learning Intention
* Work with a relational database

# Success Criteria
* I can query  a relational database using equi-joins
* I can describe the purpose of a foreign key in a relational database

## Foreign Key
A foreign key is a Primary Key from *another* table which allows us to link data in one table to another. 

## Related Tables
Look at the following two tables:
![image](image.png)

![image](image_2.png)

They are *related*.
Every guidance teacher is in a house.
Every pupil is in a house.

This means the data is related using the house field in both tables.

In the guidance table, the house is set as the Primary Key.
In the pupil table, the house is set as the Foreign Key (the primary key from a related table).

This joins the two tables together in a relationship called a "one-to-many" relationship: one house has many pupils.

It is one house as each pupil can only be in a single house.

## Displaying information using equi-joins
An equi-join allows us to display information from more than one table. To create an equi-join, we use the `WHERE` clause.

An equi-join is performed on the foreign key.

For example, if we wanted to display the pupil name with their house colour, we would need data from both the pupil table (for their name) and the guidance table (for the colour). 

```sqlite
/*selecting the fields we need*/
SELECT pupil, colour
/*select both tables*/
FROM pupil, guidance
/*create the equi-join on the foreign key*/
WHERE guidance.house = pupil.house;
```

Notice we have included the tablename in the `WHERE` clause as both fields share the same name (house).

This would display the following list:
![image](image_3.png)

## Task
1. Create a query which displays the pupil name and their guidance teacher.
2. Create a query which displays the pupil name and their guidance teacher, where the level is Higher.
3. Create a query which displays the pupil name and their guidance teacher, where the level is N5, ordered by house group.