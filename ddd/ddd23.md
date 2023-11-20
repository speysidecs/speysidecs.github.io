# DDD 2.3: INSERT multiple records

## Learning Intentions:
* Add more than one record to a database using a single query

## Success Criteria
* I can construct an `INSERT INTO` query to add more than one record at a time

## Structuring the query
Formatting an `INSERT INTO` query for adding multiple records is not very different from a single record as shown below.

```sql
INSERT INTO staff (title, surname,subject,favouriteColour)
VALUES
("Mr","Harris","Business","Red"),
("Miss", "McWilliam", "English","Orange"),
("Mrs", "Boardman", "English","Green"),
("Miss", "Childs","Mod Studies","Yellow");
```
Each record is listed within a set of brackets, and if another record should be added afterwards, is followed by a comma. The final record to be added is finished with a semi-colon.

### Task
The menu has been expanded, add the following items to the `menu` table using one query. 
```
Item 8, Hotdog, 1.99, 400 calories, not vegan.
Item 9, Hotdog 2.10, 300 calories, vegan.
Item 10, ice cream, 0.99, 350 calories, not vegan.
Item 11, frozen coconut cream, 0.99, 400 calories, vegan.
```