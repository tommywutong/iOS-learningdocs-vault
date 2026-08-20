---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/More/EOSQLExpression.html
archived_at: '2026-07-15T08:11:35.865312Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md) 

# EOSQLExpression

## Building Expressions

The following four methods create EOSQLExpression objects
for the four basic database operations-select, insert, update,
and delete:

- [+ selectStatementForAttributes:lock:fetchSpecification:entity:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk3dfmn2fg5dborsw2zloordg64sbor2he2lcov2gk4z2nrxwg2z2mzsxiy3iknygky3jmzuwgylunfxw4otfnz2gs5dzhi)
- [+ insertStatementForRow:entity:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5uw443foj2fg5dborsw2zloordg64ssn53tuzlooruxi6j2)
- [+ updateStatementForRow:qualifier:entity:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xazdborsvg5dborsw2zloordg64ssn53tu4lvmfwgsztjmvzduzlooruxi6j2)
- [+ deleteStatementWithQualifier:entity:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2mvxhi2lupe5a)

Unless you're implementing an EOSQLExpression subclass,
these and the class method [expressionForString:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi) are
the only EOSQLExpression methods you should ever need. If, on the
other hand, you are creating a subclass, you need to understand
the mechanics of how EOSQLExpression builds SQL statements. Each
of the creation methods above creates an EOSQLExpression, initializes
the expression with a specified entity, and sends the new expression
object one of the following __prepare...__ methods:

- [- prepareSelectExpressionWithAttributes:lock:fetchSpecification:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2)
- [- prepareInsertExpressionWithRow:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq)
- [- prepareUpdateExpressionWithRow:qualifier:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq)
- [- prepareDeleteExpressionForQualifier:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq)

The __prepare...__ methods, in turn,
invoke a corresponding __assemble...__ method,
first generating values for the __assemble...__ method's
arguments. The __assemble...__ methods:

- [- assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder:selectString:columnList:tableList:whereClause:joinClause:orderByClause:lockClause:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvjwk3dfmn2fg5dborsw2zloorlws5diif2hi4tjmj2xizlthjwg6y3lhjyxkylmnftgszlshjtgk5ddnbhxezdfoi5hgzlmmvrxiu3uojuw4zz2mnxwy5lnnzggs43uhj2gcytmmvggs43uhj3wqzlsmvbwyylvonstu2tpnfxeg3dbovzwkotpojsgk4scpfbwyylvonstu3dpmnvug3dbovzwkoq)
- [- assembleInsertStatementWithRow:tableList:columnList:valueList:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvew443foj2fg5dborsw2zloorlws5dikjxxootumfrgyzkmnfzxiotdn5whk3lojruxg5b2ozqwy5lfjruxg5b2)
- [- assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvkxazdborsvg5dborsw2zloorlws5dikjxxootrovqwy2lgnfsxeotumfrgyzkmnfzxiotvobsgc5dfjruxg5b2o5ugk4tfinwgc5ltmu5a)
- [- assembleDeleteStatementWithQualifier:tableList:whereClause:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvcgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2orqwe3dfjruxg5b2o5ugk4tfinwgc5ltmu5a)

combine their arguments into SQL statements that the database
server can understand.

These three sets of methods establish a framework in which
SQL statements are generated. The bulk of the remaining methods
generate pieces of an SQL statement.

