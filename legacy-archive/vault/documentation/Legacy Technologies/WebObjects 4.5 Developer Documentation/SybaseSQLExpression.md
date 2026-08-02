---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/SybaseEOAdaptor.framework/Java/Classes/SybaseSQLExpression.html
archived_at: '2026-07-15T08:11:46.450747Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
SybaseEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)

# SybaseSQLExpression

> __Inherits
> from:__  EOSQLExpression : NSObject

> __Package:__ com.apple.yellow.sybaseeoadaptor

---

## Class Description

---

SybaseSQLExpression defines how to build SQL statements for
SybaseChannels.

## Static Methods

---

### serverTypeIdForName

`public static int serverTypeIdForName(String typeName)`

Returns the Sybase type code (such as 47, 56,
or 55) for _typeName_ (such as "char",
"int", or "decimal").

---

## Instance Methods

---

### lockClause

`public String lockClause()`

Overrides the EOSQLExpression method [lockClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6u3zmjqxgzktkfgek6dqojsxg43jn5xc63dpmnvug3dbovzwk) to return
the SQL string used in a SELECT statement to lock selected rows,
which is "HOLDLOCK".

---

[![Table of Contents](attachments/images/up.gif)](../SybaseEOAdaptorTOC.md)
