---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOSQLExpression.html
archived_at: '2026-07-18T01:28:10.513070Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](Creating%20Relationships-2.md)
[!](EOSQLExpression-2.md)

---

# EOSQLExpression

__Inherits From:__
NSObject

__Inherits From:__
com.apple.yellow.eoaccess

---

## Class Description

EOSQLExpression is an abstract superclass that defines how to build SQL statements for adaptor channels. You don't typically use instances of EOSQLExpression; rather, you use EOSQLExpression subclasses written to work with a particular RDBMS and corresponding adaptor. A concrete subclass of EOSQLExpression overrides many of its methods in terms of the query language syntax for its specific RDBMS. EOSQLExpression objects are used internally by the Framework, and unless you're creating a concrete adaptor, you won't ordinarily need to interact with EOSQLExpression objects yourself. You most commonly create and use an EOSQLExpression object when you want to send an SQL statement directly to the server. In this case, you simply create an expression with the EOSQLExpression static method [`expressionForString`](#apple-geydsoi), and send the expression object to an adaptor channel using [EOAdaptorChannel](EOAdaptorChannel.md#apple-geydaoi)'s `evaluateExpression:` method.

For more information, see ["More about EOSQLExpression"](EOSQLExpression-2.md).

---

## Method Types

**Constructors**

