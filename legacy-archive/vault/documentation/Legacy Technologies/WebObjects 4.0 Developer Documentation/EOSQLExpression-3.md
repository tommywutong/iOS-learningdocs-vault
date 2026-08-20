---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOSQLExpression.html
archived_at: '2026-07-18T01:28:17.329754Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOAccess Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOAccess.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](Creating%20Relationships-3.md)
[!](More%20about%20EOSQLExpression.md)

---

# EOSQLExpression

__Inherits From:__
NSObject

__Conforms To:__
NSObject (NSObject)

__Declared in:__
EOAccess/EOSQLExpression.h
EOAccess/EOSchemaGeneration.h

---

## Class Description

EOSQLExpression is an abstract superclass that defines how to build SQL statements for adaptor channels. You don't typically use instances of EOSQLExpression; rather, you use EOSQLExpression subclasses written to work with a particular RDBMS and corresponding adaptor. A concrete subclass of EOSQLExpression overrides many of its methods in terms of the query language syntax for its specific RDBMS. EOSQLExpression objects are used internally by the Framework, and unless you're creating a concrete adaptor, you won't ordinarily need to interact with EOSQLExpression objects yourself. You most commonly create and use an EOSQLExpression object when you want to send an SQL statement directly to the server. In this case, you simply create an expression with the EOSQLExpression class method [`expressionForString:`](#apple-geydsoi), and send the expression object to an adaptor channel using [EOAdaptorChannel](EOAdaptorChannel-2.md)'s `evaluateExpression:` method.

For more information, see ["More about EOSQLExpression"](More%20about%20EOSQLExpression.md).

---

## Method Types

**Creating an EOSQLExpression object**

