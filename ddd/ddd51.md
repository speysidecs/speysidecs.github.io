# DDD 5.1 Primary Keys

# Learning Intention
* Describe the purpose of a primary key in a database table

# Success Criteria
* I can describe the use of a primary key within a database table.

## Primary Key
We have discussed "unique fields" in both `UPDATE` and `DELETE` queries. These unique identifiers for a record in a table have a special name: primary keys. You all have many primary keys attached to you in real life - your SQA number, your national insurance number, your NHS number. Each of these unique codes identifies you in various databases.

When signing up to a website, your e-mail address tends to be used as a unique primary key for your account - thats why if you already have an account with your email address, you can't make another. 

## Creating Primary Keys
At National 5 level you only have design primary keys on paper. Setting a primary key is done during the `CREATE TABLE` query, which is done at Advanced Higher level.

It looks like the following example on line 4:
![image](image.png)

In this example the table has been set for the glowusername to be the field which uniquely identifies a record - no other record should have this value. 

## Task
In `main.sql`, change the `SELECT` query so that it displays a description of what a primary key is. Note, here we are using `SELECT` like a print command!