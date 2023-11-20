# DDD 2.2 Persistent Databases

# Learning Intention
* I understand that my database changes will not be persistent in repl.it unless I commit the changes

# Success Criteria
* I can use the `.save` command to save the current state of a database
* I can use the `.open` command to reload a persistent database file

# SQA Exam
The dot commands (.read, .save, .open) are not part of your SQA Exam but are useful for working with databases.

## Using .save and .open
Our main.sql files so far have contained the code to create our tables. This means every time we run them, your database is created fresh again. 

This does not work when we wish to add, modify and delete records. However we can save the state of any database running on repl.it using the following command:

`.save filename.db`

This will allow you to save your database in its current state. This is useful for saving your database for tasks that require you to prove you have inserted (or modified or deleted, too) a record. 

You could save the database at the end of each task in your coursework to be able to return to the state of the database at any given task.

To use this database in its state again, you will need to use the `.open filename.db` command. 

When we open a database with `.open` all changes we make to that database will be saved automatically - so before making any changes you don't want to commit to you may want to `.save.` a new copy.


## main.sql
If your main.sql has code to `CREATE TABLE`s then it will always recreate the table and any changes you have made will not be visible in the results of queries.

### Tasks

1. In main.sql use the `.open` command to open the file `menu.db`
2. Show all records from the `menu` table - note what this looks like.
3. Save a copy of the menu database called menuExpanded.db using `.save menuExpanded.db`
4. Use `.open menuExpanded.db` to open the copy of the database
5. Insert a new record for menu item 8 - the hot dog, which is 1.99, 400 calories and is not vegan (False).
6. Now switch between menu.db and menuExpanded.db and show the records in both, you should see that your new item - the hot dog is in one database and not the other.