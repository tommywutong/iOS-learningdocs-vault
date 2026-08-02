---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/OracleAdaptor.html
archived_at: '2026-07-18T01:28:49.377501Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20OracleEOAdaptor%20Framework-2.md)
[!](OracleChannel-2.md)

---

# OracleAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Declared in:__
OracleEOAdaptor/OracleAdaptor.h

---

## Class Description

An OracleAdaptor represents a single connection to an Oracle database server, and is responsible for keeping login and model information, performing Oracle-specific formatting of SQL expressions, and reporting errors.

The OracleAdaptor class has these restrictions: You can't have nested transactions, and the adaptor doesn't support full outer joins.

---

## Method Types

**Mapping external types to internal types**

**[+ externalTypesWithModel:](#apple-giytami)

**[+ internalTypeForExternalType:model:](#apple-giytcmq)****

**Working with channels and contexts**

**[- adaptorChannelClass](#apple-he3dg)

**[- adaptorContextClass](#apple-ha3tm)****

**Testing the connection dictionary**

**[- assertConnectionDictionaryIsValid](#apple-ha4da)**

**Getting information from the connection dictionary**

**[- connectionKeys](#apple-ha4di)

**[- oracleConnectionString](#apple-hezda)****

**Coercing fetched values**

**[- fetchedValueForDataValue:attribute:](#apple-gizdimi)

**[- fetchedValueForDateValue:attribute:](#apple-gizdini)

**[- fetchedValueForNumberValue:attribute:](#apple-gizdioi)

**[- fetchedValueForStringValue:attribute:](#apple-gizdkmy)********

**Returning the default expression class**

**[- defaultExpressionClass](#apple-gizdgny)**

**Verifying a qualifier type**

**[- isValidQualifierType:model:](#apple-gizdmmi)**

---

## Class Methods

---

### externalTypesWithModel:

+ (NSArray \*)`externalTypesWithModel:`(EOModel \*)_model_

Overrides the EOAdaptor method `externalTypesWithModel:` to return the Oracle database types.

__See also:__
[- `internalTypeForExternalType:model:`](#apple-giytcmq)

---

### internalTypeForExternalType:model:

+ (NSString \*)`internalTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Overrides the EOAdaptor method `internalTypeForExternalType:model:` to return the name of the Objective-C class used to represent values stored in the database as _externalType_.

__See also:__
[+ `externalTypesWithModel:`](#apple-giytami)

---

## Instance Methods

---

### adaptorChannelClass

- (Class)`adaptorChannelClass`

Returns the OracleChannel class.

---

### adaptorContextClass

- (Class)`adaptorContextClass`

Returns the OracleContext class.

---

### assertConnectionDictionaryIsValid

- (void)`assertConnectionDictionaryIsValid`

Overrides the EOAdaptor method `assertConnectionDictionaryIsValid` to verify that the receiver can connect to the database with its connection dictionary. Briefly forms a connection to the server to validate the connection dictionary and then closes the connection. The adaptor uses this method in conjunction with displaying a server login panel. Raises an exception if an error occurs.

Note that this method doesn't open a connection to the database-that happens when the first adaptor channel is sent an message.

---

### connectionKeys

- (NSArray \*)`connectionKeys`

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### defaultExpressionClass

- (Class)`defaultExpressionClass`

Returns the OracleSQLExpression class.

---

### fetchedValueForDataValue:attribute:

- (NSData \*)`fetchedValueForDataValue:`(NSData \*)_value_ `attribute:`(EOAttribute \*)_attribute_

Returns _value_.

---

### fetchedValueForDateValue:attribute:

- (NSCalendarDate \*)`fetchedValueForDateValue:`(NSCalendarDate \*)_date_ `attribute:`(EOAttribute \*)_attribute_

Returns an NSCalendarDate based on _date_ whose millisecond value is set to 0.

---

### fetchedValueForNumberValue:attribute:

- (NSNumber \*)`fetchedValueForNumberValue:`(NSNumber \*)_numberValue_`attribute:`(EOAttribute \*)_attribute_

Returns an NSNumber based on _numberValue_ that has been rounded according to the precision and scale specified for _attribute_.

---

### fetchedValueForStringValue:attribute:

- (NSString \*)`fetchedValueForStringValue:`(NSString \*)_value_ `attribute:`(EOAttribute \*)_attribute_

Provides default processing for string values. Trims trailing spaces and returns `nil` for 0 length strings.

---

### isValidQualifierType:model:

- (BOOL)`isValidQualifierType:`(NSString \*)_typeName_ `model:`(EOModel \*)_model_

Overrides the EOAdaptor method `isValidQualifierType:model:` to return YES if an attribute of type _typeName_ can be used in a qualifier (a SQL WHERE clause) sent to the database server, NO otherwise. _typeName_ is the name of a type as required by the database server, such as an Oracle "NUMBER".

---

### oracleConnectionString

- (NSString \*)`oracleConnectionString`

Returns the user name, password, host machine, and server id as a string suitable to be supplied as an argument to orlon().

---

[!](The%20OracleEOAdaptor%20Framework-2.md)
[!](OracleChannel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
