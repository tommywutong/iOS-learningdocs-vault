---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/OracleSQLExpression.html
archived_at: '2026-07-18T01:28:49.280514Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[SybaseEOAdaptor Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/OracleEOAdaptor.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](OracleContext.md)

---

# OracleSQLExpression

__Inherits From:__
EOSQLExpression : NSObject

__Inherits From:__
com.apple.yellow.oracleeoadaptorjava

---

## Class Description

OracleSQLExpression defines how to build SQL statements for OracleChannels.

---

## Method Types

**Generating SQL for attributes and values**

**[formatValueForAttribute](#apple-ge4dk)**

**Getting the server type ID**

**[serverTypeIdForName](#apple-ge4dq)**

**Working with no wait locks**

**[setUseNoWaitLocks](#apple-ge4tc)

**[useNoWaitLocks](#apple-giyda)****

**Getting the lock clause**

**[lockClause](#apple-giytg)**

**Managing bind variables**

**[mustUseBindVariableForAttribute](#apple-giytm)

**[shouldUseBindVariableForAttribute](#apple-gizda)

**[bindVariableDictionaryForAttribute](#apple-giyds)******

---

## Class Methods

---

### formatValueForAttribute

public static java.lang.String `formatValueForAttribute`(java.lang.Object _value_, com.apple.yellow.eoaccess.EOAttribute _attribute_)

Overrides the EOSQLExpression method [`formatValueForAttribute`](#apple-ge4dk) to return a formatted string representation of _value_ for _attribute_ that is suitable for use in a SQL statement.

---

### serverTypeIdForName

public static int `serverTypeIdForName`(java.lang.String _typeName_)

Returns the Oracle type code (such as OraVARCHAR2 or OraNumber) for _typeName_ (such as "VARCHAR2" or "NUMBER").

---

### setUseNoWaitLocks

public static void `setUseNoWaitLocks`(boolean _flag_)

Sets according to _flag_ whether the lock clause of the OracleSQLExpression is "FOR UPDATE" (block until the row is available) or "FOR UPDATE NOWAIT" (return an error immediately if an attempt to lock a row would block). By default OracleSQLExpression uses the clause "FOR UPDATE"-that is, by default it does _not_ use NOWAIT locks. This behavior is also controllable through the EOOracleUseNoWaitLocks user default.

__See also:__
[`useNoWaitLocks`](#apple-giyda)

---

### useNoWaitLocks

public static boolean `useNoWaitLocks`()

Returns `true` to indicate that the OracleSQLExpression uses NOWAIT locks, `false` otherwise. The default is `false`.

__See also:__
[`setUseNoWaitLocks`](#apple-ge4tc)

---

## Instance Methods

---

### bindVariableDictionaryForAttribute

public com.apple.yellow.foundation.NSMutableDictionary `bindVariableDictionaryForAttribute`(com.apple.yellow.eoaccess.EOAttribute _attribute_, java.lang.Object _value_)

Overrides the EOSQLExpression method [`bindVariableDictionaryForAttribute`](#apple-giyds) to return the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
[`mustUseBindVariableForAttribute`](#apple-giytm), [`shouldUseBindVariableForAttribute`](#apple-gizda)

---

### lockClause

public java.lang.String `lockClause`()

Overrides the EOSQLExpression method [`lockClause`](#apple-giytg) to return the SQL string used in a SELECT statement to lock selected rows. Queries the user default EOOracleUseNoWaitLocks. If this default is not set or if it is set to `false`, this method returns the string "FOR UPDATE". If the default is set to `true`, this method returns "FOR UPDATE NOWAIT"_._

---

### mustUseBindVariableForAttribute

public boolean `mustUseBindVariableForAttribute`(com.apple.yellow.eoaccess.EOAttribute _attribute_)

Overrides the EOSQLExpression method [`mustUseBindVariableForAttribute`](#apple-giytm) to return `true` if the receiver must use bind variables for _attribute_, `false` otherwise. A returned value of `true` indicates that the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
[`bindVariableDictionaryForAttribute`](#apple-giyds), [`shouldUseBindVariableForAttribute`](#apple-gizda)

---

### shouldUseBindVariableForAttribute

public boolean `shouldUseBindVariableForAttribute`(com.apple.yellow.eoaccess.EOAttribute _attribute_)

Overrides the EOSQLExpression method [`shouldUseBindVariableForAttribute`](#apple-gizda) to return `true` if the receiver can provide a bind variable dictionary for _attribute_, `false` otherwise. A returned value of `true` indicates that the receiver should use bind variables for attributes with _attribute_'s external type.

__See also:__
[`bindVariableDictionaryForAttribute`](#apple-giyds), [`mustUseBindVariableForAttribute`](#apple-giytm)

---

[!](OracleContext.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
