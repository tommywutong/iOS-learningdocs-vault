---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/More/EOSQLExpression_more.html
archived_at: '2026-07-18T01:28:13.735262Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](EOSQLExpression.md)
[!](EOSQLQualifier.md)

---

# EOSQLExpression

---

## Building Expressions

The following four methods create EOSQLExpression objects for the four basic database operations-select, insert, update, and delete:

- [selectStatementForAttributes](EOSQLExpression.md#apple-geytcny)
- [insertStatementForRow](EOSQLExpression.md#apple-geytcmy)
- [updateStatementForRow](EOSQLExpression.md#apple-geytgmy)
- [deleteStatementWithQualifier](EOSQLExpression.md#apple-geydsni)
- Unless you're implementing an EOSQLExpression subclass, these and the static method [`expressionForString`](../EOSQLExpression.md#apple-geydsoi) are the only EOSQLExpression methods you should ever need. If, on the other hand, you are creating a subclass, you need to understand the mechanics of how EOSQLExpression builds SQL statements. Each of the creation methods above creates an EOSQLExpression, initializes the expression with a specified entity, and sends the new expression object one of the following `prepare...` methods:[prepareSelectExpressionWithAttributes](EOSQLExpression.md#apple-gy4dgmi)
- [prepareInsertExpressionWithRow](EOSQLExpression.md#apple-gy3tqoa)
- [prepareUpdateExpressionWithRow](EOSQLExpression.md#apple-gy4dknq)
- [prepareDeleteExpressionForQualifier](EOSQLExpression.md#apple-gy3tkmi)

The `prepare...` methods, in turn, invoke a corresponding `assemble...` method, first generating values for the `assemble...` method's arguments. The `assemble...` methods:

- [assembleSelectStatementWithAttributes](EOSQLExpression.md#apple-gy2tgny)
- [assembleInsertStatementWithRow](EOSQLExpression.md#apple-gy2teoa)
- [assembleUpdateStatementWithRow](EOSQLExpression.md#apple-gy2tkma)
- [assembleDeleteStatementWithQualifier](EOSQLExpression.md#apple-gy2tanq)

combine their arguments into SQL statements that the database server can understand.

These three sets of methods establish a framework in which SQL statements are generated. The bulk of the remaining methods generate pieces of an SQL statement.

An individual SQL statement is constructed by combining the SQL strings for any model or value objects specified in the "build" method in the appropriate form. An SQL string for a modeling or value object is a string representation of the object that the database understands; for example, the SQL string for an EOEntity is ultimately its table name. An EOSQLExpression gets the SQL strings for attributes and values with the methods [`sqlStringForAttributeNamed`](../EOSQLExpression.md#apple-gy4tmmq) and [`sqlStringForValue`](../EOSQLExpression.md#apple-g4ytsmy). If necessary, it also formats the SQL strings according to an EOAttribute's "read" or "write" format with the static method [`formatSQLString`](../EOSQLExpression.md#apple-geytamy).

Each of the "build" methods above invokes a number of instance methods. These methods are documented individually below.

---

## Using Table Aliases

By default, EOSQLExpression uses table aliases in SELECT statements. For example, the following SELECT statement uses table aliases:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAMEFROM EMPLOYEE t0, DEPARTMENT t1WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The EMPLOYEE table is aliased t0, and the DEPARTMENT table is aliased t1. Table aliases are necessary in some SELECT statements-when a table contains a self-referential relationship, for example. Assume the EMPLOYEE table contains a manager column. Managers are also employees, so to retrieve all the employees whose manager is Bob Smith, the SELECT statement looks like this:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAMEFROM EMPLOYEE t0, EMPLOYEE t1WHERE t1.FIRST_NAME = "BOB" AND t1.LAST_NAME = "SMITH" AND    t0.MANAGER_ID = t1.EMPLOYEE_ID
> ```

When the Framework maps operations on enterprise objects to operations on database rows, it reduces insert, update, and delete operations to one or more single-table operations. As a result, EOSQLExpression assumes that INSERT, UPDATE, and DELETE statements are always single-table operations, and does not use table aliases in the statements of these types.

In addition, if EOSQLExpression detects that all the attributes in a SELECT statement's attribute list are flattened attributes and they're all flattened from the same table, the expression doesn't use table aliases. For example, suppose that an EOSQLExpression object is created to select a customer's credit card. In the application, a customer object has a credit card object as one of its properties, and all operations on credit cards are described in terms of a customer. As a result, the expression object is initialized with the entity for the Customer object. Rather than create a statement like the following:

> ```
> SELECT t1.TYPE, t1.NUMBER, t1.EXPIRATION, t1.CREDIT_LIMIT, t1.CUSTOMER_IDFROM CUSTOMER t0, CREDIT_CARD t1WHERE t1.CUSTOMER_ID = t0.CUSTOMER_ID AND t1.CUSTOMER_ID = 459
> ```

EOSQLExpression detects that all the attributes correspond to columns in the CREDIT_CARD table and creates the following statement:

> ```
> SELECT TYPE, NUMBER, EXPIRATION, CREDIT_LIMIT, CUSTOMER_IDFROM CREDIT_CARDWHERE CUSTOMER_ID = 459
> ```

---

## Bind Variables

Some RDBMS client libraries use bind variables. A bind variable is a placeholder used in an SQL statement that is replaced with an actual value after the database server determines an execution plan. If you are writing an adaptor for a database server that uses bind variables, you must override the following EOSQLExpression methods:

- [bindVariableDictionaryForAttribute](EOSQLExpression.md#apple-gy2tmoi)
- [mustUseBindVariableForAttribute](EOSQLExpression.md#apple-gy3tgmi)
- [shouldUseBindVariableForAttribute](EOSQLExpression.md#apple-gy4tama)

If your adaptor doesn't need to use bind variables, the default implementations of the bind variable methods are sufficient.

---

## Generating SQL for EOModeler's Schema Generation

EOSQLExpression provides a set of methods that generate SQL that can be used to create a database. EOModeler uses these methods to generate scripts that you can execute from within EOModeler to create a database or that you can copy and paste into an interactive SQL shell for your database. If you are writing an adaptor, you must ensure that the following EOSQLExpression method implementations are sufficient to support EOModeler's schema generation:

- [schemaCreationScriptForEntities](EOSQLExpression.md#apple-ge4tsmrz)
- [schemaCreationStatementsForEntities](EOSQLExpression.md#apple-ge4tsnbv)
- [appendExpression](EOSQLExpression.md#apple-ge4tkoby)
- [createTableStatementsForEntityGroup](EOSQLExpression.md#apple-ge4tkojz)
- [createTableStatementsForEntityGroups](EOSQLExpression.md#apple-ge4tmnbx)
- [dropTableStatementsForEntityGroup](EOSQLExpression.md#apple-ge4tomrv)
- [dropTableStatementsForEntityGroups](EOSQLExpression.md#apple-ge4tonbw)
- [primaryKeyConstraintStatementsForEntityGroup](EOSQLExpression.md#apple-ge4tqnjz)
- [primaryKeyConstraintStatementsForEntityGroups](EOSQLExpression.md#apple-ge4tqobw)
- [primaryKeySupportStatementsForEntityGroup](EOSQLExpression.md#apple-ge4tqojw)
- [primaryKeySupportStatementsForEntityGroups](EOSQLExpression.md#apple-ge4tsmjz)
- [dropPrimaryKeySupportStatementsForEntityGroup](EOSQLExpression.md#apple-ge4tmojq)
- [dropPrimaryKeySupportStatementsForEntityGroups](EOSQLExpression.md#apple-ge4tomjr)
- [prepareConstraintStatementForRelationship](EOSQLExpression.md#apple-giydiobr)
- [foreignKeyConstraintStatementsForRelationship](EOSQLExpression.md#apple-ge4tonrz)
- [addCreateClauseForAttribute](EOSQLExpression.md#apple-giydcnzz)
- [columnTypeStringForAttribute](EOSQLExpression.md#apple-giydgnrz)
- [allowsNullClauseForConstraint](EOSQLExpression.md#apple-giydenjs)

  ****

---

[!](EOSQLExpression.md)
[!](EOSQLQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
