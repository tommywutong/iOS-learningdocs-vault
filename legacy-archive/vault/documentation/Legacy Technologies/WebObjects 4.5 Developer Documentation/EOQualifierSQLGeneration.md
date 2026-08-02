---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Protocols/EOQualifierSQLGeneration.html
archived_at: '2026-07-15T08:11:36.072816Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)

# EOQualifierSQLGeneration

> __Adopted by:__
> EOAndQualifier, EOKeyComparisonQualifier, EOKeyValueQualifier, EONotQualifier, EOOrQualifier,
> EOSQLQualifier

> __Declared in:__  EOAccess/EOSQLQualifier.h

## Protocol Description

---

The EOQualifierSQLGeneration protocol declares two methods
that are adopted by qualifier classes to qualify fetches from a
database. One of the methods, [schemaBasedQualifierWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxgy3imvwwcqtbonswiulvmfwgsztjmvzfo2lunbjg633uivxhi2lupe5a),
is used to provide a qualifier suitable for evaluation by a database
from a qualifier suitable for in-memory evaluation. The other method, [sqlStringForSQLExpression:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu), is used
by concrete subclasses of EOSQLExpression to generate WHERE clauses
for SQL statements.

## Instance Methods

---

### sqlStringForSQLExpression:

`- (NSString *)sqlStringForSQLExpression:(EOSQLExpression
*)sqlExpression`

Returns a SQL statement suitable for inclusion
in a WHERE clause. Invoked from a concrete subclass of EOSQLExpression
while it's preparing a SELECT, UPDATE, or DELETE statement.

__See Also:__
[whereClauseString](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th) ( [EOSQLExpression](EOSQLExpression-3.md#apple-infeoq2fi5cei))

---

### schemaBasedQualifierWithRootEntity:

`- (EOQualifier *)schemaBasedQualifierWithRootEntity:(EOEntity
*)entity`

Returns a qualifier suitable for evaluation
by a database (as opposed to in-memory evaluation). Invoked by an
EODatabaseChannel object before it uses its EOAdaptorChannel to
perform a database operation.

Whereas in-memory qualifier evaluation uses pointers to resolve
relationships, a database qualifier must use foreign keys. For example,
consider the qualifier below that is used to fetch all employees
who work in a specified department:

> ```
> Department *dept;    // Assume this exists.
> EOQualifier *qualifier;
>
> qualifier = [EOQualifier qualifierWithQualifierFormat:@"department = %@", dept];
> ```

For an in-memory search, the Framework queries employee objects
for their department object and includes an employee in the result
list if its department object is equal to __dept__.
(See the EOQualifierEvaluation protocol description for more information
on in-memory searching.)

For a database search, the Framework needs to qualify the
fetch by specifying a foreign key value for __dept__.
The Framework sends __qualifier__ a __schemaBasedQualifierWithRootEntity:__ message
that creates and returns a new qualifier. Assume that the entity
for employee objects has an attribute named __departmentID__ and
that the primary key value for __dept__ is
459, the resulting qualifier specifies the search conditions as:

department.departmentID = 459

__See Also:__
[selectObjectsWithFetchSpecification:editingContext:](EODatabaseChannel-2.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2emf2gcytbonsug2dbnzxgk3bponswyzldorhwe2tfmn2hgv3joruemzlumnufg4dfmnuwm2ldmf2gs33ohjswi2lunfxgoq3pnz2gk6duhi) ( [EODatabaseChannel](EODatabaseChannel-2.md#apple-incucrcci5eei))

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
