# DDD 7.1 Database Challenges

# Learning Intentions
1. Test your SQL skills up to coursework level

# Success Criteria
1. I can use an appropriate query type to perform a task (`SELECT, UPDATE, INSERT, DELETE`)
2. I can use appropriate clauses in my queries, like `WHERE, FROM, AND, ORDER BY`
3. I can use equi-joins when appropriate to get related information

## Introduction
The Speyside Librarian needs to create a new database to manage the books which they have in stock. In database there are two tables, one to store books and one to store author details.

A data dictionary is displayed for the two tables below, which you can reference when completing the queries.

`Required` shows fields which must have data entered for them.
`Validation` shows checks which restrict the values which can be entered into the database.

![image](image.png)

An entity relationship diagram is shown below. This displays the entities (tables), their attributes (fields) and the relationship between the two entities. You can use this to help you plan your queries.

![image](image_2.png)


## Tasks

Using the library.db file, produce a file for each of these queries, consulting your previous tasks and code journals as you go. 
#### Level 1
`Save each of these queries as a new file in your database file – e.g Level 1-1.sql and Level 1-2.sql.`

`Remember to use the .read command to read your new query and test it out.`
1.	Display a list of all fields within the book table
2.	Display a list of all fields within the author table
3.	Display a list of all books by authorID 1
4.	Display a list of all fiction books
5.	Display a list of all books that have been borrowed (1)
6.	Display a list of all books that have not been borrowed
7.	Display a list of all books by authorID 1 that have not been borrowed
#### Level 2
1.	Display a list of books, sorted by authorID highest to lowest, then borrowed lowest to highest.
2.	The book with the ISBN 1 has now been returned to the library. Update this record accordingly.
3.	A new book by JK Rowling has been published. It is called The Tales of Beedle the Bard, it is considered an easy read and has not yet been borrowed. Give it an appropriate ISBN number and add it to the book table.
4.	Unfortunately, Fantastic Mr Fox has been lost. Remove it from the database using its primary key.
5.	The Librarian has decided that Terry Pratchett's record should be updated to read his forename as Sir Terry. Update this record. 
#### Level 3
1.	Display a list of all books by JK Rowling, including the fields – title, forename, surname and borrowed status.
2.	Display a list of all books by Roald Dahl, including the fields – title, forename, surname and borrowed status which are currently not borrowed.
3.	Display a list of all book titles, forename and surname for British authors only, ordered by surname alphabetically, then book ID descending. 
