---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/More/EOSQLExpression.html
archived_at: '2026-07-15T08:11:33.111382Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.5 Documentation](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md) 

# EOSQLExpression

## Building Expressions

The following four methods create EOSQLExpression objects
for the four basic database operations-select, insert, update,
and delete:

- [selectStatementForAttributes](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlmmvrxiu3umf2gk3lfnz2em33sif2hi4tjmj2xizlt)
- [insertStatementForRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxws3ttmvzhiu3umf2gk3lfnz2em33skjxxo)
- [updateStatementForRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk4demf2gku3umf2gk3lfnz2em33skjxxo)
- [deleteStatementWithQualifier](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls)

Unless you're implementing an EOSQLExpression subclass,
these and the static method [expressionForString](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwk6dqojsxg43jn5xem33skn2he2lom4) are
the only EOSQLExpression methods you should ever need. If, on the
other hand, you are creating a subclass, you need to understand
the mechanics of how EOSQLExpression builds SQL statements. Each
of the creation methods above creates an EOSQLExpression, initializes
the expression with a specified entity, and sends the new expression
object one of the following __prepare...__ methods:

- [prepareSelectExpressionWithAttributes](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom)
- [prepareInsertExpressionWithRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y)
- [prepareUpdateExpressionWithRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y)
- [prepareDeleteExpressionForQualifier](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q)

The __prepare...__ methods, in turn,
invoke a corresponding __assemble...__ method,
first generating values for the __assemble...__ method's
arguments. The __assemble...__ methods:

