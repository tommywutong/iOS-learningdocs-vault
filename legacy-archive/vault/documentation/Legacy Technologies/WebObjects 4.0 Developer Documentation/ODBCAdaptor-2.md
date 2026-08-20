---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/ODBCAdaptor.html
archived_at: '2026-07-18T01:28:48.649708Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20ODBCEOAdaptor%20Framework-2.md)
[!](ODBCChannel-2.md)

---

# ODBCAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Declared in:__
ODBCEOAdaptor/ODBCAdaptor.h

---

## Class Description

An ODBCAdaptor represents a single connection to an ODBC database server, and is responsible for keeping login and model information, performing ODBC-specific formatting of SQL expressions, and reporting errors.

ODBC (Open Data Base Connectivity) defines a standard interface that Windows applications can use to access any data source. Unlike the other Enterprise Objects Frameworks adaptors that support a single type of database, the ODBC adaptor supports any data source that has an ODBC driver. Consequently, in addition to having standard adaptor features, the ODBC adaptor also manages information relating to the driver and to the data types defined by the data source the driver supports.

The ODBCAdaptor class doesn't support nested transactions.

---

## Method Types

**Mapping external types to internal types**

**[+ assignExternalTypeForAttribute:](#apple-gizdqmq)

**[+ externalTypeForOdbcType:model:](#apple-gq3q)

**[+ externalTypesWithModel:](#apple-giztcma)

**[+ getOdbcInfoWithConnectionDictionary:](#apple-gu2q)

**[+ internalTypeForExternalType:model:](#apple-gizteoi)

**[+ odbcTypeForExternalType:model:](#apple-gyzq)

**[+ odbcTypeForStringRepresentation:](#apple-gy3q)

**[+ resetOdbcInfoWithConnectionDictionary:](#apple-g4yq)

**[+ stringRepresentationForOdbcType:](#apple-g42q)******************

**Access information in the connection dictionary**

**[+ driverInfoForModel:](#apple-gqzq)

**[+ typeInfoForModel:](#apple-g44q)

**[- driverInfo](#apple-he2q)

**[- typeInfo](#apple-geytc)********

**Testing the connection dictionary**

**[- assertConnectionDictionaryIsValid](#apple-giztqoa)

**[- defaultExpressionClass](#apple-giztsny)

****[- isValidQualifierType:model:](#apple-gi2denq)

**[- odbcConnectionString](#apple-geydg)

**[- odbcEnvironment](#apple-gi2dgoi)************

---

## Class Methods

---

### assignExternalTypeForAttribute:

+ (void)`assignExternalTypeForAttribute:`(EOAttribute \*)_attribute_

Sets the external information for _attribute_ based on the internal type, precision, and width.

---

### driverInfoForModel:

+ (NSDictionary \*)`driverInfoForModel:`(EOModel \*)_model_

Returns an NSDictionary containing the driver information cached in the connection dictionary of _model_. If the information is not yet cached in _model_, connects to the database to get it.

__See also:__
`typeInfoForModel:`, - `driverInfo`, - `typeInfo`

---

### externalTypeForOdbcType:model:

+ (NSString \*)`externalTypeForOdbcType:`(int)_type_ `model:`(EOModel \*)_model_

Returns the external type that represents the best match for an ODBC _type_ in _model_.

---

### externalTypesWithModel:

+ (NSArray \*)`externalTypesWithModel:`(EOModel \*)_model_

Overrides the EOAdaptor method `externalTypesWithModel:` to return the ODBC database types.

__See also:__
`internalTypeForExternalType:model:`

---

### getOdbcInfoWithConnectionDictionary:

+ (NSDictionary \*)`getOdbcInfoWithConnectionDictionary:`(NSDictionary \*)_connectionDictionary_

Sets up the typeInfo and driverInfo dictionaries in _connectionDictionary_, and returns an updated connection dictionary. Creates an ODBCAdaptor, ODBCContext, and ODBCChannel, and connects to the database to get the information for the typeInfo and driverInfo dictionaries.

---

### internalTypeForExternalType:model:

+ (NSString \*)`internalTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Overrides the EOAdaptor method `internalTypeForExternalType:model:` to return the name of the Objective-C class used to represent values stored in the database as _externalType_.

__See also:__
`externalTypesWithModel:`

---

### odbcTypeForExternalType:model:

+ (NSString \*)`odbcTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Returns the ODBC type for _externalType_, as defined in the typeInfo dictionary in _model_'s connection dictionary.

---

### odbcTypeForStringRepresentation:

+ (int)`odbcTypeForStringRepresentation:`(NSString \*)_type_

Returns the ODBC type (such as SQL_CHAR) for _type_ (such as @"CHAR"). The method `stringRepresentationForOdbcType:` performs the opposite function: returning a string for a specified ODBC type. These methods are used in conjunction to encode ODBC types in the typeInfo dictionary.

---

### resetOdbcInfoWithConnectionDictionary:

+ (NSDictionary \*)`resetOdbcInfoWithConnectionDictionary:`(NSDictionary \*)_connectionDictionary_

Removes the typeInfo and driverInfo dictionaries from a copy of _connectionDictionary_ and returns the modified connection dictionary.

---

### stringRepresentationForOdbcType:

+ (NSString \*)`stringRepresentationForOdbcType:`(int)_type_

Returns the string representation of _type_-for example, for the type SQL_CHAR this method would return the string @"CHAR". The method `odbcTypeForStringRepresentation:` performs the opposite function: returning the ODBC type for a specified string. These methods are used in conjunction to encode ODBC types in the typeInfo dictionary.

---

### typeInfoForModel:

+ (NSDictionary \*)`typeInfoForModel:`(EOModel \*)_model_

Returns an NSDictionary containing the type information cached in the connection dictionary of _model_. If the information is not yet cached in _model_, connects to the database to get it.

__See also:__
`driverInfoForModel:`, - `driverInfo`, - `typeInfo`

---

## Instance Methods

---

### assertConnectionDictionaryIsValid

- (void)`assertConnectionDictionaryIsValid`

Determines whether the receiver's connection dictionary is valid. The adaptor uses this method in conjunction with displaying a server login panel. Raises an exception if an error occurs.

Note that this method doesn't open a connection to the database-that happens when the first adaptor channel is sent an `openChannel` message.

---

### defaultExpressionClass

- (Class)`defaultExpressionClass`

Returns the ODBCSQLExpression class.

---

### driverInfo

- (NSDictionary \*)`driverInfo`

Returns an NSDictionary containing the driver information cached in the receiver's model's connection dictionary. If the information is not yet cached in the model, connects to the database to get it.

__See also:__
- `typeInfo`

---

### isValidQualifierType:model:

- (BOOL)`isValidQualifierType:`(NSString \*)_typeName_ `model:`(EOModel \*)_model_

Returns YES if _model_'s attribute of the type _typeName_ can be used in a qualifier, otherwise returns NO.

---

### odbcConnectionString

- (NSString \*)`odbcConnectionString`

Returns the user name, password, and data source as a string that's used to connect to the database.

---

### odbcEnvironment

- (void \*)`odbcEnvironment`

Returns the ODBC Environment Handle HENV as a `void*`; to work with it, you must cast it to HENV.

---

### typeInfo

- (NSDictionary \*)`typeInfo`

Returns an NSDictionary containing the type information cached in the receiver's model's connection dictionary. If the information is not yet cached in the model, connects to the database to get it.

__See also:__
- `driverInfo`, `driverInfoForModel:`, `typeInfoForModel:`

---

[!](The%20ODBCEOAdaptor%20Framework-2.md)
[!](ODBCChannel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
