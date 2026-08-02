---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/Java/Classes/EOSQLExpression.html
archived_at: '2026-07-15T08:11:31.938115Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAdaptor Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOSQLExpression

> __Inherits
> from:__  NSObject

> __Package:__ com.apple.yellow.eoaccess

---

## Class Description

---

EOSQLExpression is an abstract superclass that defines how
to build SQL statements for adaptor channels. You don't typically
use instances of EOSQLExpression; rather, you use EOSQLExpression subclasses
written to work with a particular RDBMS and corresponding adaptor.
A concrete subclass of EOSQLExpression overrides many of its methods
in terms of the query language syntax for its specific RDBMS. EOSQLExpression
objects are used internally by the Framework, and unless you're creating
a concrete adaptor, you won't ordinarily need to interact with
EOSQLExpression objects yourself. You most commonly create and use
an EOSQLExpression object when you want to send an SQL statement
directly to the server. In this case, you simply create an expression
with the EOSQLExpression static method [expressionForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwk6dqojsxg43jn5xem33skn2he2lom4),
and send the expression object to an adaptor channel using [EOAdaptorChannel](EOAdaptorChannel.md#apple-ijaucqsbjfcei)'s [evaluateExpression](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpmv3gc3dvmf2gkrlyobzgk43tnfxw4) method.

For more information on using EOSQLExpressions, see the following
sections:

- ["Building Expressions"](EOSQLExpression-2.md#apple-ijduoq2ki5ceu)
- ["Using Table Aliases"](EOSQLExpression-2.md#apple-ijduoqscincec)
- ["Bind Variables"](EOSQLExpression-2.md#apple-ijduoq2bi5eei)
- ["Schema Generation"](EOSQLExpression-2.md#apple-ijduoq2cijbue)

## Constants

---

EOSQLExpression defines the following String constants.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| BindVariableNameKey | The key for the name of a bind variable in a bind variable dictionary. |
| BindVariablePlaceHolderKey | A key for use in bind variable dictionaries. The corresponding value is the placeholder string to be used in SQL. |
| BindVariableAttributeKey | A key for use in bind variable dictionaries. The corresponding value is the attribute that uses the bind variable. |
| BindVariableValueKey | A key for use in bind variable dictionaries. The corresponding value is the value for the bind variable. |
| CreateTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create tables. |
| DropTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop tables. |
| CreatePrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key support. |
| DropPrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop primary key support. |
| PrimaryKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key constraints. |
| ForeignKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create foreign key constraints. |
| CreateDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create a database. |
| DropDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop a database. |
| AllowsNullKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ColumnNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ExternalNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| ExternalTypeKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| NameKey | Key for use in change dictionaries. A corresponding value indicates the old value of the table or column. |
| PrecisionKey | Key for use in change dictionaries. A corresponding value indicates the value a column's precision should be changed from. |
| RelationshipsKey | Key for use in change dictionaries. The corresponding value is a dictionary of relationships which have been modified since the last time the model and schema were sychronized. For more information see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). |
| ScaleKey | Key for use in change dictionaries. A corresponding value indicates the value the column's scale should be changed from. |
| WidthKey | Key for use in change dictionaries. A corresponding value indicates the value the column's width should be changed from. |

## Method Types

---

> **Constructors**
> : [EOSQLExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l2fj5jvctcfpbyhezltonuw63q)
>
> **Creating an EOSQLExpression
> object**
> : [selectStatementForAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlmmvrxiu3umf2gk3lfnz2em33sif2hi4tjmj2xizlt)
> : [insertStatementForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxws3ttmvzhiu3umf2gk3lfnz2em33skjxxo)
> : [updateStatementForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk4demf2gku3umf2gk3lfnz2em33skjxxo)
> : [deleteStatementWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls)
> : [expressionForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwk6dqojsxg43jn5xem33skn2he2lom4)
>
> **Building SQL Expressions**
> : [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom)
> : [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y)
> : [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y)
> : [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q)
> : [setStatement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fg5dborsw2zlooq)
> : [statement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3torqxizlnmvxhi)
>
> **Generating SQL for attributes
> and values**
> : [formatSQLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq)
> : [formatValueForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxivtbnr2wkrtpojaxi5dsnfrhk5df)
> : [formatStringValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu3uojuw4z2wmfwhkzi)
> : [sqlStringForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu)
> : [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle)
> : [sqlStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5df)
> : [sqlStringForAttributePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfkbqxi2a)
> : [sqlStringForNumber](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkn2he2lom5dg64soovwwezls)
> : [sqlStringForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkn2he2lom5dg64storzgs3th)
>
> **Generating SQL for names
> of database objects**
> : [sqlStringForSchemaObjectName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwg2dfnvqu6ytkmvrxittbnvsq)
> : [setUseQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlukvzwkulvn52gkzcfpb2gk4tomfwe4ylnmvzq)
> : [useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fkf2w65dfmrcxq5dfojxgc3comfwwk4y)
> : [externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fpb2gk4tomfwe4ylnmvixk33umvbwqylsmfrxizls)
>
> **Generating an attribute
> list**
> : [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfgzlmmvrxitdjon2ec5duojuwe5lumu)
> : [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu)
> : [addUpdateListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfk4demf2gktdjon2ec5duojuwe5lumu)
> : [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bobygk3tejf2gk3kun5ggs43ukn2he2lom4)
> : [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy)
>
> **Generating a value list**
> : [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu)
> : [addUpdateListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfk4demf2gktdjon2ec5duojuwe5lumu)
> : [valueList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3wmfwhkzkmnfzxi)
>
> **Generating a table list**
> : [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q)
> : [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a)
>
> **Generating the join clause**
> : [joinExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4rlyobzgk43tnfxw4)
> : [addJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseu33jnzbwyylvonsq)
> : [assembleJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsuu33jnzbwyylvonsq)
> : [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4q3mmf2xgzktorzgs3th)
>
> **Generating a search pattern**
> : [sqlPatternFromShellPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkbqxi5dfojxem4tpnvjwqzlmnrigc5dumvzg4)
> : [sqlPatternFromShellPatternWithEscapeCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkbqxi5dfojxem4tpnvjwqzlmnrigc5dumvzg4v3joruek43dmfygkq3imfzgcy3umvza)
>
> **Generating a relational
> operator**
> : [sqlStringForSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwk3dfmn2g64q)
>
> **Accessing the where clause**
> : [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4)
>
> **Generating an order by
> clause**
> : [addOrderByAttributeOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrse64temvzee6kbor2he2lcov2gkt3smrsxe2lom4)
> : [orderByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3pojsgk4scpfjxi4tjnztq)
>
> **Accessing the lock clause**
> : [lockClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mn5rwwq3mmf2xgzi)
>
> **Assembling a statement**
> : [assembleSelectStatementWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvgzlmmvrxiu3umf2gk3lfnz2fo2lunbaxi5dsnfrhk5dfom)
> : [assembleInsertStatementWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsus3ttmvzhiu3umf2gk3lfnz2fo2lunbjg65y)
> : [assembleUpdateStatementWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvk4demf2gku3umf2gk3lfnz2fo2lunbjg65y)
> : [assembleDeleteStatementWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsuizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls)
>
> **Generating SQL for qualifiers**
> : [sqlStringForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojixkylmnftgszls)
> : [sqlStringForConjoinedQualifiers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojbw63tkn5uw4zlekf2wc3djmzuwk4tt)
> : [sqlStringForDisjoinedQualifiers](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojcgs43kn5uw4zlekf2wc3djmzuwk4tt)
> : [sqlStringForKeyComparisonQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojfwk6kdn5wxaylsnfzw63srovqwy2lgnfsxe)
> : [sqlStringForKeyValueQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojfwk6kwmfwhkzkrovqwy2lgnfsxe)
> : [sqlStringForNegatedQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojhgkz3borswiulvmfwgsztjmvza)
>
> **Managing bind variables**
> : [setUseBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlukvzwkqtjnzsfmylsnfqwe3dfom)
> : [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fijuw4zcwmfzgsylcnrsxg)
> : [addBindVariableDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsee2lomrlgc4tjmfrgyzkenfrxi2lpnzqxe6i)
> : [bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylsnfsxg)
> : [bindVariableDictionaryForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylspfdg64sbor2he2lcov2gk)
> : [mustUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3novzxivltmvbgs3tekzqxe2lbmjwgkrtpojaxi5dsnfrhk5df)
> : [shouldUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tnbxxk3dekvzwkqtjnzsfmylsnfqwe3dfizxxeqluorzgsytvorsq)
>
> **Using table aliases**
> : [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)
> : [useAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3vonsuc3djmfzwk4y)
>
> **Accessing the entity**
> : [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fnz2gs5dz)
>
> **Creating a schema generation
> script**
> : [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjwg4tjob2em33sivxhi2lunfsxg)
> : [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)
> : [appendExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwc4dqmvxgirlyobzgk43tnfxw4)
> : [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)
> : [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
> : [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq)
> : [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom)
> : [primaryKeyConstraintStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33voa)
> : [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq)
> : [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa)
> : [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y)
> : [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)
> : [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
> : [addCreateClauseForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseg4tfmf2gkq3mmf2xgzkgn5zec5duojuwe5lumu)
> : [columnTypeStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3dn5whk3lokr4xazktorzgs3thizxxeqluorzgsytvorsq)
> : [allowsNullClauseForConstraint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnrwg653tjz2wy3cdnrqxk43fizxxeq3pnzzxi4tbnfxhi)
> : [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33smvuwo3slmv4ug33oon2heyljnz2fg5dborsw2zloorzum33skjswyylunfxw443infya)
> : [prepareConstraintStatementForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvbw63ttorzgc2loorjxiylumvwwk3tuizxxeutfnrqxi2lpnzzwq2lq)
> : [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkrdborqweyltmvjxiylumvwwk3tuondg64sdn5xg4zldoruw63senfrxi2lpnzqxe6i)
> : [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobcgc5dbmjqxgzktorqxizlnmvxhi42gn5zeg33onzswg5djn5xei2ldoruw63tboj4q)
>
> **Synchronizing the database
> with a model**
> : [statementsToUpdateObjectStoreForModel](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64snn5sgk3a)
> : [statementsToUpdateObjectStoreForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64sfnz2gs5dzi5zg65lq)
> : [statementsToCopyTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32dn5yhsvdbmjwgkttbnvswi)
> : [phraseCastingColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa2dsmfzwkq3bon2gs3thinxwy5lnnzhgc3lfmq)
> : [statementsToRenameTableNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32smvxgc3lfkrqwe3dfjzqw2zle)
> : [statementsToInsertColumnForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32jnzzwk4tuinxwy5lnnzdg64sbor2he2lcov2gk)
> : [statementsToDeleteColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32emvwgk5dfinxwy5lnnzhgc3lfmq)
> : [statementsToRenameColumnNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32smvxgc3lfinxwy5lnnzhgc3lfmq)
> : [statementsToModifyColumnNullRule](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32nn5sgsztzinxwy5lnnzhhk3dmkj2wyzi)
> : [statementsToConvertColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32dn5xhmzlsorbw63dvnvxfi6lqmu)
> : [isColumnTypeEquivalentToColumnType](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxws42dn5whk3lokr4xazkfof2ws5tbnrsw45cun5bw63dvnvxfi6lqmu)
> : [statementsToDropForeignKeyConstraintsOnEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32eojxxartpojswsz3ojnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovya)
> : [statementsToDropPrimaryKeyConstraintsOnEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32eojxxaudsnfwwc4tzjnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovya)
> : [statementsToDropPrimaryKeySupportForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32eojxxaudsnfwwc4tzjnsxsu3vobyg64tuizxxerlooruxi6khojxxk4a)
> : [statementsToImplementForeignKeyConstraintsOnEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhirtpojswsz3ojnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovya)
> : [statementsToImplementPrimaryKeyConstraintsOnEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhiudsnfwwc4tzjnsxsq3pnzzxi4tbnfxhi42pnzcw45djor4uo4tpovya)
> : [statementsToImplementPrimaryKeySupportForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32jnvygyzlnmvxhiudsnfwwc4tzjnsxsu3vobyg64tuizxxerlooruxi6khojxxk4a)
>
> **Querying about database
> synchronization support**
> : [supportsSchemaSynchronization](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtknrwqzlnmfjxs3tdnbzg63tjpjqxi2lpny)
> : [supportsDirectColumnCoercion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxeg33fojrws33o)
> : [supportsDirectColumnDeletion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxeizlmmv2gs33o)
> : [supportsDirectColumnInsertion](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxes3ttmvzhi2lpny)
> : [supportsDirectColumnNullRuleModification](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxe45lmnrjhk3dfjvxwi2lgnfrwc5djn5xa)
> : [supportsDirectColumnRenaming](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5lqobxxe5dtiruxezldorbw63dvnvxfezlomfwws3th)

## Constructors

---

### EOSQLExpression

`public EOSQLExpression(EOEntity anEntity)`

Creates a new EOSQLExpression rooted to _anEntity_.

__See
Also:__  [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fnz2gs5dz)

---

## Static Methods

---

### appendExpression

`public static void appendExpression(
EOSQLExpression anSQLExpression,
String script)`

Append's _anSQLExpression_'s [statement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3torqxizlnmvxhi) to _script_ along
with any necessary delimiter. EOSQLExpression's implementation
appends the SQL statement for _anSQLExpression_ to _script_ followed
by a semicolon and a newline. A subclass of EOSQLExpression only
needs to override this method if the delimiter for its database
server is different. For example, the Oracle and Informix use the default
implementation, whereas the Sybase adaptor appends the word "go"
instead of a semicolon.

__See Also:__  [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)

---

### createDatabaseStatementsForConnectionDictionary

`public static NSArray createDatabaseStatementsForConnectionDictionary(
NSDictionary connectionDictionary,
NSDictionary adminDictionary)`

Generates the SQL statements that will create
a database (or user, for Oracle) that can be accessed by the provided
connection dictionary and administrative connection dictionary.

__See
Also:__  [dropDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobcgc5dbmjqxgzktorqxizlnmvxhi42gn5zeg33onzswg5djn5xei2ldoruw63tboj4q)

---

### createTableStatementsForEntityGroup

`public static NSArray createTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create a table for _entityGroup_,
an array of EOEntity objects that have the same [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi). Returns an empty array
if _entityGroup_ is null or empty.

EOSQLExpression's
implementation does the following:

1. Creates
   an EOSQLExpression object.
2. Sets the expression's [entity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fnz2gs5dz) to the first entity in _entityGroup_.
3. Adds a create clause for each Attribute in _entityGroup_'s
   Entities.
4. Sets the expression's [statement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3torqxizlnmvxhi) to CREATE TABLE _TABLE_NAME_ (_LIST_STRING_),
   where _TABLE_NAME_ is the __externalName__ of
   the Entity objects in _entityGroup_ and _LIST_STRING_ is
   the expression's [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy).
5. Adds the expression to an array.
6. Returns the array.

The following
is an example of a CREATE TABLE statement produced by the default
implementation:

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

If a subclass's
database server's table creation semantics are different, the
subclass should override this method or one or more of the following
methods as appropriate:

- [addCreateClauseForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseg4tfmf2gkq3mmf2xgzkgn5zec5duojuwe5lumu)
- [columnTypeStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3dn5whk3lokr4xazktorzgs3thizxxeqluorzgsytvorsq)
- [allowsNullClauseForConstraint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnrwg653tjz2wy3cdnrqxk43fizxxeq3pnzzxi4tbnfxhi)

__See
Also:__  [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya), [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq)

---

### createTableStatementsForEntityGroups

`public static NSArray createTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the tables specified in _entityGroups_.
An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is
an array of entity groups. Returns an empty array if _entityGroups_ is null or
empty. EOSQLExpression's implementation invokes [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### deleteStatementWithQualifier

`public static EOSQLExpression deleteStatementWithQualifier(
com.apple.yellow.eocontrol.EOQualifier qualifier,
Object entity)`

Creates and returns an SQL DELETE expression
to delete the rows described by qualifier. Creates an instance of
EOSQLExpression, initializes it with _entity_ (an
EOEntity object), and sends it a [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q) message. Throws an `exception` if
qualifier is null.

The expression created with this method
does not use table aliases because Enterprise Objects Framework
assumes that all INSERT, UPDATE, and DELETE statements are single-table
operations. As a result, all keys in _qualifier_ should
be simple key names; no key paths are allowed. To generate DELETE
statements that do use table aliases, you must override [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q) to
send a [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)`(true)` message
prior to invoking `super`'s
version.

---

### dropDatabaseStatementsForConnectionDictionary

`public static NSArray dropDatabaseStatementsForConnectionDictionary(
NSDictionary connectionDictionary,
NSDictionary adminDictionary)`

Generates the SQL statements to drop a database
(or user, for Oracle).

__See Also:__  [createDatabaseStatementsForConnectionDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkrdborqweyltmvjxiylumvwwk3tuondg64sdn5xg4zldoruw63senfrxi2lpnzqxe6i)

---

### dropPrimaryKeySupportStatementsForEntityGroup

`public static NSArray dropPrimaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the primary key generation
support for _entityGroup_, an array
of Entity objects that have the same __externalName__.
The drop statement generated by this method should be sufficient
to remove the primary key support created by [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa)'s
statements.

EOSQLExpression's implementation creates a statement
of the following form:

> ```
> drop sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is
the [primaryKeyRootName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4ve33porhgc3lf) for
the first entity in _entityGroup_ concatenated
with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass
uses a different primary key generation mechanism or if the subclass's
database server's drop semantics are different, the subclass should
override this method.

---

### dropPrimaryKeySupportStatementsForEntityGroups

`public static NSArray dropPrimaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the primary key generation
support for the entities specified in _entityGroups_.
An entity group is an array of EOEntity objects that have the same __externalName__,
and _entityGroups_ is an array of entity
groups. EOSQLExpression's implementation invokes [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya) for each
entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### dropTableStatementsForEntityGroup

`public static NSArray dropTableStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the table identified by _entityGroup_,
an array of Entity objects that have the same __externalName__.
The drop statement generated by this method should be sufficient
to remove the table created by [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya)'s
statements.

EOSQLExpression's implementation creates a statement
of the following form:

> ```
> DROP TABLE TABLE_NAME
> ```

Where _TABLE_NAME_ is
the __externalName__ of the first entity in _entityGroup_.

If
a subclass's database server's drop semantics are different,
the subclass should override this method.

---

### dropTableStatementsForEntityGroups

`public static NSArray dropTableStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the tables for _entityGroups_.
An entity group is an array of Entity objects that have the same __externalName__,
and _entityGroups_ is an array of entity
groups. EOSQLExpression's implementation invokes [dropTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lq) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### expressionForString

`public static EOSQLExpression expressionForString(String string)`

Creates and returns an SQL expression for _string_. _string_ should
be a valid expression in the target query language. This method
does not perform substitutions or formatting of any kind.

__See
Also:__  [setStatement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fg5dborsw2zlooq)

---

### foreignKeyConstraintStatementsForRelationship

`public static NSArray foreignKeyConstraintStatementsForRelationship(EORelationship aRelationship)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create foreign key constraints
for _aRelationship_. EOSQLExpression's
implementation generates statements such as the following:
> ```
> ALTER TABLE EMPLOYEE ADD CONSTRAINT TO_DEPARTMENT FOREIGN KEY (DEPT_ID)
>         REFERENCES DEPARTMENT(DEPT_ID)
> ```

It
returns an empty array if either of the following are true:

- _aRelationship_ spans models
  (if _aRelationship_'s [destinationEntity](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zdfon2gs3tboruw63sfnz2gs5dz) is
  in a different model than _aRelationship_'s
  source [entity](EORelationship.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkjswyylunfxw443infyc6zlooruxi6i))
- _aRelationship_ is a to-many
  relationship, or if the inverse relationship of _aRelationship_ is
  not a to-many. In other words, foreign key constraint statements
  are only created for to-one relationships whose inverse is a to-many.

If
neither of the above are true, this method creates a new EOSQLExpression,
assigns its entity to _aRelationship_'s
entity, invokes [prepareConstraintStatementForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvbw63ttorzgc2loorjxiylumvwwk3tuizxxeutfnrqxi2lpnzzwq2lq),
and returns an array containing the expression.

If a
subclass's database server's foreign key constraint semantics
are different, the subclass should override this method or override
the method __prepareConstraintStatementForRelationship__.

__See
Also:__  [schemaCreationStatementsForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjxiylumvwwk3tuondg64sfnz2gs5djmvzq)

---

### formatSQLString

`public static String formatSQLString(
String sqlString,
String format)`

Applies _format_ (an
EOAttribute object's "read" or "write" format) to _sqlString_ (a
value for the attribute). If _format_ is null,
this method returns _sqlString_ unchanged.

__See
Also:__  [readFormat](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpojswczcgn5zg2ylu) (EOAttribute), [writeFormat](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5zgs5dfizxxe3lboq) (EOAttribute)

---

### formatStringValue

`public static String formatStringValue(String string)`

Formats _string_ for
use as a string constant in a SQL statement. EOSQLExpression's
implementation encloses the string in single quotes, escaping any
single quotes already present in _string_. Throws an exception if _string_ is null.

---

### formatValueForAttribute

`public static String formatValueForAttribute(
Object value,
EOAttribute attribute)`

Overridden by subclasses to return a string
representation of _value_ suitable
for use in an SQL statement. EOSQLExpression's implementation
returns _value_ unchanged. A subclass
should override this method to format _value_ depending
on _attribute_'s [externalType](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq). For example, a subclass
might format a date using a special database-specific syntax or
standard form or truncate numbers to attribute's precision and
scale.

---

### insertStatementForRow

`public static EOSQLExpression insertStatementForRow(
NSDictionary row,
EOEntity entity)`

Creates and returns an SQL INSERT expression
to insert _row_. Creates an instance
of EOSQLExpression, initializes it with _entity_,
and sends it [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y). Throws an exception if
entity is null.

The expression created with this method does
not use table aliases because Enterprise Objects Framework assumes
that all INSERT, UPDATE, and DELETE statements are single-table
operations. To generate INSERT statements that do use table aliases,
you must override [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y) to
send a [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)`(true)` message
prior to invoking `super`'s version.

---

### isColumnTypeEquivalentToColumnType

`public static boolean isColumnTypeEquivalentToColumnType(
EOSQLExpression.EOColumnTypes columnTypeA,
EOSQLExpression.EOColumnTypes columnTypeB,
NSDictionary options)`

Returns true if values in a column of _columnTypeA_ can
be copied into a column of _columnTypeB_ without the
use of a casting phrase, false otherwise. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### phraseCastingColumnNamed

`public static String phraseCastingColumnNamed(
String columnName,
EOSQLExpression.EOColumnTypes fromType,
EOSQLExpression.EOColumnTypes castType
NSDictionary options)`

Returns an SQL string to cast the values in
the column specified by _columnName_ to
a new type. This method is used when the adaptor doesn't support
in-place column type coercion, and the table has to be recreated.
To move data from the old table to the new table, sometimes a conversion
statement is needed (for example, to convert strings in a VARCHAR
column to numbers). The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### primaryKeyConstraintStatementsForEntityGroup

`public static NSArray primaryKeyConstraintStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key constraints
for _entityGroup_, an array of EOEntity
objects that have the same [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi).
Returns an empty array if any of the primary key attributes in _entityGroup_ don't
have a [columnName](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf).

EOSQLExpression's
implementation creates a statement of the following form:

> ```
> ALTER TABLE TABLE_NAME ADD PRIMARY KEY (PRIMARY_KEY_COLUMN_NAMES)
> ```

Where _TABLE_NAME_ is
the [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi) for
the first entity in _entityGroup_ and _PRIMARY_KEY_COLUMN_NAMES_ is
a comma-separated list of the [columnName](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmnxwy5lnnzhgc3lf)s of the first entity's [primaryKeyAttributes](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4uc5duojuwe5lumvzq).

If
the subclass's database server's primary key constraint semantics
are different, the subclass should override this method.

---

### primaryKeyConstraintStatementsForEntityGroups

`public static NSArray primaryKeyConstraintStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key constraints
for the Entities specified in _entityGroups_.
An entity group is an array of Entity objects that have the same [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi), and _entityGroups_ is
an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

---

### primaryKeySupportStatementsForEntityGroup

`public static NSArray primaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key generation
support for _entityGroup_, an array
of EOEntity objects that have the same [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi). EOSQLExpression's
implementation creates a statement of the following form:
> ```
> create sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is
the [primaryKeyRootName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexxa4tjnvqxe6klmv4ve33porhgc3lf) for
the first entity in _entityGroup_ concatenated
with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass
uses a different primary key generation mechanism or if the subclass's
database server's drop semantics are different, the subclass should
override this method.

__See Also:__  [dropPrimaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya), [primaryKeyForNewRowWithEntity](EOAdaptorChannel.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpifsgc4dun5zeg2dbnzxgk3bpobzgs3lboj4uwzlzizxxettfo5jg652xnf2gqrlooruxi6i) (EOAdaptorChannel)

---

### primaryKeySupportStatementsForEntityGroups

`public static NSArray primaryKeySupportStatementsForEntityGroups(NSArray entityGroups)`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key generation
support for the Entities specified in _entityGroups_.
An entity group is an array of Entity objects that have the same [externalName](EOEntity.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpivxhi2lupexwk6dumvzg4ylmjzqw2zi), and _entityGroups_ is
an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

---

### schemaCreationScriptForEntities

`public static String schemaCreationScriptForEntities(
NSArray entities,
NSDictionary options)`

Returns a script of SQL statements suitable
to create the schema for the EOEntity objects in _entities_. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec). EOSQLExpression's
implementation invokes __schemaCreationStatementsForEntities__ with _entities_ and _options_ and
then uses [appendExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwc4dqmvxgirlyobzgk43tnfxw4) to generate
the script from the EOSQLExpressions generated by __schemaCreationStatementsForEntities__.

---

### schemaCreationStatementsForEntities

`public static NSArray schemaCreationStatementsForEntities(
NSArray entities,
NSDictionary options)`

Returns an array of EOSQLExpressions suitable
to create the schema for the Entity objects in _entities_. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

EOSQLExpression's
implementation uses the following methods:

- [createTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
- [dropTableStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobkgcytmmvjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom)
- [primaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4vg5lqobxxe5ctorqxizlnmvxhi42gn5zek3tunf2hsr3sn52xa4y)
- [dropPrimaryKeySupportStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwi4tpobihe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhg)
- [primaryKeyConstraintStatementsForEntityGroups](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxa4tjnvqxe6klmv4ug33oon2heyljnz2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobzq)
- [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33smvuwo3slmv4ug33oon2heyljnz2fg5dborsw2zloorzum33skjswyylunfxw443infya)

to
generate EOSQLExpressions for the support identified in _options_.

__See
Also:__  [schemaCreationScriptForEntities](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgy3imvwwcq3smvqxi2lpnzjwg4tjob2em33sivxhi2lunfsxg)

---

### selectStatementForAttributes

`public static EOSQLExpression selectStatementForAttributes(
NSArray attributes,
boolean flag,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification,
EOEntity entity)`

Creates and returns an SQL SELECT expression.
Creates an instance of EOSQLExpression, initializes it with _entity_,
and sends it [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom).
The expression created with this method uses table aliases. Throws an exception if
attributes is null or empty, _fetchSpecification_ is null,
or _entity_ is null.

The expression
created with this method uses table aliases. To generate SELECT
statements that don't use them, you must override [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom) to
send a [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)`(false)` message
prior to invoking `super`'s
version.

---

### setUseBindVariables

`public static void setUseBindVariables(boolean flag)`

Sets according to _flag_ whether
all instances of EOSQLExpression subclasses use bind variables.
By default, instances don't use bind variables; if the value for
the global user default named `EOAdaptorUseBindVariables` is true,
though, instances do use them. For more information on bind variables,
see the discussion in the class description.

__See
Also:__  [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fijuw4zcwmfzgsylcnrsxg)

---

### setUseQuotedExternalNames

`public static void setUseQuotedExternalNames(boolean flag)`

Sets whether all instances of EOSQLExpression
subclasses quote external names when they are referenced in SQL
statements. By setting _flag_ to true,
you can access database tables with names such as "%return",
"1st year", and "TABLE" that you couldn't otherwise access.
By default, instances don't quote external names; if the value for
the global user default named `EOAdaptorQuotesExternalNames` is true,
though, instances do use quotes.

__See Also:__  [useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fkf2w65dfmrcxq5dfojxgc3comfwwk4y), [sqlStringForSchemaObjectName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwg2dfnvqu6ytkmvrxittbnvsq), [externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fpb2gk4tomfwe4ylnmvixk33umvbwqylsmfrxizls)

---

### sqlPatternFromShellPattern

`public static String sqlPatternFromShellPattern(String pattern)`

Translates a "like" qualifier to an SQL
"like" expression. Invoked from [sqlStringForKeyValueQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojfwk6kwmfwhkzkrovqwy2lgnfsxe) when
the qualifier argument is an EOKeyValueQualifier object whose selector
is `EOQualifier.QualifierOperatorLike`.
EOSQLExpression's implementation performs the following substitutions

|  |  |
| --- | --- |
| __Character in pattern__ | __Substitution string__ |
| \* | % |
| ? | _ |
| % | [%] _(unless the percent character appears in square brackets)_ |
| _ | [_] _(unless the underscore character appears in square brackets)_ |

__See Also:__  [sqlPatternFromShellPatternWithEscapeCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkbqxi5dfojxem4tpnvjwqzlmnrigc5dumvzg4v3joruek43dmfygkq3imfzgcy3umvza)

---

### sqlPatternFromShellPatternWithEscapeCharacter

`public static String sqlPatternFromShellPatternWithEscapeCharacter(
String pattern,
char escapeCharacter)`

Like [sqlPatternFromShellPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkbqxi5dfojxem4tpnvjwqzlmnrigc5dumvzg4) except
the argument _escapeCharacter_ allows
you to specify a character for escaping the wild card characters
"%" and "_".

---

### statementsToConvertColumnType

`public static NSArray statementsToConvertColumnType(
String columnName,
String tableName,
EOSQLExpression.EOColumnTypes type,
EOSQLExpression.EOColumnTypes newType,
NSDictionary options)`

Returns an array of EOSQLExpressions to convert
in place the type of the specified column. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToCopyTableNamed

`public static NSArray statementsToCopyTableNamed(
String tableName,
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to copy
the specified table into a new table, whose definition is provided
by _entityGroup_-an array of EOEntity
objects rooted to the table named _tableName_.
This method is used when the adaptor doesn't support the in-place
table modifications required to synchronize the database to a model.

The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToDeleteColumnNamed

`public static NSArray statementsToDeleteColumnNamed(
String columnName,
String tableName,
NSDictionary options)`

Returns an array of EOSQLExpressions to delete
in place the specified column from the specified table. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToDropForeignKeyConstraintsOnEntityGroup

`public static NSArray statementsToDropForeignKeyConstraintsOnEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to drop
foreign key constraints for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToDropPrimaryKeyConstraintsOnEntityGroup

`public static NSArray statementsToDropPrimaryKeyConstraintsOnEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to drop
primary key constraints for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToDropPrimaryKeySupportForEntityGroup

`public static NSArray statementsToDropPrimaryKeySupportForEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to drop
the primary key support mechanism for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToImplementForeignKeyConstraintsOnEntityGroup

`public static NSArray statementsToImplementForeignKeyConstraintsOnEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to implement
foreign key constraints on the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToImplementPrimaryKeyConstraintsOnEntityGroup

`public static NSArray statementsToImplementPrimaryKeyConstraintsOnEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to implement
primary key constraints on the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToImplementPrimaryKeySupportForEntityGroup

`public static NSArray statementsToImplementPrimaryKeySupportForEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to implement
support mechanisms for primary key generation for the table corresponding
to _entityGroup_-an array of EOEntity
objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToInsertColumnForAttribute

`public static NSArray statementsToInsertColumnForAttribute(
EOAttribute attribute,
NSDictionary options)`

Returns an array of EOSQLExpressions to insert
in place a column for the specified attribute. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToModifyColumnNullRule

`public static NSArray statementsToModifyColumnNullRule(
String columnName,
String tableName,
boolean allowsNull,
NSDictionary options)`

Returns an array of EOSQLExpressions to modify
in place the specified column to either allow or not allow NULL
values as specified by _allowsNull_.
The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToRenameColumnNamed

`public static NSArray statementsToRenameColumnNamed(
String columnName,
String tableName,
String newName,
NSDictionary options)`

Returns an array of EOSQLExpressions to rename
in place the specified column. The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToRenameTableNamed

`public static NSArray statementsToRenameTableNamed(
String tableName,
String newName,
NSDictionary options)`

Returns an array of EOSQLExpressions to rename
in place the specified table. The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToUpdateObjectStoreForEntityGroup

`public static NSArray statementsToUpdateObjectStoreForEntityGroup(
NSArray entityGroup,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to update
the table that corresponds to _entityGroup_-an
array of EOEntity objects rooted to the same table. Inserts and
deletes columns, and updates modified columns. The _changes_ dictionary
identifies the changes to make to the database schema; for more information,
see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### statementsToUpdateObjectStoreForModel

`public static NSArray statementsToUpdateObjectStoreForModel(
EOModel model,
NSDictionary changes,
NSDictionary options)`

Returns an array of EOSQLExpressions to synchronize
the database with _model_. Prepares
the statements to insert and delete new and deleted tables before
invoking [statementsToUpdateObjectStoreForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg5dborsw2zloorzvi32vobsgc5dfj5rguzldorjxi33smvdg64sfnz2gs5dzi5zg65lq) for
each modified table. The _changes_ dictionary identifies
the changes to make to the database schema; for more information,
see ["The Change Dictionary"](EOSQLExpression-2.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-2.md#apple-ijeugq2kjjfec).

---

### sqlStringForNumber

`public static String sqlStringForNumber(Number aNumber)`

Returns the SQL string for _aNumber_.

---

### sqlStringForString

`public static String sqlStringForString(String aString)`

Returns the SQL string for _aString_.

---

### supportsDirectColumnCoercion

`public static boolean supportsDirectColumnCoercion()`

Returns true if the adaptor can change the type
of an existing column in place, false otherwise.

---

### supportsDirectColumnDeletion

`public static boolean supportsDirectColumnDeletion()`

Returns true if the adaptor can delete columns, false otherwise.

---

### supportsDirectColumnInsertion

`public static boolean supportsDirectColumnInsertion()`

Returns true if the adaptor can add columns
to a table, false otherwise.

---

### supportsDirectColumnNullRuleModification

`public static boolean supportsDirectColumnNullRuleModification()`

Returns true if the adaptor can modify the null
rule of an existing column in place, false otherwise.

---

### supportsDirectColumnRenaming

`public static boolean supportsDirectColumnRenaming()`

Returns true if the adaptor can rename table
columns, false otherwise.

---

### supportsSchemaSynchronization

`public static boolean supportsSchemaSynchronization()`

Returns true if the adaptor can update the database
to reflect changes in a model, false otherwise.

---

### updateStatementForRow

`public static EOSQLExpression updateStatementForRow(
NSDictionary row,
com.apple.yellow.eocontrol.EOQualifier qualifier,
EOEntity entity)`

Creates and returns an SQL UPDATE expression
to update the row identified by _qualifier_ with
the values in _row_. _row_ should
only contain entries for values that have actually changed. Creates
an instance of EOSQLExpression, initializes it with _entity_,
and sends it [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y).

The
expression created with this method does not use table aliases because
Enterprise Objects Framework assumes that all INSERT, UPDATE, and
DELETE statements are single-table operations. As a result, all
keys in _qualifier_ should be simple
key names; no key paths are allowed. To generate UPDATE statements
that do use table aliases, you must override [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y) to send
a [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)`(true)` message
prior to invoking `super`'s
version.

__See Also:__  [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq)

---

### useBindVariables

`public static boolean useBindVariables()`

Returns true if instances use bind variables, false otherwise.
For more information on bind variables, see the discussion in the
class description.

__See Also:__  [setUseBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlukvzwkqtjnzsfmylsnfqwe3dfom)

---

### useQuotedExternalNames

`public static boolean useQuotedExternalNames()`

Returns true if instances use quoted external
names, false otherwise.

__See Also:__  [setUseQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlukvzwkulvn52gkzcfpb2gk4tomfwe4ylnmvzq), [sqlStringForSchemaObjectName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwg2dfnvqu6ytkmvrxittbnvsq), [externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fpb2gk4tomfwe4ylnmvixk33umvbwqylsmfrxizls)

---

## Instance Methods

---

### addBindVariableDictionary

`public void addBindVariableDictionary(NSMutableDictionary binding)`

Adds _binding_ to
the receiver's array of bind variable dictionaries. _binding_ is
generally created using the method [bindVariableDictionaryForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylspfdg64sbor2he2lcov2gk) and
is added to the receiver's bind variable dictionaries in [sqlStringForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu) when the receiver
uses a bind variable for the specified attribute. See the method description
for __bindVariableDictionaryForAttribute__ for
a description of the contents of a bind variable dictionary, and
for more information on bind variables, see the discussion in the
class description.

__See Also:__  [bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylsnfsxg)

---

### addCreateClauseForAttribute

`public void addCreateClauseForAttribute(EOAttribute attribute)`

Adds the SQL string for creating _attribute_ to
a comma-separated list of attribute creation clauses. The list is
constructed for use in a CREATE TABLE statement produced by [createTableStatementsForEntityGroup](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwg4tfmf2gkvdbmjwgku3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovya).
Use the method [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy) to
access creation clauses.

EOSQLExpression's implementation
creates clauses in the following form:

> ```
> COLUMN_NAME COLUMN_TYPE ALLOWS_NULL_CLAUSE
> ```

Where

- _COLUMN_TYPE_ is the string returned
  from [columnTypeStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3dn5whk3lokr4xazktorzgs3thizxxeqluorzgsytvorsq) for _anAttribute._
- _ALLOWS_NULL_CLAUSE_ is the string
  returned from [allowsNullClauseForConstraint](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnrwg653tjz2wy3cdnrqxk43fizxxeq3pnzzxi4tbnfxhi) with true if _anAttribute_ [allowsNull](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmfwgy33xonhhk3dm) or with false if _anAttribute_ doesn't.

---

### addInsertListAttribute

`public void addInsertListAttribute(
EOAttribute attribute,
String value)`

Adds the SQL string for _attribute_ to
a comma-separated list of attributes and _value_ to
a comma-separated list of values. Both lists are constructed for
use in an INSERT statement. Use the methods [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy) and [valueList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3wmfwhkzkmnfzxi) to access the attributes
and value lists.

Invokes [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bobygk3tejf2gk3kun5ggs43ukn2he2lom4) to
add an SQL string for _attribute_ to
the receiver's [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy),
and again to add a formatted SQL string for _value_ to
the receiver's [valueList](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3wmfwhkzkmnfzxi).

__See
Also:__  [sqlStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5df), [sqlStringForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu), [formatValueForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxivtbnr2wkrtpojaxi5dsnfrhk5df)

---

### addJoinClause

`public void addJoinClause(
String leftName,
String rightName,
int semantic)`

Creates a new join clause by invoking [assembleJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsuu33jnzbwyylvonsq) and
adds it to the receiver's join clause string. Separates join conditions
already in the join clause string with the word "and". Invoked
from [joinExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4rlyobzgk43tnfxw4).

__See
Also:__  [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4q3mmf2xgzktorzgs3th)

---

### addOrderByAttributeOrdering

`public void addOrderByAttributeOrdering(com.apple.yellow.eocontrol.EOSortOrdering sortOrdering)`

Adds an attribute-direction pair ("LAST_NAME
asc", for example) to the receiver's ORDER BY string. If _sortOrdering_'s
selector is `EOSortOrdering.CompareCaseInsensitiveAscending` or `EOSortOrdering.CompareCaseInsensitiveAscending`,
the string generated has the format "upper(attribute) direction".
Use the method [orderByString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3pojsgk4scpfjxi4tjnztq) to
access the ORDER BY string. [addOrderByAttributeOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrse64temvzee6kbor2he2lcov2gkt3smrsxe2lom4) invokes [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bobygk3tejf2gk3kun5ggs43ukn2he2lom4) to add the
attribute-direction pair.

__See Also:__  [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle)

---

### addSelectListAttribute

`public void addSelectListAttribute(EOAttribute attribute)`

Adds an SQL string for _attribute_ to
a comma-separated list of attribute names for use in a SELECT statement.
The SQL string for _attribute_ is formatted
with _attribute_'s "read" format.
Use [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy) to access
the list. __addSelectListAttribute__ invokes [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bobygk3tejf2gk3kun5ggs43ukn2he2lom4) to add the
attribute name.

__See Also:__  [sqlStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5df), [formatSQLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq), [readFormat](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpojswczcgn5zg2ylu) (EOAttribute)

---

### addUpdateListAttribute

`public void addUpdateListAttribute(
EOAttribute attribute,
String value)`

Adds an attribute-value assignment ("LAST_NAME
= ‘Thomas'", for example) to a comma-separated list for use
in an UPDATE statement. Formats _value_ with _attribute_'s
"write" format. Use [listString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mnfzxiu3uojuw4zy) to access
the list. __addUpdateListAttribute__ invokes [appendItemToListString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bobygk3tejf2gk3kun5ggs43ukn2he2lom4) to add the
attribute-value assignment.

__See Also:__  [formatSQLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq)

---

### aliasesByRelationshipPath

`public NSMutableDictionary aliasesByRelationshipPath()`

Returns a dictionary of table aliases. The keys
of the dictionary are relationship paths-"department" and
"department.location", for example. The values are the table
aliases for the corresponding table-"t1" and "t2", for
example. The [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a) dictionary
always has at least one entry: an entry for the EOSQLExpression's
entity. The key of this entry is the empty string ("") and the
value is "t0". The dictionary returned from this method is built
up over time with successive calls to [sqlStringForAttributePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfkbqxi2a).

__See
Also:__  [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q)

---

### allowsNullClauseForConstraint

`public String allowsNullClauseForConstraint(boolean flag)`

Returns according to _flag_ an
adaptor specific string for use in a CREATE TABLE statement. The returned
string indicates whether a column allows null values. EOSQLExpression's
implementation returns the empty string if _flag_ is true,
"NOT NULL" otherwise. A subclass should override this if its database
server's semantics are different. For example, the SybaseSLQExpression
returns "null" if _flag_ is true,
the empty string otherwise.

__See Also:__  [addCreateClauseForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseg4tfmf2gkq3mmf2xgzkgn5zec5duojuwe5lumu)

---

### appendItemToListString

`public void appendItemToListString(
String itemString,
String listString)`

Adds _itemString_ to
a comma-separated list. If _listString_ already
has entries, this method appends a comma followed by _itemString_.
Invoked from [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfgzlmmvrxitdjon2ec5duojuwe5lumu), [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu), [addUpdateListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfk4demf2gktdjon2ec5duojuwe5lumu), and [addOrderByAttributeOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrse64temvzee6kbor2he2lcov2gkt3smrsxe2lom4)

---

### assembleDeleteStatementWithQualifier

`public String assembleDeleteStatementWithQualifier(
com.apple.yellow.eocontrol.EOQualifier qualifier,
String tableList,
String whereClause)`

Invoked from [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q) to
return an SQL DELETE statement of the form:
> ```
> DELETE FROM tableList
> SQL_WHERE whereClause
> ```

_qualifier_ is
the argument to [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q) from
which _whereClause_ was derived. It
is provided for subclasses that need to generate the WHERE clause
in a particular way.

---

### assembleInsertStatementWithRow

`public String assembleInsertStatementWithRow(
NSDictionary row,
String tableList,
String columnList,
String valueList)`

Invoked from [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y) to
return an SQL INSERT statement of the form:
> ```
> INSERT INTO tableList (columnList)
> VALUES valueList
> ```

or,
if _columnList_ is null:

> ```
> INSERT INTO tableList
> VALUES valueList
> ```

_row_ is
the argument to [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y) from
which _columnList_ and _valueList_ were derived.
It is provided for subclasses that need to generate the list of
columns and values in a particular way.

---

### assembleJoinClause

`public String assembleJoinClause(
String leftName,
String rightName,
int semantic)`

Returns a join clause of the form:
> ```
> leftName operator rightName
> ```

Where
operator is "=" for an inner join, "\*=" for a left-outer
join, and "=\*" for a right-outer join. Invoked from [addJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseu33jnzbwyylvonsq).

---

### assembleSelectStatementWithAttributes

`public String assembleSelectStatementWithAttributes(
NSArray attributes,
boolean lock,
com.apple.yellow.eocontrol.EOQualifier qualifier,
NSArray fetchOrder,
String selectString,
String columnList,
String tableList,
String whereClause,
String joinClause,
String orderByClause,
String lockClause)`

Invoked from [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom) to
return an SQL SELECT statement of the form:
> ```
> SELECT columnList
> FROM tableList lockClause
> WHERE whereClause AND joinClause
> ORDER BY orderByClause
> ```

If _lockClause_ is null,
it is omitted from the statement. Similarly, if _orderByClause_ is null,
the "ORDER BY _orderByClause_"
is omitted. If either _whereClause_ or _joinClause_ is null,
the "AND" and null-valued argument are omitted. If both are null,
the entire WHERE clause is omitted.

_attributes_, _lock_, _qualifier_,
and _fetchOrder_ are the arguments
to [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom) from
which the other __assembleSelect...__ arguments
were derived. They are provided for subclasses that need to generate
the clauses of the SELECT statement in a particular way.

---

### assembleUpdateStatementWithRow

`public String assembleUpdateStatementWithRow(
NSDictionary row,
com.apple.yellow.eocontrol.EOQualifier qualifier,
String tableList,
String updateList,
String whereClause)`

Invoked from [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y) to
return an SQL UPDATE statement of the form:
> ```
> UPDATE tableList
> SET updateList
> WHERE whereClause
> ```

_row_ and _qualifier_ are
the arguments to [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y) from
which _updateList_ and _whereClause_ were
derived. They are provided for subclasses that need to generate
the clauses of the UPDATE statement in a particular way.

---

### bindVariableDictionaries

`public NSArray bindVariableDictionaries()`

Returns the receiver's bind variable dictionaries.
For more information on bind variables, see the discussion in the
class description.

__See Also:__  [addBindVariableDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsee2lomrlgc4tjmfrgyzkenfrxi2lpnzqxe6i)

---

### bindVariableDictionaryForAttribute

`public NSMutableDictionary bindVariableDictionaryForAttribute(
EOAttribute attribute,
Object value)`

Implemented by subclasses to create and return
the bind variable dictionary for _attribute_ and _value_. The
dictionary returned from this method must contain the following
key-value pairs:

|  |  |
| --- | --- |
| __Key__ | __Corresponding Value__ |
| `BindVariableNameKey` | Name of the bind variable for _attribute_ |
| `BindVariablePlaceHolderKey` | Placeholder string used in the SQL statement |
| `BindVariableAttributeKey` | _attribute_ |
| `BindVariableValueKey` | _value_ |

An adaptor subclass may define additional entries
as required by its RDBMS.

Invoked from [sqlStringForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu) when the message [mustUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3novzxivltmvbgs3tekzqxe2lbmjwgkrtpojaxi5dsnfrhk5df)(_attribute)_ returns true or
when the receiver's class uses bind variables and the message [shouldUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tnbxxk3dekvzwkqtjnzsfmylsnfqwe3dfizxxeqluorzgsytvorsq)(_attribute_) returns true.
For more information on bind variables, see the discussion in the
class description.

A subclass that uses bind variables
should implement this method without invoking EOSQLExpression's
implementation. The subclass implementation must return a dictionary
with entries for the keys listed above and may add additional keys.

__See
Also:__  [bindVariableDictionaryForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylspfdg64sbor2he2lcov2gk), [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fijuw4zcwmfzgsylcnrsxg)

---

### columnTypeStringForAttribute

`public String columnTypeStringForAttribute(EOAttribute anAttribute)`

Returns an adaptor specific type string for _anAttribute_ that's
suitable for use in a CREATE TABLE statement. EOSQLExpression's
implementation creates a string based on _anAttribute_'s [externalType](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpmv4hizlsnzqwyvdzobsq), [precision](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpobzgky3jonuw63q), and [width](EOAttribute.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpif2hi4tjmj2xizjpo5uwi5di) as follows:

|  |  |
| --- | --- |
| __If Condition__ | __Generated String__ |
| precision is non-zero | externalType(precision, scale) |
| precision is zero and width is non-zero | externalType(scale) |
| precision and width are zero | externalType |

A subclass should override the default implementation
if its database server requires column types in a different format.

__See
Also:__  [addCreateClauseForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseg4tfmf2gkq3mmf2xgzkgn5zec5duojuwe5lumu)

---

### entity

`public EOEntity entity()`

Returns the receiver's entity.

__See
Also:__  [EOSQLExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l2fj5jvctcfpbyhezltonuw63q) constructor

---

### externalNameQuoteCharacter

`public String externalNameQuoteCharacter()`

Returns the string ‘\"' (an escaped quote
character) if the receiver uses quoted external names, or the empty
string ("") otherwise.

__See Also:__  [useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fkf2w65dfmrcxq5dfojxgc3comfwwk4y), [sqlStringForSchemaObjectName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwg2dfnvqu6ytkmvrxittbnvsq)

---

### joinClauseString

`public String joinClauseString()`

Returns the part of the receiver's WHERE clause
that specifies join conditions. Together, the __joinExpression__ and
the [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4) make
up a statement's WHERE clause. If the receiver's statement doesn't
contain join conditions, this method returns an empty string.

An
EOSQLExpression's __joinClauseString__ is
generally set by invoking [joinExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4rlyobzgk43tnfxw4).

__See
Also:__  [addJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseu33jnzbwyylvonsq)

---

### joinExpression

`public void joinExpression()`

Builds up the [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4q3mmf2xgzktorzgs3th) for use in a SELECT
statement. For each relationship path in the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a) dictionary,
this method invokes [addJoinClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrseu33jnzbwyylvonsq) for
each of the relationship's EOJoin objects.

If the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a) dictionary
only has one entry (the entry for the EOSQLExpression's entity),
the __joinClauseString__ is empty.

You
must invoke this method after invoking [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfgzlmmvrxitdjon2ec5duojuwe5lumu) for each attribute
to be selected and after sending __sqlStringForSQLExpression__`(this)` to
the qualifier for the SELECT statement. (These methods build up
the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a) dictionary
by invoking [sqlStringForAttributePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfkbqxi2a).)

__See
Also:__  [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4)

---

### listString

`public String listString()`

Returns a comma-separated list of attributes
or "attribute = value" assignments. __listString__ is
built up with successive invocations of [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu), [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfgzlmmvrxitdjon2ec5duojuwe5lumu), or [addUpdateListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfk4demf2gktdjon2ec5duojuwe5lumu) for INSERT
statements, SELECT statements, and UPDATE statements, respectively.
The contents of __listString__ vary according
to the type of statement the receiver is building:

|  |  |
| --- | --- |
| __Type of Statement__ | __Sample listString Contents__ |
| INSERT | FIRST_NAME, LAST_NAME, EMPLOYEE_ID |
| UPDATE | FIRST_NAME = "Timothy", LAST_NAME = "Richardson" |
| SELECT | t0.FIRST_NAME, t0.LAST_NAME, t1.DEPARTMENT_NAME |

---

### lockClause

`public String lockClause()`

Overridden by subclasses to return the SQL string
used in a SELECT statement to lock selected rows. A concrete subclass
of EOSQLExpression must override this method to return the string
used by its adaptor's RDBMS.

---

### mustUseBindVariableForAttribute

`public boolean mustUseBindVariableForAttribute(EOAttribute attribute)`

Returns true if the receiver must use bind variables
for _attribute_, false otherwise. EOSQLExpression's implementation
returns false. An SQL expression subclass that uses bind variables
should override this method to return true if the underlying RDBMS
requires that bind variables be used for attributes with _attribute_'s
external type.

__See Also:__  [shouldUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tnbxxk3dekvzwkqtjnzsfmylsnfqwe3dfizxxeqluorzgsytvorsq), [bindVariableDictionaryForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylspfdg64sbor2he2lcov2gk)

---

### orderByString

`public String orderByString()`

Returns the comma-separated list of "attribute
direction" pairs ("LAST_NAME asc, FIRST_NAME asc", for example)
for use in a SELECT statement.

__See Also:__  [addOrderByAttributeOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrse64temvzee6kbor2he2lcov2gkt3smrsxe2lom4)

---

### prepareConstraintStatementForRelationship

`public void prepareConstraintStatementForRelationship(
EORelationship relationship,
NSArray sourceColumns,
NSArray destinationColumns)`

Sets the receiver's [statement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3torqxizlnmvxhi) to an adaptor specific
constraint for _relationship_. EOSQLExpression's implementation
generates statements of the form:
> ```
> ALTER TABLE TABLE_NAME ADD CONSTRAINT CONSTRAINT_NAME
>     FOREIGN KEY (SOURCE_KEY_LIST)
>     REFERENCES DESTINATION_TABLE_NAME (DESTINATION_KEY_LIST)
> ```

Where

- _TABLE_NAME_ is the external
  name of the receiver's entity.
- _CONSTRAINT_NAME_ is the external
  name of the receiver's entity, _relationship_'s
  name, and the string "FK", concatenated with underbars between
  them (EMPLOYEE_MANAGER_FK, for example),
- _SOURCE_KEY_LIST_ is a comma-separated
  list of the source columns in _sourceColumns_.
- _DESTINATION_TABLE_NAME_ is the
  external name of _relationship_'s
  destination entity.
- _DESTINATION_KEY_LIST_ is a comma-separated
  list of the destination columns in _destinationColumns_

__See
Also:__  [foreignKeyConstraintStatementsForRelationship](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33smvuwo3slmv4ug33oon2heyljnz2fg5dborsw2zloorzum33skjswyylunfxw443infya)

---

### prepareDeleteExpressionForQualifier

`public void prepareDeleteExpressionForQualifier(
com.apple.yellow.eocontrol.EOQualifier qualifier)`

Generates a DELETE statement by performing the
following steps:

1. Sends an __sqlStringForSQLExpression__`(this)` message
   to _qualifier_ to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4).
2. Invokes [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q) to
   get the table name for the FROM clause.
3. Invokes [assembleDeleteStatementWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsuizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls).

__See
Also:__  [deleteStatementWithQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwizlmmv2gku3umf2gk3lfnz2fo2lunbixkylmnftgszls)

---

### prepareInsertExpressionWithRow

`public void prepareInsertExpressionWithRow(NSDictionary row)`

Generates an INSERT statement by performing
the following steps:

1. Invokes [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu) for each entry
   in _row_ to prepare the comma-separated
   list of attributes and the corresponding list of values.
2. Invokes [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q) to
   get the table name.
3. Invokes [assembleInsertStatementWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsus3ttmvzhiu3umf2gk3lfnz2fo2lunbjg65y).

__See
Also:__  [insertStatementForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxws3ttmvzhiu3umf2gk3lfnz2em33skjxxo)

---

### prepareSelectExpressionWithAttributes

`public void prepareSelectExpressionWithAttributes(
NSArray attributes,
boolean flag,
com.apple.yellow.eocontrol.EOFetchSpecification fetchSpecification)`

Generates a SELECT statement by performing the
following steps:

1. Invokes [addSelectListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfgzlmmvrxitdjon2ec5duojuwe5lumu) for each entry
   in _attributes_ to prepare the comma-separated
   list of attributes.
2. Sends an __sqlStringForSQLExpression__`(this)`message
   to _fetchSpecification_'s qualifier
   to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4).
3. Invokes [addOrderByAttributeOrdering](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrse64temvzee6kbor2he2lcov2gkt3smrsxe2lom4) for
   each EOAttributeOrdering object in fetchSpecification.First
   conjoins the qualifier in _fetchSpecification_ with
   the restricting qualifier, if any, of the receiver's entity.
4. Invokes [joinExpression](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4rlyobzgk43tnfxw4) to
   generate the receiver's [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4q3mmf2xgzktorzgs3th).
5. Invokes [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q) to
   get the comma-separated list of tables for the FROM clause.
6. If _flag_ is true, invokes [lockClause](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3mn5rwwq3mmf2xgzi) to get
   the SQL string to lock selected rows.
7. Invokes [assembleSelectStatementWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvgzlmmvrxiu3umf2gk3lfnz2fo2lunbaxi5dsnfrhk5dfom).

__See
Also:__  [selectStatementForAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxgzlmmvrxiu3umf2gk3lfnz2em33sif2hi4tjmj2xizlt)

---

### prepareUpdateExpressionWithRow

`public void prepareUpdateExpressionWithRow(
NSDictionary row,
com.apple.yellow.eocontrol.EOQualifier qualifier)`

Generates an UPDATE statement by performing
the following steps:

1. Invokes [addUpdateListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsfk4demf2gktdjon2ec5duojuwe5lumu) for each entry
   in _row_ to prepare the comma-separated
   list of "attribute = value" assignments.
2. Sends an __sqlStringForSQLExpression__`(this)`message
   to _qualifier_ to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4).
3. Invokes [tableListWithRootEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3umfrgyzkmnfzxiv3jorufe33porcw45djor4q) to
   get the table name for the FROM clause.
4. Invokes [assembleUpdateStatementWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bonzwk3lcnrsvk4demf2gku3umf2gk3lfnz2fo2lunbjg65y).

__See
Also:__  [updateStatementForRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk4demf2gku3umf2gk3lfnz2em33skjxxo)

---

### setStatement

`public void setStatement(String string)`

Sets the receiver's SQL statement to _string_,
which should be a valid expression in the target query language.
Use this method-instead of a __prepare...__ method-to
directly assign an SQL string to an EOSQLExpression object. This
method does not perform substitutions or formatting of any kind.

__See
Also:__  [expressionForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwk6dqojsxg43jn5xem33skn2he2lom4), [statement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3torqxizlnmvxhi)

---

### setUseAliases

`public void setUseAliases(boolean flag)`

Tells the receiver whether or not to use table
aliases.

__See Also:__  [useAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3vonsuc3djmfzwk4y)

---

### shouldUseBindVariableForAttribute

`public boolean shouldUseBindVariableForAttribute(EOAttribute attribute)`

Returns true if the receiver can provide a bind
variable dictionary for _attribute_, false otherwise.
Bind variables aren't used for values associated with this attribute
when the static method [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fijuw4zcwmfzgsylcnrsxg) returns false. EOSQLExpression's
implementation returns false. An SQL expression subclass should override
this method to return true if the receiver should use bind variables
for attributes with _attribute_'s
external type. It should also return true for any attribute for
which the receiver must use bind variables.

__See
Also:__  [mustUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3novzxivltmvbgs3tekzqxe2lbmjwgkrtpojaxi5dsnfrhk5df)

---

### sqlStringForAttribute

`public String sqlStringForAttribute(EOAttribute attribute)`

Returns the SQL string for attribute, complete
with a table alias if the receiver uses table aliases. Invoked from [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle) when the
attribute name is not a path.

__See Also:__  [sqlStringForAttributePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfkbqxi2a)

---

### sqlStringForAttributeNamed

`public String sqlStringForAttributeNamed(String name)`

Returns the SQL string for the attribute named _name_,
complete with a table alias if the receiver uses table aliases.
Generates the return value using [sqlStringForAttributePath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfkbqxi2a) if _name_ is
an attribute path ("department.name", for example); otherwise,
uses [sqlStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5df).

---

### sqlStringForAttributePath

`public String sqlStringForAttributePath(NSArray path)`

Returns the SQL string for _path_,
complete with a table alias if the receiver uses table aliases.
Invoked from [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle) when the
specified attribute name is a path ("department.location.officeNumber",
for example). _path_ is an array of
any number of EORelationship objects followed by an EOAttribute
object. The EORelationship and EOAttribute objects each correspond
to a component in path. For example, if the attribute name argument
to __sqlStringForAttributeNamed__ is "department.location.officeNumber", _path_ is
an array containing the following objects in the order listed:

- The EORelationship object in the receiver's entity named
  "department". (Assume the relationship's destination entity
  is named "Department".)
- The EORelationship object in the Department entity named "location".
  (Assume the relationship's destination entity is named "Location".)
- The EOAttribute object in the Location entity named "officeNumber".

Assuming
that the receiver uses aliases and the alias for the Location table
is t2, the SQL string for this sample attribute path is "t2.officeNumber".

If
the receiver uses table aliases, this method has the side effect
of adding a "relationship path"-"alias name" entry to the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a) dictionary.

__See
Also:__  [sqlStringForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5df), [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a)

---

### sqlStringForCaseInsensitiveLike

`public String sqlStringForCaseInsensitiveLike(
String valueString,
String keyString)`

Overridden by subclasses to return a case insensitive
comparison of _valueString_ and _keyString_.
For example, a subclass implementation might return the string "UPPER(_keyString_)
LIKE UPPER(_valueString_)".

---

### sqlStringForConjoinedQualifiers

`public String sqlStringForConjoinedQualifiers(NSArray qualifiers)`

Creates and returns an SQL string that is the
result of interposing the word "AND" between the SQL strings
for the qualifiers in _qualifiers_.
Generates an SQL string for each qualifier by sending sqlStringForSQLExpression: messages
to the qualifiers with `this` as
the argument. If the SQL string for a qualifier contains only white
space, it isn't included in the return value. The return value
is enclosed in parentheses if the SQL strings for two or more qualifiers
were ANDed together.

---

### sqlStringForDisjoinedQualifiers

`public String sqlStringForDisjoinedQualifiers(NSArray qualifiers)`

Creates and returns an SQL string that is the
result of interposing the word "OR" between the SQL strings
for the qualifiers in _qualifiers_.
Generates an SQL string for each qualifier by sending sqlStringForSQLExpression: messages
to the qualifiers with this as the argument. If the SQL string for a
qualifier contains only white space, it isn't included in the
return value. The return value is enclosed in parentheses if the
SQL strings for two or more qualifiers were ORed together.

---

### sqlStringForKeyComparisonQualifier

`public String sqlStringForKeyComparisonQualifier(
com.apple.yellow.eocontrol.EOKeyComparisonQualifier qualifier)`

Creates and returns an SQL string that is the
result of interposing an operator between the SQL strings for the
right and left keys in _qualifier_.
Determines the SQL operator by invoking [sqlStringForSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwk3dfmn2g64q) with _qualifier_'s
selector and null for the value. Generates SQL strings for _qualifier_'s
keys by invoking [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle) to
get SQL strings. This method also formats the strings for the right
and left keys using [formatSQLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq) with
the corresponding attributes' "read" formats.

---

### sqlStringForKeyValueQualifier

`public String sqlStringForKeyValueQualifier(
com.apple.yellow.eocontrol.EOKeyValueQualifier qualifier)`

Creates and returns an SQL string that is the
result of interposing an operator between the SQL strings for _qualifier_'s
key and value. Determines the SQL operator by invoking [sqlStringForSelector](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojjwk3dfmn2g64q) with _qualifier_'s
selector and value. Generates an SQL string for _qualifier_'s
key by invoking [sqlStringForAttributeNamed](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojaxi5dsnfrhk5dfjzqw2zle) to
get an SQL string and [formatSQLString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxiu2rjrjxi4tjnztq) with
the corresponding attribute's "read" format. Similarly, generates
an SQL string for qualifier's value by invoking [sqlStringForValue](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojlgc3dvmu) to get an SQL string
and [formatValueForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxivtbnr2wkrtpojaxi5dsnfrhk5df) to format
it. (First invokes [sqlPatternFromShellPattern](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxg4lmkbqxi5dfojxem4tpnvjwqzlmnrigc5dumvzg4) for
the value if _qualifier_'s selector
is `EOQualifier.QualifierOperatorLike`.)

---

### sqlStringForNegatedQualifier

`public String sqlStringForNegatedQualifier(com.apple.yellow.eocontrol.EOQualifier qualifier)`

Creates and returns an SQL string that is the
result of surrounding the SQL string for _qualifier_ in parentheses
and appending it to the word "not". For example, if the string
for _qualifier_ is "FIRST_NAME =
‘John'", __sqlStringForNegatedQualifier__ returns
the string "not (FIRST_NAME = ‘John')".

Generates an
SQL string for _qualifier_ by sending
an sqlStringForSQLExpression: message
to _qualifier_ with this as the argument.
If the SQL string for _qualifier_ contains
only white space, this method returns null.

---

### sqlStringForQualifier

`public String sqlStringForQualifier(com.apple.yellow.eocontrol.EOQualifier aQualifier)`

Returns a SQL statement for _aQualifier_ suitable
for inclusion in a WHERE clause. Invoked from an EOSQLExpression
while it's preparing a SELECT, UPDATE, or DELETE statement.

__See
Also:__  [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3xnbsxezkdnrqxk43fkn2he2lom4)

---

### sqlStringForSchemaObjectName

`public String sqlStringForSchemaObjectName(String name)`

Returns _name_ enclosed
in the external name quote character if the receiver uses quoted
external names, otherwise simply returns _name_ unaltered.

__See
Also:__  [useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fkf2w65dfmrcxq5dfojxgc3comfwwk4y), [externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3fpb2gk4tomfwe4ylnmvixk33umvbwqylsmfrxizls)

---

### sqlStringForSelector

`public String sqlStringForSelector(
NSSelector selector,
Object value)`

Returns an SQL operator for _selector_ and _value_.
The possible values for _selector_ are
defined as constants (in EOControl). The following table summarizes
EOSQLExpression's default mapping:

|  |  |
| --- | --- |
| __Selector (Constant)__ | __SQL Operator__ |
| `EOQualifier.QualifierOperatorIsEqual` | "is" if value is an EONullValue, "=" otherwise |
| `EOQualifier.QualifierOperatorNotEqual` | "is not" if _value_ is an EONullValue, "<>" otherwise |
| `EOQualifier.QualifierOperatorLessThan` | "<" |
| `EOQualifier.QualifierOperatorGreaterThan` | ">" |
| `EOQualifier.QualifierOperatorLessThanOrEqualTo` | "<=" |
| `EOQualifier.QualifierOperatorGreaterThanOrEqualTo` | ">=" |
| `EOQualifier.QualifierOperatorLike` | "like" |

Throws an exception if _selector_ is
an unknown operator.

__See Also:__  [sqlStringForKeyComparisonQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojfwk6kdn5wxaylsnfzw63srovqwy2lgnfsxe), [sqlStringForKeyValueQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tofwfg5dsnfxgortpojfwk6kwmfwhkzkrovqwy2lgnfsxe)

---

### sqlStringForValue

`public String sqlStringForValue(
Object value,
String name)`

Returns a string for _value_ appropriate
for use in an SQL statement. If the receiver uses a bind variable for
the attribute named _name_, then __sqlStringForValue__ gets
the bind variable dictionary for the attribute, adds it to the receiver's
array of bind variables dictionaries, and returns the value for
the binding's [BindVariablePlaceHolderKey](#apple-ijduorkcincuq).
Otherwise, this method invokes [formatValueForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwm33snvqxivtbnr2wkrtpojaxi5dsnfrhk5df) and
returns the formatted string for _value_.

__See
Also:__  [mustUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3novzxivltmvbgs3tekzqxe2lbmjwgkrtpojaxi5dsnfrhk5df), [shouldUseBindVariableForAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tnbxxk3dekvzwkqtjnzsfmylsnfqwe3dfizxxeqluorzgsytvorsq), [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxxk43fijuw4zcwmfzgsylcnrsxg), [bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3cnfxgivtbojuwcytmmvcgsy3unfxw4ylsnfsxg), [addBindVariableDictionary](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrsee2lomrlgc4tjmfrgyzkenfrxi2lpnzqxe6i)

---

### statement

`public String statement()`

Returns the complete SQL statement for the receiver.
An SQL statement can be assigned to an EOSQLExpression object directly
using the static method [expressionForString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3dnf5cu6u2rjrcxq4dsmvzxg2lpnyxwk6dqojsxg43jn5xem33skn2he2lom4) or
using the instance method [setStatement](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fg5dborsw2zlooq). Generally, however,
an EOSQLExpression's statement is built up using one of the following
methods:

- [prepareSelectExpressionWithAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvjwk3dfmn2ek6dqojsxg43jn5xfo2lunbaxi5dsnfrhk5dfom)
- [prepareInsertExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvew443foj2ek6dqojsxg43jn5xfo2lunbjg65y)
- [prepareUpdateExpressionWithRow](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvkxazdborsuk6dqojsxg43jn5xfo2lunbjg65y)
- [prepareDeleteExpressionForQualifier](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3qojsxaylsmvcgk3dforsuk6dqojsxg43jn5xem33skf2wc3djmzuwk4q)

---

### tableListWithRootEntity

`public String tableListWithRootEntity(EOEntity entity)`

Returns the comma-separated list of tables for
use in a SELECT, UPDATE, or DELETE statement's FROM clause. If
the receiver doesn't use table aliases, the table list consists
only of the table name for _entity_-"EMPLOYEE",
for example. If the receiver does use table aliases (only in SELECT
statements by default), the table list is a comma separated list
of table names and their aliases, for example:
> ```
> EMPLOYEE t0, DEPARTMENT t1
> ```

__tableListWithRootEntity__ creates
a string containing the table name for _entity_ and
a corresponding table alias ("EMPLOYEE t0", for example). For
each entry in [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a),
this method appends a new table name and table alias.

__See
Also:__  [useAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3vonsuc3djmfzwk4y), [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a)

---

### useAliases

`public boolean useAliases()`

Returns true if the receiver generates statements
with table aliases, false otherwise. For example, the following
SELECT statement uses table aliases:
> ```
> SELECT t0.FIRST_NAME, t0.LAST_NAME, t1.NAME
> FROM EMPLOYEE t0, DEPARTMENT t1
> WHERE t0.DEPARTMENT_ID = t1.DEPARTMENT_ID
> ```

The
EMPLOYEE table has the alias t0, and the DEPARTMENT table has the
alias t1.

By default, EOSQLExpression uses table aliases
only in SELECT statements. Enterprise Objects Framework assumes
that INSERT, UPDATE, and DELETE statements are single-table operations.
For more information, see the discussion in the class description.

__See
Also:__  [setUseAliases](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3tmv2fk43fifwgsyltmvzq), [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bnruwc43fonbhsutfnrqxi2lpnzzwq2lqkbqxi2a)

---

### valueList

`public String valueList()`

Returns the comma-separated list of values used
in an INSERT statement. For example, the value list for the following
INSERT statement:
> ```
> INSERT EMPLOYEE (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, DEPARTMENT_ID, SALARY)
> VALUES ('Shaun', 'Hayes', 1319, 23, 4600)
> ```

is
"‘Shaun', ‘Hayes', 1319, 23, 4600". An EOSQLExpression's `valueList` is
generated a value at a time with [addInsertListAttribute](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3bmrses3ttmvzhitdjon2ec5duojuwe5lumu) messages.

---

### whereClauseString

`public String whereClauseString()`

Returns the part of the receiver's WHERE clause
that qualifies rows. The whereClauseString does not specify join
conditions; the [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l3kn5uw4q3mmf2xgzktorzgs3th) does
that. Together, the __whereClauseString__ and
the __joinClauseString__ make up a statement's
where clause. For example, a qualifier for an Employee entity specifies
that a statement only affects employees who belong to the Finance
department and whose monthly salary is greater than $4500. Assume
the corresponding where clause looks like this:
> ```
> WHERE EMPLOYEE.SALARY > 4500 AND DEPARTMENT.NAME = ‘Finance'
>     AND EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID
> ```

EOSQLExpression
generates both a __whereClauseString__ and
a __joinClauseString__ for this qualifier.
The __whereClauseString__ qualifies the rows
and looks like this:

> ```
> EMPLOYEE.SALARY > 4500 AND DEPARTMENT.NAME = ‘Finance'
> ```

The __joinClauseString__ specifies
the join conditions between the EMPLOYEE table and the DEPARTMENT
table and looks like this:

> ```
> EMPLOYEE.DEPARTMENT_ID = DEPARTMENT.DEPARTMENT_ID
> ```

An
EOSQLExpression's __whereClauseString__ is
generally set by sending a sqlStringForSQLExpression: message
to an EOQualifier object.

__See Also:__  sqlStringForSQLExpression: (EOQualifierSQLGeneration
protocol)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
