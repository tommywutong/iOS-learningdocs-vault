---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/SybaseSQLExpression.html
archived_at: '2026-07-18T01:28:50.581492Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/SybaseEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](SybaseContext-2.md)
[!](SybaseChannelDelegate.md)

---

# SybaseSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Declared in:__
SybaseEOAdaptor/SybaseSQLExpression.h

---

## Class Description

SybaseSQLExpression defines how to build SQL statements for SybaseChannels.

---

## Method Types

**Generating SQL for attributes and values**

**[+ formatValue:forAttribute:](#apple-ge4dgoi)**

**Getting the server type ID**

**[+ serverTypeIdForName:](#apple-geydi)**

**Getting the lock clause**

**[- lockClause](#apple-geydq)**

****

---

## Class Methods

---

### formatValue:forAttribute:

+ (NSString \*)__formatValue:__ (id)_value_ __forAttribute:__ (EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`formatValue:forAttribute:`](#apple-ge4dgoi) to return a formatted string representation of _value_ for _attribute_ that is suitable for use in a SQL statement.

---

### serverTypeIdForName:

+ (int)__serverTypeIdForName:__ (NSString \*)_typeName_

Returns the Sybase type code (such as 47, 56, or 55) for _typeName_ (such as "char", "int", or "decimal").

---

## Instance Methods

---

### lockClause

- (NSString \*)__lockClause__

Overrides the EOSQLExpression method [`lockClause`](#apple-geydq) to return the SQL string used in a SELECT statement to lock selected rows, which is @"HOLDLOCK"_._

---

[!](SybaseContext-2.md)
[!](SybaseChannelDelegate.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
