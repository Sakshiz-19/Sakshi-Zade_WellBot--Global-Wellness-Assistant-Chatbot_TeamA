ASSIGNMENT 2

	BASIC SQL METHODS
Basic SQL Methods (CRUD Operations)
SQL methods are the primary commands used to interact with data within a database. These are often referred to as CRUD (Create, Read, Update, Delete). 

1. SELECT (Read)
The most common method, used to retrieve data from one or more tables. 
•	Syntax: SELECT column1, column2 FROM table_name;
•	Example: Retrieve names of all students in the 'History' department.
SELECT name FROM students WHERE department = 'History';
 
2. INSERT (Create)
Used to add new rows of data into a table. 
•	Syntax: INSERT INTO table_name (col1, col2) VALUES (val1, val2);
•	Example:
INSERT INTO students (id, name, department) VALUES (101, 'John Doe', 'Science');
 
3. UPDATE (Update)
Used to modify existing records. Note: Always use a WHERE clause to avoid updating every row in the table. 
•	Syntax: UPDATE table_name SET col1 = val1 WHERE condition;
•	Example:
UPDATE students SET department = 'Math' WHERE id = 101;
 
4. DELETE (Delete)
Used to remove records from a table. 
•	Syntax: DELETE FROM table_name WHERE condition;
•	Example:DELETE FROM students WHERE id = 101;
 
SQL JOINs 
A JOIN clause is used to combine rows from two or more tables based on a related column between them. 
Example Tables for Reference:
•	Table A (Students): Contains StudentID and StudentName.
•	Table B (Grades): Contains StudentID and Grade. 
1. INNER JOIN
Returns records that have matching values in both tables. If a StudentID exists in Table A but not in Table B, that record is excluded. 
•	Example: Get a list of students who have assigned grades.
sql
SELECT Students.StudentName, Grades.Grade
FROM Students
INNER JOIN Grades ON Students.StudentID = Grades.StudentID;

