---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/OracleSQLExpression.html
archived_at: '2026-07-18T01:28:49.659484Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](OracleContext-2.md)

---

# OracleSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Declared in:__
OracleEOAdaptor/OracleSQLExpression.h

---

## Class Description

OracleSQLExpression defines how to build SQL statements for OracleChannels.

---

## Method Types

**Generating SQL for attributes and values**

**[+ formatValue:forAttribute:](#apple-ge4dk)**

**Getting the server type ID**

**[+ serverTypeIdForName:](#apple-ge4dq)**

**Working with no wait locks**

**[+ setUseNoWaitLocks:](#apple-ge4tc)

**[+ useNoWaitLocks](#apple-giyda)****

**Getting the lock clause**

**[- lockClause](#apple-giytg)**

**Managing bind variables**

**[- mustUseBindVariableForAttribute:](#apple-giytm)

**[- shouldUseBindVariableForAttribute:](#apple-gizda)

**[- bindVariableDictionaryForAttribute:value:](#apple-giyds)******

---

## Class Methods

---

### formatValue:forAttribute:

+ (NSString \*)__formatValue:__ (id)_value_ __forAttribute:__ (EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`formatValue:forAttribute:`](#apple-ge4dk) to return a formatted string representation of _value_ for _attribute_ that is suitable for use in a SQL statement.

---

### serverTypeIdForName:

+ (int)__serverTypeIdForName:__ (NSString \*)_typeName_

Returns the Oracle type code (such as OraVARCHAR2 or OraNumber) for _typeName_ (such as "VARCHAR2" or "NUMBER").

---

### setUseNoWaitLocks:

+ (void)__setUseNoWaitLocks:__ (BOOL)_flag_

Sets according to _flag_ whether the lock clause of the OracleSQLExpression is @"FOR UPDATE" (block until the row is available) or @"FOR UPDATE NOWAIT" (return an error immediately if an attempt to lock a row would block). By default OracleSQLExpression uses the clause @"FOR UPDATE"-that is, by default it does _not_ use NOWAIT locks. This behavior is also controllable through the EOOracleUseNoWaitLocks user default.

__See also:__
[+ `useNoWaitLocks`](#apple-giyda)

---

### useNoWaitLocks

+ (BOOL)__useNoWaitLocks__

Returns YES to indicate that the OracleSQLExpression uses NOWAIT locks, NO otherwise. The default is NO.

__See also:__
[+ `setUseNoWaitLocks:`](#apple-ge4tc)

---

## Instance Methods

---

### bindVariableDictionaryForAttribute:value:

- (NSMutableDictionary \*)__bindVariableDictionaryForAttribute:__ (EOAttribute \*)attribute
__value:__ value

Overrides the EOSQLExpression method [`bindVariableDictionaryForAttribute:value:`](#apple-giyds) to return the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
[- `mustUseBindVariableForAttribute:`](#apple-giytm), [- `shouldUseBindVariableForAttribute:`](#apple-gizda)

---

### lockClause

- (NSString \*)__lockClause__

Overrides the EOSQLExpression method [`lockClause`](#apple-giytg) to return the SQL string used in a SELECT statement to lock selected rows. Queries the user default EOOracleUseNoWaitLocks. If this default is not set or if it is set to NO, this method returns the string @"FOR UPDATE". If the default is set to YES, this method returns @"FOR UPDATE NOWAIT"_._

---

### mustUseBindVariableForAttribute:

- (BOOL)__mustUseBindVariableForAttribute:__ (EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`mustUseBindVariableForAttribute:`](#apple-giytm) to return YES if the receiver must use bind variables for _attribute_, NO otherwise. A returned value of YES indicates that the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
[- `bindVariableDictionaryForAttribute:value:`](#apple-giyds), [- `shouldUseBindVariableForAttribute:`](#apple-gizda)

---

### shouldUseBindVariableForAttribute:

- (BOOL)__shouldUseBindVariableForAttribute:__ (EOAttribute \*)_attribute_

Overrides the EOSQLExpression method [`shouldUseBindVariableForAttribute:`](#apple-gizda) to return YES if the receiver can provide a bind variable dictionary for _attribute_, NO otherwise. A returned value of YES indicates that the receiver should use bind variables for attributes with _attribute_'s external type.

__See also:__
[- `bindVariableDictionaryForAttribute:value:`](#apple-giyds), [- `mustUseBindVariableForAttribute:`](#apple-giytm)

---

[!](OracleContext-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
