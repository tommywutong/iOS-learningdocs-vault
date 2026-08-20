---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/ObjC_classic/Introduction.html
archived_at: '2026-07-15T08:11:46.608778Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](SybaseEOAdaptorTOC.md)

# SybaseEOAdaptor Framework

> __Framework:__
> System/Library/Frameworks/SybaseEOAdaptor.framework

> __Header File Directories:__
> System/Library/Frameworks/SybaseEOAdaptor.framework/Headers

## Introduction

The SybaseEOAdaptor framework is a set of classes that allow
your programs to connect to a Sybase server. These classes provide
Sybase-specific method implementations for the EOAccess framework's EOAdaptor,
EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract
classes.

The following table lists the classes in the SybaseEOAdaptor
Framework and provides a brief description of each class.

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| SybaseAdaptor | Represents a single connection to a Sybase database server, and is responsible for keeping login and model information, performing Sybase-specific formatting of SQL expressions, and reporting errors. |
| SybaseChannel | Represents an independent communication channel to the database server its SybaseAdaptor is connected to. |
| SybaseContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| SybaseSQLExpression | Defines how to build SQL statements for SybaseChannels. |

## The Connection Dictionary

The connection dictionary contains items needed to connect
to a Sybase server, such as the server name and database (it's
common to omit the user name and password from the connection dictionary,
and prompt users to enter those values in a login panel). The keys
of this dictionary identify the information the server expects,
and the values of those keys are the values that the adaptor uses
when trying to connect to the server.

The Sybase adaptor defines string constants for use as connection
dictionary keys:

