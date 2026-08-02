---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Documentation/Developer/EnterpriseObjects/DevGuide/FAQ2.html
archived_at: '2026-07-15T08:03:16.295630Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOF Developer's Guide

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Previous Section](How%20Can%20I%20Improve%20Performance.md)

# How Do I Generate Primary Keys?

Enterprise Objects Framework requires you to specify a primary key for each entity in a model. In applications that create new enterprise objects to insert into a database, unique values must be generated and assigned to an object's primary key. The Framework typically does this for you, but you can override or customize its default behavior.
__Note:__  Enterprise Objects Framework doesn't support modifiable primary key values-you shouldn't design your application so that users can change a primary key's value. If you really need this behavior, you have to implement it by deleting an affected object and reinserting it with a new primary key.

## Defining a Primary Key

When designing a database, keep the following tips in mind for defining primary keys:

- Don't use floating point values such as doubles and dates because they aren't precise in equality tests.
- Use integer or 12 byte binary primary keys when you want Enterprise Objects Framework to generate primary key values automatically. For more information on the format of 12 byte primary keys, see the constructor description (or the method description for __assignGloballyUniqueBytes:__ in Objective-C) in the EOTemporaryGlobalID class specification in the _Enterprise Objects Framework Reference_.
- Try to avoid using compound keys. A compound key incurs additional overhead in not only its entity but also in related entities: the destination entities of all to-one relationships must contain an attribute for each primary key attribute in the source. In addition, you can't use Enterprise Objects Framework's automatic primary key generation mechanism for compound primary keys.

