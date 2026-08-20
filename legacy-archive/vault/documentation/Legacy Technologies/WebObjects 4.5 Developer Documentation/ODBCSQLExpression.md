---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/ODBCEOAdaptor.framework/ObjC_classic/Classes/ODBCSQLExpression.html
archived_at: '2026-07-15T08:11:46.151230Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


[an error occurred while processing this directive]

__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
ODBCEOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)

# ODBCSQLExpression

> __Inherits
> from:__  EOSQLExpression : NSObject

> __Declared in:__  ODBCEOAdaptor/ODBCSQLExpression.h

---

## Class Description

---

ODBCSQLExpression defines how to build SQL statements for
ODBCChannels.

## Bind Variables

The ODBCAdaptor uses bind variables. A bind variable is a
placeholder used in an SQL statement that is replaced with an actual
value after the database server determines an execution plan. You
use the following methods to operate on bind variables:

- [bindVariableDictionaryForAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq)
- [mustUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)
- [shouldUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpj5ceeq2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a)

For more information on using bind variables, see the EOSQLExpression
class specification.

## Class Methods

---

### bindVariableDictionaryForAttribute:value:

`- (NSMutableDictionary *)bindVariableDictionaryForAttribute:(EOAttribute
*)attribute
value:value`

Overrides the EOSQLExpression implementation
to return the receiver's bind variable dictionaries. For more
information on bind variables, see the discussion in the class description.

---

### lockClause

`- (NSString *)lockClause`

Overrides the EOSQLExpression implementation
to return the SQL string used in a SELECT statement to lock selected
rows. If you're using the Microsoft SQL Server, this method returns
@"HOLDLOCK". Otherwise, it returns @"FOR UPDATE"_._

---

### mustUseBindVariableForAttribute:

`- (BOOL)mustUseBindVariableForAttribute:(EOAttribute
*)attribute`

Overrides the EOSQLExpression implementation
to return YES since in the ODBC adaptor, the receiver must always
use bind variables for _attribute_.
A returned value of YES indicates that the underlying RDBMS requires
that bind variables be used for attributes with _attribute_'s
external type.

---

### shouldUseBindVariableForAttribute:

`- (BOOL)shouldUseBindVariableForAttribute:(EOAttribute
*)attribute`

Overrides the EOSQLExpression implementation
to return YES since in the ODBC adaptor, the receiver must always
be able to provide a bind variable dictionary for _attribute_.
A returned value of YES indicates that the receiver should use bind
variables for attributes with _attribute_'s
external type.

---

[![Table of Contents](attachments/images/up.gif)](../ODBCEOAdaptorTOC.md)