**[EOSQLExpression](#apple-ge4tknzv)**

**Creating an EOSQLExpression object**

**[selectStatementForAttributes](#apple-geytcny)

**[insertStatementForRow](#apple-geytcmy)

**[updateStatementForRow](#apple-geytgmy)

**[deleteStatementWithQualifier](#apple-geydsni)

**[expressionForString](#apple-geydsoi)**********

**Building SQL Expressions**

**[prepareSelectExpressionWithAttributes](#apple-gy4dgmi)

**[prepareInsertExpressionWithRow](#apple-gy3tqoa)

**[prepareUpdateExpressionWithRow](#apple-gy4dknq)

**[prepareDeleteExpressionForQualifier](#apple-gy3tkmi)

**[setStatement](#apple-gy4dooa)

**[statement](#apple-gq2dcna)************

**Generating SQL for attributes and values**

**[formatSQLString](#apple-geytamy)

**[formatValue:forAttribute](#apple-geytcma)

**[formatStringValue](#apple-geytany)

**[sqlStringForValue](#apple-g4ytsmy)

**[sqlStringForAttributeNamed](#apple-gy4tmmq)

**[sqlStringForAttribute](#apple-gy4teni)

**[sqlStringForAttributePath](#apple-gy4toni)**************

**Generating SQL for names of database objects**

**[sqlStringForSchemaObjectName](#apple-g4ytgmi)

**[setUseQuotedExternalNames](#apple-ge2dema)

**[useQuotedExternalNames](#apple-ge2dena)

**[externalNameQuoteCharacter](#apple-gq3tgma)********

**Generating an attribute list**

**[addSelectListAttribute](#apple-gyztema)

**[addInsertListAttribute](#apple-geytiny)

**[addUpdateListAttribute](#apple-gy2damy)

**[appendItemToListString](#apple-gy2dmna)

**[listString](#apple-gq3dmmq)**********

**Generating a value list**

**[addInsertListAttribute](#apple-geytiny)

**[addUpdateListAttribute](#apple-gy2damy)

**[valueList](#apple-g4zdioa)******

**Generating a table list**

**[tableListWithRootEntity](#apple-geydsojq)

**[aliasesByRelationshipPath](#apple-gyztqna)****

**Generating the join clause**

**[joinExpression](#apple-gq3tcmy)

**[addJoinClauseWithLeftName:rightName:joinSemantic:](#apple-geytkmq)

**[assembleJoinClause](#apple-geytsma)

**[joinClauseString](#apple-gy3dena)********

**Generating a search pattern**

**[sqlPatternFromShellPattern](#apple-ge2dgny)

**[sqlPatternFromShellPattern:withEscapeCharacter](#apple-geyteni)****

**Generating a relational operator**

**[sqlStringForSelector](#apple-g4ytknq)**

**Accessing the where clause**

**[whereClauseString](#apple-gqztmny)**

**Generating an order by clause**

**[addOrderByAttributeOrdering](#apple-gyzdqnq)

**[orderByString](#apple-gq3dina)****

**Accessing the lock clause**

**[lockClause](#apple-gy3dqma)**

**Assembling a statement**

**[assembleSelectStatementWithAttributes](#apple-gy2tgny)

**[assembleInsertStatementWithRow](#apple-gy2teoa)

**[assembleUpdateStatementWithRow](#apple-gy2tkma)

**[assembleDeleteStatementWithQualifier](#apple-gy2tanq)********

**Generating SQL for qualifiers**

**[sqlStringForQualifier](#apple-giydmnry)

**[sqlStringForConjoinedQualifiers](#apple-gy4tsoi)

**[sqlStringForDisjoinedQualifiers](#apple-gezteny)

**[sqlStringForKeyComparisonQualifier](#apple-geydqobq)

**[sqlStringForKeyValueQualifier](#apple-g4ydmmq)

**[sqlStringForNegatedQualifier](#apple-g4ydqni)************

**Managing bind variables**

**[setUseBindVariables](#apple-geydanrt)

**[useBindVariables](#apple-geytgoa)

**[addBindVariableDictionary](#apple-gyytqnq)

**[bindVariableDictionaries](#apple-gq3tsna)

**[bindVariableDictionaryForAttribute](#apple-gy2tmoi)

**[mustUseBindVariableForAttribute](#apple-gy3tgmi)

**[shouldUseBindVariableForAttribute](#apple-gy4tama)**************

**Using table aliases**

**[setUseAliases](#apple-gy4dsmi)

**[useAliases](#apple-gqztqni)****

**Accessing the entity**

**[entity](#apple-gq3tomq)**

**Creating a schema generation script**

**[schemaCreationScriptForEntities](#apple-ge4tsmrz)

**[schemaCreationStatementsForEntities](#apple-ge4tsnbv)

**[appendExpression](#apple-ge4tkoby)******

**Generating table definition part of schema generation script for a list of entity groups**

**[createTableStatementsForEntityGroups](#apple-ge4tmnbx)

**[dropTableStatementsForEntityGroups](#apple-ge4tonbw)

**[primaryKeyConstraintStatementsForEntityGroups](#apple-ge4tqobw)

**[primaryKeySupportStatementsForEntityGroups](#apple-ge4tsmjz)

**[dropPrimaryKeySupportStatementsForEntityGroups](#apple-ge4tomjr)**********

**Generating table definition part of schema generation script for an entity group**

**[createTableStatementsForEntityGroup](#apple-ge4tkojz)

**[dropTableStatementsForEntityGroup](#apple-ge4tomrv)

**[primaryKeyConstraintStatementsForEntityGroup](#apple-ge4tqnjz)

**[primaryKeySupportStatementsForEntityGroup](#apple-ge4tqojw)

**[dropPrimaryKeySupportStatementsForEntityGroup](#apple-ge4tmojq)**********

**Generating attribute definition part of schema generation script**

**[addCreateClauseForAttribute](#apple-giydcnzz)

**[columnTypeStringForAttribute](#apple-giydgnrz)

**[allowsNullClauseForConstraint](#apple-giydenjs)******

**Generating relationship constraint part of schema generation script**

**[foreignKeyConstraintStatementsForRelationship](#apple-ge4tonrz)

**[prepareConstraintStatementForRelationship](#apple-giydiobr)****

**Other**

**[createDatabaseStatementsForConnectionDictionary](#apple-gi2temzz)

**[dropDatabaseStatementsForConnectionDictionary](#apple-gi2tgmjz)

**[sqlStringForNumber](#apple-gi2tgnzu)

**[sqlStringForQualifier](#apple-giydmnry)

**[sqlStringForString](#apple-gi2tgnbt)**********

---

## Constructors

---

### EOSQLExpression

public `EOSQLExpression`()

public `EOSQLExpression`(EOEntity _anEntity_)

Creates a new EOSQLExpression. If _anEntity_ is provided, the new EOSQLExpression is rooted to _anEntity_.

__See also:__
[`entity`](#apple-gq3tomq)

#

---

### appendExpression

public static void `appendExpression`(EOSQLExpression _anSQLExpression_, java.lang.String _script_)

Append's _anSQLExpression_'s [`statement`](#apple-gq2dcna) to _script_ along with any necessary delimiter. EOSQLExpression's implementation append the SQL statement for _anSQLExpression_ to _script_ followed by a semicolon and a newline. A subclass of EOSQLExpression only needs to override this method if the delimiter for its database server is different. For example, the Oracle and Informix use the default implementation, whereas the Sybase adaptor appends the word "go" instead of a semicolon.

__See also:__
[`createTableStatementsForEntityGroups`](#apple-ge4tmnbx)

---

### createDatabaseStatementsForConnectionDictionary

public static NSArray `createDatabaseStatementsForConnectionDictionary`(
NSDictionary _connectionDictionary,_NSDictionary _adminDictionary,_)

Generates the SQL statements that will create a database (or user, for Oracle) that can be accessed by the provided connection dictionary and administrative connection dictionary.

__See also:__
[`dropDatabaseStatementsForConnectionDictionary`](#apple-gi2tgmjz)

---

### createTableStatementsForEntityGroup

public static NSArray `createTableStatementsForEntityGroup`(NSArray _entityGroup_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create a table for _entityGroup_, an array of Entity objects that have the same [`externalName`](EOEntity.md#apple-g44de). Returns an empty array if entityGroup is `null` or empty.

EOSQLExpression's implementation does the following:

- Creates an EOSQLExpression object.
- Sets the expression's [`entity`](#apple-gq3tomq) to the first entity in _entityGroup_.
- Adds a create clause for each Attribute in _entityGroup_'s Entities.
- Sets the expression's [`statement`](#apple-gq2dcna) to CREATE TABLE _TABLE_NAME_ (_LIST_STRING_), where _TABLE_NAME_ is the `externalName` of the Entity objects in _entityGroup_ and _LIST_STRING_ is the expression's `listString`.
- Adds the expression to an array.
- Returns the array.

The following is an example of a CREATE TABLE statement produced by the default implementation:
> ```
> create table  EMPLOYEE (    EMP_ID      int  not null ,    DEPT_ID     int  null ,    LAST_NAME   varchar( 40 )  not null ,    PHONE       char( 12 )  null ,    HIRE_DATE   date  null ,    SALARY      number( 7 , 2 )  null)
> ```

If a subclass's database server's table creation semantics are different, the subclass should override this method or one or more of the following methods as appropriate:

- [addCreateClauseForAttribute](#apple-giydcnzz)
- [columnTypeStringForAttribute](#apple-giydgnrz)
- [allowsNullClauseForConstraint](#apple-giydenjs)

__See also:__
[`createTableStatementsForEntityGroups`](#apple-ge4tmnbx), [`dropTableStatementsForEntityGroup`](#apple-ge4tomrv)

---

### createTableStatementsForEntityGroups

public static NSArray `createTableStatementsForEntityGroups`(NSArray _entityGroups_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create the tables specified in _entityGroups_. An entity group is an array of Entity objects that have the same `externalName`, and _entityGroups_ is an array of entity groups. Returns an empty array if _entityGroups_ is `null` or empty. EOSQLExpression's implementation invokes [`createTableStatementsForEntityGroup`](#apple-ge4tkojz) for each entity group in _entityGroups_ and returns an array of all the resulting SQLExpressions.

__See also:__
[`schemaCreationStatementsForEntities`](#apple-ge4tsnbv)

---

### deleteStatementWithQualifier

public static EOSQLExpression `deleteStatementWithQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_, java.lang.Object _entity_)

Creates and returns an SQL DELETE expression to delete the rows described by _qualifier_. Creates an instance of EOSQLExpression, initializes it with _entity_ (an EOEntity object), and sends it a [`prepareDeleteExpressionForQualifier`](#apple-gy3tkmi) message. Throws an exception if _qualifier_ is `null`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.As a result, all keys in _qualifier_ should be simple key names; no key paths are allowed. To generate DELETE statements that do use table aliases, you must override `prepareDeleteExpressionForQualifier:` to send a [`setUseAliases`](#apple-gy4dsmi)(`true`) message prior to invoking `super`'s version.

---

### dropDatabaseStatementsForConnectionDictionary

public static NSArray `dropDatabaseStatementsForConnectionDictionary`(
NSDictionary _connectionDictionary,_NSDictionary _adminDictionary,_)

Generates the SQL statements to drop the database (or user, for Oracle).

__See also:__
[`createDatabaseStatementsForConnectionDictionary`](#apple-gi2temzz)

---

### dropPrimaryKeySupportStatementsForEntityGroup

public static NSArray `dropPrimaryKeySupportStatementsForEntityGroup`(NSArray _entityGroup_)

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for _entityGroup_, an array of Entity objects that have the same `externalName`. The drop statement generated by this method should be sufficient to remove the primary key support created by [`primaryKeySupportStatementsForEntityGroup`](#apple-ge4tqojw)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> drop sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the [`primaryKeyRootName`](EOEntity.md#apple-guytany) for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

__See also:__
[`dropPrimaryKeySupportStatementsForEntityGroups`](#apple-ge4tomjr)

---

### dropPrimaryKeySupportStatementsForEntityGroups

public static NSArray `dropPrimaryKeySupportStatementsForEntityGroups`(
NSArray _entityGroups_)

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same `externalName`, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [`dropPrimaryKeySupportStatementsForEntityGroup`](#apple-ge4tmojq) for each entity group in _entityGroups_ and returns an array of all the resulting SQLExpressions.

__See also:__
[`schemaCreationStatementsForEntities`](#apple-ge4tsnbv)

---

### dropTableStatementsForEntityGroup

public static NSArray `dropTableStatementsForEntityGroup`(NSArray _entityGroup_)

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the table identified by _entityGroup_, an array of Entity objects that have the same `externalName`. The drop statement generated by this method should be sufficient to remove the table created by [`createTableStatementsForEntityGroup`](#apple-ge4tkojz)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> DROP TABLE TABLE_NAME
> ```

Where _TABLE_NAME_ is the `externalName` of the first entity in _entityGroup_.

If a subclass's database server's drop semantics are different, the subclass should override this method.

__See also:__
[`dropTableStatementsForEntityGroups`](#apple-ge4tonbw)

---

### dropTableStatementsForEntityGroups

public static NSArray `dropTableStatementsForEntityGroups`(NSArray _entityGroups_)

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the tables for _entityGroups_. An entity group is an array of Entity objects that have the same `externalName`, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [`dropTableStatementsForEntityGroups`](#apple-ge4tonbw) for each entity group in _entityGroups_ and returns an array of all the resulting SQLExpressions.

__See also:__
[`schemaCreationStatementsForEntities`](#apple-ge4tsnbv)

---

### expressionForString

public static EOSQLExpression `expressionForString`(java.lang.String _string_)

Creates and returns an SQL expression for _string_. _string_ should be a valid expression in the target query language. This method does not perform substitutions or formatting of any kind.

__See also:__
[`setStatement`](#apple-gy4dooa)

---

### foreignKeyConstraintStatementsForRelationship

public static NSArray `foreignKeyConstraintStatementsForRelationship`(EORelationship _aRelationship_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create foreign key constraints for _aRelationship_. EOSQLExpression's implementation generates statements such as the following:

> ```
> ALTER TABLE EMPLOYEE ADD CONSTRAINT TO_DEPARTMENT FOREIGN KEY (DEPT_ID)        REFERENCES DEPARTMENT(DEPT_ID)
> ```

It returns an empty array if either of the following are true:

- _aRelationship_ spans models (if _aRelationship_'s [`destinationEntity`](EORelationship.md#apple-guytq) is in a different model than _aRelationship_'s source [`entity`](EORelationship.md#apple-guzde))
- _aRelationship_ is a to-many relationship, or if the inverse relationship of _aRelationship_ is not a to-many. In other words, foreign key constraint statements are only created for to-one relationships whose inverse is a to-many.

If neither of the above are true, this method creates a new EOSQLExpression, assigns its entity to _aRelationship_'s entity, invokes [`prepareConstraintStatementForRelationship`](#apple-giydiobr), and returns an array containing the expression.

If a subclass's database server's foreign key constraint semantics are different, the subclass should override this method or override the method `prepareConstraintStatementForRelationship`.

__See also:__
[`schemaCreationStatementsForEntities`](#apple-ge4tsnbv)

---

### formatSQLString

public static java.lang.String `formatSQLString`(java.lang.String _sqlString_, java.lang.String _format_)

Applies _format_ (an EOAttribute object's "read" or "write" format) to _sqlString_ (a value for the attribute). If _format_ is `null`, this method returns _sqlString_ unchanged.

__See also:__
__-- readFormat__  (EOAttribute), __- writeFormat__  (EOAttribute)

---

### formatStringValue

public static java.lang.String `formatStringValue`(java.lang.String _string_)

Formats _string_ for use as a string constant in a SQL statement. EOSQLExpression's implementation encloses the string in single quotes, escaping any single quotes already present in _string_. Throws an exception if _string_ is `null`.

---

### formatValue:forAttribute

public static java.lang.String `formatValueForAttribute`(java.lang.Object _value_, EOAttribute _attribute_)

Overridden by subclasses to return a string representation of _value_ suitable for use in an SQL statement. EOSQLExpression's implementation returns _value_ unchanged. A subclass should override this method to format _value_ depending on _attribute_'s [`externalType`](EOAttribute.md#apple-hazdq). For example, a subclass might format a date using a special database-specific syntax or standard form or truncate numbers to _attribute_'s precision and scale.

---

### insertStatementForRow

public static EOSQLExpression `insertStatementForRow`(NSDictionary _row_, EOEntity _entity_)

Creates and returns an SQL INSERT expression to insert _row_. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareInsertExpressionWithRow`](#apple-gy3tqoa). Throws an exception if _entity_ is `null`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.To generate INSERT statements that do use table aliases, you must override `prepareInsertExpressionWithRow:` to send a [`setUseAliases`](#apple-gy4dsmi)(`true`) message prior to invoking `super`'s version.

---

### primaryKeyConstraintStatementsForEntityGroup

public static NSArray `primaryKeyConstraintStatementsForEntityGroup`(NSArray _entityGroup_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for _entityGroup_, an array of Entity objects that have the same [`externalName`](EOEntity.md#apple-g44de). Returns an empty array if any of the primary key attributes in _entityGroup_ don't have a [`columnName`](EOAttribute.md#apple-ge4dcnbz).

EOSQLExpression's implementation creates a statement of the following form:

> ```
> ALTER TABLE TABLE_NAME ADD PRIMARY KEY (PRIMARY_KEY_COLUMN_NAMES)
> ```

Where _TABLE_NAME_ is the [`externalName`](EOEntity.md#apple-g44de) for the first entity in _entityGroup_ and _PRIMARY_KEY_COLUMN_NAMES_ is a comma-separated list of the [`columnName`](EOAttribute.md#apple-ge4dcnbz)s of the first entity's [`primaryKeyAttributes`](EOEntity.md#apple-hazto).

If the subclass's database server's primary key constraint semantics are different, the subclass should override this method.

__See also:__
[`primaryKeyConstraintStatementsForEntityGroups`](#apple-ge4tqobw)

---

### primaryKeyConstraintStatementsForEntityGroups

public static NSArray `primaryKeyConstraintStatementsForEntityGroups`(NSArray _entityGroups_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same [`externalName`](EOEntity.md#apple-g44de), and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [`primaryKeyConstraintStatementsForEntityGroup`](#apple-ge4tqnjz) for each entity group in _entityGroups_ and returns an array of all the resulting SQLExpressions.

---

### primaryKeySupportStatementsForEntityGroup

public static NSArray `primaryKeySupportStatementsForEntityGroup`(NSArray _entityGroup_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for _entityGroup_, an array of Entity objects that have the same [`externalName`](EOEntity.md#apple-g44de). EOSQLExpression's implementation creates a statement of the following form:

> ```
> create sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the [`primaryKeyRootName`](EOEntity.md#apple-guytany) for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

__See also:__
[`primaryKeySupportStatementsForEntityGroups`](#apple-ge4tsmjz), [`dropPrimaryKeySupportStatementsForEntityGroup`](#apple-ge4tmojq), [`primaryKeyForNewRowWithEntity`](EOAdaptorChannel.md#apple-geydqna)
(EOAdaptorChannel)

---

### primaryKeySupportStatementsForEntityGroups

public static NSArray `primaryKeySupportStatementsForEntityGroups`(NSArray _entityGroups_)

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same [`externalName`](EOEntity.md#apple-g44de), and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [`primaryKeySupportStatementsForEntityGroup`](#apple-ge4tqojw) for each entity group in _entityGroups_ and returns an array of all the resulting SQLExpressions.

---

### schemaCreationScriptForEntities

public static java.lang.String `schemaCreationScriptForEntities`(NSArray _entities_, NSDictionary _options_)

Returns a script of SQL statements suitable to create the schema for the Entity objects in _entities_. The _options_ dictionary specifies the aspects of the schema for which to create SQL statements as described in the method description for [`schemaCreationStatementsForEntities`](#apple-ge4tsnbv). EOSQLExpression's implementation invokes `schemaCreationStatementsForEntities:options:` with _entities_ and _options_ and then uses [`appendExpression`](#apple-ge4tkoby) to generate the script from the SQLExpressions generated by `schemaCreationStatementsForEntities:options:`.

---

### schemaCreationStatementsForEntities

public static NSArray `schemaCreationStatementsForEntities`(NSArray _entities_, NSDictionary _options_)

Returns an array of SQLExpressions suitable to create the schema for the Entity objects in _entities_. The _options_ dictionary specifies the aspects of the schema for which to create SQLExpressions:

| __Dictionary Key__ | __Acceptable Values (java.util.Strings)__ | __Default__ |
| createTables | "YES" or "NO" | YES |
| dropTables | "YES" or "NO" | YES |
| createPrimaryKeySupport | "YES" or "NO" | YES |
| dropPrimaryKeySupport | "YES" or "NO" | YES |
| primaryKeyConstraints | "YES" or "NO" | YES |
| foreignKeyConstraints | "YES" or "NO" | NO |
| createDatabase | "YES" or "NO" | NO |
| dropDatabase | "YES" or "NO" | NO |

```
```

If you specify "createDatabase" or "dropDatabase," the SQL for those statements must be executed by an administrative user.

EOSQLExpression's implementation uses the following methods:

- [createTableStatementsForEntityGroups](#apple-ge4tmnbx)
- [dropTableStatementsForEntityGroups](#apple-ge4tonbw)
- [primaryKeySupportStatementsForEntityGroups](#apple-ge4tsmjz)
- [dropPrimaryKeySupportStatementsForEntityGroups](#apple-ge4tomjr)
- [primaryKeyConstraintStatementsForEntityGroups](#apple-ge4tqobw)
- [foreignKeyConstraintStatementsForRelationship](#apple-ge4tonrz)

to generate SQLExpressions for the support identified in _options_.

__See also:__
[`schemaCreationScriptForEntities`](#apple-ge4tsmrz)

---

### selectStatementForAttributes

public static EOSQLExpression `selectStatementForAttributes`(NSArray _attributes_,
boolean _flag_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_,
EOEntity _entity_)

Creates and returns an SQL SELECT expression. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareSelectExpressionWithAttributes`](#apple-gy4dgmi). The expression created with this method uses table aliases. Throws an exception if _attributes_ is `null` or empty, _fetchSpecification_ is `null`, or _entity_ is `null`.

The expression created with this method uses table aliases.To generate SELECT statements that don't use them, you must override `prepareSelectExpressionWithAttributes:lock:fetchSpecification:` to send a [`setUseAliases`](#apple-gy4dsmi)(`false`) message prior to invoking `super`'s version.

---

### setUseBindVariables

public static void `setUseBindVariables`(boolean _flag_)

Sets according to _flag_ whether all instances of EOSQLExpression subclasses use bind variables. By default, instances don't use bind variables; if the value for the global user default named EOAdaptorUseBindVariables is `true`, though, instances do use them. For more information on bind variables, see the discussion in the class description.

__See also:__
[`useBindVariables`](#apple-geytgoa)

---

### setUseQuotedExternalNames

public static void `setUseQuotedExternalNames`(boolean _flag_)

Sets whether all instances of EOSQLExpression subclasses quote external names when they are referenced in SQL statements. By setting _flag_ to `true`, you can access database tables with names such as "%return", "1st year", and "TABLE" that you couldn't otherwise access. By default, instances don't quote external names; if the value for the global user default named EOAdaptorQuotesExternalNames is `true`, though, instances do use quotes.

__See also:__
[`useQuotedExternalNames`](#apple-ge2dena), [`sqlStringForSchemaObjectName`](#apple-g4ytgmi),
[`externalNameQuoteCharacter`](#apple-gq3tgma)

---

### sqlPatternFromShellPattern

public static java.lang.String `sqlPatternFromShellPattern`(java.lang.String _pattern_)

Translates a "like" qualifier to an SQL "like" expression. Invoked from [`sqlStringForKeyValueQualifier`](#apple-g4ydmmq) when the qualifier argument is an EOKeyValueQualifier object whose selector is QualifierOperatorLike. EOSQLExpression's implementation performs the following substitutions

| ____Character in pattern____ | __Substitution string__ |
| \* | % |
| ? | _ |
| % | [%] _(unless the percent character appears in square brackets)_ |
| _ | [_] _(unless the underscore character appears in square brackets)_ |

```
```

__See also:__
[`sqlPatternFromShellPattern:withEscapeCharacter`](#apple-geyteni)

---

### sqlPatternFromShellPattern:withEscapeCharacter

public static java.lang.String `sqlPatternFromShellPatternWithEscapeCharacter`(java.lang.String _pattern_, char _escapeCharacter_)

Like[`sqlPatternFromShellPattern`](#apple-ge2dgny) except the argument _escapeCharacter_ allows you to specify a character for escaping the wild card characters "%" and "_".

---

### updateStatementForRow

public static EOSQLExpression `updateStatementForRow`(NSDictionary _row_, com.apple.yellow.eocontrol.EOQualifier _qualifier_,
EOEntity _entity_)

Creates and returns an SQL UPDATE expression to update the row identified by _qualifier_ with the values in _row_. _row_ should only contain entries for values that have actually changed. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareUpdateExpressionWithRow`](#apple-gy4dknq). Throws an exception if _row_ is `null` or empty, _qualifier_ is `null`, or _entity_ is `null`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.As a result, all keys in _qualifier_ should be simple key names; no key paths are allowed. To generate UPDATE statements that do use table aliases, you must override `prepareUpdateExpressionWithRow:qualifier:` to send a [`setUseAliases`](#apple-gy4dsmi)(`true`) message prior to invoking `super`'s version.

__See also:__
[`setUseAliases`](#apple-gy4dsmi)

---

### useBindVariables

public static boolean `useBindVariables`()

Returns `true` if instances use bind variables, `false` otherwise. For more information on bind variables, see the discussion in the class description.

__See also:__
[`setUseBindVariables`](#apple-geydanrt)

---

### useQuotedExternalNames

public static boolean `useQuotedExternalNames`()

Returns `true` if instances use quoted external names, `false` otherwise.

__See also:__
[`setUseQuotedExternalNames`](#apple-ge2dema), [`sqlStringForSchemaObjectName`](#apple-g4ytgmi),
[`externalNameQuoteCharacter`](#apple-gq3tgma)

---

## Instance Methods

---

### addBindVariableDictionary

public void `addBindVariableDictionary`(NSMutableDictionary _binding_)

Adds _binding_ to the receiver's array of bind variable dictionaries. _binding_ is generally created using the method [`bindVariableDictionaryForAttribute`](#apple-gy2tmoi) and is added to the receiver's bind variable dictionaries in [`sqlStringForValue`](#apple-g4ytsmy) when the receiver uses a bind variable for the specified attribute. See the method description for `bindVariableDictionaryForAttribute:value:` for a description of the contents of a bind variable dictionary, and for more information on bind variables, see the discussion in the class description.

__See also:__
[`bindVariableDictionaries`](#apple-gq3tsna)

---

### addCreateClauseForAttribute

public void `addCreateClauseForAttribute`(EOAttribute _attribute_)

Adds the SQL string for creating _attribute_ to a comma-separated list of attribute creation clauses. The list is constructed for use in a CREATE TABLE statement produced by [`createTableStatementsForEntityGroup`](#apple-ge4tkojz). Use the method [`listString`](#apple-gq3dmmq) to access creation clauses.

EOSQLExpression's implementation creates clauses in the following form:

> ```
> COLUMN_NAME COLUMN_TYPE ALLOWS_NULL_CLAUSE
> ```

Where

- _COLUMN_TYPE_ is the string returned from [`columnTypeStringForAttribute`](#apple-giydgnrz) for _anAttribute._
- _ALLOWS_NULL_CLAUSE_ is the string returned from [`allowsNullClauseForConstraint`](#apple-giydenjs) with `true` if _anAttribute_ [`allowsNull`](EOAttribute.md#apple-gq4dmoi) or with `false` if _anAttribute_ doesn't.

---

### addInsertListAttribute

public void `addInsertListAttribute`(EOAttribute _attribute_, java.lang.String _value_)

Adds the SQL string for _attribute_ to a comma-separated list of attributes and _value_ to a comma-separated list of values. Both lists are constructed for use in an INSERT statement. Use the methods [`listString`](#apple-gq3dmmq) and [`valueList`](#apple-g4zdioa) to access the attributes and value lists.

Invokes [`appendItemToListString`](#apple-gy2dmna) to add an SQL string for _attribute_ to the receiver's `listString`, and again to add a formatted SQL string for _value_ to the receiver's `valueList`.

__See also:__
[`sqlStringForAttribute`](#apple-gy4teni), [`sqlStringForValue`](#apple-g4ytsmy), [`formatValue:forAttribute`](#apple-geytcma)

---

### addJoinClauseWithLeftName:rightName:joinSemantic:

public void `addJoinClause`(java.lang.String _leftName_, java.lang.String _rightName_, int _semantic_)

Creates a new join clause by invoking [`assembleJoinClause`](#apple-geytsma) and adds it to the receiver's join clause string. Separates join conditions already in the join clause string with the word "and". Invoked from [`joinExpression`](#apple-gq3tcmy).

__See also:__
[`joinClauseString`](#apple-gy3dena)

---

### addOrderByAttributeOrdering

public void `addOrderByAttributeOrdering`(com.apple.yellow.eocontrol.EOSortOrdering _sortOrdering_)

Adds an attribute-direction pair ("LAST_NAME asc", for example) to the receiver's ORDER BY string. If _sortOrdering_'s selector is CompareCaseInsensitiveAscending or CompareCaseInsensitiveDescending, the string generated has the format "upper(attribute) direction". Use the method [`orderByString`](#apple-gq3dina) to access the ORDER BY string. `addOrderByAttributeOrdering:` invokes [`appendItemToListString`](#apple-gy2dmna) to add the attribute-direction pair.

__See also:__
[`sqlStringForAttributeNamed`](#apple-gy4tmmq)

---

### addSelectListAttribute

public void `addSelectListAttribute`(EOAttribute _attribute_)

Adds an SQL string for _attribute_ to a comma-separated list of attribute names for use in a SELECT statement. The SQL string for _attribute_ is formatted with _attribute_'s "read" format. Use [`listString`](#apple-gq3dmmq) to access the list. `addSelectListAttribute:` invokes [`appendItemToListString`](#apple-gy2dmna) to add the attribute name.

__See also:__
[`sqlStringForAttribute`](#apple-gy4teni), [`formatSQLString`](#apple-geytamy), __- readFormat__  (EOAttribute)

---

### addUpdateListAttribute

public void `addUpdateListAttribute`(EOAttribute _attribute_, java.lang.String _value_)

Adds a attribute-value assignment ("LAST_NAME = `Thomas'", for example) to a comma-separated list for use in an UPDATE statement. Formats _value_ with _attribute_'s "write" format. Use [`listString`](#apple-gq3dmmq) to access the list. `addUpdateListAttribute:value:` invokes [`appendItemToListString`](#apple-gy2dmna) to add the attribute-value assignment.

__See also:__
[`formatSQLString`](#apple-geytamy)

---

### aliasesByRelationshipPath

public NSMutableDictionary `aliasesByRelationshipPath`()

Returns a dictionary of table aliases. The keys of the dictionary are relationship paths-"department" and "department.location", for example. The values are the table aliases for the corresponding table-"t1" and "t2", for example. The `aliasesByRelationshipPath` dictionary always has at least one entry: an entry for the EOSQLExpression's entity. The key of this entry is the empty string ("") and the value is "t0". The dictionary returned from this method is built up over time with successive calls to [`sqlStringForAttributePath`](#apple-gy4toni).

__See also:__
[`tableListWithRootEntity`](#apple-geydsojq)

---

### allowsNullClauseForConstraint

public java.lang.String `allowsNullClauseForConstraint`(boolean _flag_)

Returns according to _flag_ an adaptor specific string for use in a CREATE TABLE statement. The returned string indicates whether a column allows null values. EOSQLExpression's implementation returns the empty string if _flag_ is `true`, "NOT NULL" otherwise. A subclass should override this if its database server's semantics are different. For example, the SybaseSLQExpression returns "null" if _flag_ is `true`, the empty string otherwise.

__See also:__
[`addCreateClauseForAttribute`](#apple-giydcnzz)

---

### appendItemToListString

public void `appendItemToListString`(java.lang.String _itemString_, java.lang.String _listString_)

Adds _itemString_ to a comma-separated list. If _listString_ already has entries, this method appends a comma followed by _itemString_. Invoked from [`addSelectListAttribute`](#apple-gyztema), [`addInsertListAttribute`](#apple-geytiny), [`addUpdateListAttribute`](#apple-gy2damy), and [`addOrderByAttributeOrdering`](#apple-gyzdqnq)

---

### assembleDeleteStatementWithQualifier

public java.lang.String `assembleDeleteStatementWithQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_, java.lang.String _tableList_, java.lang.String _whereClause_)

Invoked from [`prepareDeleteExpressionForQualifier`](#apple-gy3tkmi) to return an SQL DELETE statement of the form:

> ```
> DELETE FROM tableListSQL_WHERE whereClause
> ```

_qualifier_ is the argument to `prepareDeleteExpressionForQualifier:` from which _whereClause_ was derived. It is provided for subclasses that need to generate the WHERE clause in a particular way.

---

### assembleInsertStatementWithRow

public java.lang.String `assembleInsertStatementWithRow`(NSDictionary _row_, java.lang.String _tableList_, java.lang.String _columnList_, java.lang.String _valueList_)

Invoked from [`prepareInsertExpressionWithRow`](#apple-gy3tqoa) to return an SQL INSERT statement of the form:

> ```
> INSERT INTO tableList (columnList)VALUES valueList
> ```

or, if _columnList_ is `null`:

> ```
> INSERT INTO tableListVALUES valueList
> ```

_row_ is the argument to `prepareInsertExpressionWithRow:` from which _columnList_ and _valueList_ were derived. It is provided for subclasses that need to generate the list of columns and values in a particular way.

---

### assembleJoinClause

public java.lang.String `assembleJoinClause`(java.lang.String _leftName_,
java.lang.String _rightName_,
int _semantic_)

Returns a join clause of the form:

> ```
> leftName operator rightName
> ```

Where operator is "=" for an inner join, "\*=" for a left-outer join, and "=\*" for a right-outer join. Invoked from [`addJoinClauseWithLeftName:rightName:joinSemantic:`](#apple-geytkmq).

---

### assembleSelectStatementWithAttributes

public java.lang.String `assembleSelectStatementWithAttributes`(NSArray _attributes_,
boolean _lock_,
com.apple.yellow.eocontrol.EOQualifier _qualifier_,
NSArray _fetchOrder_,
java.lang.String _selectString_,
java.lang.String _columnList_,
java.lang.String _tableList_,
java.lang.String _whereClause_,
java.lang.String _joinClause_,
java.lang.String _orderByClause_,
java.lang.String _lockClause_)

Invoked from [`prepareSelectExpressionWithAttributes`](#apple-gy4dgmi) to return an SQL SELECT statement of the form:

> ```
> SELECT columnListFROM tableList lockClause WHERE whereClause AND joinClause ORDER BY orderByClause
> ```

If _lockClause_ is `null`, it is omitted from the statement. Similarly, if _orderByClause_ is `null`, the "ORDER BY _orderByClause_" is omitted. If either _whereClause_ or _joinClause_ is `null`, the "AND" and `null`-valued argument are omitted. If both are `null`, the entire WHERE clause is omitted.

_attributes_, _lock_, _qualifier_, and _fetchOrder_ are the arguments to `prepareSelectExpressionWithAttributes:lock:fetchSpecification:` from which the other `assembleSelect...` arguments were derived. They are provided for subclasses that need to generate the clauses of the SELECT statement in a particular way.

---

### assembleUpdateStatementWithRow

public java.lang.String `assembleUpdateStatementWithRow`(NSDictionary _row_, com.apple.yellow.eocontrol.EOQualifier _qualifier_, java.lang.String _tableList_, java.lang.String _updateList_, java.lang.String _whereClause_)

Invoked from [`prepareUpdateExpressionWithRow`](#apple-gy4dknq) to return an SQL UPDATE statement of the form:

> ```
> UPDATE tableListSET updateListWHERE whereClause
> ```

_row_ and _qualifier_ are the arguments to `prepareUpdateExpressionWithRow:qualifier:` from which _updateList_ and _whereClause_ were derived. They are provided for subclasses that need to generate the clauses of the UPDATE statement in a particular way.

---

### bindVariableDictionaries

public NSArray `bindVariableDictionaries`()

Returns the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
[`addBindVariableDictionary`](#apple-gyytqnq)

---

### bindVariableDictionaryForAttribute

public abstract NSMutableDictionary `bindVariableDictionaryForAttribute`(EOAttribute _attribute_, java.lang.Object _value_)

Implemented by subclasses to create and return the bind variable dictionary for _attribute_ and _value_. The dictionary returned from this method must contain at least the following key-value pairs:

| __Key__ | __Value__ |
| BindVariableNameKey | the name of the bind variable for _attribute_ |
| BindVariablePlaceHolderKey | the placeholder string used in the SQL statement |
| BindVariableAttributeKey | _attribute_ |
| BindVariableValueKey | _value_ |

```
```

An adaptor subclass may define additional entries as required by its RDBMS.

Invoked from [`sqlStringForValue`](#apple-g4ytsmy) when the message [`mustUseBindVariableForAttribute`](#apple-gy3tgmi)(_attribute)_ returns `true` or when the receiver's class uses bind variables and the message [`shouldUseBindVariableForAttribute`](#apple-gy4tama)(_attribute_) returns `true`. For more information on bind variables, see the discussion in the class description.

A subclass that uses bind variables should implement this method without invoking EOSQLExpression's implementation. The subclass implementation must return a dictionary with entries for the keys listed above and may add additional keys.

__See also:__
[`bindVariableDictionaryForAttribute`](#apple-gy2tmoi), [`useBindVariables`](#apple-geytgoa)

---

### columnTypeStringForAttribute

public java.lang.String `columnTypeStringForAttribute`(EOAttribute _anAttribute_)

Returns an adaptor specific type string for _anAttribute_ that's suitable for use in a CREATE TABLE statement. EOSQLExpression's implementation creates a string based on _anAttribute_'s [`externalType`](EOAttribute.md#apple-hazdq), [`precision`](EOAttribute.md#apple-ha3tk), and [`width`](EOAttribute.md#apple-geydanq) as follows:

| __If Condition__ | __Generated Type String__ |
| precision is non-zero | externalType(precision, scale) |
| precision is zero and width is non-zero | externalType(scale) |
| precision and width are zero | externalType |

```
```

A subclass should override the default implementation if its database server requires column types in a different format.

__See also:__
[`addCreateClauseForAttribute`](#apple-giydcnzz)

---

### entity

public EOEntity `entity`()

Returns the receiver's entity.

__See also:__
["Constructors"](#apple-ge4tknzt)

---

### externalNameQuoteCharacter

public java.lang.String `externalNameQuoteCharacter`()

Returns the string `\"' (an escaped quote character) if the receiver uses quoted external names, or the empty string ("") otherwise.

__See also:__
[`useQuotedExternalNames`](#apple-ge2dena), [`sqlStringForSchemaObjectName`](#apple-g4ytgmi)

---

### joinClauseString

public java.lang.String `joinClauseString`()

Returns the part of the receiver's WHERE clause that specifies join conditions. Together, the `joinClauseString` and the `[whereClauseString](#apple-gqztmny)` make up a statement's WHERE clause. If the receiver's statement doesn't contain join conditions, this method returns an empty string.

An EOSQLExpression's `joinClauseString` is generally set by invoking [`joinExpression`](#apple-gq3tcmy).

__See also:__
[`addJoinClauseWithLeftName:rightName:joinSemantic:`](#apple-geytkmq)

---

### joinExpression

public void `joinExpression()`

Builds up the `[joinClauseString](#apple-gy3dena)` for use in a SELECT statement. For each relationship path in the [`aliasesByRelationshipPath`](#apple-gyztqna) dictionary, this method invokes [`addJoinClauseWithLeftName:rightName:joinSemantic:`](#apple-geytkmq) for each of the relationship's EOJoin objects.

If the `aliasesByRelationshipPath` dictionary only has one entry (the entry for the EOSQLExpression's entity), the `joinClauseString` is empty.

You must invoke this method _after_ invoking [`addSelectListAttribute`](#apple-gyztema) for each attribute to be selected and after sending `sqlStringForSQLExpression`(`this`)to the qualifier for the SELECT statement. (These methods build up the `aliasesByRelationshipPath` dictionary by invoking [`sqlStringForAttributePath`](#apple-gy4toni).)

__See also:__
[`whereClauseString`](#apple-gqztmny)

---

### listString

public java.lang.String `listString`()

Returns a comma-separated list of attributes or "attribute = value" assignments. `listString` is built up with successive invocations of [`addInsertListAttribute`](#apple-geytiny), [`addSelectListAttribute`](#apple-gyztema), or [`addUpdateListAttribute`](#apple-gy2damy) for INSERT statements, SELECT statements, and UPDATE statements, respectively. The contents of `listString` vary according to the type of statement the receiver is building:

| __Type of Statement__ | __Sample listString Contents__ |
| INSERT | FIRST_NAME, LAST_NAME, EMPLOYEE_ID |
| UPDATE | FIRST_NAME = "Timothy", LAST_NAME = "Richardson" |
| SELECT | t0.FIRST_NAME, t0.LAST_NAME, t1.DEPARTMENT_NAME |

```
```


---

### lockClause

public java.lang.String `lockClause`()

Overridden by subclasses to return the SQL string used in a SELECT statement to lock selected rows. A concrete subclass of EOSQLExpression must override this method to return the string used by its adaptor's RDBMS.

---

### mustUseBindVariableForAttribute

public boolean `mustUseBindVariableForAttribute`(EOAttribute _attribute_)

Returns `true` if the receiver must use bind variables for _attribute_, `false` otherwise. EOSQLExpression's implementation returns `false`. An SQL expression subclass that uses bind variables should override this method to return `true` if the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
[`shouldUseBindVariableForAttribute`](#apple-gy4tama), [`bindVariableDictionaryForAttribute`](#apple-gy2tmoi)

---

### orderByString

public java.lang.String `orderByString`()

Returns the comma-separated list of "attribute direction" pairs ("LAST_NAME asc, FIRST_NAME asc", for example) for use in a SELECT statement.

__See also:__
[`addOrderByAttributeOrdering`](#apple-gyzdqnq)

---

### prepareConstraintStatementForRelationship

public void `prepareConstraintStatementForRelationship`(EORelationship _relationship_, NSArray _sourceColumns_, NSArray _destinationColumns_)

Sets the receiver's [`statement`](#apple-gq2dcna) to an adaptor specific constraint for _relationship_. EOSQLExpression's implementation generates statements of the form:

> ```
> ALTER TABLE TABLE_NAME ADD CONSTRAINT CONSTRAINT_NAME    FOREIGN KEY (SOURCE_KEY_LIST)    REFERENCES DESTINATION_TABLE_NAME (DESTINATION_KEY_LIST)
> ```

Where

- _TABLE_NAME_ is the external name of the receiver's entity.
- _CONSTRAINT_NAME_ is the external name of the receiver's entity, _relationship_'s name, and the string "FK", concatenated with underbars between them (EMPLOYEE_MANAGER_FK, for example),
- _SOURCE_KEY_LIST_ is a comma-separated list of the source columns in _sourceColumns_.
- _DESTINATION_TABLE_NAME_ is the external name of _relationship_'s destination entity.
- _DESTINATION_KEY_LIST_ is a comma-separated list of the destination columns in _destinationColumns_

__See also:__
[`foreignKeyConstraintStatementsForRelationship`](#apple-ge4tonrz)

---

### prepareDeleteExpressionForQualifier

public void `prepareDeleteExpressionForQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_)

Generates a DELETE statement by performing the following steps:

- Sends an `sqlStringForSQLExpression`(`this`)message to _qualifier_ to generate the receiver's `[whereClauseString](#apple-gqztmny)`.
- Invokes [`tableListWithRootEntity`](#apple-geydsojq) to get the table name for the FROM clause.
- Invokes [`assembleDeleteStatementWithQualifier`](#apple-gy2tanq).

__See also:__
[`deleteStatementWithQualifier`](#apple-geydsni)

---

### prepareInsertExpressionWithRow

public void `prepareInsertExpressionWithRow`(NSDictionary _row_)

Generates an INSERT statement by performing the following steps:

- Invokes [`addInsertListAttribute`](#apple-geytiny) for each entry in _row_ to prepare the comma-separated list of attributes and the corresponding list of values.
- Invokes [`tableListWithRootEntity`](#apple-geydsojq) to get the table name.
- Invokes [`assembleInsertStatementWithRow`](#apple-gy2teoa).

__See also:__
[`insertStatementForRow`](#apple-geytcmy)

---

### prepareSelectExpressionWithAttributes

public void `prepareSelectExpressionWithAttributes`(NSArray _attributes_, boolean _flag_,
com.apple.yellow.eocontrol.EOFetchSpecification _fetchSpecification_)

Generates a SELECT statement by performing the following steps:

- Invokes [`addSelectListAttribute`](#apple-gyztema) for each entry in _attributes_ to prepare the comma-separated list of attributes.
- Sends an `sqlStringForSQLExpression`(`this`)message to _fetchSpecification_'s qualifier to generate the receiver's [`whereClauseString`](#apple-gqztmny).
- Invokes [`addOrderByAttributeOrdering`](#apple-gyzdqnq) for each EOAttributeOrdering object in _fetchSpecification_.First conjoins the qualifier in _fetchSpecification_ with the restricting qualifier, if any, of the receiver's entity.
- Invokes [`joinExpression`](#apple-gq3tcmy) to generate the receiver's [`joinClauseString`](#apple-gy3dena).
- Invokes [`tableListWithRootEntity`](#apple-geydsojq) to get the comma-separated list of tables for the FROM clause.
- If _flag_ is `true`, invokes [`lockClause`](#apple-gy3dqma) to get the SQL string to lock selected rows.
- Invokes [`assembleSelectStatementWithAttributes`](#apple-gy2tgny).

__See also:__
[`selectStatementForAttributes`](#apple-geytcny)

---

### prepareUpdateExpressionWithRow

public void `prepareUpdateExpressionWithRow`(NSDictionary _row_, com.apple.yellow.eocontrol.EOQualifier _qualifier_)

Generates an UPDATE statement by performing the following steps:

- Invokes [`addUpdateListAttribute`](#apple-gy2damy) for each entry in _row_ to prepare the comma-separated list of "attribute = value" assignments.
- Sends an `sqlStringForSQLExpression`(`this`)message to _qualifier_ to generate the receiver's `[whereClauseString](#apple-gqztmny)`.
- Invokes [`tableListWithRootEntity`](#apple-geydsojq) to get the table name for the FROM clause.
- Invokes [`assembleUpdateStatementWithRow`](#apple-gy2tkma).

__See also:__
[`updateStatementForRow`](#apple-geytgmy)

---

### setStatement

public void `setStatement`(java.lang.String _string_)

Sets the receiver's SQL statement to _string_, which should be a valid expression in the target query language. Use this method-instead of a `prepare...` method-to directly assign an SQL string to an EOSQLExpression object. This method does not perform substitutions or formatting of any kind.

__See also:__
[`expressionForString`](#apple-geydsoi), [`statement`](#apple-gq2dcna)

---

### setUseAliases

public void `setUseAliases`(boolean _flag_)

Tells the receiver whether or not to use table aliases.

__See also:__
[`useAliases`](#apple-gqztqni)

---

### shouldUseBindVariableForAttribute

public boolean `shouldUseBindVariableForAttribute`(EOAttribute _attribute_)

Returns `true` if the receiver can provide a bind variable dictionary for _attribute_, `false` otherwise. Bind variables aren't used for values associated with this attribute when the static method [`useBindVariables`](#apple-geytgoa) returns `false`. EOSQLExpression's implementation returns `false`. An SQL expression subclass should override this method to return `true` if the receiver should use bind variables for attributes with _attribute_'s external type. It should also return `true` for any attribute for which the receiver must use bind variables.

__See also:__
[`mustUseBindVariableForAttribute`](#apple-gy3tgmi)

---

### sqlStringForAttribute

public java.lang.String `sqlStringForAttribute`(EOAttribute _attribute_)

Returns the SQL string for _attribute_, complete with a table alias if the receiver uses table aliases. Invoked from [`sqlStringForAttributeNamed`](#apple-gy4tmmq) when the attribute name is not a path.

__See also:__
[`sqlStringForAttributePath`](#apple-gy4toni)

---

### sqlStringForAttributeNamed

public java.lang.String `sqlStringForAttributeNamed`(java.lang.String _name_)

Returns the SQL string for the attribute named _name_, complete with a table alias if the receiver uses table aliases. Generates the return value using [`sqlStringForAttributePath`](#apple-gy4toni) if _name_ is an attribute path ("department.name", for example); otherwise, uses [`sqlStringForAttribute`](#apple-gy4teni).

---

### sqlStringForAttributePath

public java.lang.String `sqlStringForAttributePath`(NSArray _path_)

Returns the SQL string for _path_, complete with a table alias if the receiver uses table aliases. Invoked from [`sqlStringForAttributeNamed`](#apple-gy4tmmq) when the specified attribute name is a path ("department.location.officeNumber", for example). _path_ is an array of any number of EORelationship objects followed by an EOAttribute object. The EORelationship and EOAttribute objects each correspond to a component in path. For example, if the attribute name argument to `sqlStringForAttributeNamed:` is "department.location.officeNumber", _path_ is an array containing the following objects in the order listed:

- The EORelationship object in the receiver's entity named "department". (Assume the relationship's destination entity is named "Department".)
- The EORelationship object in the Department entity named "location". (Assume the relationship's destination entity is named "Location".)
- The EOAttribute object in the Location entity named "officeNumber".

Assuming that the receiver uses aliases and the alias for the Location table is t2, the SQL string for this sample attribute path is "t2.officeNumber".

If the receiver uses table aliases, this method has the side effect of adding a "relationship path"-"alias name" entry to the `aliasesByRelationship` dictionary.

__See also:__
[`sqlStringForAttribute`](#apple-gy4teni)

---

### sqlStringForConjoinedQualifiers

public java.lang.String `sqlStringForConjoinedQualifiers`(NSArray _qualifiers_)

Creates and returns an SQL string that is the result of interposing the word "AND" between the SQL strings for the qualifiers in _qualifiers_. Generates an SQL string for each qualifier by sending `sqlStringForSQLExpression:` messages to the qualifiers with `this` as the argument. If the SQL string for a qualifier contains only white space, it isn't included in the return value. The return value is enclosed in parentheses if the SQL strings for two or more qualifiers were ANDed together.

---

### sqlStringForDisjoinedQualifiers

public java.lang.String `sqlStringForDisjoinedQualifiers`(NSArray _qualifiers_)

Creates and returns an SQL string that is the result of interposing the word "OR" between the SQL strings for the qualifiers in _qualifiers_. Generates an SQL string for each qualifier by sending `sqlStringForSQLExpression:` messages to the qualifiers with `this` as the argument. If the SQL string for a qualifier contains only white space, it isn't included in the return value. The return value is enclosed in parentheses if the SQL strings for two or more qualifiers were ORed together.

---

### sqlStringForKeyComparisonQualifier

public java.lang.String `sqlStringForKeyComparisonQualifier`(
com.apple.yellow.eocontrol.EOKeyComparisonQualifier _qualifier_)

Creates and returns an SQL string that is the result of interposing an operator between the SQL strings for the right and left keys in _qualifier_. Determines the SQL operator by invoking [`sqlStringForSelector`](#apple-g4ytknq) with _qualifier_'s selector and `null` for the value. Generates SQL strings for _qualifier_'s keys by invoking [`sqlStringForAttributeNamed`](#apple-gy4tmmq) to get SQL strings. This method also formats the strings for the right and left keys using [`formatSQLString`](#apple-geytamy) with the corresponding attributes' "read" formats.

---

### sqlStringForKeyValueQualifier

public java.lang.String `sqlStringForKeyValueQualifier`(
com.apple.yellow.eocontrol.EOKeyValueQualifier _qualifier_)

Creates and returns an SQL string that is the result of interposing an operator between the SQL strings for _qualifier_'s key and value. Determines the SQL operator by invoking [`sqlStringForSelector`](#apple-g4ytknq) with _qualifier_'s selector and value. Generates an SQL string for _qualifier_'s key by invoking [`sqlStringForAttributeNamed`](#apple-gy4tmmq) to get an SQL string and [`formatSQLString`](#apple-geytamy) with the corresponding attribute's "read" format. Similarly, generates an SQL string for qualifier's value by invoking [`sqlStringForValue`](#apple-g4ytsmy) to get an SQL string and [`formatValue:forAttribute`](#apple-geytcma) to format it. (First invokes [`sqlPatternFromShellPattern`](#apple-ge2dgny) for the value if _qualifier_'s selector is QualifierOperatorLike.)

---

### sqlStringForNegatedQualifier

public java.lang.String `sqlStringForNegatedQualifier`(com.apple.yellow.eocontrol.EOQualifier _qualifier_)

Creates and returns an SQL string that is the result of surrounding the SQL string for _qualifier_ in parentheses and appending it to the word "not". For example, if the string for _qualifier_ is "FIRST_NAME = `John'", `sqlStringForNegatedQualifier:` returns the string "not (FIRST_NAME = `John')".

Generates an SQL string for _qualifier_ by sending an `sqlStringForSQLExpression:``:` message to _qualifier_ with `this` as the argument. If the SQL string for _qualifier_ contains only white space, this method returns `null`.

---

### sqlStringForNumber

public java.lang.String `sqlStringForNumber`(java.lang.Number _aNumber_)

Returns the SQL string for _aNumber_.

---

### sqlStringForQualifier

public java.lang.String `sqlStringForQualifier`(com.apple.yellow.eocontrol.EOQualifier _aQualifier_)

Returns a SQL statement for _aQualifier_ suitable for inclusion in a WHERE clause. Invoked from an EOSQLExpression while it's preparing a SELECT, UPDATE, or DELETE statement.

__See also:__
[`whereClauseString`](#apple-gqztmny)

---

### sqlStringForSchemaObjectName

public java.lang.String `sqlStringForSchemaObjectName`(java.lang.String _name_)

Returns _name_ enclosed in the external name quote character if the receiver uses quoted external names, otherwise simply returns _name_ unaltered.

__See also:__
[`useQuotedExternalNames`](#apple-ge2dena), [`externalNameQuoteCharacter`](#apple-gq3tgma)

---

### sqlStringForSelector

public java.lang.String `sqlStringForSelector`(NSSelector _selector_, java.lang.Object _value_)

Returns an SQL operator for _selector_ and _value_. The following table summarizes EOSQLExpression's default mapping:

| __Selector__ | __SQL Operator__ |
| QualifierOperatorIsEqual | "is" if value is an EONull, "=" otherwise |
| QualifierOperatorNotEqual | "is not" if _value_ is an EONull, "<> otherwise |
| QualifierOperatorLessThan | "<" |
| QualifierOperatorGreaterThan | ">" |
| QualifierOperatorLessThanOrEqualTo | "<=" |
| QualifierOperatorGreaterThanOrEqualTo | ">=" |
| QualifierOperatorLike | "like" |

```
```

Throws an exception if selector is an unknown operator.

__See also:__
[`sqlStringForKeyComparisonQualifier`](#apple-geydqobq), [`sqlStringForKeyValueQualifier`](#apple-g4ydmmq)

---

### sqlStringForString

public java.lang.String `sqlStringForString`(java.lang.String _aString_)

Returns the SQL string for _aString_.

---

### sqlStringForValue

public java.lang.String `sqlStringForValue`(java.lang.Object _value_, java.lang.String _name_)

Returns a string for _value_ appropriate for use in an SQL statement. If the receiver uses a bind variable for the attribute named _name_, then `sqlStringForValue:attributeNamed:` gets the bind variable dictionary for the attribute, adds it to the receiver's array of bind variables dictionaries, and returns the value for the binding's EOBindVariablePlaceHolderKey. Otherwise, this method invokes [`formatValue:forAttribute`](#apple-geytcma) and returns the formatted string for _value_.

__See also:__
[`mustUseBindVariableForAttribute`](#apple-gy3tgmi), [`shouldUseBindVariableForAttribute`](#apple-gy4tama), [`useBindVariables`](#apple-geytgoa),
[`bindVariableDictionaries`](#apple-gq3tsna), [`addBindVariableDictionary`](#apple-gyytqnq)

---

### statement

public java.lang.String `statement`()

Returns the complete SQL statement for the receiver. An SQL statement can be assigned to an EOSQLExpression object directly using the static method [`expressionForString`](#apple-geydsoi) or using the instance method [`setStatement`](#apple-gy4dooa). Generally, however, an EOSQLExpression's statement is built up using one of the following methods:

- [prepareSelectExpressionWithAttributes](#apple-gy4dgmi)
- [prepareInsertExpressionWithRow](#apple-gy3tqoa)
- [prepareUpdateExpressionWithRow](#apple-gy4dknq)
- [prepareDeleteExpressionForQualifier](#apple-gy3tkmi)

---

### tableListWithRootEntity

public java.lang.String `tableListWithRootEntity`(EOEntity _entity_)

Returns the comma-separated list of tables for use in a SELECT, UPDATE, or DELETE statement's FROM clause. If the receiver doesn't use table aliases, the table list consists only of the table name for _entity_-"EMPLOYEE", for example. If the receiver does use table aliases (only in SELECT statements by default), the table list is a comma separated list of table names and their aliases, for example:

> ```
> EMPLOYEE t0, DEPARTMENT t1
> ```

`tableListWithRootEntity:` creates a string containing the table name for _entity_ and a corresponding table alias ("EMPLOYEE t0", for example). For each entry in [`aliasesByRelationshipPath`](#apple-gyztqna), this method appends a new table name and table alias.

__See also:__
[`useAliases`](#apple-gqztqni)

---

### useAliases

public boolean `useAliases()`

Returns `true` if the receiver generates statements with table aliases, `false` otherwise. For example, the following SELECT statement uses table aliases:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAMEFROM EMPLOYEE t0, DEPARTMENT t1WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The EMPLOYEE table has the alias t0, and the DEPARTMENT table has the alias t1.

By default, EOSQLExpression uses table aliases only in SELECT statements. Enterprise Objects Framework assumes that INSERT, UPDATE, and DELETE statements are single-table operations. For more information, see the discussion in the class description.

__See also:__
[`setUseAliases`](#apple-gy4dsmi), [`aliasesByRelationshipPath`](#apple-gyztqna)

---

### valueList

public java.lang.String `valueList`()

Returns the comma-separated list of values used in an INSERT statement. For example, the value list for the following INSERT statement:

> ```
> INSERT EMPLOYEE (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, DEPARTMENT_ID, SALARY)VALUES ('Shaun', 'Hayes', 1319, 23, 4600)
> ```

is "`Shaun', `Hayes', 1319, 23, 4600". An EOSQLExpression's `valueList` is generated a value at a time with [`addInsertListAttribute`](#apple-geytiny) messages.

---

### whereClauseString

public java.lang.String `whereClauseString`()

Returns the part of the receiver's WHERE clause that qualifies rows. The whereClauseString does not specify join conditions; the [`joinClauseString`](#apple-gy3dena) does that. Together, the `whereClauseString` and the `joinClauseString` make up a statement's where clause. For example, a qualifier for an Employee entity specifies that a statement only affects employees who belong to the Finance department and whose monthly salary is greater than $4500. Assume the corresponding where clause looks like this:

> ```
> WHERE EMPLOYEE.SALARY > 4500 AND DEPARTMENT.NAME = `Finance'    AND EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID
> ```

EOSQLExpression generates both a `whereClauseString` and a `joinClauseString` for this qualifier. The `whereClauseString` qualifies the rows and looks like this:

> ```
> EMPLOYEE.SALARY > 4500 AND DEPARTMENT.NAME = `Finance'
> ```

The `joinClauseString` specifies the join conditions between the EMPLOYEE table and the DEPARTMENT table and looks like this:

> ```
> EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID
> ```

An EOSQLExpression's `whereClauseString` is generally set by sending a `sqlStringForSQLExpression:` message to an EOQualifier object.

---

[!](Creating%20Relationships-2.md)
[!](EOSQLExpression-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
