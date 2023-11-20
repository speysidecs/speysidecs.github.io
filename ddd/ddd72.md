# Note
Your database task will be worth 15 marks (37% of total of coursework). The coursework in total is worth 40 marks (out of 120 available in the course).


Task  — part A requires candidates to analyse and design a database. In the real coursework you  must submit your evidence to the teacher before you get part B.

Task — part B is a separate section. This ensures that candidates do not access part A
and change their responses. This is because the task in Part B and access to the database may reveal answers to part A.

## Task 

You will get part A from your teacher and should complete this before reading beyond the point that tells you to stop.

ScotAuction sells property in Aberdeen, Dundee, Edinburgh, Glasgow, Inverness, Perth and
Stirling.

To register a property for sale, ScotAuction requests the following details from sellers:
name, email address, telephone number and home address. ScotAuction gives each seller a
unique ID and will contact the seller if an offer is made.

Every property registered for sale must have the following information recorded: house number, street, city, postcode, asking price and estimated property value. ScotAuction
generates a unique reference code for all properties. Sellers should also state the number of bedrooms in the property.
A seller can have multiple properties for sale. A property cannot be listed for sale without the seller’s details being recorded first.

ScotAuction wants to create a database to store the seller and property details.
# STOP! Get Sheet 2a from your teacher, then sheet 2b. Do not read any further until you have completed these and handed them in.

## Part C


You have a file in your repl called `homes.db` with two linked tables. 
Save each query as a sql file with the name of the task, e.g. `2ci.sql`

### 2ci
The asking price for propertyRef DUN-101 has been recorded incorrectly. This
should be changed from £105500 to £112000.

Implement an SQL statement that will make the required change to the asking
price.
(2 marks)

Save evidence of the implemented SQL statement.  Include your name and candidate number (if you know it!) in a comment on all evidence.

A comment can be written using `/*` to open and `*/` to close as follows: 
```sqlite
/*I'm a comment
over multiple
lines*/
```
### 2cii

Implement an SQL statement that will add the following details of a new seller to the database.

	sellerID: 1502
	sellerName: Eve Grace
	sellerAddress: 128 Cameron Drive Edinburgh EH4 5DS
	email: EveGrace@yehoo.net
	telephoneNumber: 0131 279100
(2 marks)

Save evidence of the implemented SQL statement.  Include your name and candidate number (if you know it!) in a comment on all evidence.

### 2ciii
ScotAuction is running a workshop to give sellers advice on how to achieve a higher sale price. Due to the limited spaces available, ScotAuction is only inviting selected sellers to attend.

Implement an SQL statement that will display the seller’s email address and telephone number and the property’s postcode for properties that have three bedrooms and an asking price of less than £150000.
(4 marks)

Save evidence of the implemented SQL statement.  Include your name and candidate number (if you know it!) in a comment on all evidence.

### 2d

ScotAuction would like a list of seller IDs and asking prices for properties in Glasgow.

The list should be sorted showing the lowest price first.

The following incorrect SQL statement is written:

```sqlite
SELECT Seller.sellerID, price
FROM Seller, Property
WHERE town = "Glasgow" AND Seller.sellerID = Property.sellerID
ORDER BY askingPrice ASC;
```
Test this SQL statement. 

State two reasons why this SQL statement produces the wrong output and save them in `2danswer.sql` (2 marks)

### 2e
The initial analysis identified the following functional requirements for the database.
It should:
* allow ScotAuction to store a seller’s email address and telephone number
* allow sellers to state an estimated value of their property
* record key details about each property, including the address and the number of
bedrooms
* limit the value and location of the properties that can be entered

Use the above analysis to evaluate the database in terms of fitness for purpose and store it as `2e.sql`. (1 mark)
