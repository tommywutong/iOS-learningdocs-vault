---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/InformixAdaptor.html
archived_at: '2026-07-18T01:28:47.447313Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20InformixEOAdaptor%20Framework.md)
[!](InformixChannel.md)

---

# InformixAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Inherits From:__
com.apple.yellow.informixeoadaptor

---

## Class Description

An InformixAdaptor represents a single connection to an Informix database server, and is responsible for keeping login and model information, performing Informix-specific formatting of SQL expressions, and reporting errors.

The InformixAdaptor class has these restrictions: You can't have nested transactions, and the adaptor doesn't support full outer joins.

---

## Method Types

**Working with channels and contexts**

**[adaptorChannelClass](#apple-gq2q)

**[adaptorContextClass](#apple-gq4q)****

**Getting information from the connection dictionary**

**[informixConnectionString](#apple-gy4q)

**[informixDefaultForKey](#apple-hayq)

**[connectionKeys](#apple-gu3q)******

**Error handling**

**[raiseInformixError](#apple-geyds)**

---

## Instance Methods

---

### adaptorChannelClass

public java.lang.Class `adaptorChannelClass`()

Returns the InformixChannel class.

---

### adaptorContextClass

public java.lang.Class `adaptorContextClass`()

Returns the InformixContext class.

---

### connectionKeys

public com.apple.yellow.foundation.NSArray `connectionKeys`()

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### informixConnectionString

public java.lang.String `informixConnectionString`()

Returns the user name, password, and database name as a string suitable to be supplied as an argument to db_connect().

---

### informixDefaultForKey

public java.lang.String `informixDefaultForKey`(java.lang.String _aString_)

Returns the user default setting for _key_. To get this information it first checks the user defaults, and then the adaptor's internal defaults dictionary.

---

### raiseInformixError

public void `raiseInformixError`(java.lang.String _aString_)

Examines Informix structures for error flags and raises an exception if one is found. Extracts the error information in the connection structure and use it to build and raise an exception.

****

---

[!](The%20InformixEOAdaptor%20Framework.md)
[!](InformixChannel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
