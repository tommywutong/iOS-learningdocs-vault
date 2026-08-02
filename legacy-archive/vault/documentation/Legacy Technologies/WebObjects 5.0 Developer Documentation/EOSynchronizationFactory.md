---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOSynchronizationFactory.html
archived_at: '2026-07-15T08:13:41.810618Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOSynchronizationFactory

> **__Inherits from:__**
> : Object

> **__Implements:__**
> : EOSchemaGeneration,: EOSchemaSynchronization

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

This class has been introduced to implement the new interfaces, EOSchemaGeneration and EOSchemaSynchronization. The methods used to be declared and implemented in EOSQLExpression. The 5.0 API is essentially the same. The only difference is that in 4.5 the methods were methods. In 5.0 the methods are instance methods. See the EOSchemaGeneration and EOSchemaSynchronization sections for more information.

## Method Types

---

> **Constructors**
> : [EOSynchronizationFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4q)
>
> **Creating a schema generation script**
> : [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfgy3snfyhirtpojcw45djoruwk4y): [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfg5dborsw2zloorzum33sivxhi2lunfsxg): [appendExpressionToScript](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6ylqobsw4zcfpbyhezltonuw63sun5jwg4tjob2a): [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa): [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y): [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfiylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa): [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfiylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq): [primaryKeyConstraintStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsq3pnzzxi4tbnfxhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya): [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsq3pnzzxi4tbnfxhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg): [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4a): [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4dt): [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa): [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y): [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6ztpojswsz3ojnsxsq3pnzzxi4tbnfxhiu3umf2gk3lfnz2hgrtpojjgk3dboruw63ttnbuxa): [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkemf2gcytbonsvg5dborsw2zloorzum33sinxw43tfmn2gs33oiruwg5djn5xgc4tz): [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yeiylumfrgc43fkn2gc5dfnvsw45dtizxxeq3pnzxgky3unfxw4rdjmn2gs33omfzhs)
>
> **Synchronizing the database with a model**
> : [statementsToUpdateObjectStoreForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpkvygiylumvhwe2tfmn2fg5dpojsum33sjvxwizlm): [statementsToUpdateObjectStoreForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpkvygiylumvhwe2tfmn2fg5dpojsum33sivxhi2lupfdxe33vobzq): [statementsToCopyTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpinxxa6kumfrgyzkomfwwkza): [phraseCastingColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64diojqxgzkdmfzxi2lom5bw63dvnvxe4ylnmvsa): [statementsToRenameTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpkjsw4ylnmvkgcytmmvhgc3lfmq): [statementsToInsertColumnForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpjfxhgzlsorbw63dvnvxem33sif2hi4tjmj2xizi): [statementsToDeleteColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpirswyzlumvbw63dvnvxe4ylnmvsa): [statementsToRenameColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpkjsw4ylnmvbw63dvnvxe4ylnmvsa): [statementsToConvertColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpinxw45tfoj2eg33movww4vdzobsq): [isColumnTypeEquivalentToColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s62ltinxwy5lnnzkhs4dfivyxk2lwmfwgk3tukrxug33movww4vdzobsq): [statementsToDropForeignKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpirzg64cgn5zgk2lhnzfwk6kdn5xhg5dsmfuw45dtj5xek3tunf2hsr3sn52xa4y): [statementsToDropPrimaryKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpirzg64cqojuw2ylspffwk6kdn5xhg5dsmfuw45dtj5xek3tunf2hsr3sn52xa4y): [statementsToDropPrimaryKeySupportForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpirzg64cqojuw2ylspffwk6ktovyha33sordg64sfnz2gs5dzi5zg65lqom): [statementsToImplementForeignKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpjfwxa3dfnvsw45cgn5zgk2lhnzfwk6kdn5xhg5dsmfuw45dtj5xek3tunf2hsr3sn52xa4y): [statementsToImplementPrimaryKeyConstraintsOnEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpjfwxa3dfnvsw45cqojuw2ylspffwk6kdn5xhg5dsmfuw45dtj5xek3tunf2hsr3sn52xa4y): [statementsToImplementPrimaryKeySupportForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpjfwxa3dfnvsw45cqojuw2ylspffwk6ktovyha33sordg64sfnz2gs5dzi5zg65lqom)
>
> **Querying about database synchronization support**
> : [supportsSchemaSynchronization](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuonjwg2dfnvqvg6lomnuhe33onf5gc5djn5xa): [supportsDirectColumnCoercion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuoncgs4tfmn2eg33movww4q3pmvzgg2lpny): [supportsDirectColumnDeletion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuoncgs4tfmn2eg33movww4rdfnrsxi2lpny): [supportsDirectColumnInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuoncgs4tfmn2eg33movww4sloonsxe5djn5xa): [supportsDirectColumnNullRuleModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuoncgs4tfmn2eg33movww4ttvnrwfe5lmmvgw6zdjmzuwgylunfxw4): [supportsDirectColumnRenaming](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643vobyg64tuoncgs4tfmn2eg33movww4utfnzqw22lom4)

