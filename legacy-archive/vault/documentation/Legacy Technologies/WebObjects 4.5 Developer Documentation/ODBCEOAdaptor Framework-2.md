---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/ObjC_classic/Introduction.html
archived_at: '2026-07-15T08:11:46.178830Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
ODBCEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](ODBCEOAdaptorTOC.md)

# ODBCEOAdaptor Framework

> __Framework:__
> System/Library/Frameworks/ODBCEOAdaptor.framework

> __Header File Directories:__
> System/Library/Frameworks/ODBCEOAdaptor.framework/Headers

## Introduction

The ODBCEOAdaptor framework is a set of classes that allow
your programs to connect to an ODBC server. These classes provide
ODBC-specific method implementations for the EOAccess framework's EOAdaptor,
EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract
classes.

ODBC (Open Data Base Connectivity) defines a standard interface
that Windows applications can use to access any data source. Unlike
the other Enterprise Objects Frameworks adaptors that support a single
type of database, the ODBC adaptor supports any data source that
has an ODBC driver. Consequently, in addition to having standard
adaptor features, the ODBC adaptor also manages information relating
to the driver and to the data types defined by the data source the
driver supports.

The following table lists the classes in the ODBCEOAdaptor
Framework and provides a brief description of each class.

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| ODBCAdaptor | Represents a single connection to a ODBC database server, and is responsible for keeping login and model information, performing ODBC-specific formatting of SQL expressions, and reporting errors. |
| ODBCChannel | Represents an independent communication channel to the database server its ODBCAdaptor is connected to. |
| ODBCContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| ODBCSQLExpression | Defines how to build SQL statements for ODBCChannels. |

## The Connection Dictionary

The connection dictionary contains items needed to connect
to an ODBC server, such as the data source (it's common to omit
the user name and password from the connection dictionary, and prompt
users to enter those values in a login panel). The keys of this
dictionary identify the information the server expects, and the
values of those keys are the values that the adaptor uses when trying
to connect to the server.

The ODBC adaptor defines string constants for use as connection
dictionary keys:

