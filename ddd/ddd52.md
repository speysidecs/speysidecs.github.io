# DDD 5.2 Primary Keys - Example Values

# Learning Intention
* Describe the purpose of a primary key in a database table
* Select, or create an appropriate primary key in a database table

# Success Criteria
* I can identify an existing field in a table which could be a primary key, or suggest the creation of a new field to be the primary key

## Primary Key
As a reminder, a Primary Key is a field that represents a unique identifier for a record in a table. This means that no other record can contain that exact value.


## Example Data Set
![image](image.png)

Look at the above data set. There are no unique fields in this table, this means there can be no primary key.

* pupil - we cannot assure that the pupil's name will be unique (There are two pupils with the value `Aiden`)
* house - this is not unique, there are many pupils in each house
* course - this is not unique, there are many pupils on each course
* year - this is not unique, there are many pupils in each year

## Options for a Primary Key
Option 1 is to find another piece of data which could represent a unique value. Some primary keys which may be a good fit for this data set...

* Glow username - every pupil has a unique Glow username
* SQA number - every pupil has a unique SQA number for exam purposes

Option 2 is to create an artificial piece of data like an ID Number, and assign each pupil a number. In this class, we have 21 pupils, so we could assign each pupil a number between 1 and 21.

 

## Task
In `main.sql`, change the `SELECT` query so that it displays a description of an example of a Primary Key you would create for this table. You must choose 1 of the options above, or suggest a different primary key.