## Constructors

---

### EOSynchronizationFactory

`public EOSynchronizationFactory(EOAdaptor adaptor)`

Description forthcoming.

---

## Instance Methods

---

### appendExpressionToScript

`public void appendExpressionToScript( EOSQLExpression anSQLExpression, StringBuffer script)`

Append's _anSQLExpression_'s statement to _script_ along with any necessary delimiter. EOSQLExpression's implementation appends the SQL statement for _anSQLExpression_ to _script_ followed by a semicolon and a newline. A subclass of EOSQLExpression only needs to override this method if the delimiter for its database server is different. For example, the Oracle and Informix use the default implementation, whereas the Sybase adaptor appends the word "go" instead of a semicolon.

__See Also:__ [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa)

---

### createDatabaseStatementsForConnectionDictionary

`public NSArray createDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

Generates the SQL statements that will create a database (or user, for Oracle) that can be accessed by the provided connection dictionary and administrative connection dictionary.

__See Also:__ [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yeiylumfrgc43fkn2gc5dfnvsw45dtizxxeq3pnzxgky3unfxw4rdjmn2gs33omfzhs)

---

### createTableStatementsForEntityGroup

`public NSArray createTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create a table for _entityGroup_, an array of EOEntity objects that have the same externalName. Returns an empty array if _entityGroup_ is null or empty.

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

__See Also:__ [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa), [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfiylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa)

---

### createTableStatementsForEntityGroups

`public NSArray createTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the tables specified in _entityGroups_. An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. Returns an empty array if _entityGroups_ is `null` or empty. EOSQLExpression's implementation invokes [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfg5dborsw2zloorzum33sivxhi2lunfsxg)

---

### dropDatabaseStatementsForConnectionDictionary

`public NSArray dropDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

Generates the SQL statements to drop a database (or user, for Oracle).

__See Also:__ [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkemf2gcytbonsvg5dborsw2zloorzum33sinxw43tfmn2gs33oiruwg5djn5xgc4tz)

---

### dropPrimaryKeySupportStatementsForEntityGroup

`public NSArray dropPrimaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for _entityGroup_, an array of Entity objects that have the same __externalName__. The drop statement generated by this method should be sufficient to remove the primary key support created by [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4a)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> drop sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the primaryKeyRootName for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

---

### dropPrimaryKeySupportStatementsForEntityGroups

`public NSArray dropPrimaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the primary key generation support for the entities specified in _entityGroups_. An entity group is an array of EOEntity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfg5dborsw2zloorzum33sivxhi2lunfsxg)

---

### dropTableStatementsForEntityGroup

`public NSArray dropTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the table identified by _entityGroup_, an array of Entity objects that have the same __externalName__. The drop statement generated by this method should be sufficient to remove the table created by [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa)'s statements.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> DROP TABLE TABLE_NAME
> ```

Where _TABLE_NAME_ is the __externalName__ of the first entity in _entityGroup_.

If a subclass's database server's drop semantics are different, the subclass should override this method.

