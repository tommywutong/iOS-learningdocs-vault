---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/OracleAdaptor.html
archived_at: '2026-07-18T01:28:49.045808Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20OracleEOAdaptor%20Framework.md)
[!](OracleChannel.md)

---

# OracleAdaptor

__Inherits From:__
EOAdaptor : NSObject

__Inherits From:__
com.apple.yellow.oracleeoadaptorjava

---

## Class Description

An OracleAdaptor represents a single connection to an Oracle database server, and is responsible for keeping login and model information, performing Oracle-specific formatting of SQL expressions, and reporting errors.

The OracleAdaptor class has these restrictions: You can't have nested transactions, and the adaptor doesn't support full outer joins.

---

## Method Types

**Working with channels and contexts**

**[adaptorChannelClass](#apple-he3dg)

**[adaptorContextClass](#apple-ha3tm)****

**Testing the connection dictionary**

**[assertConnectionDictionaryIsValid](#apple-ha4da)**

**Getting information from the connection dictionary**

**[connectionKeys](#apple-ha4di)

**[oracleConnectionString](#apple-hezda)

********

---

## Instance Methods

---

### adaptorChannelClass

public java.lang.Class `adaptorChannelClass`()

Returns the OracleChannel class.

---

### adaptorContextClass

public java.lang.Class `adaptorContextClass`()

Returns the OracleContext class.

---

### assertConnectionDictionaryIsValid

public void `assertConnectionDictionaryIsValid`()

Overrides the EOAdaptor method `assertConnectionDictionaryIsValid` to verify that the receiver can connect to the database with its connection dictionary. Briefly forms a connection to the server to validate the connection dictionary and then closes the connection. The adaptor uses this method in conjunction with displaying a server login panel. Raises an exception if an error occurs.

Note that this method doesn't open a connection to the database-that happens when the first adaptor channel is sent an message.

---

### connectionKeys

public com.apple.yellow.foundation.NSArray `connectionKeys`()

Returns an NSArray containing the keys in the receiver's connection dictionary. You can use this method to prompt the user to supply values for the connection dictionary.

---

### oracleConnectionString

public java.lang.String `oracleConnectionString`()

Returns the user name, password, host machine, and server id as a string suitable to be supplied as an argument to orlon().

---

[!](The%20OracleEOAdaptor%20Framework.md)
[!](OracleChannel.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
