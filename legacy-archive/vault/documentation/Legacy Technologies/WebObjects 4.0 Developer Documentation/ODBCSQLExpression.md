---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/ODBCSQLExpression.html
archived_at: '2026-07-18T01:28:48.561113Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](ODBCContext.md)

---

# ODBCSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Inherits From:__
com.apple.yellow.odbceoadaptor

---

## Class Description

ODBCSQLExpression defines how to build SQL statements for ODBCChannels.

---

## Bind Variables

- The ODBCAdaptor uses bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan.

---

## Instance Methods

---

### bindVariableDictionaryForAttribute

public com.apple.yellow.foundation.NSMutableDictionary `bindVariableDictionaryForAttribute`(com.apple.yellow.eoaccess.EOAttribute _attribute_, java.lang.Object _value_)

Overrides the EOSQLExpression method `bindVariableDictionaryForAttribute` to return the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

---

[!](ODBCContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