---

### dropTableStatementsForEntityGroups

`public NSArray dropTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to drop the tables for _entityGroups_. An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfiylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfg5dborsw2zloorzum33sivxhi2lunfsxg)

---

### foreignKeyConstraintStatementsForRelationship

`public NSArray foreignKeyConstraintStatementsForRelationship(EORelationship aRelationship)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create foreign key constraints for _aRelationship_. EOSQLExpression's implementation generates statements such as the following:
> ```
> ALTER TABLE EMPLOYEE ADD CONSTRAINT TO_DEPARTMENT FOREIGN KEY (DEPT_ID)
>         REFERENCES DEPARTMENT(DEPT_ID)
> ```

It returns an empty array if either of the following are true:

- _aRelationship_ spans models (if _aRelationship_'s destinationEntity is in a different model than _aRelationship_'s source entity)
- _aRelationship_ is a to-many relationship, or if the inverse relationship of _aRelationship_ is not a to-many. In other words, foreign key constraint statements are only created for to-one relationships whose inverse is a to-many.

If a subclass's database server's foreign key constraint semantics are different, the subclass should override this method or override the method __prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:__.

__See Also:__ [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfg5dborsw2zloorzum33sivxhi2lunfsxg)

---

### __isCaseSensitive__

`public boolean isCaseSensitive()`

Description forthcoming.

---

### isColumnTypeEquivalentToColumnType

`public boolean isColumnTypeEquivalentToColumnType( EOSchemaSynchronization.ColumnTypes columnTypeA, EOSchemaSynchronization.ColumnTypes columnTypeB, NSDictionary options)`

Returns `true` if values in a column of _columnTypeA_ can be copied into a column of _columnTypeB_ without the use of a casting phrase, `false` otherwise. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### __logicalErrorsInChangeDictionaryForModelOptions__

`public NSArray logicalErrorsInChangeDictionaryForModelOptions( NSDictionary, EOModel, NSDictionary)`

Description forthcoming.

---

### __objectStoreChangesFromAttributeToAttribute__

`public NSDictionary objectStoreChangesFromAttributeToAttribute( EOAttribute anAttribute, EOAttribute anotherAttribute)`

Description forthcoming.

---

### phraseCastingColumnNamed

`public String phraseCastingColumnNamed( String columnName, EOSchemaSynchronization.ColumnTypes fromType, EOSchemaSynchronization.ColumnTypes castType NSDictionary options)`

Returns an SQL string to cast the values in the column specified by _columnName_ to a new type. This method is used when the adaptor doesn't support in-place column type coercion, and the table has to be recreated. To move data from the old table to the new table, sometimes a conversion statement is needed (for example, to convert strings in a VARCHAR column to numbers). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### primaryKeyConstraintStatementsForEntityGroup

`public NSArray primaryKeyConstraintStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for _entityGroup_, an array of EOEntity objects that have the same externalName. Returns an empty array if any of the primary key attributes in _entityGroup_ don't have a columnName.

EOSQLExpression's implementation creates a statement of the following form:

> ```
> ALTER TABLE TABLE_NAME ADD PRIMARY KEY (PRIMARY_KEY_COLUMN_NAMES)
> ```

Where _TABLE_NAME_ is the externalName for the first entity in _entityGroup_ and _PRIMARY_KEY_COLUMN_NAMES_ is a comma-separated list of the columnNames of the first entity's primaryKeyAttributes.

If the subclass's database server's primary key constraint semantics are different, the subclass should override this method.

---

### primaryKeyConstraintStatementsForEntityGroups

`public NSArray primaryKeyConstraintStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key constraints for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same externalName, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4a) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

---

### primaryKeySupportStatementsForEntityGroup

`public NSArray primaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for _entityGroup_, an array of EOEntity objects that have the same externalName. EOSQLExpression's implementation creates a statement of the following form:
> ```
> create sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is the primaryKeyRootName for the first entity in _entityGroup_ concatenated with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass uses a different primary key generation mechanism or if the subclass's database server's drop semantics are different, the subclass should override this method.

