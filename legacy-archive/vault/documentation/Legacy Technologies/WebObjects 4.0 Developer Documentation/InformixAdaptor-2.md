---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/InformixAdaptor.html
archived_at: '2026-07-18T01:28:47.846873Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20InformixEOAdaptor%20Framework-2.md)
[!](InformixChannel-2.md)

---

# InformixAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Declared in:__
InformixEOAdaptor/InformixAdaptor.h

---

## Class Description

An InformixAdaptor represents a single connection to an Informix database server, and is responsible for keeping login and model information, performing Informix-specific formatting of SQL expressions, and reporting errors.

The InformixAdaptor class has these restrictions: You can't have nested transactions, and the adaptor doesn't support full outer joins.

---

## Method Types

**Mapping external types to internal types**

**[+ externalTypesWithModel:](#apple-gm2tgnq)

**[+ internalTypeForExternalType:model:](#apple-gm2tioi)****

**Working with channels and contexts**

**[- adaptorChannelClass](#apple-gq2q)

**[- adaptorContextClass](#apple-gq4q)****

**Testing the connection dictionary**

**[- assertConnectionDictionaryIsValid](#apple-gm2tomq)**

**Getting information from the connection dictionary**

**[- informixConnectionString](#apple-gy4q)

**[- informixDefaultForKey:](#apple-hayq)

**[- connectionKeys](#apple-gu3q)******

**Getting the default expression class**

**[- defaultExpressionClass](#apple-gm2tqnq)**

**Verifying a qualifier type**

**[- isValidQualifierType:model:](#apple-gm3dcmi)**

**Error handling**

**[- raiseInformixError:](#apple-geyds)**

---

## Class Methods

---

### externalTypesWithModel:

+ (NSArray \*)`externalTypesWithModel:`(EOModel \*)_model_

Overrides the EOAdaptor method `externalTypesWithModel:` to return the Informix database types.

__See also:__
[`internalTypeForExternalType:model:`](#apple-gm2tioi)

---

### internalTypeForExternalType:model:

+ (NSString \*)`internalTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Overrides the EOAdaptor method `internalTypeForExternalType:model:` to return the name of the Objective-C class used to represent values stored in the database as _externalType_.

__See also:__
[`externalTypesWithModel:`](#apple-gm2tgnq)

---

## Instance Methods

---

### adaptorChannelClass

- (Class)`adaptorChannelClass`

Returns the InformixChannel class.

---

### adaptorContextClass

- (Class)`adaptorContextClass`

Returns the InformixContext class.

---

### assertConnectionDictionaryIsValid

- (void)`assertConnectionDictionaryIsValid`

Overrides the EOAdaptor method `assertConnectionDictionaryIsValid` to verify that the receiver can connect to the database with its connection dictionary. Briefly forms a connection to the server to validate the connection dictionary and then closes the connection (in other words, this method doesn't open a connecton to the database-that happens when the first adaptor channel is sent an `openChannel` message). The adaptor uses this method in conjunction with displaying a server login panel. Raises an exception if an error occurs.

---

### connectionKeys

- (NSArray \*)`connectionKeys`

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### defaultExpressionClass

- (Class)`defaultExpressionClass`

Returns the InformixSQLExpression class.

---

### informixConnectionString

- (NSString \*)`informixConnectionString`

Returns the user name, password, and database name as a string suitable to be supplied as an argument to db_connect().

---

### informixDefaultForKey:

- (NSString \*)`informixDefaultForKey:`(NSString \*)_key_

Returns the user default setting for _key_. To get this information it first checks the user defaults, and then the adaptor's internal defaults dictionary.

---

### isValidQualifierType:model:

- (BOOL)`isValidQualifierType:`(NSString \*)_typeName_ `model:`(EOModel \*)_model_

Overrides the EOAdaptor method `isValidQualifierType:model:` to return YES if an attribute of type _typeName_ can be used in a qualifier (a SQL WHERE clause) sent to the database server, or NO otherwise. _typeName_ is the name of a type as required by the database server, such as an Informix "VARCHAR".

---

### raiseInformixError:

- (void)`raiseInformixError:`(NSString \*)_sqlString_

Examines Informix structures for error flags and raises an exception if one is found. Extracts the error information in the connection structure and use it to build and raise an exception.

****

---

[!](The%20InformixEOAdaptor%20Framework-2.md)
[!](InformixChannel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
