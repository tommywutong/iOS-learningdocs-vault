---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/Concepts/EOSQLExpression.html
archived_at: '2026-07-15T08:13:40.763041Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md) 

# EOSQLExpression.Concepts

## Building Expressions

The following four methods create EOSQLExpression objects for the four basic database operations-select, insert, update, and delete:

- selectStatementForAttributes
- insertStatementForRow
- updateStatementForRow
- deleteStatementWithQualifier

Unless you're implementing an EOSQLExpression subclass, these four methods are the only EOSQLExpression methods you should ever need. If, on the other hand, you are creating a subclass, you need to understand the mechanics of how EOSQLExpression builds SQL statements. Each of the creation methods above creates an EOSQLExpression, initializes the expression with a specified entity, and sends the new expression object one of the following __prepare...__ methods:

- prepareSelectExpressionWithAttributes
- prepareInsertExpressionWithRow
- prepareUpdateExpressionWithRow
- prepareDeleteExpressionForQualifier

The __prepare...__ methods, in turn, invoke a corresponding __assemble...__ method, first generating values for the __assemble...__ method's arguments. The __assemble...__ methods:

- assembleSelectStatementWithAttributes
- assembleInsertStatementWithRow
- assembleUpdateStatementWithRow
- assembleDeleteStatementWithQualifier

combine their arguments into SQL statements that the database server can understand.

These three sets of methods establish a framework in which SQL statements are generated. The bulk of the remaining methods generate pieces of an SQL statement.

An individual SQL statement is constructed by combining the SQL strings for any model or value objects specified in the "build" method in the appropriate form. An SQL string for a modeling or value object is a string representation of the object that the database understands; for example, the SQL string for an `EOEntity` is ultimately its table name. An EOSQLExpression gets the SQL strings for attributes and values with the methods sqlStringForAttributeNamed and sqlStringForValue. If necessary, it also formats the SQL strings according to an EOAttribute's "read" or "write" format with the static method formatSQLString.

Each of the "build" methods above invokes a number of instance methods. These methods are documented individually below.

## Using Table Aliases

