---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOSchemaGeneration.html
archived_at: '2026-07-15T08:13:41.743285Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOSchemaGeneration

> Implemented by:: EOSynchronizationFactory

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

This interface has been introduced to define API for generating database schemas from model files. None of the API is new. Rather, it was moved to EOSchemaGeneration from EOSQLExpression. The API is essentially the same except that in 4.5, the methods were static methods. In 5.0 the methods on EOSchemaGeneration are instance methods.

An implementation of the EOSchemaGeneration API is provided by the class, EOSynchronizationFactory, which is new in 5.0. For more information, see the sections for EOSQLExpression and EOSynchronizationFactory.

## Constants

---

EOSchemeGeneration defines the following String constants.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| CreateTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create tables. |
| DropTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop tables. |
| CreatePrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key support. |
| DropPrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop primary key support. |
| PrimaryKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key constraints. |
| ForeignKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create foreign key constraints. |
| CreateDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create a database. |
| DropDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop a database. |

## Method Types

---

> **Creating a schema generation script**
> : [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjwg4tjob2em33sivxhi2lunfsxg): [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq): [appendExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwc4dqmvxgirlyobzgk43tnfxw4): [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya): [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg): [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq): [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom): [primaryKeyConstraintStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33voa): [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq): [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa): [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y): [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya): [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg): [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwm33smvuwo3slmv4ug33oon2heyljnz2fg5dborsw2zloorzum33skjswyylunfxw443infya): [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkrdborqweyltmvjxiylumvwwk3tuondg64sdn5xg4zldoruw63senfrxi2lpnzqxe6i): [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobcgc5dbmjqxgzktorqxizlnmvxhi42gn5zeg33onzswg5djn5xei2ldoruw63tboj4q)

## Instance Methods

---

### appendExpression

`public abstract void appendExpressionToScript( EOSQLExpression anSQLExpression, StringBuffer script)`

Append's _anSQLExpression_'s statement to _script_ along with any necessary delimiter. EOSQLExpression's implementation appends the SQL statement for _anSQLExpression_ to _script_ followed by a semicolon and a newline. A subclass of EOSQLExpression only needs to override this method if the delimiter for its database server is different. For example, the Oracle and Informix use the default implementation, whereas the Sybase adaptor appends the word "go" instead of a semicolon.

__See Also:__ [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)

---

### createDatabaseStatementsForConnectionDictionary

`public abstract NSArray createDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

Generates the SQL statements that will create a database (or user, for Oracle) that can be accessed by the provided connection dictionary and administrative connection dictionary.

__See Also:__ [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobcgc5dbmjqxgzktorqxizlnmvxhi42gn5zeg33onzswg5djn5xei2ldoruw63tboj4q)

---

### createTableStatementsForEntityGroup

`public abstract NSArray createTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create a table for _entityGroup_, an array of EOEntity objects that have the same externalName. Returns an empty array if _entityGroup_ is `null` or empty.

EOSQLExpression's implementation does the following:

1. Creates an EOSQLExpression object.
2. Sets the expression's entity to the first entity in _entityGroup_.
3. Adds a create clause for each Attribute in _entityGroup_'s Entities.
4. Sets the expression's statement to CREATE TABLE _TABLE_NAME_ (_LIST_STRING_), where _TABLE_NAME_ is the __externalName__ of the Entity objects in _entityGroup_ and _LIST_STRING_ is the expression's listString.
5. Adds the expression to an array.
6. Returns the array.

The following is an example of a CREATE TABLE statement produced by the default implementation:

> ```
> create table EMPLOYEE (
>     EMP_ID      int not null,
>     DEPT_ID     int null,
>     LAST_NAME   varchar(40) not null,
>     PHONE       char(12) null,
>     HIRE_DATE   date null,
>     SALARY      number(7, 2) null
> )
> ```

If a subclass's database server's table creation semantics are different, the subclass should override this method or one or more of the following methods as appropriate:

- addCreateClauseForAttribute
- columnTypeStringForAttribute
- allowsNullClauseForConstraint

__See Also:__ [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya), [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq)

---

### createTableStatementsForEntityGroups

`public abstract NSArray createTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the tables specified in _entityGroups_. An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. Returns an empty array if _entityGroups_ is `null` or empty. EOSQLExpression's implementation invokes [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### dropDatabaseStatementsForConnectionDictionary

`public abstract NSArray dropDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

Generates the SQL statements to drop a database (or user, for Oracle).

__See Also:__ [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkrdborqweyltmvjxiylumvwwk3tuondg64sdn5xg4zldoruw63senfrxi2lpnzqxe6i)