**[+ selectStatementForAttributes:lock:fetchSpecification:entity:](#apple-geytcny)

**[+ insertStatementForRow:entity:](#apple-geytcmy)

**[+ updateStatementForRow:qualifier:entity:](#apple-geytgmy)

**[+ deleteStatementWithQualifier:entity:](#apple-geydsni)

**[+ expressionForString:](#apple-geydsoi)

**[- initWithEntity:](#apple-gi2dmojz)************

**Building SQL Expressions**

**[- prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-gy4dgmi)

**[- prepareInsertExpressionWithRow:](#apple-gy3tqoa)

**[- prepareUpdateExpressionWithRow:qualifier:](#apple-gy4dknq)

**[- prepareDeleteExpressionForQualifier:](#apple-gy3tkmi)

**[- setStatement:](#apple-gy4dooa)

**[- statement](#apple-gq2dcna)************

**Generating SQL for attributes and values**

**[+ formatSQLString:format:](#apple-geytamy)

**[+ formatValue:forAttribute:](#apple-geytcma)

**[+ formatStringValue:](#apple-geytany)

**[- sqlStringForValue:attributeNamed:](#apple-g4ytsmy)

**[- sqlStringForAttributeNamed:](#apple-gy4tmmq)

**[- sqlStringForAttribute:](#apple-gy4teni)

**[- sqlStringForAttributePath:](#apple-gy4toni)**************

**Generating SQL for names of database objects**

**[- sqlStringForSchemaObjectName:](#apple-g4ytgmi)

**[+ setUseQuotedExternalNames:](#apple-ge2dema)

**[+ useQuotedExternalNames](#apple-ge2dena)

**[- externalNameQuoteCharacter](#apple-gq3tgma)********

**Generating an attribute list**

**[- addSelectListAttribute:](#apple-gyztema)

**[- addInsertListAttribute:value:](#apple-geytiny)

**[- addUpdateListAttribute:value:](#apple-gy2damy)

**[- appendItem:toListString:](#apple-gy2dmna)

**[- listString](#apple-gq3dmmq)**********

**Generating a value list**

**[- addInsertListAttribute:value:](#apple-geytiny)

**[- addUpdateListAttribute:value:](#apple-gy2damy)

**[- valueList](#apple-g4zdioa)******

**Generating a table list**

**[- tableListWithRootEntity:](#apple-geydsojq)

**[- aliasesByRelationshipPath](#apple-gyztqna)****

**Generating the join clause**

**[- joinExpression](#apple-gq3tcmy)

**[- addJoinClause](#apple-geytkmq)

**[- assembleJoinClauseWithLeftName:rightName:joinSemantic:](#apple-geytsma)

**[- joinClauseString](#apple-gy3dena)********

**Generating a search pattern**

**[+ sqlPatternFromShellPattern:](#apple-ge2dgny)

**[+ sqlPatternFromShellPattern:withEscapeCharacter:](#apple-geyteni)****

**Generating a relational operator**

**[- sqlStringForSelector:value:](#apple-g4ytknq)**

**Accessing the where clause**

**[- whereClauseString](#apple-gqztmny)**

**Generating an order by clause**

**[- addOrderByAttributeOrdering:](#apple-gyzdqnq)

**[- orderByString](#apple-gq3dina)****

**Accessing the lock clause**

**[- lockClause](#apple-gy3dqma)**

**Assembling a statement**

**[- assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder:
selectString:columnList:tableList:whereClause:joinClause:
orderByClause:lockClause:](#apple-gy2tgny)

**[- assembleInsertStatementWithRow:tableList:columnList:valueList:](#apple-gy2teoa)

**[- assembleUpdateStatementWithRow:qualifier:tableList:updateList:
whereClause:](#apple-gy2tkma)

**[- assembleDeleteStatementWithQualifier:tableList:whereClause:](#apple-gy2tanq)********

**Generating SQL for qualifiers**

**[- sqlStringForConjoinedQualifiers:](#apple-gy4tsoi)

**[- sqlStringForDisjoinedQualifiers:](#apple-gezteny)

**[- sqlStringForKeyComparisonQualifier:](#apple-geydqobq)

**[- sqlStringForKeyValueQualifier:](#apple-g4ydmmq)

**[- sqlStringForNegatedQualifier:](#apple-g4ydqni)**********

**Managing bind variables**

**[+ setUseBindVariables:](#apple-geydanrt)

**[+ useBindVariables](#apple-geytgoa)

**[- addBindVariableDictionary:](#apple-gyytqnq)

**[- bindVariableDictionaries](#apple-gq3tsna)

**[- bindVariableDictionaryForAttribute:value:](#apple-gy2tmoi)

**[- mustUseBindVariableForAttribute:](#apple-gy3tgmi)

**[- shouldUseBindVariableForAttribute:](#apple-gy4tama)**************

**Using table aliases**

**[- setUseAliases:](#apple-gy4dsmi)

**[- useAliases](#apple-gqztqni)****

**Accessing the entity**

**[entity](#apple-gq3tomq)**

**Creating a schema generation script**

**[+ schemaCreationStatementsForEntities:options:](#apple-ge4tsnbv)

**[- createDatabaseStatementsForConnectionDictionary:
administrativeConnectionDictionary:](#apple-gi2temzz)

**[- dropDatabaseStatementsForConnectionDictionary:
administrativeConnectionDictionary:](#apple-gi2tgmjz)******

---

## Class Methods

---

### createDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:

+ (NSArray \*)__createDatabaseStatementsForConnectionDictionary:__ (NSDictionary \*)_connectionDictionary___administrativeConnectionDictionary:__ (NSDictionary \*)_adminDictionary_

Generates the SQL statements that will create a database (or user, for Oracle) that can be accessed by the provided connection dictionary and administrative connection dictionary.

__See also:__
[+ `dropDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:`](#apple-gi2tgmjz)

---

### deleteStatementWithQualifier:entity:

+ (EOSQLExpression \*)__deleteStatementWithQualifier:__ (EOQualifier \*)_qualifier_ __entity:__ (id)_entity_

Creates and returns an SQL DELETE expression to delete the rows described by _qualifier_. Creates an instance of EOSQLExpression, initializes it with _entity_ (an EOEntity object), and sends it a [`prepareDeleteExpressionForQualifier:`](#apple-gy3tkmi) message. Raises an NSInvalidArgumentException if _qualifier_ is `nil`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.As a result, all keys in _qualifier_ should be simple key names; no key paths are allowed. To generate DELETE statements that do use table aliases, you must override `prepareDeleteExpressionForQualifier:` to send a [`setUseAliases:`](#apple-gy4dsmi)YES message prior to invoking `super`'s version.

---

### dropDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:

+ (NSArray \*)__dropDatabaseStatementsForConnectionDictionary:__ (NSDictionary \*)_connectionDictionary___administrativeConnectionDictionary:__ (NSDictionary \*)_adminDictionary_

Generates the SQL statements to drop the database (or user, for Oracle).

__See also:__
[+ `createDatabaseStatementsForConnectionDictionary:
administrativeConnectionDictionary:`](#apple-gi2temzz)

---

### expressionForString:

+ (EOSQLExpression \*)__expressionForString:__ (NSString \*)_string_

Creates and returns an SQL expression for _string_. _string_ should be a valid expression in the target query language. This method does not perform substitutions or formatting of any kind.

__See also:__
[- `setStatement:`](#apple-gy4dooa)

---

### formatSQLString:format:

+ (NSString \*)__formatSQLString:__ (NSString \*)_sqlString_ __format:__ (NSString \*)_format_

Applies _format_ (an EOAttribute object's "read" or "write" format) to _sqlString_ (a value for the attribute). If _format_ is `nil`, this method returns _sqlString_ unchanged.

__See also:__
__-- readFormat__  (EOAttribute), __- writeFormat__  (EOAttribute)

---

### formatStringValue:

+ (NSString \*)__formatStringValue:__ (NSString \*)_string_

Formats _string_ for use as a string constant in a SQL statement. EOSQLExpression's implementation encloses the string in single quotes, escaping any single quotes already present in _string_. Raises an NSInternalInconsistencyException if _string_ is `nil`.

---

### formatValue:forAttribute:

+ (NSString \*)__formatValue:__ (id)_value_ __forAttribute:__ (EOAttribute \*)_attribute_

Overridden by subclasses to return a string representation of _value_ suitable for use in an SQL statement. EOSQLExpression's implementation returns _value_ unchanged. A subclass should override this method to format _value_ depending on _attribute_'s [`externalType`](EOAttribute.md#apple-hazdq). For example, a subclass might format a date using a special database-specific syntax or standard form or truncate numbers to _attribute_'s precision and scale.

---

### insertStatementForRow:entity:

+ (EOSQLExpression \*)__insertStatementForRow:__ (NSDictionary \*)_row_ __entity:__ (EOEntity \*)_entity_

Creates and returns an SQL INSERT expression to insert _row_. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareInsertExpressionWithRow:`](#apple-gy3tqoa). Raises an NSInvalidArgumentException if _entity_ is `nil`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.To generate INSERT statements that do use table aliases, you must override `prepareInsertExpressionWithRow:` to send a [`setUseAliases:`](#apple-gy4dsmi)YES message prior to invoking `super`'s version.

---

### schemaCreationStatementsForEntities:options:

+ (NSArray \*)__schemaCreationStatementsForEntities:__ (NSArray \*)_entities___options:__ (NSDictionary \*)_options_

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

- createTableStatementsForEntityGroups
- dropTableStatementsForEntityGroups
- primaryKeySupportStatementsForEntityGroups
- dropPrimaryKeySupportStatementsForEntityGroups
- primaryKeyConstraintStatementsForEntityGroups
- foreignKeyConstraintStatementsForRelationship

to generate SQLExpressions for the support identified in _options_.

---

### selectStatementForAttributes:lock:fetchSpecification:entity:

+ (EOSQLExpression \*)__selectStatementForAttributes:__ (NSArray \*)_attributes___lock:__ (BOOL)_flag___fetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification___entity:__ (EOEntity \*)_entity_

Creates and returns an SQL SELECT expression. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareSelectExpressionWithAttributes:lock:fetchSpecification:`](#apple-gy4dgmi). The expression created with this method uses table aliases. Raises an NSInvalidArgumentException if _attributes_ is `nil` or empty, _fetchSpecification_ is `nil`, or _entity_ is `nil`.

The expression created with this method uses table aliases.To generate SELECT statements that don't use them, you must override `prepareSelectExpressionWithAttributes:lock:fetchSpecification:` to send a [`setUseAliases:`](#apple-gy4dsmi)NO message prior to invoking `super`'s version.

---

### setUseBindVariables:

+ (void)__setUseBindVariables:__ (BOOL)_flag_

Sets according to _flag_ whether all instances of EOSQLExpression subclasses use bind variables. By default, instances don't use bind variables; if the value for the global user default named EOAdaptorUseBindVariables is YES, though, instances do use them. For more information on bind variables, see the discussion in the class description.

__See also:__
[+ `useBindVariables`](#apple-geytgoa)

---

### setUseQuotedExternalNames:

+ (void)`setUseQuotedExternalNames:`(BOOL)_flag_

Sets whether all instances of EOSQLExpression subclasses quote external names when they are referenced in SQL statements. By setting _flag_ to YES, you can access database tables with names such as "%return", "1st year", and "TABLE" that you couldn't otherwise access. By default, instances don't quote external names; if the value for the global user default named EOAdaptorQuotesExternalNames is YES, though, instances do use quotes.

__See also:__
[+ `useQuotedExternalNames`](#apple-ge2dena), [- `sqlStringForSchemaObjectName:`](#apple-g4ytgmi),
[- `externalNameQuoteCharacter`](#apple-gq3tgma)

---

### sqlPatternFromShellPattern:

+ (NSString \*)__sqlPatternFromShellPattern:__ (NSString \*)_pattern_

Translates a "like" qualifier to an SQL "like" expression. Invoked from [`sqlStringForKeyValueQualifier:`](#apple-g4ydmmq) when the qualifier argument is an EOKeyValueQualifier object whose selector is `isLike:`. EOSQLExpression's implementation performs the following substitutions

| ____Character in pattern____ | __Substitution string__ |
| \* | % |
| ? | _ |
| % | [%] _(unless the percent character appears in square brackets)_ |
| _ | [_] _(unless the underscore character appears in square brackets)_ |

```
```

__See also:__
[+ `sqlPatternFromShellPattern:withEscapeCharacter:`](#apple-geyteni)

---

### sqlPatternFromShellPattern:withEscapeCharacter:

+ (NSString \*)__sqlPatternFromShellPattern:__ (NSString \*)_pattern_`withEscapeCharacter:`(unichar)_escapeCharacter_

Like[`sqlPatternFromShellPattern:`](#apple-ge2dgny) except the argument _escapeCharacter_ allows you to specify a character for escaping the wild card characters "%" and "_".

---

### updateStatementForRow:qualifier:entity:

+ (EOSQLExpression \*)__updateStatementForRow:__ (NSDictionary \*)_row___qualifier:__ (EOQualifier \*)_qualifier___entity:__ (EOEntity \*)_entity_

Creates and returns an SQL UPDATE expression to update the row identified by _qualifier_ with the values in _row_. _row_ should only contain entries for values that have actually changed. Creates an instance of EOSQLExpression, initializes it with _entity_, and sends it [`prepareUpdateExpressionWithRow:qualifier:`](#apple-gy4dknq). Raises an NSInvalidArgumentException if _row_ is `nil` or empty, _qualifier_ is `nil`, or _entity_ is `nil`.

The expression created with this method does not use table aliases because Enterprise Objects Framework assumes that all INSERT, UPDATE, and DELETE statements are single-table operations.As a result, all keys in _qualifier_ should be simple key names; no key paths are allowed. To generate UPDATE statements that do use table aliases, you must override `prepareUpdateExpressionWithRow:qualifier:` to send a [`setUseAliases:`](#apple-gy4dsmi)YES message prior to invoking `super`'s version.

__See also:__
[- `setUseAliases:`](#apple-gy4dsmi)

---

### useBindVariables

+ (BOOL)__useBindVariables__

Returns YES if instances use bind variables, NO otherwise. For more information on bind variables, see the discussion in the class description.

__See also:__
[+ `setUseBindVariables:`](#apple-geydanrt)

---

### useQuotedExternalNames

+ (BOOL)`useQuotedExternalNames`

Returns YES if instances use quoted external names, NO otherwise.

__See also:__
[+ `setUseQuotedExternalNames:`](#apple-ge2dema), [- `sqlStringForSchemaObjectName:`](#apple-g4ytgmi),
[- `externalNameQuoteCharacter`](#apple-gq3tgma)

---

## Instance Methods

---

### addBindVariableDictionary:

- (void)__addBindVariableDictionary:__ (NSMutableDictionary \*)_binding_

Adds _binding_ to the receiver's array of bind variable dictionaries. _binding_ is generally created using the method [`bindVariableDictionaryForAttribute:value:`](#apple-gy2tmoi) and is added to the receiver's bind variable dictionaries in [`sqlStringForValue:attributeNamed:`](#apple-g4ytsmy) when the receiver uses a bind variable for the specified attribute. See the method description for `bindVariableDictionaryForAttribute:value:` for a description of the contents of a bind variable dictionary, and for more information on bind variables, see the discussion in the class description.

__See also:__
[- `bindVariableDictionaries`](#apple-gq3tsna)

---

### addInsertListAttribute:value:

- (void)__addInsertListAttribute:__ (EOAttribute \*)_attribute_ __value:__ (NSString \*)_value_

Adds the SQL string for _attribute_ to a comma-separated list of attributes and _value_ to a comma-separated list of values. Both lists are constructed for use in an INSERT statement. Use the methods [`listString`](#apple-gq3dmmq) and [`valueList`](#apple-g4zdioa) to access the attributes and value lists.

Invokes [`appendItem:toListString:`](#apple-gy2dmna) to add an SQL string for _attribute_ to the receiver's `listString`, and again to add a formatted SQL string for _value_ to the receiver's `valueList`.

__See also:__
[- `sqlStringForAttribute:`](#apple-gy4teni), [- `sqlStringForValue:attributeNamed:`](#apple-g4ytsmy), [+ `formatValue:
forAttribute:`](#apple-geytcma)

---

### addJoinClause

- (void)__addJoinClauseWithLeftName:__ (NSString \*)_leftName_ __rightName:__ (NSString \*)_rightName_ __joinSemantic:__ (EOJoinSemantic)_semantic_

Creates a new join clause by invoking [`assembleJoinClauseWithLeftName:rightName:joinSemantic:`](#apple-geytsma) and adds it to the receiver's join clause string. Separates join conditions already in the join clause string with the word "and". Invoked from [`joinExpression`](#apple-gq3tcmy).

__See also:__
[`joinClauseString`](#apple-gy3dena)

---

### addOrderByAttributeOrdering:

- (void)__addOrderByAttributeOrdering:__ (EOSortOrdering \*)_sortOrdering_

Adds an attribute-direction pair ("LAST_NAME asc", for example) to the receiver's ORDER BY string. If _sortOrdering_'s selector is `c`ompareCaseInsensitiveAscending`:` or `c`ompareCaseInsensitiveDescending`:`, the string generated has the format "upper(attribute) direction". Use the method [`orderByString`](#apple-gq3dina) to access the ORDER BY string. `addOrderByAttributeOrdering:` invokes [`appendItem:toListString:`](#apple-gy2dmna) to add the attribute-direction pair.

__See also:__
[`sqlStringForAttributeNamed:`](#apple-gy4tmmq)

---

### addSelectListAttribute:

- (void)__addSelectListAttribute:__ (EOAttribute \*)_attribute_

Adds an SQL string for _attribute_ to a comma-separated list of attribute names for use in a SELECT statement. The SQL string for _attribute_ is formatted with _attribute_'s "read" format. Use [`listString`](#apple-gq3dmmq) to access the list. `addSelectListAttribute:` invokes [`appendItem:toListString:`](#apple-gy2dmna) to add the attribute name.

__See also:__
[- `sqlStringForAttribute:`](#apple-gy4teni), [+ `formatSQLString:format:`](#apple-geytamy), __- readFormat__  (EOAttribute)

---

### addUpdateListAttribute:value:

- (void)__addUpdateListAttribute:__ (EOAttribute \*)_attribute_ __value:__ (NSString \*)_value_

Adds a attribute-value assignment ("LAST_NAME = `Thomas'", for example) to a comma-separated list for use in an UPDATE statement. Formats _value_ with _attribute_'s "write" format. Use [`listString`](#apple-gq3dmmq) to access the list. `addUpdateListAttribute:value:` invokes [`appendItem:toListString:`](#apple-gy2dmna) to add the attribute-value assignment.

__See also:__
[+ `formatSQLString:format:`](#apple-geytamy)

---

### aliasesByRelationshipPath

- (NSMutableDictionary \*)__aliasesByRelationshipPath__

Returns a dictionary of table aliases. The keys of the dictionary are relationship paths-"department" and "department.location", for example. The values are the table aliases for the corresponding table-"t1" and "t2", for example. The `aliasesByRelationshipPath` dictionary always has at least one entry: an entry for the EOSQLExpression's entity. The key of this entry is the empty string (@"") and the value is "t0". The dictionary returned from this method is built up over time with successive calls to [`sqlStringForAttributePath:`](#apple-gy4toni).

__See also:__
[- `tableListWithRootEntity:`](#apple-geydsojq)

---

### appendItem:toListString:

- (void)__appendItem:__ (NSString \*)_itemString_ __toListString:__ (NSMutableString \*)_listString_

Adds _itemString_ to a comma-separated list. If _listString_ already has entries, this method appends a comma followed by _itemString_. Invoked from [`addSelectListAttribute:`](#apple-gyztema), [`addInsertListAttribute:value:`](#apple-geytiny), [`addUpdateListAttribute:value:`](#apple-gy2damy), and [`addOrderByAttributeOrdering:`](#apple-gyzdqnq)

---

### assembleDeleteStatementWithQualifier:tableList:whereClause:

- (NSString \*)__assembleDeleteStatementWithQualifier:__ (EOQualifier \*)_qualifier___tableList:__ (NSString \*)_tableList___whereClause:__ (NSString \*)_whereClause_

Invoked from [`prepareDeleteExpressionForQualifier:`](#apple-gy3tkmi) to return an SQL DELETE statement of the form:

> ```
> DELETE FROM tableListSQL_WHERE whereClause
> ```

_qualifier_ is the argument to `prepareDeleteExpressionForQualifier:` from which _whereClause_ was derived. It is provided for subclasses that need to generate the WHERE clause in a particular way.

---

### assembleInsertStatementWithRow:tableList:columnList:valueList:

- (NSString \*)__assembleInsertStatementWithRow:__ (NSDictionary \*)_row___tableList:__ (NSString \*)_tableList___columnList:__ (NSString \*)_columnList___valueList:__ (NSString \*)_valueList_

Invoked from [`prepareInsertExpressionWithRow:`](#apple-gy3tqoa) to return an SQL INSERT statement of the form:

> ```
> INSERT INTO tableList (columnList)VALUES valueList
> ```

or, if _columnList_ is `nil`:

> ```
> INSERT INTO tableListVALUES valueList
> ```

_row_ is the argument to `prepareInsertExpressionWithRow:` from which _columnList_ and _valueList_ were derived. It is provided for subclasses that need to generate the list of columns and values in a particular way.

---

### assembleJoinClauseWithLeftName:rightName:joinSemantic:

- (NSString \*)__assembleJoinClauseWithLeftName:__ (NSString \*)_leftName___rightName:__ (NSString \*)_rightName___joinSemantic:__ (EOJoinSemantic)_semantic_

Returns a join clause of the form:

> ```
> leftName operator rightName
> ```

Where operator is "=" for an inner join, "\*=" for a left-outer join, and "=\*" for a right-outer join. Invoked from [`addJoinClause`](#apple-geytkmq).

---

### assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder: selectString:columnList:tableList:whereClause:joinClause: orderByClause:lockClause:

- (NSString \*)__assembleSelectStatementWithAttributes:__ (NSArray \*)_attributes___lock:__ (BOOL)_lock___qualifier:__ (EOQualifier \*)_qualifier___fetchOrder:__ (NSArray \*)_fetchOrder___selectString:__ (NSString \*)_selectString___columnList:__ (NSString \*)_columnList___tableList:__ (NSString \*)_tableList___whereClause:__ (NSString \*)_whereClause___joinClause:__ (NSString \*)_joinClause___orderByClause:__ (NSString \*)_orderByClause___lockClause:__ (NSString \*)_lockClause_

Invoked from [`prepareSelectExpressionWithAttributes:lock:fetchSpecification:`](#apple-gy4dgmi) to return an SQL SELECT statement of the form:

> ```
> SELECT columnListFROM tableList lockClause WHERE whereClause AND joinClause ORDER BY orderByClause
> ```

If _lockClause_ is `nil`, it is omitted from the statement. Similarly, if _orderByClause_ is `nil`, the "ORDER BY _orderByClause_" is omitted. If either _whereClause_ or _joinClause_ is `nil`, the "AND" and `nil`-valued argument are omitted. If both are `nil`, the entire WHERE clause is omitted.

_attributes_, _lock_, _qualifier_, and _fetchOrder_ are the arguments to `prepareSelectExpressionWithAttributes:lock:fetchSpecification:` from which the other `assembleSelect...` arguments were derived. They are provided for subclasses that need to generate the clauses of the SELECT statement in a particular way.

---

### assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:

- (NSString \*)__assembleUpdateStatementWithRow:__ (NSDictionary \*)_row___qualifier:__ (EOQualifier \*)_qualifier___tableList:__ (NSString \*)_tableList___updateList:__ (NSString \*)_updateList___whereClause:__ (NSString \*)_whereClause_

Invoked from [`prepareUpdateExpressionWithRow:qualifier:`](#apple-gy4dknq) to return an SQL UPDATE statement of the form:

> ```
> UPDATE tableListSET updateListWHERE whereClause
> ```

_row_ and _qualifier_ are the arguments to `prepareUpdateExpressionWithRow:qualifier:` from which _updateList_ and _whereClause_ were derived. They are provided for subclasses that need to generate the clauses of the UPDATE statement in a particular way.

---

### bindVariableDictionaries

- (NSArray \*)__bindVariableDictionaries__

Returns the receiver's bind variable dictionaries. For more information on bind variables, see the discussion in the class description.

__See also:__
[- `addBindVariableDictionary:`](#apple-gyytqnq)

---

### bindVariableDictionaryForAttribute:value:

- (NSMutableDictionary \*)__bindVariableDictionaryForAttribute:__ (EOAttribute \*)_attribute_ __value:__ (id)_value_

Implemented by subclasses to create and return the bind variable dictionary for _attribute_ and _value_. The dictionary returned from this method must contain at least the following key-value pairs:

| __Key__ | __Value__ |
| EOBindVariableNameKey | the name of the bind variable for _attribute_ |
| EOBindVariablePlaceHolderKey | the placeholder string used in the SQL statement |
| EOBindVariableAttributeKey | _attribute_ |
| EOBindVariableValueKey | _value_ |

```
```

An adaptor subclass may define additional entries as required by its RDBMS.

Invoked from [`sqlStringForValue:attributeNamed:`](#apple-g4ytsmy) when the message [`mustUseBindVariableForAttribute:`](#apple-gy3tgmi)_attribute_ returns YES or when the receiver's class uses bind variables and the message [`shouldUseBindVariableForAttribute:`](#apple-gy4tama)_attribute_ returns YES. For more information on bind variables, see the discussion in the class description.

A subclass that uses bind variables should implement this method without invoking EOSQLExpression's implementation. The subclass implementation must return a dictionary with entries for the keys listed above and may add additional keys.

__See also:__
[- `bindVariableDictionaryForAttribute:value:`](#apple-gy2tmoi), [+ `useBindVariables`](#apple-geytgoa)

---

### entity

- (EOEntity \*)__entity__

Returns the receiver's entity.

__See also:__
[- `initWithEntity:`](#apple-gi2dmojz)

---

### externalNameQuoteCharacter

- (NSString \*)`externalNameQuoteCharacter`

Returns the string `\"' (an escaped quote character) if the receiver uses quoted external names, or the empty string ("") otherwise.

__See also:__
[+ `useQuotedExternalNames`](#apple-ge2dena), [- `sqlStringForSchemaObjectName:`](#apple-g4ytgmi)

---

### initWithEntity:

- __initWithEntity:__ (EOEntity \*)_entity_

Initializes a new instance of EOSQLExpression with _entity_.

__See also:__
[- `entity`](#apple-gq3tomq)

---

### joinClauseString

- (NSMutableString \*)__joinClauseString__

Returns the part of the receiver's WHERE clause that specifies join conditions. Together, the `joinClauseString` and the `[whereClauseString](#apple-gqztmny)` make up a statement's WHERE clause. If the receiver's statement doesn't contain join conditions, this method returns an empty string.

An EOSQLExpression's `joinClauseString` is generally set by invoking [`joinExpression`](#apple-gq3tcmy).

__See also:__
[- `addJoinClause`](#apple-geytkmq)

---

### joinExpression

- (void)__joinExpression__

Builds up the `[joinClauseString](#apple-gy3dena)` for use in a SELECT statement. For each relationship path in the [`aliasesByRelationshipPath`](#apple-gyztqna) dictionary, this method invokes [`addJoinClause`](#apple-geytkmq) for each of the relationship's EOJoin objects.

If the `aliasesByRelationshipPath` dictionary only has one entry (the entry for the EOSQLExpression's entity), the `joinClauseString` is empty.

You must invoke this method _after_ invoking [`addSelectListAttribute:`](#apple-gyztema) for each attribute to be selected and after sending `sqlStringForSQLExpression:self` to the qualifier for the SELECT statement. (These methods build up the `aliasesByRelationshipPath` dictionary by invoking [`sqlStringForAttributePath:`](#apple-gy4toni).)

__See also:__
[- `whereClauseString`](#apple-gqztmny), __-__ `sqlStringForSQLExpression:` (EOQualifierSQLGeneration protocol)

---

### listString

- (NSMutableString \*)__listString__

Returns a comma-separated list of attributes or "attribute = value" assignments. `listString` is built up with successive invocations of [`addInsertListAttribute:value:`](#apple-geytiny), [`addSelectListAttribute:`](#apple-gyztema), or [`addUpdateListAttribute:value:`](#apple-gy2damy) for INSERT statements, SELECT statements, and UPDATE statements, respectively. The contents of `listString` vary according to the type of statement the receiver is building:

| __Type of Statement__ | __Sample listString Contents__ |
| INSERT | FIRST_NAME, LAST_NAME, EMPLOYEE_ID |
| UPDATE | FIRST_NAME = "Timothy", LAST_NAME = "Richardson" |
| SELECT | t0.FIRST_NAME, t0.LAST_NAME, t1.DEPARTMENT_NAME |

```
```


---

### lockClause

- (NSString \*)__lockClause__

Overridden by subclasses to return the SQL string used in a SELECT statement to lock selected rows. A concrete subclass of EOSQLExpression must override this method to return the string used by its adaptor's RDBMS.

---

### mustUseBindVariableForAttribute:

- (BOOL)__mustUseBindVariableForAttribute:__ (EOAttribute \*)_attribute_

Returns YES if the receiver must use bind variables for _attribute_, NO otherwise. EOSQLExpression's implementation returns NO. An SQL expression subclass that uses bind variables should override this method to return YES if the underlying RDBMS requires that bind variables be used for attributes with _attribute_'s external type.

__See also:__
[- `shouldUseBindVariableForAttribute:`](#apple-gy4tama), [- `bindVariableDictionaryForAttribute:value:`](#apple-gy2tmoi)

---

### orderByString

- (NSMutableString \*)__orderByString__

Returns the comma-separated list of "attribute direction" pairs ("LAST_NAME asc, FIRST_NAME asc", for example) for use in a SELECT statement.

__See also:__
[- `addOrderByAttributeOrdering:`](#apple-gyzdqnq)

---

### prepareDeleteExpressionForQualifier:

- (void)__prepareDeleteExpressionForQualifier:__ (EOQualifier \*)_qualifier_

Generates a DELETE statement by performing the following steps:

- Sends an `sqlStringForSQLExpression:self` message to _qualifier_ to generate the receiver's `[whereClauseString](#apple-gqztmny)`.
- Invokes [`tableListWithRootEntity:`](#apple-geydsojq) to get the table name for the FROM clause.
- Invokes [`assembleDeleteStatementWithQualifier:tableList:whereClause:`](#apple-gy2tanq).

__See also:__
[+ `deleteStatementWithQualifier:entity:`](#apple-geydsni)

---

### prepareInsertExpressionWithRow:

- (void)__prepareInsertExpressionWithRow:__ (NSDictionary \*)_row_

Generates an INSERT statement by performing the following steps:

- Invokes [`addInsertListAttribute:value:`](#apple-geytiny) for each entry in _row_ to prepare the comma-separated list of attributes and the corresponding list of values.
- Invokes [`tableListWithRootEntity:`](#apple-geydsojq) to get the table name.
- Invokes [`assembleInsertStatementWithRow:tableList:columnList:valueList:`](#apple-gy2teoa).

__See also:__
[+ `insertStatementForRow:entity:`](#apple-geytcmy)

---

### prepareSelectExpressionWithAttributes:lock:fetchSpecification:

- (void)__prepareSelectExpressionWithAttributes:__ (NSArray \*)_attributes___lock:__ (BOOL)_flag___fetchSpecification:__ (EOFetchSpecification \*)_fetchSpecification_

Generates a SELECT statement by performing the following steps:

- Invokes [`addSelectListAttribute:`](#apple-gyztema) for each entry in _attributes_ to prepare the comma-separated list of attributes.
- Sends an `sqlStringForSQLExpression:self` message to _fetchSpecification_'s qualifier to generate the receiver's [`whereClauseString`](#apple-gqztmny).
- Invokes [`addOrderByAttributeOrdering:`](#apple-gyzdqnq) for each EOAttributeOrdering object in _fetchSpecification_.First conjoins the qualifier in _fetchSpecification_ with the restricting qualifier, if any, of the receiver's entity.
- Invokes [`joinExpression`](#apple-gq3tcmy) to generate the receiver's [`joinClauseString`](#apple-gy3dena).
- Invokes [`tableListWithRootEntity:`](#apple-geydsojq) to get the comma-separated list of tables for the FROM clause.
- If _flag_ is YES, invokes [`lockClause`](#apple-gy3dqma) to get the SQL string to lock selected rows.
- Invokes [`assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder: selectString:columnList:tableList:whereClause:joinClause: orderByClause:lockClause:`](#apple-gy2tgny).

__See also:__
[+ `selectStatementForAttributes:lock:fetchSpecification:entity:`](#apple-geytcny)

---

### prepareUpdateExpressionWithRow:qualifier:

- (void)__prepareUpdateExpressionWithRow:__ (NSDictionary \*)_row_ __qualifier:__ (EOQualifier \*)_qualifier_

Generates an UPDATE statement by performing the following steps:

- Invokes [`addUpdateListAttribute:value:`](#apple-gy2damy) for each entry in _row_ to prepare the comma-separated list of "attribute = value" assignments.
- Sends an `sqlStringForSQLExpression:self` message to _qualifier_ to generate the receiver's `[whereClauseString](#apple-gqztmny)`.
- Invokes [`tableListWithRootEntity:`](#apple-geydsojq) to get the table name for the FROM clause.
- Invokes [`assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:`](#apple-gy2tkma).

__See also:__
[+ `updateStatementForRow:qualifier:entity:`](#apple-geytgmy)

---

### setStatement:

- (void)__setStatement:__ (NSString \*)_string_

Sets the receiver's SQL statement to _string_, which should be a valid expression in the target query language. Use this method-instead of a `prepare...` method-to directly assign an SQL string to an EOSQLExpression object. This method does not perform substitutions or formatting of any kind.

__See also:__
[+ `expressionForString:`](#apple-geydsoi), [- `statement`](#apple-gq2dcna)

---

### setUseAliases:

- (void)__setUseAliases:__ (BOOL)_flag_

Tells the receiver whether or not to use table aliases.

__See also:__
[- `useAliases`](#apple-gqztqni)

---

### shouldUseBindVariableForAttribute:

- (BOOL)__shouldUseBindVariableForAttribute:__ (EOAttribute \*)_attribute_

Returns YES if the receiver can provide a bind variable dictionary for _attribute_, NO otherwise. Bind variables aren't used for values associated with this attribute when the class method [`useBindVariables`](#apple-geytgoa) returns NO. EOSQLExpression's implementation returns NO. An SQL expression subclass should override this method to return YES if the receiver should use bind variables for attributes with _attribute_'s external type. It should also return YES for any attribute for which the receiver must use bind variables.

__See also:__
[- `mustUseBindVariableForAttribute:`](#apple-gy3tgmi)

---

### sqlStringForAttribute:

- (NSString \*)__sqlStringForAttribute:__ (EOAttribute \*)_attribute_

Returns the SQL string for _attribute_, complete with a table alias if the receiver uses table aliases. Invoked from [`sqlStringForAttributeNamed:`](#apple-gy4tmmq) when the attribute name is not a path.

__See also:__
[- `sqlStringForAttributePath:`](#apple-gy4toni)

---

### sqlStringForAttributeNamed:

- (NSString \*)__sqlStringForAttributeNamed:__ (NSString \*)_name_

Returns the SQL string for the attribute named _name_, complete with a table alias if the receiver uses table aliases. Generates the return value using [`sqlStringForAttributePath:`](#apple-gy4toni) if _name_ is an attribute path ("department.name", for example); otherwise, uses [`sqlStringForAttribute:`](#apple-gy4teni).

---

### sqlStringForAttributePath:

- (NSString \*)__sqlStringForAttributePath:__ (NSArray \*)_path_

Returns the SQL string for _path_, complete with a table alias if the receiver uses table aliases. Invoked from [`sqlStringForAttributeNamed:`](#apple-gy4tmmq) when the specified attribute name is a path ("department.location.officeNumber", for example). _path_ is an array of any number of EORelationship objects followed by an EOAttribute object. The EORelationship and EOAttribute objects each correspond to a component in path. For example, if the attribute name argument to `sqlStringForAttributeNamed:` is "department.location.officeNumber", _path_ is an array containing the following objects in the order listed:

- The EORelationship object in the receiver's entity named "department". (Assume the relationship's destination entity is named "Department".)
- The EORelationship object in the Department entity named "location". (Assume the relationship's destination entity is named "Location".)
- The EOAttribute object in the Location entity named "officeNumber".

Assuming that the receiver uses aliases and the alias for the Location table is t2, the SQL string for this sample attribute path is "t2.officeNumber".

If the receiver uses table aliases, this method has the side effect of adding a "relationship path"-"alias name" entry to the `aliasesByRelationship` dictionary.

__See also:__
[- `sqlStringForAttribute:`](#apple-gy4teni), [- `aliasesByRelationshipPath`](#apple-gyztqna)

---

### sqlStringForConjoinedQualifiers:

- (NSString \*)__sqlStringForConjoinedQualifiers:__ (NSArray \*)_qualifiers_

Creates and returns an SQL string that is the result of interposing the word "AND" between the SQL strings for the qualifiers in _qualifiers_. Generates an SQL string for each qualifier by sending [`sqlStringForSQLExpression:`](../Protocols/EOQualifierSQLGeneration.md#apple-g42a) messages to the qualifiers with `self` as the argument. If the SQL string for a qualifier contains only white space, it isn't included in the return value. The return value is enclosed in parentheses if the SQL strings for two or more qualifiers were ANDed together.

---

### sqlStringForDisjoinedQualifiers:

- (NSString \*)__sqlStringForDisjoinedQualifiers:__ (NSArray \*)_qualifiers_

Creates and returns an SQL string that is the result of interposing the word "OR" between the SQL strings for the qualifiers in _qualifiers_. Generates an SQL string for each qualifier by sending [`sqlStringForSQLExpression:`](../Protocols/EOQualifierSQLGeneration.md#apple-g42a) messages to the qualifiers with `self` as the argument. If the SQL string for a qualifier contains only white space, it isn't included in the return value. The return value is enclosed in parentheses if the SQL strings for two or more qualifiers were ORed together.

---

### sqlStringForKeyComparisonQualifier:

- (NSString \*)__sqlStringForKeyComparisonQualifier:__ (EOKeyComparisonQualifier \*)_qualifier_

Creates and returns an SQL string that is the result of interposing an operator between the SQL strings for the right and left keys in _qualifier_. Determines the SQL operator by invoking [`sqlStringForSelector:value:`](#apple-g4ytknq) with _qualifier_'s selector and `nil` for the value. Generates SQL strings for _qualifier_'s keys by invoking [`sqlStringForAttributeNamed:`](#apple-gy4tmmq) to get SQL strings. This method also formats the strings for the right and left keys using [`formatSQLString:format:`](#apple-geytamy) with the corresponding attributes' "read" formats.

---

### sqlStringForKeyValueQualifier:

- (NSString \*)__sqlStringForKeyValueQualifier:__ (EOKeyValueQualifier \*)_qualifier_

Creates and returns an SQL string that is the result of interposing an operator between the SQL strings for _qualifier_'s key and value. Determines the SQL operator by invoking [`sqlStringForSelector:value:`](#apple-g4ytknq) with _qualifier_'s selector and value. Generates an SQL string for _qualifier_'s key by invoking [`sqlStringForAttributeNamed:`](#apple-gy4tmmq) to get an SQL string and [`formatSQLString:format:`](#apple-geytamy) with the corresponding attribute's "read" format. Similarly, generates an SQL string for qualifier's value by invoking [`sqlStringForValue:attributeNamed:`](#apple-g4ytsmy) to get an SQL string and [`formatValue:forAttribute:`](#apple-geytcma) to format it. (First invokes [`sqlPatternFromShellPattern:`](#apple-ge2dgny) for the value if _qualifier_'s selector is `isLike:`.)

---

### sqlStringForNegatedQualifier:

- (NSString \*)__sqlStringForNegatedQualifier:__ (EOQualifier \*)_qualifier_

Creates and returns an SQL string that is the result of surrounding the SQL string for _qualifier_ in parentheses and appending it to the word "not". For example, if the string for _qualifier_ is "FIRST_NAME = `John'", `sqlStringForNegatedQualifier:` returns the string "not (FIRST_NAME = `John')".

Generates an SQL string for _qualifier_ by sending an [`sqlStringForSQLExpression:`](../Protocols/EOQualifierSQLGeneration.md#apple-g42a)`:` message to _qualifier_ with `self` as the argument. If the SQL string for _qualifier_ contains only white space, this method returns `nil`.

---

### sqlStringForSchemaObjectName:

- (NSString \*)`sqlStringForSchemaObjectName:`(NSString \*)_name_

Returns _name_ enclosed in the external name quote character if the receiver uses quoted external names, otherwise simply returns _name_ unaltered.

__See also:__
[+ `useQuotedExternalNames`](#apple-ge2dena), [- `externalNameQuoteCharacter`](#apple-gq3tgma)

---

### sqlStringForSelector:value:

- (NSString \*)__sqlStringForSelector:__ (SEL)_selector_ __value:__ (id)_value_

Returns an SQL operator for _selector_ and _value_. The following table summarizes EOSQLExpression's default mapping:

| __Selector__ | __SQL Operator__ |
| isEqualTo: | "is" if value is an EONull, "=" otherwise |
| isNotEqualTo: | "is not" if _value_ is an EONull, "<> otherwise |
| isLessThan: | "<" |
| isGreaterThan: | ">" |
| isLessThanOrEqualTo: | "<=" |
| isGreaterThanOrEqualTo: | ">=" |
| isLike: | "like" |

```
```

Raises an NSInternalInconsistencyException if selector is an unknown operator.

__See also:__
[- `sqlStringForKeyComparisonQualifier:`](#apple-geydqobq), [- `sqlStringForKeyValueQualifier:`](#apple-g4ydmmq)

---

### sqlStringForValue:attributeNamed:

- (NSString \*)__sqlStringForValue:__ (id)_value_ __attributeNamed:__ (NSString \*)_name_

Returns a string for _value_ appropriate for use in an SQL statement. If the receiver uses a bind variable for the attribute named _name_, then `sqlStringForValue:attributeNamed:` gets the bind variable dictionary for the attribute, adds it to the receiver's array of bind variables dictionaries, and returns the value for the binding's EOBindVariablePlaceHolderKey. Otherwise, this method invokes [`formatValue:forAttribute:`](#apple-geytcma) and returns the formatted string for _value_.

__See also:__
[- `mustUseBindVariableForAttribute:`](#apple-gy3tgmi), [- `shouldUseBindVariableForAttribute:`](#apple-gy4tama),
[+ `useBindVariables`](#apple-geytgoa), [- `bindVariableDictionaries`](#apple-gq3tsna), [- `addBindVariableDictionary:`](#apple-gyytqnq)

---

### statement

- (NSString \*)__statement__

Returns the complete SQL statement for the receiver. An SQL statement can be assigned to an EOSQLExpression object directly using the class method [`expressionForString:`](#apple-geydsoi) or using the instance method [`setStatement:`](#apple-gy4dooa). Generally, however, an EOSQLExpression's statement is built up using one of the following methods:

- [- prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-gy4dgmi)
- [- prepareInsertExpressionWithRow:](#apple-gy3tqoa)
- [- prepareUpdateExpressionWithRow:qualifier:](#apple-gy4dknq)
- [- prepareDeleteExpressionForQualifier:](#apple-gy3tkmi)

---

### tableListWithRootEntity:

- (NSString \*)__tableListWithRootEntity:__ (EOEntity \*)_entity_

Returns the comma-separated list of tables for use in a SELECT, UPDATE, or DELETE statement's FROM clause. If the receiver doesn't use table aliases, the table list consists only of the table name for _entity_-"EMPLOYEE", for example. If the receiver does use table aliases (only in SELECT statements by default), the table list is a comma separated list of table names and their aliases, for example:

> ```
> EMPLOYEE t0, DEPARTMENT t1
> ```

`tableListWithRootEntity:` creates a string containing the table name for _entity_ and a corresponding table alias ("EMPLOYEE t0", for example). For each entry in [`aliasesByRelationshipPath`](#apple-gyztqna), this method appends a new table name and table alias.

__See also:__
[- `useAliases`](#apple-gqztqni), [- `aliasesByRelationshipPath`](#apple-gyztqna)

---

### useAliases

- (BOOL)__useAliases__

Returns YES if the receiver generates statements with table aliases, NO otherwise. For example, the following SELECT statement uses table aliases:

> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAMEFROM EMPLOYEE t0, DEPARTMENT t1WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The EMPLOYEE table has the alias t0, and the DEPARTMENT table has the alias t1.

By default, EOSQLExpression uses table aliases only in SELECT statements. Enterprise Objects Framework assumes that INSERT, UPDATE, and DELETE statements are single-table operations. For more information, see the discussion in the class description.

__See also:__
[- `setUseAliases:`](#apple-gy4dsmi), [- `aliasesByRelationshipPath`](#apple-gyztqna)

---

### valueList

- (NSMutableString \*)__valueList__

Returns the comma-separated list of values used in an INSERT statement. For example, the value list for the following INSERT statement:

> ```
> INSERT EMPLOYEE (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, DEPARTMENT_ID, SALARY)VALUES ('Shaun', 'Hayes', 1319, 23, 4600)
> ```

is "`Shaun', `Hayes', 1319, 23, 4600". An EOSQLExpression's `valueList` is generated a value at a time with [`addInsertListAttribute:value:`](#apple-geytiny) messages.

---

### whereClauseString

- (NSString \*)__whereClauseString__

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

An EOSQLExpression's `whereClauseString` is generally set by sending a [`sqlStringForSQLExpression:`](../Protocols/EOQualifierSQLGeneration.md#apple-g42a) message to an EOQualifier object.

__See also:__
[- `sqlStringForSQLExpression:`](../Protocols/EOQualifierSQLGeneration.md#apple-g42a) (EOQualifierSQLGeneration protocol)

---

[!](Creating%20Relationships-3.md)
[!](More%20about%20EOSQLExpression.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights
reserved._
