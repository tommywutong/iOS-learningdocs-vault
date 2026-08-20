---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/OracleEOAdaptor.framework/Java/Classes/OracleSQLExpression.html
archived_at: '2026-07-15T08:11:46.254071Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
OracleEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)

# OracleSQLExpression

> __Inherits
> from:__  EOSQLExpression : NSObject

> __Package:__ com.apple.yellow.oracleeoadaptorjava

---

## Class Description

---

OracleSQLExpression defines how to build SQL statements for
OracleChannels.

## Static Methods

---

### serverTypeIdForName

`public static int serverTypeIdForName(String typeName)`

Returns the Oracle type code (such as OraVARCHAR2
or OraNumber) for _typeName_ (such
as "VARCHAR2" or "NUMBER").

---

### setUseNoWaitLocks

`public static void setUseNoWaitLocks(boolean flag)`

Sets according to _flag_ whether
the lock clause of the OracleSQLExpression is "FOR UPDATE" (block until
the row is available) or "FOR UPDATE NOWAIT" (return an error
immediately if an attempt to lock a row would block). By default
OracleSQLExpression uses the clause "FOR UPDATE"-that is,
by default it does not use NOWAIT locks. This behavior is also controllable
through the `EOOracleUseNoWaitLocks` user
default.

---

### setUseQuotedExternalNames

`public static void setUseQuotedExternalNames(boolean flag)`

Sets according to _flag_ whether
the OracleSQLExpression expects external (database) names to be enclosed
in quotation marks. This is useful if the database has table or
column names that are either reserved words or that are not all
uppercase. The default is NO.

This behavior can also be controlled
through the `EOOracleUseQuotedExternalNames` user
default.

---

### useNoWaitLocks

`public static boolean useNoWaitLocks()`

Returns true to indicate that the OracleSQLExpression
uses NOWAIT locks, false otherwise. The default is false.

---

### useQuotedExternalNames

`public static boolean useQuotedExternalNames()`

Returns YES to indicate that the OracleSQLExpression
uses quoted external (database) names, NO otherwise.

---

## Instance Methods

---

### lockClause

`public String lockClause()`

Overrides the EOSQLExpression method [lockClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzktkfgek6dqojsxg43jn5xc63dpmnvug3dbovzwk) to return
the SQL string used in a SELECT statement to lock selected rows.
Queries the user default EOOracleUseNoWaitLocks. If this default
is not set or if it is set to false, this method returns the string "FOR
UPDATE". If the default is set to true, this method returns "FOR
UPDATE NOWAIT".

---

[![Table of Contents](attachments/images/up.gif)](../OracleEOAdaptorTOC.md)
