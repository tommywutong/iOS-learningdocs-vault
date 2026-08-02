---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/ODBCEOAdaptor.html
archived_at: '2026-07-15T08:02:04.815085Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](ODBCAdaptor-2.md)

---

# The ODBCEOAdaptor Framework

__Framework:__
System/Library/Frameworks/ODBCEOAdaptor.framework

__Header File Directories:__
System/Library/Frameworks/ODBCEOAdaptor.framework/Headers

# Introduction

The ODBCEOAdaptor framework is a set of classes that allow your programs to connect to an ODBC server. These classes provide ODBC-specific method implementations for the EOAccess framework's EOAdaptor, EOAdaptorChannel, EOAdaptorContext, and EOSQLExpression abstract classes.

ODBC (Open Data Base Connectivity) defines a standard interface that Windows applications can use to access any data source. Unlike the other Enterprise Objects Frameworks adaptors that support a single type of database, the ODBC adaptor supports any data source that has an ODBC driver. Consequently, in addition to having standard adaptor features, the ODBC adaptor also manages information relating to the driver and to the data types defined by the data source the driver supports.

The following table lists the classes in the ODBCEOAdaptor Framework and provides a brief description of each class.

| __Class__ | __Description__ |
| ODBCAdaptor | Represents a single connection to a ODBC database server, and is responsible for keeping login and model information, performing ODBC-specific formatting of SQL expressions, and reporting errors. |
| ODBCChannel | Represents an independent communication channel to the database server its ODBCAdaptor is connected to. |
| ODBCContext | Represents a single transaction scope on the database server to which its adaptor object is connected. |
| ODBCSQLExpression | Defines how to build SQL statements for ODBCChannels. |

```
```


---

## The Connection Dictionary

