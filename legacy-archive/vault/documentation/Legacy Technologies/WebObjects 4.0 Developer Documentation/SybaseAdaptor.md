---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/SybaseAdaptor.html
archived_at: '2026-07-18T01:28:49.766213Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20SybaseEOAdaptor%20Framework.md)
[!](SybaseChannel.md)

---

# SybaseAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Inherits From:__
com.apple.yellow.sybaseeoadaptor

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

**[externalTypesWithModel:](#apple-ge2do)

**[primitiveTypeForExternalTypeInModel](#apple-geztgni)****

**Getting information from the connection dictionary**

**[connectionKeys](#apple-ge2tm)**

**Bracketing calls to ct_connect()**

**[prepareEnvironmentForConnect](#apple-gezdmni)

**[resetEnvironmentAfterConnect](#apple-gezdmnq)****

**Callback methods**

**[sybaseContextDidDisconnect](#apple-gezdmoa)

**[sybaseContextWillConnect](#apple-gezdony)****

---

## Class Methods

---

### externalTypesWithModel:

public static com.apple.yellow.foundation.NSArray `externalTypesWithModel`(com.apple.yellow.eoaccess.EOModel _model_)

Overrides the EOAdaptor method [`externalTypesWithModel:`](#apple-ge2do) to return the Sybase database types.

---

### primitiveTypeForExternalTypeInModel

public static java.lang.String `primitiveTypeForExternalTypeInModel`(java.lang.String _externalType_, com.apple.yellow.eoaccess.EOModel _model_)

+ (NSString \*)`primitiveTypeForExternalType:`(NSString \*)_externalType_ `model:`(EOModel \*)_model_

Returns the primitive type on which a given custom type, defined on the server, is based.

---

## Instance Methods

---

### connectionKeys

public com.apple.yellow.foundation.NSArray `connectionKeys`()

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### prepareEnvironmentForConnect

public void `prepareEnvironmentForConnect`()

A call to this method should preceed all calls to `ct_connect`() to set the `LC_ALL` environment variable setting to the value specified in the model connection dictionary.

__See also:__
[`resetEnvironmentAfterConnect`](#apple-gezdmnq)

---

### resetEnvironmentAfterConnect

public void `resetEnvironmentAfterConnect`()

A call to this method should follow all calls to `ct_connect`() to set the `LC_ALL` environment variable setting to the value specified in the model connection dictionary.

__See also:__
[`prepareEnvironmentForConnect`](#apple-gezdmni)

---

### sybaseContextDidDisconnect

public void `sybaseContextDidDisconnect`(SybaseContext _aSybaseContext_)

Callback method that is invoked after the associated Sybase context disconnects.

---

### sybaseContextWillConnect

public void `sybaseContextWillDisconnect`(SybaseContext _aSybaseContext_)

Callback method that is invoked just before the associated Sybase context disconnects.

---

[!](The%20SybaseEOAdaptor%20Framework.md)
[!](SybaseChannel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