__See Also:__ [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa), primaryKeyForNewRowWithEntity (EOAdaptorChannel)

---

### primaryKeySupportStatementsForEntityGroups

`public NSArray primaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects that define the SQL necessary to create the primary key generation support for the Entities specified in _entityGroups_. An entity group is an array of Entity objects that have the same externalName, and _entityGroups_ is an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4a) for each entity group in _entityGroups_ and returns an array of all the resulting EOSQLExpressions.

---

### schemaCreationScriptForEntities

`public String schemaCreationScriptForEntities( NSArray entities, NSDictionary options)`

Returns a script of SQL statements suitable to create the schema for the EOEntity objects in _entities_. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306). EOSQLExpression's implementation invokes __schemaCreationStatementsForEntities__ with _entities_ and _options_ and then uses [appendExpressionToScript](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6ylqobsw4zcfpbyhezltonuw63sun5jwg4tjob2a) to generate the script from the EOSQLExpressions generated by __schemaCreationStatementsForEntities__.

---

### schemaCreationStatementsForEntities

`public NSArray schemaCreationStatementsForEntities( NSArray entities, NSDictionary options)`

Returns an array of EOSQLExpressions suitable to create the schema for the Entity objects in _entities_. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

EOSQLExpression's implementation uses the following methods:

- [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6y3smvqxizkumfrgyzktorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y)
- [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfiylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq)
- [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsu3vobyg64tukn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4dt)
- [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6zdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y)
- [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s64dsnfwwc4tzjnsxsq3pnzzxi4tbnfxhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
- [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s6ztpojswsz3ojnsxsq3pnzzxi4tbnfxhiu3umf2gk3lfnz2hgrtpojjgk3dboruw63ttnbuxa)

to generate EOSQLExpressions for the support identified in _options_.

__See Also:__ [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643dnbsw2ykdojswc5djn5xfgy3snfyhirtpojcw45djoruwk4y)

---

### __schemaSynchronizationDelegate__

`public EOSynchronizationFactory.Delegate schemaSynchronizationDelegate()`

Description forthcoming.

---

### __setSchemaSynchronizationDelegate__

`public void setSchemaSynchronizationDelegate( EOSynchronizationFactory.Delegate aDelegate)`

Description forthcoming.

---

### statementsToConvertColumnType

`public NSArray statementsToConvertColumnType( String columnName, String tableName, EOSchemaSynchronization.ColumnTypes type, EOSchemaSynchronization.ColumnTypes newType, NSDictionary options)`

Returns an array of EOSQLExpressions to convert in place the type of the specified column. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToCopyTableNamed

`public NSArray statementsToCopyTableNamed( String tableName, NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to copy the specified table into a new table, whose definition is provided by _entityGroup_-an array of EOEntity objects rooted to the table named _tableName_. This method is used when the adaptor doesn't support the in-place table modifications required to synchronize the database to a model.

The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDeleteColumnNamed

`public NSArray statementsToDeleteColumnNamed( String columnName, String tableName, NSDictionary options)`

Returns an array of EOSQLExpressions to delete in place the specified column from the specified table. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropForeignKeyConstraintsOnEntityGroups

`public NSArray statementsToDropForeignKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop foreign key constraints for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropPrimaryKeyConstraintsOnEntityGroups

`public NSArray statementsToDropPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop primary key constraints for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToDropPrimaryKeySupportForEntityGroups

`public NSArray statementsToDropPrimaryKeySupportForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to drop the primary key support mechanism for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementForeignKeyConstraintsOnEntityGroups

`public NSArray statementsToImplementForeignKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement foreign key constraints on the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementPrimaryKeyConstraintsOnEntityGroups

`public NSArray statementsToImplementPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement primary key constraints on the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToImplementPrimaryKeySupportForEntityGroups

`public NSArray statementsToImplementPrimaryKeySupportForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to implement support mechanisms for primary key generation for the table corresponding to _entityGroup_-an array of EOEntity objects rooted to the same table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToInsertColumnForAttribute

`public NSArray statementsToInsertColumnForAttribute( EOAttribute attribute, NSDictionary options)`

Returns an array of EOSQLExpressions to insert in place a column for the specified attribute. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### __statementsToModifyColumnNullRule__

`public NSArray statementsToModifyColumnNullRule( String, String, boolean, NSDictionary)`

Description forthcoming.

---

### statementsToRenameColumnNamed

`public NSArray statementsToRenameColumnNamed( String columnName, String tableName, String newName, NSDictionary options)`

Returns an array of EOSQLExpressions to rename in place the specified column. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToRenameTableNamed

`public NSArray statementsToRenameTableNamed( String tableName, String newName, NSDictionary options)`

Returns an array of EOSQLExpressions to rename in place the specified table. The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToUpdateObjectStoreForEntityGroups

`public NSArray statementsToUpdateObjectStoreForEntityGroups( NSArray entityGroup, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to update the table that corresponds to _entityGroup_-an array of EOEntity objects rooted to the same table. Inserts and deletes columns, and updates modified columns. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### statementsToUpdateObjectStoreForModel

`public NSArray statementsToUpdateObjectStoreForModel( EOModel model, NSDictionary changes, NSDictionary options)`

Returns an array of EOSQLExpressions to synchronize the database with _model_. Prepares the statements to insert and delete new and deleted tables before invoking [statementsToUpdateObjectStoreForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkn4w4y3iojxw42l2mf2gs33oizqwg5dpoj4s643umf2gk3lfnz2hgvdpkvygiylumvhwe2tfmn2fg5dpojsum33sivxhi2lupfdxe33vobzq) for each modified table. The _changes_ dictionary identifies the changes to make to the database schema; for more information, see "The Change Dictionary" (page 306). The _options_ dictionary describes the aspects of the schema for which to create SQL statements; for more information, see "The Options Dictionary" (page 306).

---

### supportsDirectColumnCoercion

`public boolean supportsDirectColumnCoercion()`

Returns `true` if the adaptor can change the type of an existing column in place, `false` otherwise.

---

### supportsDirectColumnDeletion

`public boolean supportsDirectColumnDeletion()`

Returns `true` if the adaptor can delete columns, `false` otherwise.

---

### supportsDirectColumnInsertion

`public boolean supportsDirectColumnInsertion()`

Returns `true` if the adaptor can add columns to a table, `false` otherwise.

---

### supportsDirectColumnNullRuleModification

`public boolean supportsDirectColumnNullRuleModification()`

Returns `true` if the adaptor can modify the null rule of an existing column in place, `false` otherwise.

---

### supportsDirectColumnRenaming

`public boolean supportsDirectColumnRenaming()`

Returns `true` if the adaptor can rename table columns, `false` otherwise.

---

### supportsSchemaSynchronization

`public boolean supportsSchemaSynchronization()`

Returns `true` if the adaptor can update the database to reflect changes in a model, `false` otherwise.

---

### isCaseSensitive

`public boolean isCaseSensitive()`

Description forthcoming.

---

### logicalErrorsInChangeDictionaryForModelOptions

`public NSArray logicalErrorsInChangeDictionaryForModelOptions( NSDictionary changes, EOModel model, NSDictionary options)`

Description forthcoming.

---

### objectStoreChangesFromAttributeToAttribute

`public NSDictionary objectStoreChangesFromAttributeToAttribute(EOAttribute schemaAttribute, EOAttribute modelAttribute)`

Description forthcoming.

---

### schemaSynchronizationDelegate

`public Delegate schemaSynchronizationDelegate()`

Returns the factory's delegate.

---

### setSchemaSynchronizationDelegate

`public void setSchemaSynchronizationDelegate(Delegate delegate)`

Sets the factory's delegate.

---

### tableEntityGroupsForEntities

`public NSArray tableEntityGroupsForEntities(NSArray entities)`

Returns an array of arrays. Filters out entities without external names or attributes having column names. Groups entities in sub-arrays by external name.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