An individual SQL statement is constructed by combining the
SQL strings for any model or value objects specified in the "build"
method in the appropriate form. An SQL string for a modeling or
value object is a string representation of the object that the database
understands; for example, the SQL string for an `EOEntity` is
ultimately its table name. An EOSQLExpression gets the SQL strings
for attributes and values with the methods [sqlStringForAttributeNamed:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2) and [sqlStringForValue:attributeNamed:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi).
If necessary, it also formats the SQL strings according to an [EOAttribute](EOAttribute-3.md#apple-incuqq2ijfeue)'s "read" or "write"
format with the class method [formatSQLString:format:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq).

Each of the "build" methods above invokes a number of
instance methods. These methods are documented individually below.

## Using Table Aliases

By default, EOSQLExpression uses table aliases in SELECT statements.
For example, the following SELECT statement uses table aliases:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAME
> FROM EMPLOYEE t0, DEPARTMENT t1
> WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The EMPLOYEE table is aliased t0, and the DEPARTMENT table
is aliased t1. Table aliases are necessary in some SELECT statements-when
a table contains a self-referential relationship, for example. Assume
the EMPLOYEE table contains a manager column. Managers are also
employees, so to retrieve all the employees whose manager is Bob
Smith, the SELECT statement looks like this:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME
> FROM EMPLOYEE t0, EMPLOYEE t1
> WHERE t1.FIRST_NAME = "BOB" AND t1.LAST_NAME = "SMITH" AND
>     t0.MANAGER_ID = t1.EMPLOYEE_ID
> ```

When the Framework maps operations on enterprise objects to
operations on database rows, it reduces insert, update, and delete
operations to one or more single-table operations. As a result, EOSQLExpression
assumes that INSERT, UPDATE, and DELETE statements are always single-table operations,
and does not use table aliases in the statements of these types.

In addition, if EOSQLExpression detects that all the attributes
in a SELECT statement's attribute list are flattened attributes
and they're all flattened from the same table, the expression
doesn't use table aliases. For example, suppose that an EOSQLExpression
object is created to select a customer's credit card. In the application,
a customer object has a credit card object as one of its properties,
and all operations on credit cards are described in terms of a customer.
As a result, the expression object is initialized with the entity
for the Customer object. Rather than create a statement like the
following:

> ```
> SELECT t1.TYPE, t1.NUMBER, t1.EXPIRATION, t1.CREDIT_LIMIT, t1.CUSTOMER_ID
> FROM CUSTOMER t0, CREDIT_CARD t1
> WHERE t1.CUSTOMER_ID = t0.CUSTOMER_ID AND t1.CUSTOMER_ID = 459
> ```

EOSQLExpression detects that all the attributes correspond
to columns in the CREDIT_CARD table and creates the following statement:

> ```
> SELECT TYPE, NUMBER, EXPIRATION, CREDIT_LIMIT, CUSTOMER_ID
> FROM CREDIT_CARD
> WHERE CUSTOMER_ID = 459
> ```

## Bind Variables

Some RDBMS client libraries use bind variables. A bind variable
is a placeholder used in an SQL statement that is replaced with
an actual value after the database server determines an execution
plan. If you are writing an adaptor for a database server that uses
bind variables, you must override the following EOSQLExpression
methods:

- [- bindVariableDictionaryForAttribute:value:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq)
- [- mustUseBindVariableForAttribute:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)
- [- shouldUseBindVariableForAttribute:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a)

If your adaptor doesn't need to use bind variables, the
default implementations of the bind variable methods are sufficient.

## Schema Generation

EOSQLExpression provides API to generate SQL that can be used
to create a database. EOModeler uses these methods to generate scripts
that you can execute from within EOModeler to create a database
or that you can copy and paste into an interactive SQL shell for
your database. It's rare that you'd ever invoke this API programmatically.
You won't need to know anything about it unless you're implementing
it for a custom adaptor. If you are writing an adaptor, you must
ensure that EOSQLExpression's implementation of the schema generation
API is sufficient to support EOModeler's schema generation.

The entry point into the schema generation code is the method [schemaCreationScriptForEntities:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33oknrxe2lqordg64sfnz2gs5djmvztu33qoruw63tthi),
which returns a script of SQL statements suitable to create the
schema for the EOEntity objects in the entities argument. The options
dictionary specifies the aspects of the schema for which to create SQL
statements. EOSQLExpression's implementation invokes [schemaCreationStatementsForEntities:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2) and
then uses [appendExpression:toScript:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5qxa4dfnzsek6dqojsxg43jn5xdu5dpknrxe2lqoq5a) to generate
the script.

## The Options Dictionary

The options dictionary specifies the aspects of the schema
for which to create SQL statements. It's contents are described
in the following table:

|  |  |  |
| --- | --- | --- |
| __Dictionary Key__ | __Acceptable Values (NSStrings)__ | __Default__ |
| `EOCreateTablesKey` | "YES" or "NO" | YES |
| `EODropTablesKey` | "YES" or "NO" | YES |
| `EOCreatePrimaryKeySupportKey` | "YES" or "NO" | YES |
| `EODropPrimaryKeySupportKey` | "YES" or "NO" | YES |
| `EOPrimaryKeyConstraintsKey` | "YES" or "NO" | YES |
| `EOForeignKeyConstraintsKey` | "YES" or "NO" | NO |
| `EOCreateDatabaseKey` | "YES" or "NO" | NO |
| `EODropDatabaseKey` | "YES" or "NO" | NO |

|  |
| --- |
| If you specify entries for `EOCreateDatabaseKey` or `EODropDatabaseKey`, the SQL for those statements must be executed by an administrative user. |

## Schema Synchronization

EOSQLExpression provides API to generate SQL that can be used
to synchronize a database with a corresponding model. As with the
schema generation API, EOModeler makes use of the schema synchronization
API, and it's rare that you'd ever invoke it programmatically.
You won't need to know anything about the API yourself unless
you're implementing the API for a custom adaptor. This section describes
what the API is an how it works in the event that you need to implement
it.

The entry point into the schema synchronization code is the class method [statementsToUpdateObjectStoreForModel:withChangeDictionary:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxetlpmrswyotxnf2gqq3imfxgozkenfrxi2lpnzqxe6j2n5yhi2lpnzztu).
The change dictionary argument identifies the changes to make to
the database schema to synchronize it with the specified model,
and the options dictionary identifies aspects of the schema for
which to create SQL statements. For more information on the changes
dictionary, see ["The Change Dictionary"](#apple-ijeugskiifdeu). For more information on the options
dictionary, see ["The Options Dictionary"](#apple-ijeugq2kjjfec). Using the change dictionary, [statementsToUpdateObjectStoreForModel:withChangeDictionary:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxetlpmrswyotxnf2gqq3imfxgozkenfrxi2lpnzqxe6j2n5yhi2lpnzztu) identifies
the database tables that need to be updated, finds the entities
that correspond to those tables, and invokes the class method [statementsToUpdateObjectStoreForEntityGroup:withChangeDictionary:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxerlooruxi6khojxxk4b2o5uxi2cdnbqw4z3firuwg5djn5xgc4tzhjxxa5djn5xhgoq) for
each table. This method determines which, if any, of the synchronization
operations can be performed in place (without creating a new table,
moving the data, and dropping the old table). Depending on the features supported
by the adaptor, the method invokes an operation specific method
to make the changes in place, or it invokes [statementsToCopyTableNamed:intoTableForEntityGroup:withChangeDictionary:options:](EOSQLExpression-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6q3pob4viylcnrsu4ylnmvsdu2loorxviylcnrsum33sivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi) to
create a new table with an updated definition, copy data from the
old table to the new table, and drop the old table. An adaptor advertises
what kind of synchronization operations it supports with `supportsOperation` methods
that return YES if they support a feature, or NO otherwise.

## The Change Dictionary

The change dictionary argument in the schema synchronization
API contains information about tables to insert, tables to delete,
tables to update, and information about how to update them.

The change dictionary can have any of the three keys `EOInsertedKey`, `EODeletedKey`,
and `EOUpdatedKey` (defined in EOControl).
The values for the `EOInsertedKey` and `EODeletedKey` are
arrays of table names to insert or delete, respectively. The value
for the `EOUpdatedKey` is a subdictionary.

The subdictionary for the `EOUpdatedKey` has
keys that are the names of the tables to update. The corresponding
values are additional dictionaries that describe how to modify the
tables. The keys of these dictionaries can be any of:

**`EOExternalNameKey`**
: The name of the table before the change.

**`EORelationshipsKey`**
: A dictionary of relationships which have been modified
since the last time the model and schema were sychronized. The keys
of the dictionary are relationship names, and the values are subdictionaries
with one entry. A subdictionary's key is `EONameKey` (defined
as "name"), and it's value is the old name of the corresponding
relationship.
For example, suppose the Movie entity has a relationship named
"movieRoles" to the MovieRole entity, and suppose that you change
that relationship's name to "roles". The `EORelationshipsKey`'s
dictionary for that change looks like this has an entry with the
key "Movie.roles". (The relationship name must be prefixed with
the name of the relationship's source entity because more than
one entity can refer to the updated table.) The corresponding value
is a subdictionary whose key is `EONameKey` and
whose value is the string "movieRoles"-the old name of the
changed relationship.
The old name of the relationship is needed because relationship
names are used to define foreign key constraints. In order to drop
the old constraints, the schema synchronization methods need to
have the old relationship names. In the movieRoles example, the
schema synchronization methods must drop the foreign key constraint
based on the old relationship name:
> ```
> alter table MOVIE drop constraint MOVIE_movieRoles_FK cascade
> ```

After any old constraints are dropped, new ones are created
based on the new relationship names.

**`EOInsertedKey`**
: An array of column names to insert into the table

**`EODeletedKey`**
: An array of column names to delete from the table

**`EOUpdatedKey`**
: A dictionary containing information on columns to update
and how to update them. The keys are the names of the columns to
update, and the values are subdictionaries on how to update the
corresponding columns. A subdictionary key identifies an updated
property of the column: name, type, and so on. The corresponding
value is the old property value. The keys are:

- `EOAllowsNullKey`
- `EOColumnNameKey`
- `EOExternalNameKey`
- `EOExternalTypeKey`
- `EONameKey`
- `EOPrecisionKey`
- `EORelationshipsKey`
- `EOScaleKey`
- `EOWidthKey`

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