The connection dictionary contains items needed to connect to an ODBC server, such as the data source (it's common to omit the user name and password from the connection dictionary, and prompt users to enter those values in a login panel). The keys of this dictionary identify the information the server expects, and the values of those keys are the values that the adaptor uses when trying to connect to the server. For ODBC the required keys are as follows:

> ```
> dataSourceuserNamepassword
> ```

The connection dictionary can also optionally have the keys connectionString, typeInfo, and driverInfo.

The connectionString contains the user name, password, and data source. If the connectionString key is present in the connection dictionary, the other login keys are ignored and this string is used to connect to the database.

The typeInfo key refers to the typeInfo dictionary, which is used to cache type information in the connection dictionary. This is done because different ODBC drivers work with different data types. Caching type information in the connection dictionary avoids costly connections to the driver and the database. The typeInfo dictionary contains the following information for every type in your database:

> ```
> defaultODBCType = (<CHAR/TIMESTAMP/BIT/...>, ...)precision = <precision>minScale = <minScale>maxScale = <maxScale>isUnsigned = <YES/NO>isNullable = <YES/NO>isSearchable = <YES/NO>createParams = <0/1/2>
> ```

Likewise, the driverInfo key refers to the driverInfo dictionary, which stores information about the driver, such as its name and version. This information is also cached in the connection dictionary.

---

## Locking

All adaptors use the database server's native locking facilities to lock rows on the server. If you're using the Microsoft SQL Server, the ODBC adaptor locks a row by using the HOLDLOCK keyword in SELECT statements. In all other cases it uses the SELECT... FOR UPDATE... statement. Locking occurs when:

- You send the adaptor channel a [`selectAttributes:fetchSpecification:lock:entity:`](ODBCChannel.md#apple-geydq) message with YES specified as the value for the `lock:` keyword.
- You explicitly lock an object's row with the EODatabaseContext's `lockObjectWithGlobalID:editingContext:` message.
- You set pessimistic locking at the database level and fetch objects.

---

## Data Type Mapping

Every adaptor provides a mapping between each server data type and the Objective-C type to which a database value will be coerced when it's fetched from the database. ODBC adds an intermediate layer: the generic ODBC type (identifier) to which each database data type maps.

For example, the following table shows the mapping from some of the Microsoft Access database data types to ODBC to Objective-C and Java:

| __Microsoft Access Database Type__ | __Generic ODBC Type__ | __Objective-C Type__ | __Java Data Type__ |
| TEXT | SQL_VARCHAR | NSString | String |
| CURRENCY | SQL_NUMERIC | NSDecimalNumber | BigDecimal |
| BINARY | SQL_BINARY | NSData | NSData |
| DATETIME | SQL_TIMESTAMP | NSCalendarDate | NSGregorianDate |

```
```

The following table lists the mapping between generic ODBC types and Objective-C types.

| __ODBC Data Type__ | __Objective-C Data Type__ | __Java Data Type__ |
| SQL_VARCHAR | NSString | String |
| SQL_CHAR | NSString | String |
| SQL_LONGVARCHAR | NSString | String |
| SQL_DECIMAL | NSDecimalNumber | BigDecimal |
| SQL_NUMERIC | NSDecimalNumber | BigDecimal |
| SQL_BIGINT | NSNumber | Number |
| SQL_SMALLINT | NSNumber | Number |
| SQL_INTEGER | NSNumber | Number |
| SQL_REAL | NSNumber | Number |
| SQL_FLOAT | NSNumber | Number |
| SQL_DOUBLE | NSNumber | Number |
| SQL_BIT | NSNumber | Number |
| SQL_TINYINT | NSNumber | Number |
| SQL_VARBINARY | NSData | NSData |
| SQL_BINARY | NSData | NSData |
| SQL_LONGVARBINARY | NSData | NSData |
| SQL_TIMESTAMP | NSCalendarDate | NSGregorianDate |
| SQL_DATE | NSCalendarDate | NSGregorianDate |
| SQL_TIME | NSCalendarDate | NSGregorianDate |

```
```

Since ODBCAdaptor's type information is stored in a model's connection dictionary, the type mapping methods-[`externalTypesWithModel:`](ODBCAdaptor.md#apple-giztcma), [`internalTypeForExternalType:model:`](ODBCAdaptor.md#apple-gizteoi), and [`isValidQualifierType:model:`](ODBCAdaptor.md#apple-gi2denq)-use the model argument if it is provided. If the model argument isn't provided, these methods don't have data type information available to them.

---

## Prototype Attributes

The ODBCEOAdaptor Framework provides the following set of prototype attributes:

| __Name__ | __External Type__ | __Value Class Name__ | __Other Attributes__ |
| binaryID | BINARY | NSData | width = 12 |
| city | CHAR | NSString | columnName = CITY width = 50 |
| date | DATETIME | NSCalendarDate | columnName = "" |
| longText | LONGTEXT | NSString |  |
| money | CURRENCY | NSDecimalNumber | columnName = "" |
| phoneNumber | CHAR | NSString | columnName = PHONE width = 20 |
| rawImage | LONGBINARY | NSData | columnName = RAW_IMAGE |
| state | CHAR | NSString | columnName = STATE; width = 2 |
| streetAddress | CHAR | NSString | columnName = STREET_ADDRESS width = 100 |
| tiffImage | LONGBINARY | NSImage | adaptorValueConversionMethodName = TIFFRepresentation columnName = PHOTO valueFactoryMethodName = "imageWithData:"; |
| uniqueID | LONG | NSNumber | columnName = "" valueType = i |
| zipCode | CHAR | NSString | columnName = ZIP width = 10 |

```
```


---

## Generating Primary Keys

Each adaptor provides a database-specific implementation of the method `primaryKeyForNewRowWithEntity:` for generating primary keys. The ODBCChannel's implementation uses a table named EO_PK_TABLE to keep track of the next available primary key value for a given table. The table contains a row for each table for which the adaptor provides primary key values.

ODBCChannel's implementation of `primaryKeyForNewRowWithEntity:` attempts to select a value from the EO_PK_TABLE for the new row's table. If the attempt fails because the table doesn't exist, the adaptor creates the table using the following SQL statement:

> ```
> CREATE TABLE EO_PK_TABLE (
> NAME TEXT_TYPE(40),
> PK NUMBER_TYPE
> )
> ```

where _TEXT_TYPE_ is the external (database) type for characters and _NUMBER_TYPE_ is the external type for the table's primary key attribute. The ODBC adaptor sets the PK value for each row to the corresponding table's maximum primary key value plus one. After determining a primary key value for the new row, the ODBC adaptor updates the counter in the corresponding row in EO_PK_TABLE.

For more information on this topic, see _Enterprise Objects Framework Developer's Guide_.

---

## Bind Variables

The ODBCAdaptor uses bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. You use the following ODBCSQLExpression methods to operate on bind variables:

- [- bindVariableDictionaryForAttribute:value:](ODBCSQLExpression-2.md#apple-gq2a)
- [- mustUseBindVariableForAttribute:](ODBCSQLExpression-2.md#apple-ge2dami)
- [- shouldUseBindVariableForAttribute:](ODBCSQLExpression-2.md#apple-ge2dema)

---

[[TOC]](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html) [Prev] [[Next]](ODBCAdaptor.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
