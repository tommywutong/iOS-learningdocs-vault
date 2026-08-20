---
title: Safari Client-Side Storage and Offline Applications Programming Guide
apple_id: TP40007256
resource_type: Guide
platform: Safari (Mobile)|Safari|iOS|macOS
topic: Data Management
technology: null
published: '2011-09-21'
source_url: https://developer.apple.com/library/archive/documentation/iPhone/Conceptual/SafariJSDatabaseGuide/RelationalDatabases/RelationalDatabases.html
archived_at: '2026-07-18T02:27:27.397079Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [Safari Client-Side Storage and Offline Applications Programming Guide](Introduction.md)


[Next](Using%20the%20JavaScript%20Database.md)[Previous](Key-Value%20Storage.md)

# Relational Database Basics

There are many kinds of databases: flat databases, relational databases, object-oriented databases, and so on. Before you can understand relational databases, you must first understand flat databases.

A flat database consists of a single table of information. The rows in the table (also called records) each contain all of the information about a single entry—a single person’s name, address, and ZIP code, for example. The row is further divided into fields, each of which represents a particular piece of information about that entry. A `name` field, for example, might contain a person’s name.

This design allows you to rapidly access a subset of the information in a table. For example, you might want to get a list of the names and phone numbers of everyone in a particular ZIP code, but you might not care about the rest of the address.

Consider this example of a medical database for an insurance company. A flat database (not relational), might contain a series of records that look like this:

| First Name | Last Name | Address | City | State | ZIP |
| --- | --- | --- | --- | --- | --- |
| John | Doe | 56989 Peach St. | Martin | TN | 38237 |
| Jane | Doe | 56989 Peach St. | Martin | TN | 38237 |

This example contains two rows, each of which contains information about a single person. Each row contains separate fields for first and last name, address, and so on.

At first glance, this database seems fairly reasonable. However, when you look more closely, it highlights a common problem with flat databases: redundancy. Notice that both of these entries contain the same address, city, state, and ZIP code. Thus, this information (and probably other information such as phone numbers) is duplicated between these two records.

A relational database is designed to maximize efficiency of storage by avoiding this duplication of information. Assuming that John and Jane are members of the same family, you could create a relational version of this information as shown in Table 3-1 and Table 3-2.

__Table 3-1__  Relational database “family” table

| ID | Last_Name | Address | City | State | ZIP |
| 1 | Doe | 56989 Peach St. | Martin | TN | 38237 |

__Table 3-2__  Relational database “familymember” table

| ID | First_Name | Family_ID |
| 1 | John | 1 |
| 2 | Jane | 1 |

Instead of two separate copies of the address, city, state, and ZIP code, the database now contains only one copy. The `Family_ID` fields in the `familymember` table tell you that both John and Jane are members of the family shown in the `family` table whose `ID` field has a value of 1. This relationship between a field in one table and a field in another is where relational databases get their name.

The advantages to such a scheme are twofold. First, by having only one copy of this information, you save storage (though in this case, the savings are minimal). Second, by keeping only a single copy, you reduce the risk of mistakes. When John and Jane have their third child and move to a bigger house, the database user only needs to change the address in one place instead of five. This reduces the risk of making a typo and removes any possibility of failing to update the address of one of their children.

When working with relational databases, instead of thinking only about what information your database describes, you should think of the relationships between pieces of information.

When you create a database, you should start by creating a conceptual model, or schema. This schema defines the overall structure of your database in terms of associations between pieces of information.

There are three basic types of relationships in databases: one-to-one, one-to-many (or many-to-one), and many-to-many. In order to use relational databases effectively, you need to think of the information in terms of those types of relationships.

A good way to show the three different types of relationships is to model a student’s class schedule.

Here are examples of each type of relationship in the context of a student class schedule:

