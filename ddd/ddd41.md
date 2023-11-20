# DDD 4.1 DELETE a record

## Learning Intention
* Remove a targeted record from the database table
## Success Criteria
* Use the `DELETE` query in order to remove a targeted record from the table.

## DELETE Query Structure

Like our other queries, the `DELETE` query uses the `WHERE` clause to target a specific field and should be used to target a unique identifier to avoid errors like deleting multiple records.

```SQL
DELETE FROM tableName
WHERE uniqueField = "value";
```

## Worked Example
We will return to the `phonebook` example.
![image](image.png)

Any `DELETE` query where we target a surname or forename in the above example would result in multiple records being deleted. To avoid this we will delete using a `WHERE` clause which specifies the `phoneNumber`.

To delete John Smith 078954321 from the table we would use the following query:
```sql
DELETE FROM phonebook
WHERE phoneNumber = "078954321";
```

## Tasks
1. Delete the record for beefburgers from the table. They haven't been selling!
2. Delete vegan nuggets from the table.