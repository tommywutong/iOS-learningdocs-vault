---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/InformixSQLExpression.html
archived_at: '2026-07-18T01:28:48.122871Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[InformixEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/InformixEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](InformixContext-2.md)

---

# InformixSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Declared in:__
InformixEOAdaptor/InformixSQLExpression.h

---

## Class Description

InformixSQLExpression defines how to build SQL statements for InformixChannels.

---

## Bind Variables

The InformixAdaptor uses bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. You use the following methods to operate on bind variables:

- [bindVariableDictionaryForAttribute:value:](#apple-gm2tsmq)
- [mustUseBindVariableForAttribute:](#apple-gm3dema)
- [shouldUseBindVariableForAttribute:](#apple-gm3dgmq)

---

## Class Methods

---

### formatValue:forAttribute:

+ (NSString \*)`formatValue:`(id)_value_ `forAttribute:`(EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`formatValue:forAttribute:`](#apple-gm2dqoa) to return a formatted string representation of _value_ for _attribute_ that is suitable for use in a SQL statement.

---

### serverTypeIdForName

+ (int)`serverTypeIdForName:`(NSString \*)_typeName_

Returns the Informix type code (such as InfDecimal, InfDate, or InfCHAR) for _typeName_ (such as "DECIMAL", "DATE", or "CHAR").

---

## Instance Methods

---

### bindVariableDictionaryForAttribute:value:

- (NSMutableDictionary \*)`bindVariableDictionaryForAttribute:`(EOAttribute \*)_attribute_
`value:`_value_

Overrides the EOSQLExpression method [`bindVariableDictionaryForAttribute:value:`](#apple-gm2tsmq) to return the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
[- `mustUseBindVariableForAttribute:`](#apple-gm3dema), [- `shouldUseBindVariableForAttribute:`](#apple-gm3dgmq)

---

### mustUseBindVariableForAttribute:

- (BOOL)`mustUseBindVariableForAttribute:`(EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`mustUseBindVariableForAttribute:`](#apple-gm3dema) to return YES if the receiver must use bind variables for _attribute_, NO otherwise. A returned value of YES indicates that the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
[- `bindVariableDictionaryForAttribute:value:`](#apple-gm2tsmq), [- `shouldUseBindVariableForAttribute:`](#apple-gm3dgmq)

---

### shouldUseBindVariableForAttribute:

- (BOOL)`shouldUseBindVariableForAttribute:`(EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`shouldUseBindVariableForAttribute:`](#apple-gm3dgmq) to return YES if the receiver can provide a bind variable dictionary for _attribute_, NO otherwise. A returned value of YES indicates that the receiver should use bind variables for attributes with _attribute_'s external type.

__See also:__
[- `bindVariableDictionaryForAttribute:value:`](#apple-gm2tsmq), [- `mustUseBindVariableForAttribute:`](#apple-gm3dema)

---

[!](InformixContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