- You can improve the efficiency of enterprise object inheritance support by encoding the class of an object in its primary key. When the class of an object is encoded in its key and you implement the EOModelGroup delegate method to tell the Framework the subentity and subclass for a key, Enterprise Objects Framework creates a more efficient fault for the object than it would otherwise. Try to encode the class of an object in a large integer or binary key instead of using a compound key. For more information, see the section["Delegation Hooks for Optimizing Inheritance"](Modeling%20Inheritance.md#apple-gq2dona) in the "[Advanced Enterprise Object Modeling](Advanced%20Enterprise%20Object%20Modeling.md#apple-ge2danbw)" chapter.

## Generating Primary Key Values

There are four ways to provide primary key values for enterprise objects:

- _An enterprise object can provide its own primary key value._ With this approach, the primary key must be a class property of the object. If the primary key value of an object is __null__ (__nil__ in Objective-C) or zero when the Framework attempts to insert it, the Framework falls back on one of the other mechanisms to provide the value.
- _An EODatabaseContext's delegate provides a primary key value._ If the EODatabaseContext that's inserting an enterprise object has a delegate, and if the delegate has a method called __databaseContextNewPrimaryKey__ (__databaseContext:newPrimaryKeyForObject:entity:__ in Objective-C) that returns a non-__null__ (non-__nil__) value, the Framework uses the returned object as the primary key value.
- _A database stored procedure provides a primary key value._ If an enterprise object's entity has a stored procedure assigned to the NextPrimaryKeyProcedureOperation, the Framework invokes the stored procedure and uses the result as the primary key value.
- _Your adaptor provides a primary key value using a database-specific mechanism._ Each adaptor provides a database-specific implementation of the method __primaryKeyForNewRowWithEntity__ (__primaryKeyForNewRowWithEntity:__ in Objective-C) that provides unique values for primary key attributes.

This is the technique used when your primary keys are integers. However, as described in the preceding section, when you want Enterprise Objects Framework to generate primary keys, you can also use 12 byte NSDatas. The difference is that integer primary keys are fetched from the database, whereas NSData keys are generated on the client (see the EOTemporaryGlobalID class specification in the _Enterprise Objects Framework Reference_ for more information). Consequently, using 12 byte NSDatas is faster, but integer primary keys have the advantage of being more readable.

If the Framework can't assign a primary key using one of the mechanisms above, it throws an exception.
The following sections provide more information on when and how to use each mechanism.

### When the Enterprise Object Provides the Key

An enterprise object generally provides its own primary key value when the primary key is meaningful to users-a social security number, account number, or part number, for example. In some cases, the user provides the primary key value by entering it in the user interface. In other cases, the enterprise object generates its own unique primary key value. For example, a Part object's primary key could encode the part's type, the plant from which it came, and the batch in which it was made. Although generated, part numbers may still be meaningful to users if they use them to identify parts.
To specify that an enterprise object provides its own key, you must set the primary key attributes as class properties in the object's entity. Your enterprise object class should provide an instance variable or accessor methods for each of the primary key attributes. If you want to provide the primary key value for a newly created enterprise object, be sure to assign it before the object is saved.
__Note:__  In the case of Number objects (NSNumbers in Objective-C), don't set the value to zero unless you intend to have the primary key generated. See the section["Why is EOF Generating Primary Key Values for Number Objects Set to Zero?"](#apple-gm2daoa) below for details.)

If an enterprise object generates its own primary key value programmatically, you must generate and assign it in an appropriate method. You could, for example, provide a primary key value when the object is first instantiated by implementing the method __awakeFromInsertion__ (__awakeFromInsertionInEditingContext:__ in Objective-C).
On the other hand, if your application's user interface provides a way for the user to enter primary key values, you don't need to handle them any differently than you handle the object's other properties. For example, if an application uses social security numbers as the primary keys for employees, it must provide a way for users to enter them. The interface layer of the Framework takes care of assigning the user-provided value to the object.
The disadvantage of letting users enter primary key values is that there's a chance for data-entry error and the possibility that the object's primary key will need to be modified later. Since Enterprise Objects Framework doesn't support modifiable primary keys, you have to delete an object and reinsert it with a new primary key value to change its primary key. It's generally better to define a "meaningless" primary key to use instead.

### When the EODatabaseContext Delegate Provides the Key

An EODatabaseContext's delegate is given an opportunity to provide a primary key value for enterprise objects that don't already have one. This is the most commonly used mechanism in applications that don't use the adaptor's database-specific primary key generation mechanism. You might use the delegate to provide primary key values when you want to avoid making a trip to the database. For example, you might implement this method to generate globally unique identifiers based on an IP address and a time stamp.
To allow your EODatabaseContext's delegate to provide primary keys, implement the method __databaseContextNewPrimaryKey__ (__databaseContext:newPrimaryKeyForObject:entity:__ in Objective-C). An EODatabaseContext sends this method to its delegate when a newly inserted enterprise object doesn't have a primary key value. If the delegate is not implemented or returns __null__ (__nil__), the EODatabaseContext gets a primary key by invoking a stored procedure or using its adaptor's database-specific mechanism.

### When a Database Stored Procedure Provides the Key

You typically use a stored procedure to provide primary key values when you need to override the adaptor's database-specific mechanism but still need to make a trip to the database to generate values.
To use a stored procedure to provide primary key values, you must define the stored procedure in your model. Stored procedures are read from the database when you create a new model and included in the model's __.eomodeld__ file. You can also add stored procedures in EOModeler using the Stored Procedure view of the Model Editor.
After defining the stored procedure, you assign it to an entity. You can set it in EOModeler: In the Stored Procedure Inspector, type the name of the stored procedure in the Get PK field. Alternatively, you can set it programmatically using EOEntity's __setStoredProcedure__ method (__setStoredProcedure:forOperation:__ in Objective-C). For more information on defining stored procedures and assigning them to entities, see the section["How Do I Invoke a Stored Procedure?"](How%20Do%20I%20Invoke%20a%20Stored%20Procedure.md#apple-gu2ti).

### When the Adaptor Provides the Key

Each adaptor provides a database-specific mechanism for generating primary keys. Unless you specify one of the other four mechanisms, Enterprise Objects Framework automatically uses the adaptor's mechanism.
Each adaptor provides an implementation of the method __primaryKeyForNewRowWithEntity__ (__primaryKeyForNewRowWithEntity:__ in Objective-C). When invoked, this method returns a unique primary key value. For example, the Oracle adaptor uses Oracle sequences to generate unique values.
To use the adaptor's database-specific mechanism, you must be sure that your database accommodates the adaptor's scheme. The primary keys of the affected tables must be simple (that is, they can't be compound primary keys), and they must be number types.
To modify your database so that it supports the adaptor's mechanism for generating primary keys:

- In EOModeler's Model Editor, select the entities for which you want the adaptor to generate primary key values.
- Choose Property µ Generate SQL.
- In the SQL Generation panel that appears, check the "Create Primary Key Support" box as well as any of the others that you might need.

The following sections describe the support added to your database for each of Enterprise Objects Framework's adaptors.
Informix and Sybase
The Informix and Sybase adaptor use the same approach to generating primary key values. Both adaptors use a table named eo_sequence_table to keep track of the next available primary key value for a given table. The table contains a row for each table for which the adaptor provides primary key values.
The statements used to create the eo_sequence_tables are:

|  Informix |  Sybase |
|  create table eo_sequence_table (table_name varchar(32, 0), counter integer) |  create table eo_sequence_table  (table_name varchar(32), counter int null) |

```
```


The adaptors use a stored procedure called eo_pk_for_table to access and maintain the primary key counters in eo_sequence_table. The stored procedures are defined as follows:

|  Informix |  Sybase |
|  create procedure  eo_pk_for_table (tname varchar(32))  returning int; define cntr int;   update EO_SEQUENCE_TABLE set COUNTER = COUNTER + 1 where TABLE_NAME = tname;  select COUNTER into cntr from EO_SEQUENCE_TABLE where TABLE_NAME = tname;  return cntr;  end procedure; |  create procedure  eo_pk_for_table @tname varchar(32) as  begin declare @max int   update eo_sequence_table set counter = counter + 1 where table_name = @tname  select counter from eo_sequence_table where table_name = @tname   end |

```
```


The stored procedures increment the counter in the eo_sequence_table row for the specified table, select the counter value, and return it. The Informix and Sybase adaptor's __primaryKeyForNewRowWithEntity__ methods execute the eo_pk_for_table stored procedure and return the stored procedure's return value.
ODBC
The approach taken by the ODBC adaptor is very similar to that of the Informix and Sybase adaptors. The ODBC adaptor uses a table named EO_PK_TABLE to keep track of the next available primary key value for a table, but the ODBC adaptor can create this table on demand. (The Informix and Sybase adaptors do not create the table and corresponding stored procedures. Rather, you create them ahead of time using the SQL Generation panel in EOModeler.)
The ODBC adaptor's __primaryKeyForNewRowWithEntity__ method attempts to select a value from the EO_PK_TABLE for the new row's table. If the attempt fails because the table doesn't exist, the adaptor creates the table using the following SQL statement:

```
CREATE TABLE EO_PK_TABLE (
    NAME TEXT_TYPE(40),
    PK NUMBER_TYPE
)
```


where _TEXT_TYPE_ is the external (database) type for characters and _NUMBER_TYPE_ is the external type for the table's primary key attribute. The ODBC adaptor sets the PK value for each row to the corresponding table's maximum primary key value plus one. After determining a primary key value for the new row, the ODBC adaptor updates the counter in the corresponding row in EO_PK_TABLE.
Oracle
The Oracle adaptor uses sequence objects to provide primary key values. It creates a sequence using the following SQL statement:

```
create sequence table_SEQ
```


where _table_ is the name of a table for which the adaptor provides primary key values. The adaptor sets the sequence start value to the corresponding table's maximum primary key value plus one.

## Why Can't I Use Identity Columns?

Some databases provide mechanisms that automatically generate primary key values. For example, Sybase allows you to specify _identity_ columns that automatically replace nulls with unique values. In databases that don't provide identity columns, you can define _triggers_ to produce the same result. These mechanisms are very useful when users interact directly with the database using SQL. However, they are difficult to use in applications that mediate between users and a database. You shouldn't use them in applications built with Enterprise Objects Framework.
Suppose that a database application allowed you to insert a row without providing a primary key value. An identity column or database trigger could generate an identifying value for the row, but the corresponding application object wouldn't have the value. The application could attempt to fetch the object using the values provided by the user, but a query that doesn't specify a primary key value might return more than one row. As a result, the application can't guarantee that it will be able to associate the current object with a row in the database. For this reason, Enterprise Objects Framework requires that you assign a primary key value to an object before it's inserted in the database.

## Why is EOF Generating Primary Key Values for Number Objects Set to Zero?

The EODatabaseContext assumes that an Number object (NSNumber in Objective-C) with a single attribute primary key value set to zero is a newly created instance, and therefore, will attempt to generate the primary key. This behavior allows you to use scalar data types (such as __int__) as an object's primary key, and still rely on automatic primary key generation.
This can cause problems if you have an existing database containing rows that use zero as the primary key value. The EODatabaseContext will incorrectly assume that an object created from that row needs a new primary key. This behavior may result in invalid foreign key references in other tables of your database.
To alter this behavior, assign a delegate to the EODatabaseContext object and implement the __databaseContextNewPrimaryKey__ delegate method (__databaseContext:newPrimaryKeyForObject:entity:__ in Objective-C) to return a Number object of value zero if the primary key should remain zero (an NSNumber in Objective-C), otherwise return __null__ (__nil__). Returning __null__ will tell EOF to find another way to generate the primary key value as described above.

## Summary

The following table summarizes the primary key generation options you have to choose from.

|  Mechanism |  Primary Use |
|  Object provides its own value |  When the primary key value is meaningful to users and is displayed in the application's user interface. |
|  EODatabaseContext delegate method |  When you don't want to use the adaptor's mechanism. |
|  Stored procedure |  When you want to use your own stored procedure to provide primary key values. |
|  Adaptor's mechanism |  When the primary key is a simple (not compound), numeric value that is not meaningful to users. |

```
```

[!Table of Contents](Answers%20to%20Common%20Design%20Questions.md) [!Next Section](How%20Do%20I%20Use%20My%20Database%20Server%27s%20Integrity-Checking%20Features.md)