---

### dropPrimaryKeySupportStatementsForEntityGroup

`public abstract NSArray dropPrimaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for _entityGroup_, an array of Entity objects that have the same __externalName__. The drop statement generated by this method should be sufficient to remove the primary key support created by [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> drop sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the primaryKeyRootName for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

---

### dropPrimaryKeySupportStatementsForEntityGroups

`public abstract NSArray dropPrimaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for the entities specified in _entityGroups_. An entity group is an array of EOEntity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### dropTableStatementsForEntityGroup

`public abstract NSArray dropTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the table identified by _entityGroup_, an array of Entity objects that have the same __externalName__. The drop statement generated by this method should be sufficient to remove the table created by [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> DROP TABLE TABLE_NAME
> ```

Where _TABLE_NAME_ is the __externalName__ of the first entity in _entityGroup_.

If a subclass's database server's drop semantics are different, the subclass should override this method.

---

### dropTableStatementsForEntityGroups

`public abstract NSArray dropTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the tables for _entityGroups_. An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### foreignKeyConstraintStatementsForRelationship

`public abstract NSArray foreignKeyConstraintStatementsForRelationship(EORelationship aRelationship)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create foreign key constraints for _aRelationship_. EOSQLExpression's implementation generates statements such as the following:
> ```
> ALTER TABLE EMPLOYEE ADD CONSTRAINT TO_DEPARTMENT FOREIGN KEY (DEPT_ID)
>         REFERENCES DEPARTMENT(DEPT_ID)
> ```

It returns an empty array if either of the following are true:

- _aRelationship_ spans models (if _aRelationship_'s destinationEntity is in a different model than _aRelationship_'s source entity)
- _aRelationship_ is a to-many relationship, or if the inverse relationship of _aRelationship_ is not a to-many. In other words, foreign key constraint statements are only created for to-one relationships whose inverse is a to-many.

If a subclass's database server's foreign key constraint semantics are different, the subclass should override this method or override the method __prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:__.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### primaryKeyConstraintStatementsForEntityGroup

`public abstract NSArray primaryKeyConstraintStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for _entityGroup_, an array of EOEntity objects that have the same externalName. Returns an empty array if any of the primary key attributes in _entityGroup_ don't have a columnName.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> ALTER TABLE TABLE_NAME ADD PRIMARY KEY (PRIMARY_KEY_COLUMN_NAMES)
> ```

Where _TABLE_NAME_ is the externalName for the first entity in _entityGroup_ and _PRIMARY_KEY_COLUMN_NAMES_ is a comma-separated list of the columnNames of the first entity's primaryKeyAttributes.

If the subclass's database server's primary key constraint semantics are different, the subclass should override this method.

---

### primaryKeyConstraintStatementsForEntityGroups

`public abstract NSArray primaryKeyConstraintStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same externalName, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

---

### primaryKeySupportStatementsForEntityGroup

`public abstract NSArray primaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for _entityGroup_, an array of EOEntity objects that have the same externalName. EOSQLExpression's implementation creates a statement of the following form:
> ```
> create sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the primaryKeyRootName for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

__See Also:__ [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya), primaryKeyForNewRowWithEntity (EOAdaptorChannel)

---

### primaryKeySupportStatementsForEntityGroups

`public abstract NSArray primaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same externalName, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

---

### schemaCreationScriptForEntities

`public abstract String schemaCreationScriptForEntities( NSArray entities, NSDictionary options)`

Returns a script of SQL statements suitable to create the schema for the EOEntity objects in _entities_. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306). EOSQLExpression's implementation invokes __schemaCreationStatementsForEntities__ with _entities_ and _options_ and then uses [appendExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwc4dqmvxgirlyobzgk43tnfxw4) to generate the script from the EOSQLExpressions generated by __schemaCreationStatementsForEntities__.

---

### schemaCreationStatementsForEntities

`public abstract NSArray schemaCreationStatementsForEntities( NSArray entities, NSDictionary options)`

Returns an array of EOSQLExpressions suitable to create the schema for the Entity objects in _entities_. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

EOSQLExpression's implementation uses the following methods:

- [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
- [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom)
- [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y)
- [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
- [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq)
- [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxwm33smvuwo3slmv4ug33oon2heyljnz2fg5dborsw2zloorzum33skjswyylunfxw443infya)

to generate EOSQLExpressions for the support identified in _options_.

__See Also:__ [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfdwk3tfojqxi2lpnyxxgy3imvwwcq3smvqxi2lpnzjwg4tjob2em33sivxhi2lunfsxg)

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
