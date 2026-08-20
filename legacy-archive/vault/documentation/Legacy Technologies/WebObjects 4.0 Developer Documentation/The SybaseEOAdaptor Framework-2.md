---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/SybaseEOAdaptor.html
archived_at: '2026-07-15T08:02:10.816974Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseAdaptor-2.md)

---

# The SybaseEOAdaptor Framework

__Framework:__
System/Library/Frameworks/SybaseEOAdaptor.framework

__Header File Directories:__
System/Library/Frameworks/SybaseEOAdaptor.framework/Headers

# Introduction

The SybaseEOAdaptor framework is a set of classes that allow your programs to connect to a Sybase server. These classes provide Sybase-specific method implementations for the EOAccess framework's EOAdaptor, EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract classes.

The following table lists the classes in the SybaseEOAdaptor Framework and provides a brief description of each class.

| __Class__ | __Description__ |
| SybaseAdaptor | Represents a single connection to a Sybase database server, and is responsible for keeping login and model information, performing Sybase-specific formatting of SQL expressions, and reporting errors. |
| SybaseChannel | Represents an independent communication channel to the database server its SybaseAdaptor is connected to. |
| SybaseContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| SybaseSQLExpression | Defines how to build SQL statements for SybaseChannels. |

```
```


---

## The Connection Dictionary

