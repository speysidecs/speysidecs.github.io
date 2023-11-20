# DDD 1.3 SELECT Queries with ORDER BY

## Learning Intention
* Produce results in an ordered format
  
## Success Criteria
* I can use `ORDER BY` to sort results
* I can order my results in `ASCENDING` or `DESCENDING` order

## Using ORDER BY to sort results using one field

The ORDER BY clause has only two options
* `ASC`  - ascending order - alphabetical, or low to high
* `DESC` - descending order - reverse-alphabetical, or high to low.

#### Examples

Given the following table called `staff`:
![image](image_2.png)

```SQL
SELECT * FROM staff ORDER BY surname ASC;
```
Would display all teachers sorted by surnames in alphabetical order (Burns first).

```sql
SELECT * FROM staff ORDER BY surname DESC;
```
Would display all teachers sorted by surnames in reverse-alphabetical order (Picksley first).

## ORDER BY on two fields

Take the following table (`menu`) which has 5 fields: `menuNumber, item, price, calories, vegan`.

![image](image.png)

We could sort on items, and then calories. This would sort the list into alphabetical order first, then by calories after it. This would put the vegan cheeseburger above the non-vegan cheeseburger. 

```Sql
SELECT * FROM menu ORDER BY item ASC, calories ASC;
```

Which would give the results: 
![image](image_3.png)

Note that when there are two items with identical names, the calorific (calories) value is then used to sort the items. In the above example,  all items are put into alphabetical order, then the duplicate named items (cheeseburger, nuggets) are sorted into calorie order.

When sorting by more than one field they are separated by commas. 

## Tasks
1. Create a query file for each task.
2. Display the entire menu in order of calories in the meal
3. Display the entire vegan menu ordered by price
4. Display cheeseburgers ordered by calories
5. Display the entire menu, in reverse alphabetical order, then by price low to high.
6. Display only items which are less than or equal to 600 calories.