- [HOSTNAME](SybaseAdaptor-2.md#apple-inceeqski5fec)
- [DATABASENAME](SybaseAdaptor-2.md#apple-inceeskbiveem)
- [USERNAME](SybaseAdaptor-2.md#apple-inceeskjircuc)
- [PASSWORD](SybaseAdaptor-2.md#apple-inceercjindeq)
- [LC_ALL_KEY](SybaseAdaptor-2.md#apple-inceerchjjbek)
- [ENCRYPTPASSWORD](SybaseAdaptor-2.md#apple-inceerkkizfeu)
- [PRIMITIVE_TYPE_MAP](SybaseAdaptor-2.md#apple-inceeqsjjfces)

The last three keys are optional. The `ENCRYPTPASSWORD` key
provides support for Sybase password encryption. A value for the `LC_ALL_KEY` declares
to the Sybase server the character set being used by the client
(such as eucjis, ascii7, or iso_1). For a complete list of types
available for this field, see your Sybase documentation. The `PRIMITIVE_TYPE_MAP` entry
describes the mapping of user-defined data types to their base Sybase
type (such as varchar or datetime). For more information on user-defined
data types, see ["Data Type Mapping"](#apple-ijbukqscjfbuo).

To add any of these optional keys and appropriate values to
your connection dictionary, you can manually edit your model file.
For example:

> ```
> connectionDictionary = {databaseName = People;
>     hostName = "";
>     LC_ALL = eucjis;
>     password = "";
>     primitiveTypeMap = {id = varchar; ssn = char(9); };
>     sybasePasswordEncryption = YES;
>     userName = "";
> };
> ```

Subsequently changing the connection dictionary in your model
file using the Set Adaptor Info command in EOModeler has no effect
on these keys and their values-they are preserved unless you edit
the file to remove them. Alternatively you can add the optional
keys to a model's connection dictionary programmatically.

The default character set for non-Japanese systems is iso_1
(that is, ISO Latin 1), while the default character set for Japanese
systems is eucjis. You only need to add the LC_ALL key to your connection dictionary
if you are using a character set other than your system's default.

See the [SybaseAdaptor](SybaseAdaptor-2.md#apple-inceer2fi5feg) class specification
for more information on the connection dictionary key constants.

## Error Handling

SybaseAdaptor, SybaseContext, and SybaseChannel can raise
exceptions due to programming errors that result in invalid argument
values or internal inconsistencies. In addition, messages, errors,
and failure status returned from the Sybase SQL Server and client
libraries can also result in EOGeneralAdaptorExceptions. When an
exception results from a callback to the CS_CLIENTMSG_CB (Sybase
ClientMessage callback) or the CS_SERVERMSG_CB (Sybase ServerMessage
callback), all of the information passed into this routine is available
in the userInfo dictionary contained by the exception. When an exception
is raised in response to a Sybase ClientMessage callback, you can
get the information provided by the client library as follows:

> ```
> clientMsgDict = [[localException userInfo]
>     objectForKey:@"sybaseClientMessageDictionary"];
> ```

The `clientMsgDict` contains
the following keys which have values corresponding to those sent
in the callback function that raised the exception: `msgstring`, `osstring`, `sqlstate`, `severity`, `msgnumber`, `osnumber`, `status`.

Similarly, when the exception is raised in response to a Sybase
ServerMessage callback, you can get the information provided by
the server as follows:

> ```
> svrMsgDict = [[localException userInfo]     objectForKey:@"sybaseServerMessageDictionary"];
> ```

The `svrMsgDict` contains
the following keys which have values corresponding to those sent
in the callback function that raised the exception: `text`, `svrname`, `proc`, `sqlstate`, `msgnumber`, `state`, `severity`, `line`, `status`.

## Locking

All adaptors use the database server's native locking facilities
to lock rows on the server. The Sybase adaptor locks a row by using
the HOLDLOCK keyword in SELECT statements. This occurs when:

- You send the adaptor channel a __selectAttributes:fetchSpecification:lock:entity:__ message
  with YES specified as the value for the lock: keyword.
- You explicitly lock an object's row with the EODatabaseContext's __lockObjectWithGlobalID:editingContext:__ message.
- You set pessimistic locking at the database level and fetch
  objects.

The semantics of the HOLDLOCK keyword are such that when you
lock a row other users can't update it, but it doesn't guarantee
that your update will succeed. This is because other users could
be holding a lock on the same row. However, you can still read rows
that are locked by other users.

## Data Type Mapping

Every adaptor provides a mapping between each server data
type (the __external__ type) and the Objective-C type
(the __internal__ type) to which a database value
will be coerced when it's fetched from the database. The following
table lists the mapping used by SybaseAdaptor.

|  |  |
| --- | --- |
| __External Data Type__ | __Internal Data Type__ |
| `binary` | NSData |
| `bit` | NSNumber |
| `char` | NSString |
| `datetime` | NSGregorianDate |
| `datetimn` | NSGregorianDate |
| `decimal` | NSDecimalNumber |
| `decimaln` | NSDecimalNumber |
| `float` | NSNumber |
| `floatn` | NSNumber |
| `image` | NSData |
| `int` | NSNumber |
| `intn` | NSNumber |
| `money` | NSDecimalNumber |
| `moneyn` | NSDecimalNumber |
| `nchar` | NSString |
| `numeric` | NSDecimalNumber |
| `numericn` | NSDecimalNumber |
| `nvarchar` | NSString |
| `real` | NSNumber |
| `smalldatetime` | NSCalendarDate |
| `smallint` | NSNumber |
| `smallmoney` | NSDecimalNumber |
| `sysname` | NSString |
| `text` | NSString |
| `timestamp` | NSData |
| `tinyint` | NSNumber |
| `varbinary` | NSData |
| `varchar` | NSString |

In addition, SybaseAdaptor provides a mapping for user-defined
data types. For example, a custom data type __partnumber__defined
as `char(10)` is mapped
to NSString-the Objective-C type to which __partnumber__'s
base data type (`char`)
is mapped. SybaseAdaptor's implementation of __describeModelWithTableNames:__ automatically
creates mappings for user-defined data types and saves them in the
connection dictionary of the newly created model. Consequently,
even models created with EOModeler automatically include information
about custom data types.

Since information about custom types is stored in a model's
connection dictionary, the type mapping methods- [externalToInternalTypeMap](SybaseAdaptor-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpkn4weyltmvawiylqorxxel3fpb2gk4tomfwfi32jnz2gk4tomfwfi6lqmvgwc4a), __internalTypeForExternalType:model:__,
and __isValidQualifierType:model:__-use the
model argument if it is provided. If the model argument isn't provided,
these methods don't have user-defined data type information available
to them.

## Prototype Attributes

The SybaseEOAdaptor Framework provides the following set of
prototype attributes:

## Generating Primary Keys

Each adaptor provides a database-specific implementation of
the method __primaryKeyForNewRowWithEntity:__ for
generating primary keys. The SybaseChannel's implementation uses
a table named `eo_sequence_table` to
keep track of the next available primary key value for a given table.
The table contains a row for each table for which the adaptor provides
primary key values. The statement used to create the `eo_sequence_table` is:

> ```
> create table eo_sequence_table (
>     table_name varchar(32),
>     counter int null
> )
> ```

SybaseChannel uses a stored procedure named `eo_pk_for_table` to
access and maintain the primary key counter in `eo_sequence_table`.
The stored procedure is defined as follows:

> ```
> create procedure
> eo_pk_for_table @tname varchar(32) as
> begin
>     define @max int
>
>     update eo_sequence_table
>     set counter = counter + 1
>     where table_name = @tname
>
>     select counter
>     from eo_sequence_table
>     where table_name = @tname
> end
> ```

The stored procedure increments the counter in the `eo_sequence_table` row
for the specified table, selects the counter value, and returns
it. SybaseChannel executes this `eo_pk_for_table` stored
procedure from __primaryKeyForNewRowWithEntity:__ and
returns the stored procedure's return value.

To use SybaseChannel's database-specific primary key generation
mechanism, be sure that your database accommodates the adaptor's
scheme. To modify your database so that it supports the adaptor's
mechanism for generating primary keys, use EOModeler. For more information
on this topic, see _Enterprise Objects Framework Developer's
Guide_.

[![Table of Contents](attachments/images/up.gif)](SybaseEOAdaptorTOC.md)
