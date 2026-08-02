---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/Java/Introduction.html
archived_at: '2026-07-15T08:11:46.280669Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
OracleEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](OracleEOAdaptorTOC.md)

# OracleEOAdaptor Framework

> __Package:__
> com.apple.yellow.oracleeoadaptor

---

## Introduction

The OracleEOAdaptor framework is a set of classes that allow
your programs to connect to an Oracle server. These classes provide
Oracle-specific method implementations for the EOAccess framework's EOAdaptor,
EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract
classes.

The following table lists the classes in the OracleEOAdaptor
Framework and provides a brief description of each class.

|  |  |
| --- | --- |
| __Class__ | __Description__ |
| OracleAdaptor | Represents a single connection to a Oracle database server, and is responsible for keeping login and model information, performing Oracle-specific formatting of SQL expressions, and reporting errors. |
| OracleChannel | Represents an independent communication channel to the database server its OracleAdaptor is connected to. |
| OracleContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| OracleSQLExpression | Defines how to build SQL statements for OracleChannels. |

## The Connection Dictionary

The connection dictionary contains items needed to connect
to an Oracle server, such as the server name and database (it's
common to omit the user name and password from the connection dictionary, and
prompt users to enter those values in a login panel). The keys of
this dictionary identify the information the server expects, and
the values of those keys are the values that the adaptor uses when trying
to connect to the server.

The Oracle adaptor defines string constants for use as connection
dictionary keys:

- [ServerIdKey](OracleAdaptor.md#apple-inceerseiveem)
- [HostMachineKey](OracleAdaptor.md#apple-inceeq2firbek)
- [UserNameKey](OracleAdaptor.md#apple-inceersdjjauo)
- [PasswordKey](OracleAdaptor.md#apple-inceeqsfivfek)
- [ConnectionStringKey](OracleAdaptor.md#apple-inceercjifdeg)
- [NlsLangKey](OracleAdaptor.md#apple-inceeskbijdes)

The OracleAdaptor attempts to connect with a connection string
of the form "userName/password@serverId". If all the values
except the one for `ServerIdKey` are
absent, then OracleAdaptor attempts to connect with just the value
for `ServerIdKey`.

The `ConnectionStringKey` and `NlsLangKey` are
optional. The value for `ConnectionStringKey` is
a string to be used to login to the database server. If the `ConnectionStringKey` is
present in the connection dictionary, the other logon keys (`ServerIdKey`, `HostMachineKey`, `UserNameKey`,
and `PasswordKey`) are ignored
and the value for the `ConnectionStringKey` is
used to connect to the database.

The value for `NlsLangKey` is
used to set the Oracle NLS_LANG environment variable. NLS_LANG declares
to the Oracle server the character set being used by the client,
as well as the language in which you want server error messages
to appear. The format is as follows:

language_territory. characterSet

For example, supplying the value `japanese_japan.jeuc` for
the `NlsLangKey` tells
the server that the language is Japanese, the territory is Japan,
and the character set is jeuc. See your Oracle documentation for
a complete list of types available for this field.

To add the `NlsLangKey` and
a value to your connection dictionary, you can manually edit your
model file. For example:

> ```
> connectionDictionary = {
>     password = tiger;
>     serverId = sjOracle;
>     userName = scott;
>     NLS_LANG = american_america.us7ascii;
> };
> ```

Subsequently changing the connection dictionary in your model
file using the Set Adaptor Info command in EOModeler has no effect
on these keys and their values-they are preserved unless you edit the
file to remove them.

The default character set for Japanese systems is jeuc. If
you are using a non-Japanese system, the default is whatever Oracle
provides. You only need to add the `NlsLangKey` to
your connection dictionary if you are using a character set other
than your system's default.

|  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Enterprise Objects Framework uses Mac OS X Server encoding to represent string data, and it passes strings to the database without converting them to the database character set. If you require that the data passed to your server is in an encoding other than Mac OS X Server encoding, you need to subclass NSString. |

## Locking

All adaptors use the database server's native locking facilities
to lock rows on the server. The Oracle adaptor locks a row by using
the SELECT... FOR UPDATE... statement. This occurs when:

- You send the adaptor channel a __selectAttributes__ message
  with true specified as the value for the __lock__ keyword.
- You explicitly lock an object's row with the EODatabaseContext's __lockObjectWithGlobalID__ message.
- You set pessimistic locking at the database level and fetch
  objects.

## Data Type Mapping

Every adaptor provides a mapping between each server data
type and the Java type to which a database value will be coerced
when it's fetched from the database. The following table lists
the mapping used by OracleAdaptor.

|  |  |
| --- | --- |
| __Oracle Data Type__ | __Java Data Type__ |
| `VARCHAR2` | String |
| `NUMBER` | BigDecimal |
| `LONG` | String |
| `DATE` | NSGregorianDate |
| `RAW` | NSData |
| `LONG RAW` | NSData |
| `CHAR` | String |
| `MLSLABEL` | String |
| `REFCURSOR` | OracleChannel |

The type mapping methods-__externalTypesWithModel__, __internalTypeForExternalTypeInModel__,
and __isValidQualifierTypeInModel__-allow
for an adaptor to supplement its set of type mappings with additional
mappings for user-defined database types. OracleAdaptor does not
make use of the model argument if one is provided.

## Prototype Attributes

The OracleAdaptor Framework provides the following set of
prototype attributes:

|  |  |  |  |
| --- | --- | --- | --- |
| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| `binaryID` | `RAW` | NSData | `width = 12` |
| `city` | `VARCHAR2` | String | `columnName = CITY` `width = 50` |
| `date` | `DATE` | NSGregorianDate | `columnName = ""` |
| `longText` | `LONG` | String |  |
| `money` | `NUMBER` | BigNumber | `columnName = ""` |
| `phoneNumber` | `VARCHAR2` | String | `columnName = PHONE` `width = 20` |
| `rawImage` | `LONG RAW` | NSData | `columnName = RAW_IMAGE` |
| `state` | `VARCHAR2` | String | `columnName = STATE` `width = 2` |
| `streetAddress` | `VARCHAR2` | String | `columnName = STREET_ADDRESS` `width = 100` |
| `tiffImage` | `LONG RAW` | NSImage | `adaptorValueConversionMethodName = TIFFRepresentation` `columnName = PHOTO` `valueFactoryMethodName = "imageWithData:"` |
| `uniqueID` | `NUMBER` | Number | `columnName = ""` `valueType = i` |
| `zipCode` | `VARCHAR2` | String | `columnName = ZIP` `width = 10` |

## Handling Errors

OracleChannel provides a method for handling errors: [raiseOracleError](OracleChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkdnbqw43tfnqxxeyljonsu64tbmnwgkrlsojxxe). This method is
invoked whenever the channel encounters an error reported by the
Oracle server.

## Generating Primary Keys

Each adaptor provides a database-specific implementation of
the method __primaryKeyForNewRowWithEntity__ for
generating primary keys. The OracleChannel's implementation uses
sequence objects to provide primary key values. The statement used
to create the sequence is:

> ```
> create sequence table_SEQ
> ```

where table is the name of the table for which the adaptor
provides primary key values. The adaptor sets the sequence start
value to the corresponding table's maximum primary key value plus
one.

To use OracleChannel's database-specific primary key generation
mechanism, be sure that your database accommodates the adaptor's
scheme. To modify your database so that it supports the adaptor's
mechanism for generating primary keys, use EOModeler. For more information
on this topic, see _Enterprise Objects Framework Developer's
Guide_.

## Bind Variables

The OracleAdaptor uses bind variables. A bind variable is
a placeholder used in an SQL statement that is replaced with an
actual value after the database server determines an execution plan.
You use the following OracleSQLExpression methods to operate on
bind variables:

- bindVariableDictionaryForAttribute
- mustUseBindVariableForAttribute
- shouldUseBindVariableForAttribute

[![Table of Contents](attachments/images/up.gif)](OracleEOAdaptorTOC.md)