- [assembleSelectStatementWithAttributes](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvgzlmmvrxiu3umf2gk3lfnz2fo2lunbaxi5dsnfrhk5dfom)
- [assembleInsertStatementWithRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsus3ttmvzhiu3umf2gk3lfnz2fo2lunbjg65y)
- [assembleUpdateStatementWithRow](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvk4demf2gku3umf2gk3lfnz2fo2lunbjg65y)
- [assembleDeleteStatementWithQualifier](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsuizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls)

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
for attributes and values with the methods [sqlStringForAttributeNamed](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle) and [sqlStringForValue](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu).
If necessary, it also formats the SQL strings according to an [EOAttribute](EOAttribute.md#apple-incuqq2ijfeue)'s "read" or "write"
format with the static method [formatSQLString](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq).

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

- [bindVariableDictionaryForAttribute](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylspfdg64sbor2he2lcov2gk)
- [mustUseBindVariableForAttribute](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3novzxivltmvbgs3tekzqxe2lbmjwgkrtpojaxi5dsnfrhk5df)
- [shouldUseBindVariableForAttribute](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tnbxxk3dekvzwkqtjnzsfmylsnfqwe3dfizxxeqluorzgsytvorsq)

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

The entry point into the schema generation code is the method [schemaCreationScriptForEntities](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjwg4tjob2em33sivxhi2lunfsxg), which
returns a script of SQL statements suitable to create the schema
for the EOEntity objects in the entities argument. The options dictionary
specifies the aspects of the schema for which to create SQL statements.
EOSQLExpression's implementation invokes [schemaCreationStatementsForEntities](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq) and then
uses [appendExpression](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwc4dqmvxgirlyobzgk43tnfxw4) to generate the
script.

## The Options Dictionary

The options dictionary specifies the aspects of the schema
for which to create SQL statements. It's contents are described
in the following table:

|  |  |  |
| --- | --- | --- |
| __Dictionary Key__ | __Acceptable Values (Strings)__ | __Default__ |
| `CreateTablesKey` | "YES" or "NO" | YES |
| `DropTablesKey` | "YES" or "NO" | YES |
| `CreatePrimaryKeySupportKey` | "YES" or "NO" | YES |
| `DropPrimaryKeySupportKey` | "YES" or "NO" | YES |
| `PrimaryKeyConstraintsKey` | "YES" or "NO" | YES |
| `ForeignKeyConstraintsKey` | "YES" or "NO" | NO |
| `CreateDatabaseKey` | "YES" or "NO" | NO |
| `DropDatabaseKey` | "YES" or "NO" | NO |

|  |
| --- |
| If you specify entries for `CreateDatabaseKey` or `DropDatabaseKey`, the SQL for those statements must be executed by an administrative user. |

## Schema Synchronization

EOSQLExpression provides API to generate SQL that can be used
to synchronize a database with a corresponding model. As with the
schema generation API, EOModeler makes use of the schema synchronization
API, and it's rare that you'd ever invoke it programmatically.
You won't need to know anything about the API yourself unless
you're implementing the API for a custom adaptor. This section describes
what the API is an how it works in the event that you need to implement
it.

The entry point into the schema synchronization code is the static method [statementsToUpdateObjectStoreForModel](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64snn5sgk3a).
The change dictionary argument identifies the changes to make to
the database schema to synchronize it with the specified model,
and the options dictionary identifies aspects of the schema for
which to create SQL statements. For more information on the changes
dictionary, see ["The Change Dictionary"](#apple-ijeugskiifdeu). For more information on the options
dictionary, see ["The Options Dictionary"](#apple-ijeugq2kjjfec). Using the change dictionary, [statementsToUpdateObjectStoreForModel](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64snn5sgk3a) identifies
the database tables that need to be updated, finds the entities
that correspond to those tables, and invokes the static method [statementsToUpdateObjectStoreForEntityGroup](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64sfnz2gs5dzi5zg65lq) for
each table. This method determines which, if any, of the synchronization
operations can be performed in place (without creating a new table,
moving the data, and dropping the old table). Depending on the features supported
by the adaptor, the method invokes an operation specific method
to make the changes in place, or it invokes [statementsToCopyTableNamed](EOSQLExpression.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32dn5yhsvdbmjwgkttbnvswi) to create
a new table with an updated definition, copy data from the old table
to the new table, and drop the old table. An adaptor advertises
what kind of synchronization operations it supports with `supportsOperation` methods
that return true if they support a feature, or false otherwise.

## The Change Dictionary

The change dictionary argument in the schema synchronization
API contains information about tables to insert, tables to delete,
tables to update, and information about how to update them.

The change dictionary can have any of the three keys `EOEditingContext.InsertedKey`, `EOEditingContext.DeletedKey`,
and `EOEditingContext.UpdatedKey` (defined
in EOControl). The values for the `InsertedKey` and `DeletedKey` are
arrays of table names to insert or delete, respectively. The value for
the `UpdatedKey` is a subdictionary.

The subdictionary for the `UpdatedKey` has
keys that are the names of the tables to update. The corresponding
values are additional dictionaries that describe how to modify the
tables. The keys of these dictionaries can be any of:

**`ExternalNameKey`**
: The name of the table before the change.

**`RelationshipsKey`**
: A dictionary of relationships which have been modified
since the last time the model and schema were sychronized. The keys
of the dictionary are relationship names, and the values are subdictionaries
with one entry. A subdictionary's key is `NameKey` (defined
as "name"), and it's value is the old name of the corresponding
relationship.
For example, suppose the Movie entity has a relationship named
"movieRoles" to the MovieRole entity, and suppose that you change
that relationship's name to "roles". The `RelationshipsKey`'s
dictionary for that change looks like this has an entry with the
key "Movie.roles". (The relationship name must be prefixed with
the name of the relationship's source entity because more than
one entity can refer to the updated table.) The corresponding value
is a subdictionary whose key is `NameKey` and
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

**`InsertedKey`**
: An array of column names to insert into the table

**`DeletedKey`**
: An array of column names to delete from the table

**`UpdatedKey`**
: A dictionary containing information on columns to update
and how to update them. The keys are the names of the columns to
update, and the values are subdictionaries on how to update the
corresponding columns. A subdictionary key identifies an updated
property of the column: name, type, and so on. The corresponding
value is the old property value. The keys are:

- `AllowsNullKey`
- `ColumnNameKey`
- `ExternalNameKey`
- `ExternalTypeKey`
- `NameKey`
- `PrecisionKey`
- `RelationshipsKey`
- `ScaleKey`
- `WidthKey`

[![Table of Contents](attachments/images/up.gif)](../../EOAccessTOC.md)