- __one-to-one relationship__—A student has only one student ID number and a student ID number is associated with only one student.
- __one-to-many relationship__—A teacher teaches many classes, but generally speaking, a class has only one teacher of record.
- __many-to-many relationship__—A student can take more than one class. With few exceptions, each class generally contains more than one student.

Because of the differences in these relationships, the database structures that represent them must also be different to maximize efficiency.

- __one-to-one__—The student ID number should be part of the same table as other information about the student. You should generally break one-to-one information out into a separate table only if one or more of the following is true:

  - You have a large blob of data that is infrequently accessed (for example, a student ID photo) and would otherwise slow down every access to the table as a whole.
  - You have differing security requirements for the information. For example, social security numbers, credit card information, and so on must by stored in a separate database.
  - You have significantly separate sets of information that are used under different conditions. For example, student grade records might take advantage of a table that contains basic information about the student, but would probably not benefit from additional information about the student’s housing or financial aid.
- __one-to-many__—You should really think of this relationship as “many-to-one.” Instead of thinking about a teacher having multiple classes, think about each class having a single teacher. This may seem counterintuitive at first, but it makes sense once you see an example such as the one shown in Table 3-3.

  __Table 3-3__  The “classes” table

  | ID | Teacher_ID | Class_Number | Class_Name |
  | 1 | 1 | MUS111 | Music Appreciation: Classical Music |
  | 2 | 1 | MUS112 | Music Appreciation: Music of the World |

  Notice that each class is associated with a teacher ID. This should contain an ID from the `teacher` table (not shown). Thus, by creating a relationship from each of the many classes to a single teacher, you have changed the relationship from an unmanageable one-to-many relationship into a very simple many-to-one relationship.
- __many-to-many__—Many-to-many relationships are essentially a convenient fiction. Your first instinct would be to somehow make each class contain a list of student IDs that were associated with this class. This, however, is not a workable approach because relational databases (or at least those based on SQL) do not support any notion of a list.

  Indeed, someone thinking about this from a flat database perspective might think of a class schedule as a table containing a student’s name and a list of classes. In a relational database world, however, you would view it as a collection of students, a collection of classes, and a collection of lists that associate each person with a particular class or classes.

  Thus, you should think of a many-to-many relationship as multiple collections of many-to-one relationships. In the case of students and classes, instead of having a class associated with multiple students or a student associated with multiple classes, you instead have a third entity—a “student class” entity. This naming tells you that the entity expresses a relationship between a student and a class. An example of a `student_class` table is shown in [Table 3-4](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknltm).

  __Table 3-4__  The “student_class” table

  | ID | Student_ID | Class_ID |
  | 1 | 19 | 37 |

  Instead of associating either the student or the class with multiple entries, you now simply have multiple `student_class` entries. Each entry associates one student with one class. Thus, you effectively have multiple students, each associated with multiple classes in a many-to-many relationship, but you did it by creating multiple instances of many-to-one relationship pairs.

The Structured Query Language, or SQL, is a standard syntax for querying or modifying the contents of a database. Using SQL, you can write software that interacts with a database without worrying about the underlying database architecture; the same basic queries can be executed on every database from SQLite to Oracle, provided that you limit yourself to the basic core queries and data types.

