---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/InformixEOAdaptor.framework/Java/Classes/InformixSQLExpression.html
archived_at: '2026-07-15T08:11:45.805730Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
InformixEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)

# InformixSQLExpression

> __Inherits
> from:__  EOSQLExpression : NSObject

> __Package:__ com.apple.yellow.informixeoadaptor

---

## Class Description

---

InformixSQLExpression defines how to build SQL statements
for InformixChannels.

## Bind Variables

The InformixAdaptor uses bind variables. A bind variable is
a placeholder used in an SQL statement that is replaced with an
actual value after the database server determines an execution plan.
You use the following methods to operate on bind variables:

- __bindVariableDictionaryForAttribute__
- __mustUseBindVariableForAttribute__
- __shouldUseBindVariableForAttribute__

For more information on using bind variables, see the EOSQLExpression
class specification.

## Static Methods

---

### serverTypeIdForName

`public static int serverTypeIdForName(String typeName)`

Returns the Informix type code (such as InfDecimal,
InfDate, or InfCHAR) for _typeName_ (such
as "DECIMAL", "DATE", or "CHAR").

---

## Instance Methods

---

### lockClause

`public String lockClause()`

Overrides the EOSQLExpression method __lockClause__ to
return the SQL string used in a SELECT statement to lock selected
rows, which is "FOR UPDATE OF".

---

[![Table of Contents](attachments/images/up.gif)](../InformixEOAdaptorTOC.md)
