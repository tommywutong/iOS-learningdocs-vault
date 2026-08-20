---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/ObjC_classic/Introduction.html
archived_at: '2026-07-15T08:11:45.960770Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](InformixEOAdaptorTOC.md)

# InformixEOAdaptor

> __Framework:__
> System/Library/Frameworks/InformixEOAdaptor.framework

> __Header File Directories:__
> System/Library/Frameworks/InformixEOAdaptor.framework/Headers

## Introduction

The InformixEOAdaptor framework is a set of classes that allow
your programs to connect to an Informix server. These classes provide
Informix-specific method implementations for the EOAccess framework's
EOAdaptor, EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression
abstract classes.

The following table lists the classes in the InformixEOAdaptor
Framework and provides a brief description of each class.

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| InformixAdaptor | Represents a single connection to a Informix database server, and is responsible for keeping login and model information, performing Informix-specific formatting of SQL expressions, and reporting errors. |
| InformixChannel | Represents an independent communication channel to the database server its InformixAdaptor is connected to. |
| InformixContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| InformixSQLExpression | Defines how to build SQL statements for InformixChannels. |

## The Connection Dictionary

The connection dictionary contains items needed to connect
to an Informix server, such as the database name (it's common to
omit the user name and password from the connection dictionary,
and prompt users to enter those values in a login panel). The keys
of this dictionary identify the information the server expects,
and the values of those keys are the values that the adaptor uses
when trying to connect to the server.

The Informix adaptor defines string constants for use as connection
dictionary keys:

- [dbNameKey](InformixAdaptor-2.md#apple-ijbukrsgizfei)
- [userNameKey](InformixAdaptor-2.md#apple-ijbukrkejjeec)
- [passwordKey](InformixAdaptor-2.md#apple-ijbukscejbdus)

See the [InformixAdaptor](InformixAdaptor-2.md#apple-ijbukrkgjbbes) class specification
for more information on the connection dictionary key constants.

## Locking

All adaptors use the database server's native locking facilities
to lock rows on the server. In the Informix adaptor locking is determined
by the isolation level, which is implemented in InformixChannel. Locking
occurs when:

- You send the adaptor channel a __selectAttributes:fetchSpecification:lock:entity:__ message
  with `YES` specified as
  the value for the __lock:__ parameter.
- You explicitly lock an object's row with the EODatabaseContext's __lockObjectWithGlobalID:editingContext:__ message.
- You set pessimistic locking at the database level and fetch
  objects.

## Data Type Mapping

Every adaptor provides a mapping between each server data
type and the Objective-C type to which a database value will be
coerced when it's fetched from the database. The following table
lists the mapping used by InformixAdaptor.

|  |  |
| --- | --- |
| __Informix Data Type__ | __Java Data Type__ |
| `VARCHAR` | NSString |
| `NVARCHAR` | NSString |
| `DECIMAL` | NSDecimalNumber |
| `MONEY` | NSDecimalNumber |
| `BYTE` | NSData |
| `TEXT` | NSString |
| `DATE` | NSCalendarDate |
| `INTEGER` | NSNumber |
| `SMALLINT` | NSNumber |
| `NCHAR` | NSString |
| `CHAR` | NSNumber |
| `SERIAL` | NSNumber |
| `FLOAT` | NSNumber |
| `SMALLFLOAT` | NSNumber |
| `DATETIME YEAR TO SECOND` | NSCalendarDate |
| `INTERVAL` | NSString |

The type mapping methods-__externalTypesWithModel:__, __internalTypeForExternalType:model:__,
and __isValidQualifierType:model:__-allow
for an adaptor to supplement its set of type mappings with additional
mappings for user-defined database types. InformixAdaptor does not
make use of the model argument if one is provided.

## Prototype Attributes

The InformixEOAdaptor Framework provides the following set
of prototype attributes:

|  |  |  |  |
| --- | --- | --- | --- |
| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| `binaryID` | `BYTE` | NSData |  |
| `city` | `VARCHAR` | NSString | `columnName = CITY` `width = 50` |
| `date` | `DATETIME YEAR TO SECOND` | NSCalendarDate | `columnName = ""` |
| `longText` | `TEXT` | NSString |  |
| `money` | `INTEGER` | NSDecimalNumber | `columnName = ""` |
| `phoneNumber` | `VARCHAR` | NSString | `columnName = PHONE` `width = 20` |
| `rawImage` | `BYTE` | NSData | `columnName = RAW_IMAGE` |
| `state` | `VARCHAR` | NSString | `columnName = STATE` `width = 2` |
| `streetAddress` | `VARCHAR` | NSString | `columnName = STREET_ADDRESS` `width = 100` |
| `tiffImage` | `BYTE` | NSImage | `adaptorValueConversionMethodName = TIFFRepresentation` `columnName = PHOTO` `valueFactoryMethodName = "imageWithData:"` |
| `uniqueID` | `INTEGER` | NSNumber | `columnName = ""` `valueType = i` |
| `zipCode` | `VARCHAR` | NSString | `columnName = ZIP` `width = 10` |

## Generating Primary Keys

Each adaptor provides a database-specific implementation of
the method __primaryKeyForNewRowWithEntity:__ for
generating primary keys. The InformixChannel's implementation uses
a table named `eo_sequence_table` to
keep track of the next available primary key value for a given table.
The table contains a row for each table for which the adaptor provides
primary key values. The statement used to create the `eo_sequence_table` is:

> ```
> create table eo_sequence_table (
>     table_name varchar(32,0),
>     counter integer
> )
> ```

InformixChannel uses a stored procedure named `eo_pk_for_table` to
access and maintain the primary key counter in `eo_sequence_table`.
The stored procedure is defined as follows:

> ```
> create procedure
> eo_pk_for_table (tname varchar(32))
> returning int;
>     define cntr int;
>
>     update EO_SEQUENCE_TABLE
>     set COUNTER = COUNTER + 1
>     where TABLE_NAME = tname;
>
>     select COUNTER into cntr
>     from EO_SEQUENCE_TABLE
>     where TABLE_NAME = tname;
>
>     return cntr;
> end procedure;
> ```

The stored procedure increments the counter in the `eo_sequence_table` row
for the specified table, selects the counter value, and returns
it. InformixChannel executes this `eo_pk_for_table` stored procedure
from __primaryKeyForNewRowWithEntity:__ and
returns the stored procedure's return value.

To use InformixChannel's database-specific primary key generation
mechanism, be sure that your database accommodates the adaptor's
scheme. To modify your database so that it supports the adaptor's
mechanism for generating primary keys, use EOModeler. For more information
on this topic, see _Enterprise Objects Framework Developer's
Guide_.

## Bind Variables

The InformixAdaptor uses bind variables. A bind variable is
a placeholder used in an SQL statement that is replaced with an
actual value after the database server determines an execution plan.
You use the following methods to operate on bind variables:

- __bindVariableDictionaryForAttribute:value:__
- __mustUseBindVariableForAttribute:__
- __shouldUseBindVariableForAttribute:__

[![Table of Contents](attachments/images/up.gif)](InformixEOAdaptorTOC.md)
