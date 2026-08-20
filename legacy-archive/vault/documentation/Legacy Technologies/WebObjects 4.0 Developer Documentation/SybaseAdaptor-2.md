---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/SybaseAdaptor.html
archived_at: '2026-07-18T01:28:50.331696Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20SybaseEOAdaptor%20Framework-2.md)
[!](SybaseChannel-2.md)

---

# SybaseAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Declared in:__
SybaseEOAdaptor/SybaseAdaptor.h

---

## Class Description

A SybaseAdaptor represents a single connection to a Sybase database server, and is responsible for keeping login and model information, performing Sybase-specific formatting of SQL expressions, and reporting errors.

The features SybaseAdaptor adds to EOAdaptor are as follows:

- The ability to specify a client character set and language
- Sybase password encryption

The SybaseAdaptor class has these restrictions: A context can only manage one channel at a time, and the adaptor doesn't support full outer joins because the Sybase server itself doesn't support them.

---

## Method Types

**Mapping external types to internal types**

**[+ externalTypesWithModel:](#apple-ge2do)

**[+ internalTypeForExternalType:model:](#apple-ge4dgmy)

**[+ primitiveTypeForExternalType:model:](#apple-geztgni)******

**Getting information from the connection dictionary**

**[- connectionKeys](#apple-ge2tm)**

**Bracketing calls to ct_connect()**

**[- prepareEnvironmentForConnect](#apple-gezdmni)

**[- resetEnvironmentAfterConnect](#apple-gezdmnq)****

**Callback methods**

**[- sybaseContextDidDisconnect:](#apple-gezdmoa)

**[- sybaseContextWillConnect:](#apple-gezdony)****

---

## Class Methods

---

### externalTypesWithModel:

+ (NSArray \*)__externalTypesWithModel:__ (EOModel \*)_model_

Overrides the EOAdaptor method [`externalTypesWithModel:`](#apple-ge2do) to return the Sybase database types.

__See also:__
[+ `internalTypeForExternalType:model:`](#apple-ge4dgmy)

---

### internalTypeForExternalType:model:

+ (NSString \*)__internalTypeForExternalType:__ (NSString \*)_extType_ __model:__ (EOModel \*)_model_

Overrides the EOAdaptor method [`internalTypeForExternalType:model:`](#apple-ge4dgmy) to return the name of the Objective-C class used to represent values stored in the database as _extType_ for the model _model_.

__See also:__
[+ `externalTypesWithModel:`](#apple-ge2do)

---

### primitiveTypeForExternalType:model:

+ (NSString \*)`primitiveTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Returns the primitive type on which a given custom type, defined on the server, is based.

---

## Instance Methods

---

### connectionKeys

- (NSArray \*)__connectionKeys__

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### prepareEnvironmentForConnect

- (void)`prepareEnvironmentForConnect`

A call to this method should preceed all calls to `ct_connect`() to set the `LC_ALL` environment variable setting to the value specified in the model connection dictionary.

__See also:__
[- `resetEnvironmentAfterConnect`](#apple-gezdmnq)

---

### resetEnvironmentAfterConnect

- (void)`resetEnvironmentAfterConnect`

A call to this method should follow all calls to `ct_connect`() to set the `LC_ALL` environment variable setting to the value specified in the model connection dictionary.

__See also:__
[- `prepareEnvironmentForConnect`](#apple-gezdmni)

---

### sybaseContextDidDisconnect:

- (void)`sybaseContextDidDisconnect:`(SybaseContext \*)_aSybaseContext_

Callback method that is invoked after the associated Sybase context disconnects.

---

### sybaseContextWillConnect:

- (void)`sybaseContextWillDisconnect:`(SybaseContext \*)_aSybaseContext_

Callback method that is invoked just before the associated Sybase context disconnects.

---

[!](The%20SybaseEOAdaptor%20Framework-2.md)
[!](SybaseChannel-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
