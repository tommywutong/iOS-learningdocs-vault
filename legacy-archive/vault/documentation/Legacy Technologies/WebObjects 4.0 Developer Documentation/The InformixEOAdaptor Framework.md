---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/InformixEOAdaptor.html
archived_at: '2026-07-15T08:02:00.107805Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](InformixAdaptor.md)

---

# The InformixEOAdaptor Framework

__Framework:__
com.apple.yellow.informixeoadaptor

__Header File Directories:__
System/Developer/Java/Headers

# Introduction

The InformixEOAdaptor framework is a set of classes that allow your programs to connect to an Informix server. These classes provide Informix-specific method implementations for the EOAccess framework's EOAdaptor, EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract classes.

The following table lists the classes in the InformixEOAdaptor Framework and provides a brief description of each class.

| __Class__ | __Description__ |
| InformixAdaptor | Represents a single connection to a Informix database server, and is responsible for keeping login and model information, performing Informix-specific formatting of SQL expressions, and reporting errors. |
| InformixChannel | Represents an independent communication channel to the database server its InformixAdaptor is connected to. |
| InformixContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| InformixSQLExpression | Defines how to build SQL statements for InformixChannels. |

```
```


---

## The Connection Dictionary

The connection dictionary contains items needed to connect to an Informix server, such as the database name (it's common to omit the user name and password from the connection dictionary, and prompt users to enter those values in a login panel). The keys of this dictionary identify the information the server expects, and the values of those keys are the values that the adaptor uses when trying to connect to the server. For Informix databases the required keys are as follows:

> `dbName
> userName
> password`

---

## Locking

All adaptors use the database server's native locking facilities to lock rows on the server. In the Informix adaptor locking is determined by the isolation level, which is implemented in InformixChannel. Locking occurs when:

- You send the adaptor channel a `selectAttributesWithFetchSpecification` message with true specified as the value for the `lock` parameter.
- You explicitly lock an object's row with the EODatabaseContext's `lockObjectWithGlobalID` message.
- You set pessimistic locking at the database level and fetch objects.

---

## Data Type Mapping

Every adaptor provides a mapping between each server data type and the Objective-C type to which a database value will be coerced when it's fetched from the database. The following table lists the mapping used by InformixAdaptor.

| __Informix Data Type__ | __Objective-C Data Type__ | __Java Data Type__ |
| VARCHAR | NSString | String |
| NVARCHAR | NSString | String |
| DECIMAL | NSDecimalNumber | BigDecimal |
| MONEY | NSDecimalNumber | BigDecimal |
| BYTE | NSData | NSData |
| TEXT | NSString | String |
| DATE | NSCalendarDate | NSGregorianDate |
| INTEGER | NSNumber | Number |
| SMALLINT | NSNumber | Number |
| NCHAR | NSString | String |
| CHAR | NSString | Number |
| SERIAL | NSNumber | Number |
| FLOAT | NSNumber | Number |
| SMALLFLOAT | NSNumber | Number |
| DATETIME YEAR TO SECOND | NSCalendarDate | NSGregorianDate |
| INTERVAL | NSString | String |

```
```


---

## Prototype Attributes

The InformixEOAdaptor Framework provides the following set of prototype attributes:

| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| binaryID | BYTE | NSData |  |
| city | VARCHAR | NSString | columnName = CITY width = 50 |
| date | "DATETIME YEAR TO SECOND" | NSCalendarDate | columnName = "" |
| longText | TEXT | NSString |  |
| money | INTEGER | NSDecimalNumber | columnName = "" |
| phoneNumber | VARCHAR | NSString | columnName = PHONE width = 20 |
| rawImage | BYTE | NSData | columnName = RAW_IMAGE |
| state | VARCHAR | NSString | columnName = STATE width = 2; |
| streetAddress | VARCHAR | NSString | columnName = STREET_ADDRESS width = 100; |
| tiffImage | BYTE | NSImage | adaptorValueConversionMethodName = TIFFRepresentation columnName = PHOTO valueFactoryMethodName = "imageWithData:" |
| uniqueID | INTEGER | NSNumber | columnName = "" valueType = i |
| zipCode | VARCHAR | NSString | columnName = ZIP width = 10 |

```
```


---

## Generating Primary Keys

Each adaptor provides a database-specific implementation of the method `primaryKeyForNewRow` for generating primary keys. The InformixChannel's implementation uses a table named eo_sequence_table to keep track of the next available primary key value for a given table. The table contains a row for each table for which the adaptor provides primary key values. The statement used to create the eo_sequence_table is:

> ```
> create table eo_sequence_table (
>     table_name varchar(32,0),
>     counter integer
> )
> ```

InformixChannel uses a stored procedure named eo_pk_for_table to access and maintain the primary key counter in eo_sequence_table. The stored procedure is defined as follows:

> ```
> create procedure
> eo_pk_for_table (tname varchar(32))
> returning int;
>     define cntr int;
>     update EO_SEQUENCE_TABLE
>     set COUNTER = COUNTER + 1
>     where TABLE_NAME = tname;
>     select COUNTER into cntr
>     from EO_SEQUENCE_TABLE
>     where TABLE_NAME = tname;
>     return cntr;
> end procedure;
> ```

The stored procedure increments the counter in the eo_sequence_table row for the specified table, selects th counter value, and returns it. InformixChannel executes this eo_pk_for_table stored procedure from `primaryKeyForNewRow` and returns the stored procedure's return value.

To use InformixChannel's database-specific primary key generation mechanism, be sure that your database accommodates the adaptor's scheme. To modify your database so that it supports the adaptor's mechanism for generating primary keys, use EOModeler. For more information on this topic, see _Enterprise Objects Framework Developer's Guide_.

---

## Bind Variables

The InformixAdaptor uses bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. You use the following methods to operate on bind variables:

- [bindVariableDictionaryForAttribute](InformixSQLExpression.md#apple-gm2tsmq)
- [mustUseBindVariableForAttribute](InformixSQLExpression.md#apple-gm3dema)
- [shouldUseBindVariableForAttribute](InformixSQLExpression.md#apple-gm3dgmq)

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html) [Prev] [[Next]](InformixAdaptor.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