The connection dictionary contains items needed to connect to a Sybase server, such as the server name and database (it's common to omit the user name and password from the connection dictionary, and prompt users to enter those values in a login panel). The keys of this dictionary identify the information the server expects, and the values of those keys are the values that the adaptor uses when trying to connect to the server. For Sybase databases the required keys are as follows (all are defined constants):

> `hostName
> databaseName
> userName
> password`

The connection dictionary can optionally include three other keys (which are also defined constants): `sybasePasswordEncryption`, `LC_ALL`, and `primitiveTypeMap`. `sybasePasswordEncryption` provides support for Sybase password encryption. `LC_ALL` declares to the Sybase server the character set being used by the client (such as eucjis, ascii7, or iso_1). For a complete list of types available for this field, see your Sybase documentation. `primitiveTypeMap` describes the mapping of user-defined data types to their base Sybase type (such as varchar or datetime). For more information on user-defined data types, see ["Data Type Mapping"](#apple-gezti).

To add any of these optional keys and appropriate values to your connection dictionary, you can manually edit your model file. For example:

> ```
> connectionDictionary = {databaseName = People;     hostName = "";
>     LC_ALL = eucjis;
>     password = "";
>     primitiveTypeMap = {id = varchar; ssn = char(9); };
>     sybasePasswordEncryption = YES;
>     userName = "";
> };
> ```

Subsequently changing the connection dictionary in your model file using the Set Adaptor Info command in EOModeler has no effect on these keys and their values-they are preserved unless you edit the file to remove them. Alternatively you can add the optional keys to a model's connection dictionary programmatically.

The default character set for non-Japanese systems is iso_1 (that is, ISO Latin 1), while the default character set for Japanese systems is eucjis. You only need to add the LC_ALL key to your connection dictionary if you are using a character set other than your system's default.

---

## Error Handling

SybaseAdaptor, SybaseContext, and SybaseChannel can raise exceptions due to programming errors that result in invalid argument values or internal inconsistencies. In addition, messages, errors, and failure status returned from the Sybase SQL Server and client libraries can also result in EOGeneralAdaptorExceptions. When an exception results from a callback to the CS_CLIENTMSG_CB (Sybase ClientMessage callback) or the CS_SERVERMSG_CB (Sybase ServerMessage callback), all of the information passed into this routine is available in the userInfo dictionary contained by the exception. When an exception is raised in response to a Sybase ClientMessage callback, you can get the information provided by the client library as follows:

> ```
> clientMsgDict = [[localException userInfo]    objectForKey:@"sybaseClientMessageDictionary"];
> ```

The __clientMsgDict__  contains the following keys which have values corresponding to those sent in the callback function that raised the exception: msgstring, osstring, sqlstate, severity, msgnumber, osnumber, status.

Similarly, when the exception is raised in response to a Sybase ServerMessage callback, you can get the information provided by the server as follows:

> ```
> svrMsgDict = [[localException userInfo]    objectForKey:@"sybaseServerMessageDictionary"];
> ```

The __svrMsgDict__  contains the following keys which have values corresponding to those sent in the callback function that raised the exception: text, svrname, proc, sqlstate, msgnumber, state, severity, line, status.

---

## Locking

All adaptors use the database server's native locking facilities to lock rows on the server. The Sybase adaptor locks a row by using the HOLDLOCK keyword in SELECT statements. This occurs when:

- You send the adaptor channel a `selectAttributes:fetchSpecification:lock:entity:` message with YES specified as the value for the __lock:__  keyword.
- You explicitly lock an object's row with the EODatabaseContext's `lockObjectWithGlobalID:editingContext:` message.
- You set pessimistic locking at the database level and fetch objects.

The semantics of the HOLDLOCK keyword are such that when you lock a row other users can't update it, but it doesn't guarantee that your update will succeed. This is because other users could be holding a lock on the same row. However, you can still read rows that are locked by other users.

---

## Data Type Mapping

Every adaptor provides a mapping between each server data type and the Objective-C type to which a database value will be coerced when it's fetched from the database. The following table lists the mapping used by SybaseAdaptor.

| __Sybase Data Type__ | __Objective-C Data Type__ | __Java Data Type__ |
| binary | NSData | NSData |
| bit | NSNumber | Number |
| char | NSString | String |
| datetime | NSCalendarDate | NSGregorianDate |
| datetimn | NSCalendarDate | NSGregorianDate |
| decimal | NSDecimalNumber | BigDecimal |
| decimaln | NSDecimalNumber | BigDecimal |
| float | NSNumber | Number |
| floatn | NSNumber | Number |
| image | NSData | NSData |
| int | NSNumber | Number |
| intn | NSNumber | Number |
| money | NSDecimalNumber | BigDecimal |
| moneyn | NSDecimalNumber | BigDecimal |
| nchar | NSString | String |
| numeric | NSDecimalNumber | BigDecimal |
| numericn | NSDecimalNumber | BigDecimal |
| nvarchar | NSString | String |
| real | NSNumber | Number |
| smalldatetime | NSCalendarDate | NSGregorianDate |
| smallint | NSNumber | Number |
| smallmoney | NSDecimalNumber | BigDecimal |
| sysname | NSString | String |
| text | NSString | String |
| timestamp | NSData | NSData |
| tinyint | NSNumber | Number |
| varbinary | NSString | String |
| varchar | NSString | String |

```
```

In addition, SybaseAdaptor provides a mapping for user-defined data types. For example, a custom data type `partnumber`defined as char(10) is mapped to NSString-the Objective-C type to which `partnumber`'s base data type (char) is mapped. SybaseAdaptor's implementation of `describeModelWithTableNames:` automatically creates mappings for user-defined data types and saves them in the connection dictionary of the newly created model. Consequently, even models created with EOModeler automatically include information about custom data types.

Since information about custom types is stored in a model's connection dictionary, the type mapping methods-[`externalTypesWithModel:`](SybaseAdaptor.md#apple-ge2do), [`internalTypeForExternalType:model:`](SybaseAdaptor.md#apple-ge4dgmy), and `isValidQualifierType:model:`-use the model argument if it is provided. If the model argument isn't provided, these methods don't have user-defined data type information available to them.

---

## Prototype Attributes

The SybaseEOAdaptor Framework provides the following set of prototype attributes:

| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| binaryID | varbinary | NSData | width = 12 |
| city | varchar | NSString | columnName = CITY width = 50 |
| date | datetime | NSCalendarDate | columnName = "" |
| longText | text | NSString |  |
| money | money | NSDecimalNumber | columnName = ""; |
| phoneNumber | varchar | NSString | columnName = PHONE width = 20 |
| rawImage | image | NSData | columnName = RAW_IMAGE |
| state | varchar | NSString | columnName = STATE width = 2 |
| streetAddress | varchar | NSString | columnName = STREET_ADDRESS width = 100 |
| tiffImage | image | NSImage | adaptorValueConversionMethodName = TIFFRepresentation columnName = PHOTO valueFactoryMethodName = "imageWithData:" |
| uniqueID | int | NSNumber | columnName = ""; valueType = i |
| zipCode | varchar | NSString | columnName = ZIP width = 10 |

```
```


---

## SQL and User-Defined Transactions

Certain data definition commands, such as CREATE TABLE, can't be executed in a user-defined transaction. However, the database channel and adaptor channel require you to start a transaction before evaluating any SQL. To work around this problem, you need to send the adaptor context or database context a __transactionDidBegin__  message to make it think a transaction is in progress. Then you can send it the SQL statement, followed by a __transactionDidCommit__  message.

---

## Processing Compute Rows and Stored Procedures

SybaseChannel's delegate methods used for processing compute rows and stored procedures give you access to the three types of non-regular rows supported by Sybase: compute rows, return parameters (from a stored procedure), and status from a stored procedure. Because the access layer can only handle regular table rows, the Sybase adaptor channel normally skips non-regular rows. However, you can use the delegate methods to intercept non-regular rows before they are skipped. These delegate methods are [`sybaseChannel:willFetchAttributes:forRowOfType:withComputeRowId:`](../Protocols/SybaseChannelDelegate.md#apple-giydmny)and[`sybaseChannel:willReturnRow:ofType:withComputeRowId:`](../Protocols/SybaseChannelDelegate.md#apple-giytamy). The method [`sybaseChannel:willFetchAttributes:forRowOfType:withComputeRowId:`](../Protocols/SybaseChannelDelegate.md#apple-giydmny) is invoked when a row is fetched, while [`sybaseChannel:willReturnRow:ofType:withComputeRowId:`](../Protocols/SybaseChannelDelegate.md#apple-giytamy) is invoked when a row is about to be returned. Based on the type of the row, the delegate can specify the appropriate behavior. This enables you to use data in one of the three non-regular row types and either extract the data from them or use the method __describeResults__  to return an array of attributes that describe the properties available in the current result set. Using __describeResults__  is appropriate if you're not concerned with format-for example, if you're just writing raw data to a report.

__Note:__
The regular rows in the results from a stored procedure must map to the attributes in the
corresponding entity, and must be in alphabetical order.

---

## Generating Primary Keys

Each adaptor provides a database-specific implementation of the method `primaryKeyForNewRowWithEntity:` for generating primary keys. The SybaseChannel's implementation uses a table named eo_sequence_table to keep track of the next available primary key value for a given table. The table contains a row for each table for which the adaptor provides primary key values. The statement used to create the eo_sequence_table is:

> ```
> create table eo_sequence_table (
>     table_name varchar(32),
>     counter int null
> )
> ```

SybaseChannel uses a stored procedure named eo_pk_for_table to access and maintain the primary key counter in eo_sequence_table. The stored procedure is defined as follows:

> ```
> create procedure
> eo_pk_for_table @tname varchar(32) as
> begin
>     define @max int
>     update eo_sequence_table
>     set counter = counter + 1
>     where table_name = @tname
>     select counter
>     from eo_sequence_table
>     where table_name = @tname
> end
> ```

The stored procedure increments the counter in the eo_sequence_table row for the specified table, selects the counter value, and returns it. SybaseChannel executes this eo_pk_for_table stored procedure from `primaryKeyForNewRowWithEntity:` and returns the stored procedure's return value.

To use SybaseChannel's database-specific primary key generation mechanism, be sure that your database accommodates the adaptor's scheme. To modify your database so that it supports the adaptor's mechanism for generating primary keys, use EOModeler. For more information on this topic, see _Enterprise Objects Framework Developer's Guide_.

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html) [Prev] [[Next]](SybaseAdaptor.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