2. LEFT (OUTER) JOIN
Returns all records from the left table (Students), and the matched records from the right table (Grades). If there is no match, the result is NULL for the right table. 
•	Example: List all students and their grades (including those who don't have a grade yet).
sql
SELECT Students.StudentName, Grades.Grade
FROM Students
LEFT JOIN Grades ON Students.StudentID = Grades.StudentID;

3. RIGHT (OUTER) JOIN
Returns all records from the right table (Grades), and the matched records from the left table (Students). 
•	Example: Useful if you want to find grades that might not be attached to a valid student ID



.
4. FULL (OUTER) JOIN
Returns all records when there is a match in either left or right table records. It combines the effect of both Left and Right joins. 
________________________________________
Summary Comparison Table

Method/Join 	Primary Purpose	Key Characteristic
SELECT	Data Retrieval	Uses WHERE to filter.
INSERT	Data Entry	Adds new rows.
INNER JOIN	Combined Matching	Only returns rows with a match in both tables.
LEFT JOIN	Inclusive Left	Returns everything from the first table + matches.


•	SELECT → Retrieves data from a table.
Example: SELECT name FROM Students;

•	WHERE → Filters rows based on a condition.
Example: SELECT name FROM Students WHERE student_id = 1;

•	ORDER BY → Sorts results in ascending or descending order.
Example: SELECT name FROM Students ORDER BY name ASC;

•	GROUP BY → Groups rows sharing a value, often used with aggregates.
Example: SELECT course_name, COUNT(*) FROM Courses GROUP BY course_name;

•	HAVING → Filters grouped results after aggregation.
Example: SELECT course_name, COUNT(*) FROM Courses GROUP BY course_name HAVING COUNT(*) > 2;

•	JOIN → Combines rows from multiple tables using a related column.
Example:SELECT s.name, c.course_name FROM Students s INNER JOIN Courses c ON s.student_id = c.student_id; 


•	COUNT → Returns the number of rows.
Example: SELECT COUNT(*) FROM Students;

•	SUM → Adds up numeric values.
Example: SELECT SUM(marks) FROM Results;

•	AVG → Calculates the average of numeric values.
Example: SELECT AVG(marks) FROM Results;

•	MIN / MAX → Finds the smallest or largest value.
Example: SELECT MIN(marks), MAX(marks) FROM Results;

•	INSERT → Adds new rows into a table.
Example: INSERT INTO Students (student_id, name) VALUES (3, 'Rahul');

•	UPDATE → Modifies existing rows in a table.
Example: UPDATE Students SET name = 'Neha Sharma' WHERE student_id = 2;

•	DELETE → Removes rows from a table.
Example: DELETE FROM Students WHERE student_id = 3;

•	CREATE TABLE → Creates a new table.
Example:CREATE TABLE Students ( student_id INT PRIMARY KEY, name VARCHAR(50) ); 

•	ALTER TABLE → Modifies table structure.
Example: ALTER TABLE Students ADD age INT;

•	DROP TABLE → Deletes a table permanently.
Example: DROP TABLE Students;

•	GRANT → Gives permissions to a user.
Example: GRANT SELECT ON Students TO user1;

•	REVOKE → Removes permissions from a user.
Example: REVOKE SELECT ON Students FROM user1;

•	COMMIT → Saves changes permanently.
Example: COMMIT;

•	ROLLBACK → Undoes changes since last commit.
Example: ROLLBACK;

•	SAVEPOINT → Sets a checkpoint in a transaction.
Example: SAVEPOINT sp1;

1. Arithmetic Operators
Used for mathematical calculations on numeric data.
Operator, Description,                            Example
+,        Addition,                           SELECT Price + 10 FROM Products;
-,        Subtraction,                        SELECT Price - 5 FROM Products;
*,         Multiplication,                    SELECT Price * 1.18 FROM Products; (Adding 18% Tax)
/,        Division,                           SELECT Total / 2 FROM Orders;
%,        Modulo (Remainder),                 SELECT ID % 2 FROM Users; (Find even/odd IDs)

2. Comparison Operators
Used to compare two values. These return a boolean (True/False).

Operator,           Description,                      Example
=,                 Equal to,                          SELECT * FROM Users WHERE name = 'Avinash';
!= or <>,          Not equal to,                      SELECT * FROM Users WHERE status <> 'Active';
>,                 Greater than,                      SELECT * FROM Products WHERE Stock > 100;
<,                 Less than,                         SELECT * FROM Products WHERE Price < 500;
>=,                Greater than or equal to,          SELECT * FROM Students WHERE Marks >= 35;
<=,                Less than or equal to,             SELECT * FROM Students WHERE Sem <= 5;

3. Logical Operators
Used to combine multiple conditions or negate them.

Operator,                  Description,                          Example
AND,                       True if all conditions are true,      WHERE Age > 18 AND City = 'Bellary'
OR,                        True if any one condition is true,    WHERE Sem = 5 OR Sem = 6
NOT,                       Reverses the condition,               WHERE NOT City = 'Pune'
BETWEEN,                   Within a range (inclusive),           WHERE Price BETWEEN 100 AND 500
IN,                        Matches any value in a list,         "WHERE Language IN ('Python', 'Java', 'C++')"
LIKE,                      Search for a pattern,                 WHERE Name LIKE 'A%' (Starts with A)
IS NULL,                   Checks for empty values,               WHERE email IS NULL
EXISTS,                    Checks if a subquery returns data,     WHERE EXISTS (SELECT 1 FROM Orders WHERE user_id = u.id)

4. Set Operators
Used to combine the results of two different SELECT statements.

UNION: Combines distinct rows from both queries.

UNION ALL: Combines all rows (including duplicates).

INTERSECT: Returns only common rows between both queries.

EXCEPT (or MINUS): Returns rows from the first query that are not in the second.

Ex: SELECT * FROM chats 
WHERE mood = 'Sad' AND timestamp > '2026-02-11';

