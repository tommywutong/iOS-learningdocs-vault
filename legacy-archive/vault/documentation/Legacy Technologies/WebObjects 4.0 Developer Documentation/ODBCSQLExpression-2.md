---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/ODBCSQLExpression.html
archived_at: '2026-07-18T01:28:48.926508Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[ODBCEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/ODBCEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](ODBCContext-2.md)

# ODBCSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Declared in:__
ODBCEOAdaptor/ODBCSQLExpression.h

---

## Class Description

ODBCSQLExpression defines how to build SQL statements for ODBCChannels.

---

## Bind Variables

The ODBCAdaptor uses bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. You use the following methods to operate on bind variables:

- - bindVariableDictionaryForAttribute:value:
- - mustUseBindVariableForAttribute:
- - shouldUseBindVariableForAttribute:

---

## Instance Methods

---

### bindVariableDictionaryForAttribute:value:

- (NSMutableDictionary \*)`bindVariableDictionaryForAttribute:`(EOAttribute \*)_attribute_`value:`_value_

Overrides the EOSQLExpression method `bindVariableDictionaryForAttribute:value:` to return the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
- `mustUseBindVariableForAttribute:`, - `shouldUseBindVariableForAttribute:`

---

### lockClause

- (NSString \*)`lockClause`

Overrides the EOSQLExpression method `lockClause` to return the SQL string used in a SELECT statement to lock selected rows. If you're using the Microsoft SQL Server, this method returns @"HOLDLOCK". Otherwise, it returns @"FOR UPDATE"_._

---

### mustUseBindVariableForAttribute:

- (BOOL)`mustUseBindVariableForAttribute:`(EOAttribute \*)_attribute_

Overrides the EOSQLExpression method `mustUseBindVariableForAttribute:` to return YES since in the ODBC adaptor, the receiver must always use bind variables for _attribute_. A returned value of YES indicates that the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
- `shouldUseBindVariableForAttribute:`, - `bindVariableDictionaryForAttribute:value:`

---

### prepareSelectExpressionWithAttributes:lock:fetchSpecification:

- (void)`prepareSelectExpressionWithAttributes:`(NSArray \*)_attributes_ `lock:`(BOOL)_lock_ `fetchSpecification:`(EOFetchSpecification \*)_fetchSpec_

Overrides the EOSQLExpression method `prepareSelectExpressionWithAttributes:lock:fetchSpecification:`to generate a SELECT statement. For a more complete description of what this entails, see the `prepareSelectExpressionWithAttributes:lock:fetchSpecification:` method description in the EOSQLExpression class specification.

---

### shouldUseBindVariableForAttribute:

- (BOOL)`shouldUseBindVariableForAttribute:`(EOAttribute \*)_attribute_

Overrides the EOSQLExpression method `shouldUseBindVariableForAttribute:` to return YES since in the ODBC adaptor, the receiver must always be able to provide a bind variable dictionary for _attribute_. A returned value of YES indicates that the receiver should use bind variables for attributes with _attribute_'s external type.

__See also:__
- `mustUseBindVariableForAttribute:`, - `bindVariableDictionaryForAttribute:value:`

---

[!](ODBCContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