By default, EOSQLExpression uses table aliases in SELECT statements. For example, the following SELECT statement uses table aliases:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAME
> FROM EMPLOYEE t0, DEPARTMENT t1
> WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The EMPLOYEE table is aliased t0, and the DEPARTMENT table is aliased t1. Table aliases are necessary in some SELECT statements-when a table contains a self-referential relationship, for example. Assume the EMPLOYEE table contains a manager column. Managers are also employees, so to retrieve all the employees whose manager is Bob Smith, the SELECT statement looks like this:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME
> FROM EMPLOYEE t0, EMPLOYEE t1
> WHERE t1.FIRST_NAME = "BOB" AND t1.LAST_NAME = "SMITH" AND
>     t0.MANAGER_ID = t1.EMPLOYEE_ID
> ```

When the Framework maps operations on enterprise objects to operations on database rows, it reduces insert, update, and delete operations to one or more single-table operations. As a result, EOSQLExpression assumes that INSERT, UPDATE, and DELETE statements are always single-table operations, and does not use table aliases in the statements of these types.

In addition, if EOSQLExpression detects that all the attributes in a SELECT statement's attribute list are flattened attributes and they're all flattened from the same table, the expression doesn't use table aliases. For example, suppose that an EOSQLExpression object is created to select a customer's credit card. In the application, a customer object has a credit card object as one of its properties, and all operations on credit cards are described in terms of a customer. As a result, the expression object is initialized with the entity for the Customer object. Rather than create a statement like the following:

> ```
> SELECT t1.TYPE, t1.NUMBER, t1.EXPIRATION, t1.CREDIT_LIMIT, t1.CUSTOMER_ID
> FROM CUSTOMER t0, CREDIT_CARD t1
> WHERE t1.CUSTOMER_ID = t0.CUSTOMER_ID AND t1.CUSTOMER_ID = 459
> ```

EOSQLExpression detects that all the attributes correspond to columns in the CREDIT_CARD table and creates the following statement:

> ```
> SELECT TYPE, NUMBER, EXPIRATION, CREDIT_LIMIT, CUSTOMER_ID
> FROM CREDIT_CARD
> WHERE CUSTOMER_ID = 459
> ```

## Bind Variables

Some RDBMS client libraries use bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. If you are writing an adaptor for a database server that uses bind variables, you must override the following EOSQLExpression methods:

- bindVariableDictionaryForAttribute
- mustUseBindVariableForAttribute
- shouldUseBindVariableForAttribute

If your adaptor doesn't need to use bind variables, the default implementations of the bind variable methods are sufficient.

## Schema Generation

EOSQLExpression provides API to generate SQL that can be used to create a database. EOModeler uses these methods to generate scripts that you can execute from within EOModeler to create a database or that you can copy and paste into an interactive SQL shell for your database. It's rare that you'd ever invoke this API programmatically. You won't need to know anything about it unless you're implementing it for a custom adaptor. If you are writing an adaptor, you must ensure that EOSQLExpression's implementation of the schema generation API is sufficient to support EOModeler's schema generation.

The entry point into the schema generation code is the method schemaCreationScriptForEntities:options:, which returns a script of SQL statements suitable to create the schema for the EOEntity objects in the entities argument. The options dictionary specifies the aspects of the schema for which to create SQL statements. EOSQLExpression's implementation invokes schemaCreationStatementsForEntities:options: and then uses appendExpression:toScript: to generate the script.

### The Options Dictionary

Description forthcoming.

## Schema Synchronization

EOSQLExpression provides API to generate SQL that can be used to synchronize a database with a corresponding model. As with the schema generation API, EOModeler makes use of the schema synchronization API, and it's rare that you'd ever invoke it programmatically. You won't need to know anything about the API yourself unless you're implementing the API for a custom adaptor. This section describes what the API is an how it works in the event that you need to implement it.

The entry point into the schema synchronization code is the static method statementsToUpdateObjectStoreForModel:withChangeDictionary:options:. The change dictionary argument identifies the changes to make to the database schema to synchronize it with the specified model, and the options dictionary identifies aspects of the schema for which to create SQL statements. For more information on the changes dictionary, see ["The Change Dictionary" (page 306)](#apple-ijeugskiifdeu). For more information on the options dictionary, see ["The Options Dictionary" (page 306)](#apple-ijeugq2kjjfec). Using the change dictionary, statementsToUpdateObjectStoreForModel:withChangeDictionary:options: identifies the database tables that need to be updated, finds the entities that correspond to those tables, and invokes the static method statementsToUpdateObjectStoreForEntityGroup:withChangeDictionary:options: for each table. This method determines which, if any, of the synchronization operations can be performed in place (without creating a new table, moving the data, and dropping the old table). Depending on the features supported by the adaptor, the method invokes an operation specific method to make the changes in place to create a new table with an updated definition, copy data from the old table to the new table, and drop the old table. An adaptor advertises what kind of synchronization operations it supports with `supportsOperation` methods that return true if they support a feature, or false otherwise.

### The Change Dictionary

The change dictionary argument in the schema synchronization API contains information about tables to insert, tables to delete, tables to update, and information about how to update them.

The change dictionary can have any of the three keys `EOEditingContext.InsertedKey`, `EOEditingContext.DeletedKey`, and `EOEditingContext.UpdatedKey` (defined in EOControl). The values for the `InsertedKey` and `DeletedKey` are arrays of table names to insert or delete, respectively. The value for the `UpdatedKey` is a subdictionary.

The subdictionary for the `UpdatedKey` has keys that are the names of the tables to update. The corresponding values are additional dictionaries that describe how to modify the tables. The keys of these dictionaries can be any of:

**`EOExternalNameKey`**
: The name of the table before the change.

**`EORelationshipsKey`**
: A dictionary of relationships which have been modified since the last time the model and schema were sychronized. The keys of the dictionary are relationship names, and the values are subdictionaries with one entry. A subdictionary's key is `EONameKey` (defined as "name"), and it's value is the old name of the corresponding relationship. For example, suppose the Movie entity has a relationship named "movieRoles" to the MovieRole entity, and suppose that you change that relationship's name to "roles". The `EORelationshipsKey`'s dictionary for that change looks like this has an entry with the key "Movie.roles". (The relationship name must be prefixed with the name of the relationship's source entity because more than one entity can refer to the updated table.) The corresponding value is a subdictionary whose key is `EONameKey` and whose value is the string "movieRoles"-the old name of the changed relationship. The old name of the relationship is needed because relationship names are used to define foreign key constraints. In order to drop the old constraints, the schema synchronization methods need to have the old relationship names. In the movieRoles example, the schema synchronization methods must drop the foreign key constraint based on the old relationship name:
> ```
> alter table MOVIE drop constraint MOVIE_movieRoles_FK cascade
> ```

After any old constraints are dropped, new ones are created based on the new relationship names.

**`InsertedKey`**
: An array of column names to insert into the table

**`DeletedKey`**
: An array of column names to delete from the table

**`UpdatedKey`**
: A dictionary containing information on columns to update and how to update them. The keys are the names of the columns to update, and the values are subdictionaries on how to update the corresponding columns. A subdictionary key identifies an updated property of the column: name, type, and so on.

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Classes/Art/up.gif)](../../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
