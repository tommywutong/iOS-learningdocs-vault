---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOSchemaSynchronization.html
archived_at: '2026-07-15T08:13:41.766957Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOSchemaSynchronization

> Implemented by: EOSynchronizationFactory

> __Package:__ com.webobjects.eoaccess

---

## Interface Description

---

EOSQLExpression is an abstract superclass that defines how to build SQL statements for adaptor channels. You don't typically use instances of EOSQLExpression; rather, you use EOSQLExpression subclasses written to work with a particular RDBMS and corresponding adaptor. A concrete subclass of EOSQLExpression overrides many of its methods in terms of the query language syntax for its specific RDBMS. EOSQLExpression objects are used internally by the Framework, and unless you're creating a concrete adaptor, you won't ordinarily need to interact with EOSQLExpression objects yourself. You most commonly create and use an EOSQLExpression object when you want to send an SQL statement directly to the server. In this case, you simply create an expression with EOSQLExpression and send the expression object to an adaptor channel using EOAdaptorChannel's evaluateExpression method.

For more information on using EOSQLExpressions, see the following sections:

- ["Building Expressions" (page 303)](EOSQLExpression.Concepts.md#apple-ijduoq2ki5ceu)
- ["Using Table Aliases" (page 304)](EOSQLExpression.Concepts.md#apple-ijduoqscincec)
- ["Bind Variables" (page 305)](EOSQLExpression.Concepts.md#apple-ijduoq2bi5eei)
- ["Schema Generation" (page 305)](EOSQLExpression.Concepts.md#apple-ijduoq2cijbue)

## Constants

---

EOSQLExpression defines the following String constants.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| SchemaSynchronizationPrimary KeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key support. |
| SchemaSynchronizationPrimary KeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key constraints. |
| SchemaSynchronizationPrimary KeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create foreign key constraints. |
| AllowsNullKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ColumnNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ExternalNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ExternalTypeKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| NameKey | Key for use in change dictionaries. A corresponding value indicates the old value of the table or column. |
| PrecisionKey | Key for use in change dictionaries. A corresponding value indicates the value a column's precision should be changed from. |
| RelationshipsKey | Key for use in change dictionaries. The corresponding value is a dictionary of relationships which have been modified since the last time the model and schema were sychronized. For more information see "The Change Dictionary" (page 306). |
| ScaleKey | Key for use in change dictionaries. A corresponding value indicates the value the column's scale should be changed from. |
| WidthKey | Key for use in change dictionaries. A corresponding value indicates the value the column's width should be changed from. |

## Method Types

---

> Synchronizing the database with a model[statementsToUpdateObjectStoreForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64snn5sgk3a)[statementsToUpdateObjectStoreForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64sfnz2gs5dzi5zg65lqom)[statementsToCopyTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32dn5yhsvdbmjwgkttbnvswi)[phraseCastingColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxa2dsmfzwkq3bon2gs3thinxwy5lnnzhgc3lfmq)[statementsToRenameTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32smvxgc3lfkrqwe3dfjzqw2zle)[statementsToInsertColumnForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32jnzzwk4tuinxwy5lnnzdg64sbor2he2lcov2gk)[statementsToDeleteColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32emvwgk5dfinxwy5lnnzhgc3lfmq)[statementsToRenameColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32smvxgc3lfinxwy5lnnzhgc3lfmq)[statementsToModifyColumnNullRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32nn5sgsztzinxwy5lnnzhhk3dmkj2wyzi)[statementsToConvertColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32dn5xhmzlsorbw63dvnvxfi6lqmu)[isColumnTypeEquivalentToColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxws42dn5whk3lokr4xazkfof2ws5tbnrsw45cun5bw63dvnvxfi6lqmu)[statementsToDropForeignKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32eojxxartpojswsz3ojnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovyhg)[statementsToDropPrimaryKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32eojxxaudsnfwwc4tzjnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovyhg)[statementsToDropPrimaryKeySupportForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32eojxxaudsnfwwc4tzjnsxsu3vobyg64tuizxxerlooruxi6khojxxk4dt)[statementsToImplementForeignKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhirtpojswsz3ojnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovyhg)[statementsToImplementPrimaryKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhiudsnfwwc4tzjnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovyhg)[statementsToImplementPrimaryKeySupportForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhiudsnfwwc4tzjnsxsu3vobyg64tuizxxerlooruxi6khojxxk4dt)Querying about database synchronization supportw[supportsSchemaSynchronization](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpny)[supportsDirectColumnCoercion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxeg33fojrws33o)[supportsDirectColumnDeletion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxeizlmmv2gs33o)[supportsDirectColumnInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxes3ttmvzhi2lpny)[supportsDirectColumnNullRuleModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxe45lmnrjhk3dfjvxwi2lgnfrwc5djn5xa)[supportsDirectColumnRenaming](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxfezlomfwws3th)

## Instance Methods

---

### isColumnTypeEquivalentToColumnType

`public abstract boolean isColumnTypeEquivalentToColumnType( EOSchemaSynchronization.ColumnTypes columnTypeA, EOSchemaSynchronization.ColumnTypes columnTypeB, NSDictionary options)`

Returns `true` if values in a column of _columnTypeA_ can be copied into a column of _columnTypeB_ without the use of a casting phrase, `false` otherwise. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### objectStoreChangesFromAttribute

`public abstract NSDictionary objectStoreChangesFromAttributeToAttribute( EOAttribute anAttribute, EOAttribute anotherAttribute`

Description forthcoming.

---

### phraseCastingColumnNamed

`public abstract String phraseCastingColumnNamed( String columnName, EOSchemaSynchronization.ColumnTypes fromType, EOSchemaSynchronization.ColumnTypes castType NSDictionary options)`

Returns an SQL string to cast the values in the column specified by _columnName_ to a new type. This method is used when the adaptor doesn't support in-place column type coercion, and the table has to be recreated. To move data from the old table to the new table, sometimes a conversion statement is needed (for example, to convert strings in a VARCHAR column to numbers). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToConvertColumnType

`public abstract NSArray statementsToConvertColumnType( String columnName, String tableName, EOSchemaSynchronization.ColumnTypes type, EOSchemaSynchronization.ColumnTypes newType, NSDictionary options)`

Returns an array of EOSQLExpressions to convert in place the type of the specified column. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToCopyTableNamed

`public abstract NSArray statementsToCopyTableNamed( String tableName, NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to copy the specified table into a new table, whose definition is provided by _entityGroup_-an array of EOEntity objects rooted to the table named _tableName_. This method is used when the adaptor doesn't support the in-place table modifications required to synchronize the database to a model.

The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDeleteColumnNamed

`public abstract NSArray statementsToDeleteColumnNamed( String columnName, String tableName, NSDictionary options)`

Returns an array of EOSQLExpressions to delete in place the specified column from the specified table. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropForeignKeyConstraintsOnEntityGroups

`public abstract NSArray statementsToDropForeignKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop foreign key constraints for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropPrimaryKeyConstraintsOnEntityGroups

`public abstract NSArray statementsToDropPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop primary key constraints for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropPrimaryKeySupportForEntityGroups

`public abstract NSArray statementsToDropPrimaryKeySupportForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop the primary key support mechanism for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementForeignKeyConstraintsOnEntityGroups

`public abstract NSArray statementsToImplementForeignKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement foreign key constraints on the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementPrimaryKeyConstraintsOnEntityGroups

`public abstract NSArray statementsToImplementPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement primary key constraints on the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementPrimaryKeySupportForEntityGroups

`public abstract NSArray statementsToImplementPrimaryKeySupportForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement support mechanisms for primary key generation for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToInsertColumnForAttribute

`public abstract NSArray statementsToInsertColumnForAttribute( EOAttribute attribute, NSDictionary options)`

Returns an array of EOSQLExpressions to insert in place a column for the specified attribute. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToModifyColumnNullRule

`public abstract NSArray statementsToModifyColumnNullRule( String columnName, String tableName, boolean allowsNull, NSDictionary options)`

Returns an array of EOSQLExpressions to modify in place the specified column to either allow or not allow NULL values as specified by _allowsNull_. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToRenameColumnNamed

`public abstract NSArray statementsToRenameColumnNamed( String columnName, String tableName, String newName, NSDictionary options)`

Returns an array of EOSQLExpressions to rename in place the specified column. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToRenameTableNamed

`public abstract NSArray statementsToRenameTableNamed( String tableName, String newName, NSDictionary options)`

Returns an array of EOSQLExpressions to rename in place the specified table. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToUpdateObjectStoreForEntityGroups

`public abstract NSArray statementsToUpdateObjectStoreForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to update the table that corresponds to _entityGroup_-an array of EOEntity objects rooted to the same table. Inserts and deletes columns, and updates modified columns. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToUpdateObjectStoreForModel

`public abstract NSArray statementsToUpdateObjectStoreForModel( EOModel model, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to synchronize the database with _model_. Prepares the statements to insert and delete new and deleted tables before invoking [statementsToUpdateObjectStoreForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3tumzws6rkpknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64sfnz2gs5dzi5zg65lqom) for each modified table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### supportsDirectColumnCoercion

`public abstract boolean supportsDirectColumnCoercion()`

Returns `true` if the adaptor can change the type of an existing column in place, `false` otherwise.

---

### supportsDirectColumnDeletion

`public abstract boolean supportsDirectColumnDeletion()`

Returns `true` if the adaptor can delete columns, `false` otherwise.

---

### supportsDirectColumnInsertion

`public abstract boolean supportsDirectColumnInsertion()`

Returns `true` if the adaptor can add columns to a table, `false` otherwise.

---

### supportsDirectColumnNullRuleModification

`public abstract boolean supportsDirectColumnNullRuleModification()`

Returns `true` if the adaptor can modify the null rule of an existing column in place, `false` otherwise.

---

### supportsDirectColumnRenaming

`public abstract boolean supportsDirectColumnRenaming()`

Returns `true` if the adaptor can rename table columns, `false` otherwise.

---

### supportsSchemaSynchronization

`public abstract boolean supportsSchemaSynchronization()`

Returns `true` if the adaptor can update the database to reflect changes in a model, `false` otherwise.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