- [dataSourceKey](ODBCAdaptor-2.md#apple-ijeugqsgirbee)
- [userNameKey](ODBCAdaptor-2.md#apple-ijeugr2iindeu)
- [passwordKey](ODBCAdaptor-2.md#apple-ijeugrsiizdum)
- [connectionStringKey](ODBCAdaptor-2.md#apple-ijeugscbizeuc)
- [typeInfoKey](ODBCAdaptor-2.md#apple-ijeugq2givcuu)
- [driverInfoKey](ODBCAdaptor-2.md#apple-ijeugssijjdeq)

The value for the `connectionStringKey` contains
the user name, password, and data source. If an entry for `connectionStringKey` is
present in the connection dictionary, the other login keys (`dataSourceKey`, `userNameKey`,
and `passwordKey`) are
ignored and the value for `connectionStringKey` is
used to connect to the database.

The value for the `typeInfoKey` is
a dictionary that is used to cache type information. This is done
because different ODBC drivers work with different data types. Caching
type information in the connection dictionary avoids costly connections
to the driver and the database. The dictionary for the `typeInfoKey` contains
the following information for every type in your database:

> ```
> defaultODBCType = (<CHAR/TIMESTAMP/BIT/...>, ...)
> precision = <precision>
> minScale = <minScale>
> maxScale = <maxScale>
> isUnsigned = <YES/NO>
> isNullable = <YES/NO>
> isSearchable = <YES/NO>
> createParams = <0/1/2>
> ```

The value for the `driverInfoKey` is
a dictionary that stores information about the driver, such as its
name and version.

For more information on the connection dictionary key constants,
see the [ODBCAdaptor](ODBCAdaptor-2.md#apple-j5ceeq2bmrqxa5dpoi) class specification.

## Locking

All adaptors use the database server's native locking facilities
to lock rows on the server. If you're using the Microsoft SQL
Server, the ODBC adaptor locks a row by using the HOLDLOCK keyword
in SELECT statements. In all other cases it uses the SELECT... FOR
UPDATE... statement. Locking occurs when:

- You send the adaptor channel a __selectAttributes:fetchSpecification:lock:entity:__ message
  with YES specified as the value for the __lock:__ keyword.
- You explicitly lock an object's row with the EODatabaseContext's __lockObjectWithGlobalID:editingContext:__ message.
- You set pessimistic locking at the database level and fetch
  objects.

## Data Type Mapping

Every adaptor provides a mapping between each server data
type and the Objective-C type to which a database value will be
coerced when it's fetched from the database. ODBC adds an intermediate
layer: the generic ODBC type (identifier) to which each database
data type maps.

For example, the following table shows the mapping from some
of the Microsoft Access database data types to ODBC to Objective-C:

|  |  |  |
| --- | --- | --- |
| __Microsoft Access Database Type__ | __Generic ODBC Type__ | __Objective-C Type__ |
| `TEXT` | `SQL_VARCHAR` | NSString |
| `CURRENCY` | `SQL_NUMERIC` | NSDecimalNumber |
| `BINARY` | `SQL_BINARY` | NSData |
| `DATETIME` | `SQL_TIMESTAMP` | NSCalendarDate |

The following table lists the mapping between generic ODBC
types and Objective-C types.

|  |  |
| --- | --- |
| __ODBC Data Type__ | __Objective-C Data Type__ |
| `SQL_VARCHAR` | NSString |
| `SQL_CHAR` | NSString |
| `SQL_LONGVARCHAR` | NSString |
| `SQL_DECIMAL` | NSDecimalNumber |
| `SQL_NUMERIC` | NSDecimalNumber |
| `SQL_BIGINT` | NSNumber |
| `SQL_SMALLINT` | NSNumber |
| `SQL_INTEGER` | NSNumber |
| `SQL_REAL` | NSNumber |
| `SQL_FLOAT` | NSNumber |
| `SQL_DOUBLE` | NSNumber |
| `SQL_BIT` | NSNumber |
| `SQL_TINYINT` | NSNumber |
| `SQL_VARBINARY` | NSData |
| `SQL_BINARY` | NSData |
| `SQL_LONGVARBINARY` | NSData |
| `SQL_TIMESTAMP` | NSCalendarDate |
| `SQL_DATE` | NSCalendarDate |
| `SQL_TIME` | NSCalendarDate |

Since ODBCAdaptor's type information is stored in a model's
connection dictionary, the type mapping methods-__externalTypesWithModel:__, __internalTypeForExternalType:model:__,
and __isValidQualifierType:model:__-use the
model argument if it is provided. If the model argument isn't provided,
these methods don't have data type information available to them.

## Prototype Attributes

The ODBCEOAdaptor Framework provides the following set of
prototype attributes:

|  |  |  |  |
| --- | --- | --- | --- |
| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| `binaryID` | `BINARY` | NSData | `width = 12` |
| `city` | `CHAR` | NSString | `columnName = CITY` `width = 50` |
| `date` | `DATETIME` | NSCalendarDate | `columnName = ""` |
| `longText` | `LONGTEXT` | NSString |  |
| `money` | `CURRENCY` | NSDecimalNumber | `columnName = ""` |
| `phoneNumber` | `CHAR` | NSString | `columnName = PHONE` `width = 20` |
| `rawImage` | `LONGBINARY` | NSData | `columnName = RAW_IMAGE` |
| `state` | `CHAR` | NSString | `columnName = STATE` `width = 2` |
| `streetAddress` | `CHAR` | NSString | `columnName = STREET_ADDRESS` `width = 100` |
| `tiffImage` | `LONGBINARY` | NSImage | `adaptorValueConversionMethodName = TIFFRepresentation` `columnName = PHOTO` `valueFactoryMethodName = "imageWithData:"` |
| `uniqueID` | `LONG` | NSNumber | `columnName = ""` `valueType = i` |
| `zipCode` | `CHAR` | NSString | `columnName = ZIP` `width = 10` |

## Generating Primary Keys

Each adaptor provides a database-specific implementation of
the method __primaryKeyForNewRowWithEntity:__ for
generating primary keys. The ODBCChannel's implementation uses
a table named `EO_PK_TABLE` to
keep track of the next available primary key value for a given table. The
table contains a row for each table for which the adaptor provides
primary key values.

ODBCChannel's implementation of __primaryKeyForNewRowWithEntity:__ attempts
to select a value from the `EO_PK_TABLE` for
the new row's table. If the attempt fails because the table doesn't
exist, the adaptor creates the table using the following SQL statement:

> ```
> CREATE TABLE EO_PK_TABLE (
>     NAME TEXT_TYPE(40),
>     PK NUMBER_TYPE
> )
> ```

where _TEXT_TYPE_ is the external
(database) type for characters and _NUMBER_TYPE_ is
the external type for the table's primary key attribute. The ODBC
adaptor sets the PK value for each row to the corresponding table's
maximum primary key value plus one. After determining a primary
key value for the new row, the ODBC adaptor updates the counter
in the corresponding row in `EO_PK_TABLE`.

For more information on this topic, see _Enterprise
Objects Framework Developer's Guide_.

## Bind Variables

The ODBCAdaptor uses bind variables. A bind variable is a
placeholder used in an SQL statement that is replaced with an actual
value after the database server determines an execution plan. You
use the following ODBCSQLExpression methods to operate on bind variables:

- [- bindVariableDictionaryForAttribute:value:](ODBCSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq)
- [- mustUseBindVariableForAttribute:](ODBCSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)
- [- shouldUseBindVariableForAttribute:](ODBCSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a)

[![Table of Contents](attachments/images/up.gif)](ODBCEOAdaptorTOC.md)