The JavaScript database uses SQLite internally to store information. SQLite is a lightweight database architecture that stores each database in a separate file. For more information about SQLite, see the SQLite website at [http://www.sqlite.org/](http://www.sqlite.org/).

For syntax descriptions in this section:

- Text enclosed in square brackets (`[]`)is optional.
- Lowercase text represents information that you choose.
- An ellipsis (`...`) means that you can specify additional parameters similar to the preceding parameter.
- Uppercase text and all other symbols are literal text and keywords that you must enter exactly as-is. (These keywords are not case sensitive, however.)

The most common SQL queries are `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE`, and `DROP TABLE`. These queries are described in the sections that follow.

For a complete list of SQL commands supported by SQLite and for additional options to the commands described above, see the SQLite language support specification at [http://www.sqlite.org/lang.html](http://www.sqlite.org/lang.html).

Creates a table.

```
CREATE [TEMP[ORARY]] TABLE [IF NOT EXISTS] table_name (
    column_name column_type [constraint],
    ...
    );
```

The most common values for `constraint` are `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, and `AUTOINCREMENT`. Column constraints are optional. For example, the following `CREATE` command creates the table described by Table 3-1 in [Relationship Models and Schema](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknltq):

```
CREATE TABLE IF NOT EXISTS family (
    ID INTEGER PRIMARY KEY,
    Last_Name NVARCHAR(63) KEY,
    Address NVARCHAR(255),
    City NVARCHAR(63),
    State NVARCHAR(2),
    Zip NVARCHAR(10));
```

Each table should contain a primary key. A primary key implicitly has the `UNIQUE`, and `NOT NULL` properties set. It doesn’t hurt to state them explicitly, as other database implementations require `NOT NULL` to be stated explicitly. This column must be of type `INTEGER` (at least in SQLite—other SQL implementations use different integer data types).

Notice that this table does not specify the `AUTOINCREMENT` option for its primary key. SQLite does not support the `AUTOINCREMENT` keyword, but SQLite implicitly enables auto-increment behavior when `PRIMARY KEY` is specified.

The data types supported by SQLite are as follows:

**`BLOB`**
: A large block of binary data.

**`BOOL`**
: A boolean (true or false) value.

**`CLOB`**
: A large block of (typically 7-bit ASCII) text.

**`FLOAT`**
: A floating-point number.

**`INTEGER`**
: An integer value.

__Note:__ Although integer values are stored internally as integers, all numerical comparisons are performed using 64-bit floating-point values. This may cause precision loss for very large numeric values (>15 digits). If you need to compare such large numbers, you should store them as a string and compare their length (to detect magnitude differences) prior to comparing their value.

**`NATIONAL VARYING CHARACTER` or `NVCHAR`**
: A Unicode (UTF-8) string of variable length (generally short). This data type requires a length parameter that provides an upper bound for the maximum data length. For example, the following statement declares a column named `Fahrenheit` whose UTF-8 data cannot exceed 451 characters in length:

```
...
    Fahrenheit NVARCHAR(451),
...
```


__Note:__ Unlike some SQL implementations, SQLite does not enforce this maximum length and does not truncate data to the length specified. However, you should still set reasonable bounds to avoid the risk of compatibility problems in the future.

SQLite also does not enforce valid Unicode encoding for this data. In effect, it is treated just like any other text unless and until you use a UTF-16 collating sequence (controlled by the `COLLATE` keyword) or SQL function. Collating sequences and SQL functions are beyond the scope of this document. See the SQLite documentation at [http://www.sqlite.org/docs.html](http://www.sqlite.org/docs.html) for more information.

**`NUMERIC`**
: A fixed-precision decimal value that is expected to hold values of a given precision. Note that SQLite does not enforce this in any way.

**`REAL`**
: A floating-point value. This is stored as a 64-bit (8-byte) IEEE double-precision floating point value.

**`VARCHAR` or `VARYING CHARACTER`**
: A (generally short) variable-length block of text. This data type requires a length parameter that provides an upper bound for the maximum data length. For example, the following statement declares a column named `Douglas` whose data cannot exceed 42 characters in length:

```
...
    Douglas VARCHAR(42),
...
```


__Note:__ Unlike some SQL implementations, SQLite does not enforce this maximum length and does not truncate data to the length specified. However, you should still set reasonable bounds to avoid the risk of compatibility problems in the future.

To avoid unexpected behavior, you should be careful to store only numeric values into numeric (`REAL`, `INTEGER`, and so on) columns. If you attempt to store a non-numeric value into a numeric column, the value is stored as text. SQLite does not warn you when this happens. In effect, although SQLite supports typed columns, the types are not enforced in any significant way, though integer values are converted to floating point values when stored in a `REAL` column.

Inserts a new row into a table.

```
INSERT INTO table_name (column_1, ...)
    VALUES (value_1, ...);
```

For example, to store the values shown in Table 3-1 in [Relationship Models and Schema](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknltq), you would use the following query:

```
INSERT INTO family (Last_Name, Address, City, State, Zip)
    VALUES ('Doe', '56989 Peach St.', 'Martin', 'TN', '38237');
```

You should notice that all non-numeric values must be surrounded by quotation marks (single or double). This is described further in [SQL Security and Quoting Characters in Strings](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknlto).

Retrieves rows (or portions thereof) from a table or tables.

```
SELECT column_1 [, ...] from table_1 [, ...] WHERE expression;
```

Each `SELECT` query returns an result array (essentially a temporary table) that contains one entry for every row in the database table that matches the provided expression. Each entry is itself an array that contains the values stored in the specified columns within that database row. For example, the following SQL query returns an array of (name, age) pairs for every row in the people table where the value in the age column is greater than 18:

```
SELECT name, age FROM people WHERE age > 18;
```

Here are some other relatively straightforward examples of expressions that are valid in `SELECT` queries:

```
# Alphabetic comparison
SELECT name, age FROM people WHERE name < "Alfalfa";

# Equality and inequality
SELECT name, age FROM people WHERE age = 18;
SELECT name, age FROM people WHERE age != 18;

# Combinations
SELECT name, age FROM people WHERE (age > 18 OR (age > 55 AND AGE <= 65));
```

The complete expression syntax is beyond the scope of this document. For further details, see the SQLite language support specification at [http://www.sqlite.org/lang.html](http://www.sqlite.org/lang.html).

To select all columns, you can use an asterisk (`*`) instead of specifying a list of column names. For example:

```
SELECT * FROM people WHERE age > 18;
```

You can also use a `SELECT` query to query multiple tables at once. For example:

```
SELECT First_Name, Last_Name FROM family, familymember WHERE familymember.Family_ID = family.ID AND familymember.ID = 2;
```

The query creates a temporary joined table that contains one row for each combination of a single row from the `family` table and a single row from the `familymember` table in which the combined row pair matches the specified constraints (`WHERE` clause). It then returns an array containing the fields `First_Name` and `Last_Name` from that temporary table. Only rows in the `familymember` table whose `ID` value is `2` are included in the output; all other rows in this table are ignored. Similarly, only rows in the `family` table that match against at least one of the returned rows from the `familymember` table are included; other rows are ignored.

For example, if you provide tables containing the values shown in [Table 3-1](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknltg) and [Table 3-2](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknlti) in [Relationship Models and Schema](#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqnjnknltq), this would return only a single row of data containing the values (‘Jane’, ‘Doe’).

Notice the constraint `family.ID`. If a column name appears in multiple tables, you cannot just use the field name as part of a `WHERE` constraint because the SQL database has no way of knowing which ID field to compare. Instead, you must specify the table name as part of the column name, in the form `table_name.column_name`. Similarly, in the field list, you can specify `table_name.*` to request all of the rows in the table called `table_name`. For example:

```
SELECT familymember.*, Last_Name from family, familymember WHERE ...
```


Changes values within an existing table row.

```
UPDATE table_name SET column_1=value_1 [, ...]
    [WHERE expression];
```

If you do not specify a `WHERE` expression, the specified change is made to every row in the table. The expression syntax is the same as for the `SELECT` statement. For example, if someone gets married, you might change that person’s `Family_ID` field with a query like this one:

```
UPDATE familymember set Family_ID=32767 WHERE ID=179;
```


Deletes a row or rows from a table.

```
DELETE FROM table_name [WHERE expression];
```

If you do not specify a `WHERE` expression, this statement deletes every row in the table. The expression syntax is the same as for the `SELECT` statement. For example, if someone drops their membership in an organization, you might remove them from the roster with a query like this one:

```
DELETE FROM people WHERE ID=973;
```


Deletes an entire table.

```
DROP TABLE table_name;
```

For example, if your code copies the contents of a table into a new table with a different name, then deletes the old table, you might delete the old table like this:

```
DROP TABLE roster_2007;
```


Most modern relational databases have the notion of a transaction. A transaction is defined as an atomic unit of work that either completes or does not complete. If any part of a transaction fails, the changes it made are rolled back—restored to their original state prior to the beginning of the transaction.

Transactions prevent something from being halfway completed. This is particularly important with relational databases because changes can span multiple tables.

For example, if you are updating someone’s class schedule, inserting a new `student_class` record might succeed, but a verification step might fail because the class itself was deleted by a previous change. Obviously, making the change would be harmful, so the changes to the first table are rolled back.

Other common reasons for failures include:

- Invalid values—a string where the database expected a number, for example, could cause a failure if the database checks for this. (SQLite does _not_, however.)
- Constraint failure—for example, if the class number column is marked with the `UNIQUE` keyword, any query that attempts to insert a second class with the same class number as an existing class fails.
- Syntax error—if the syntax of a query is invalid, the query fails.

The mechanism for performing a transaction is database-specific. In the case of the JavaScript Database, transactions are built into the query API itself, as described in [Executing a Query](Using%20the%20JavaScript%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknltg).

Relational databases and data structures inside applications should be closely coupled to avoid problems. The best in-memory architecture is generally an object for each row in each table. This means that each object in your code would have the same relationships with other objects that the underlying database entries themselves have with each other.

Tying database objects to data structures is important for two reasons:

- It reduces the likelihood of conflicting information. You can be certain that no two objects will ever point to the same information in the database. Thus, changing one object will never require changing another object.
- It makes it a lot easier to keep track of what data is stored in which table when you are debugging.

It is best to keep the names of tables and classes as similar as possible. Similarly, it is best to keep the names of instance variables as similar as possible to the names of the database fields whose contents they contain.

When working with user-entered strings, additional care is needed. Because strings can contain arbitrary characters, it is possible to construct a value that, if handled incorrectly by your code, could produce unforeseen side effects. Consider the following SQL query:

```
 UPDATE MyTable SET MyValue='VARIABLE_VALUE';
```

Suppose for a moment that your code substitutes a user-entered string in place of `VARIABLE_VALUE` without any additional processing. The user enters the following value:

```
'; DROP TABLE MyTable; --
```

The single quote mark terminates the value to be stored in `MyValue`. The semicolon ends the command. The next command deletes the table entirely. Finally, the two hyphens cause the remainder of the line (the trailing `';`) to be treated as a comment and ignored. Clearly, allowing a user to delete a table in your database is an undesirable side effect. This is known as a SQL injection attack because it allows arbitrary SQL commands to be injected into your application as though your application sent them explicitly.

When you perform actual queries using user-provided data, to avoid mistakes, you should use placeholders for any user-provided values and rely on whatever SQL query API you are using to quote them properly. In the case of the JavaScript database API, this process is described in [Executing a Query](Using%20the%20JavaScript%20Database.md#apple-f4xwc4dqnrsv64tfmyxwi33df52wszbpkridimbqga3tenjwfvbuqmznknltg).

If you need to manually insert strings with constant string values, however, using placeholders is overkill and can make the query harder to read. To insert these strings manually, use double-quote marks around any strings that contain a single-quote mark, and vice-versa. In the rare event that you must manually insert a string that contains both types of quotation marks, use single quotes, but add a backslash before every single-quote mark within the string. For example, to insert the value

```
"It's a boy," he whispered softly.
```

you would write it like this:

```
'"It\'s a boy," he whispered softly.'
```

[Next](Using%20the%20JavaScript%20Database.md)[Previous](Key-Value%20Storage.md)

