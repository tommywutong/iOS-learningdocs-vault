---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EOSQLExpression.html
archived_at: '2026-07-15T08:11:33.785676Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOAccess Reference

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md) 

# EOSQLExpression

> __Inherits
> from:__  NSObject

> __Conforms to:__  NSObject
> (NSObject)

> __Declared in:__  EOAccess/EOSQLExpression.h
> EOAccess/EOSchemaGeneration.h
> EOAccess/EOSchemaSynchronization.h

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
with the EOSQLExpression class method [expressionForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi),
and send the expression object to an adaptor channel using [EOAdaptorChannel](EOAdaptorChannel-3.md#apple-ijaucqsbjfcei)'s [evaluateExpression:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3fozqwy5lborsuk6dqojsxg43jn5xdu) method.

For more information on using EOSQLExpressions, see the following
sections:

- ["Building Expressions"](EOSQLExpression-4.md#apple-ijduoq2ki5ceu)
- ["Using Table Aliases"](EOSQLExpression-4.md#apple-ijduoqscincec)
- ["Bind Variables"](EOSQLExpression-4.md#apple-ijduoq2bi5eei)
- ["Schema Generation"](EOSQLExpression-4.md#apple-ijduoq2cijbue)

## Constants

---

In EOSQLExpression.h, EOSchemaGeneration.h,
and EOSchemaSynchronization.h, EOAccess defines
the following NSString constants.

|  |  |
| --- | --- |
| __Constant__ | __Description__ |
| EOBindVariableNameKey | The key for the name of a bind variable in a bind variable dictionary. |
| EOBindVariablePlaceHolderKey | A key for use in bind variable dictionaries. The corresponding value is the placeholder string to be used in SQL. |
| EOBindVariableAttributeKey | A key for use in bind variable dictionaries. The corresponding value is the attribute that uses the bind variable. |
| EOBindVariableValueKey | A key for use in bind variable dictionaries. The corresponding value is the value for the bind variable. |
| EOCreateTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create tables. |
| EODropTablesKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop tables. |
| EOCreatePrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key support. |
| EODropPrimaryKeySupportKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop primary key support. |
| EOPrimaryKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create primary key constraints. |
| EOForeignKeyConstraintsKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create foreign key constraints. |
| EOCreateDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to create a database. |
| EODropDatabaseKey | Key for use in options dictionaries. A corresponding value of "YES" indicates that the EOSQLExpression should generate SQL to drop a database. |
| EOAllowsNullKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| EOColumnNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| EOExternalNameKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| EOExternalTypeKey | Key for use in change dictionaries. A corresponding value indicates that the column's allows NULL value should be changed from. |
| EONameKey | Key for use in change dictionaries. A corresponding value indicates the old value of the table or column. |
| EOPrecisionKey | Key for use in change dictionaries. A corresponding value indicates the value a column's precision should be changed from. |
| EORelationshipsKey | Key for use in change dictionaries. The corresponding value is a dictionary of relationships which have been modified since the last time the model and schema were sychronized. For more information see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). |
| EOScaleKey | Key for use in change dictionaries. A corresponding value indicates the value the column's scale should be changed from. |
| EOWidthKey | Key for use in change dictionaries. A corresponding value indicates the value the column's width should be changed from. |

## Method Types

---

> **Creating an EOSQLExpression
> object**
> : [+ selectStatementForAttributes:lock:fetchSpecification:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk3dfmn2fg5dborsw2zloordg64sbor2he2lcov2gk4z2nrxwg2z2mzsxiy3iknygky3jmzuwgylunfxw4otfnz2gs5dzhi)
> : [+ insertStatementForRow:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5uw443foj2fg5dborsw2zloordg64ssn53tuzlooruxi6j2)
> : [+ updateStatementForRow:qualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xazdborsvg5dborsw2zloordg64ssn53tu4lvmfwgsztjmvzduzlooruxi6j2)
> : [+ deleteStatementWithQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2mvxhi2lupe5a)
> : [+ expressionForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi)
> : [- initWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62lonf2fo2lunbcw45djor4tu)
>
> **Building SQL Expressions**
> : [- prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2)
> : [- prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq)
> : [- prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq)
> : [- prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq)
> : [- setStatement:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forjxiylumvwwk3tuhi)
> : [- statement](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643umf2gk3lfnz2a)
>
> **Generating SQL for attributes
> and values**
> : [+ formatSQLString:format:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq)
> : [+ formatValue:forAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fmylmovstuztpojaxi5dsnfrhk5dfhi)
> : [+ formatStringValue:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fg5dsnfxgovtbnr2wkoq)
> : [- sqlStringForValue:attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi)
> : [- sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2)
> : [- sqlStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizj2)
> : [- sqlStringForAttributePath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkqmf2gqoq)
>
> **Generating SQL for names
> of database objects**
> : [- sqlStringForSchemaObjectName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknrwqzlnmfhwe2tfmn2e4ylnmu5a)
> : [+ setUseQuotedExternalNames:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk5cvonsvc5lporswirlyorsxe3tbnrhgc3lfom5a)
> : [+ useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkrovxxizleiv4hizlsnzqwyttbnvsxg)
> : [- externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlyorsxe3tbnrhgc3lfkf2w65dfinugc4tbmn2gk4q)
>
> **Generating an attribute
> list**
> : [- addSelectListAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5dfhi)
> : [- addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a)
> : [- addUpdateListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrkxazdborsuy2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a)
> : [- appendItem:toListString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylqobsw4zcjorsw2otun5ggs43ukn2he2lom45a)
> : [- listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo)
>
> **Generating a value list**
> : [- addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a)
> : [- addUpdateListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrkxazdborsuy2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a)
> : [- valueList](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65tbnr2wktdjon2a)
>
> **Generating a table list**
> : [- tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a)
> : [- aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq)
>
> **Generating the join clause**
> : [- joinExpression](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxek6dqojsxg43jn5xa)
> : [- addJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a)
> : [- assembleJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a)
> : [- joinClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxeg3dbovzwku3uojuw4zy)
>
> **Generating a search pattern**
> : [+ sqlPatternFromShellPattern:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxc3cqmf2hizlsnzdhe33nknugk3dmkbqxi5dfojxdu)
> : [+ sqlPatternFromShellPattern:withEscapeCharacter:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxc3cqmf2hizlsnzdhe33nknugk3dmkbqxi5dfojxdu53joruek43dmfygkq3imfzgcy3umvzdu)
>
> **Generating a relational
> operator**
> : [- sqlStringForSelector:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknswyzldorxxeotwmfwhkzj2)
>
> **Accessing the where clause**
> : [- whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th)
>
> **Generating an order by
> clause**
> : [- addOrderByAttributeOrdering:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrhxezdfojbhsqluorzgsytvorsu64temvzgs3thhi)
> : [- orderByString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc633smrsxeqtzkn2he2lom4)
>
> **Accessing the lock clause**
> : [- lockClause](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63dpmnvug3dbovzwk)
>
> **Assembling a statement**
> : [- assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder:selectString:columnList:tableList:whereClause:joinClause:orderByClause:lockClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvjwk3dfmn2fg5dborsw2zloorlws5diif2hi4tjmj2xizlthjwg6y3lhjyxkylmnftgszlshjtgk5ddnbhxezdfoi5hgzlmmvrxiu3uojuw4zz2mnxwy5lnnzggs43uhj2gcytmmvggs43uhj3wqzlsmvbwyylvonstu2tpnfxeg3dbovzwkotpojsgk4scpfbwyylvonstu3dpmnvug3dbovzwkoq)
> : [- assembleInsertStatementWithRow:tableList:columnList:valueList:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvew443foj2fg5dborsw2zloorlws5dikjxxootumfrgyzkmnfzxiotdn5whk3lojruxg5b2ozqwy5lfjruxg5b2)
> : [- assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvkxazdborsvg5dborsw2zloorlws5dikjxxootrovqwy2lgnfsxeotumfrgyzkmnfzxiotvobsgc5dfjruxg5b2o5ugk4tfinwgc5ltmu5a)
> : [- assembleDeleteStatementWithQualifier:tableList:whereClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvcgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2orqwe3dfjruxg5b2o5ugk4tfinwgc5ltmu5a)
>
> **Generating SQL for qualifiers**
> : [- sqlStringForConjoinedQualifiers:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sinxw42tpnfxgkzcrovqwy2lgnfsxe4z2)
> : [- sqlStringForDisjoinedQualifiers:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33siruxg2tpnfxgkzcrovqwy2lgnfsxe4z2)
> : [- sqlStringForKeyComparisonQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvzdu)
> : [- sqlStringForKeyValueQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjnsxsvtbnr2wkulvmfwgsztjmvzdu)
> : [- sqlStringForNegatedQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjzswoylumvsfc5lbnruwm2lfoi5a)
>
> **Managing bind variables**
> : [+ setUseBindVariables:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk5cvonsue2lomrlgc4tjmfrgyzlthi)
> : [+ useBindVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkcnfxgivtbojuwcytmmvzq)
> : [- addBindVariableDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbgs3tekzqxe2lbmjwgkrdjmn2gs33omfzhsoq)
> : [- bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tjmvzq)
> : [- bindVariableDictionaryForAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq)
> : [- mustUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)
> : [- shouldUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a)
>
> **Using table aliases**
> : [- setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)
> : [- useAliases](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65ltmvawy2lbonsxg)
>
> **Accessing the entity**
> : [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlooruxi6i)
>
> **Creating a schema generation
> script**
> : [+ schemaCreationScriptForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33oknrxe2lqordg64sfnz2gs5djmvztu33qoruw63tthi)
> : [+ schemaCreationStatementsForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2)
> : [+ appendExpression:toScript:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5qxa4dfnzsek6dqojsxg43jn5xdu5dpknrxe2lqoq5a)
> : [+ createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a)
> : [+ createTableStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33vobztu)
> : [+ dropTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkrqwe3dfkn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4b2)
> : [+ dropTableStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkrqwe3dfkn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4dthi)
> : [+ primaryKeyConstraintStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqhi)
> : [+ primaryKeyConstraintStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom5a)
> : [+ primaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovydu)
> : [+ primaryKeySupportStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhgoq)
> : [+ dropPrimaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkbzgs3lboj4uwzlzkn2xa4dpoj2fg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a)
> : [+ dropPrimaryKeySupportStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkbzgs3lboj4uwzlzkn2xa4dpoj2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobztu)
> : [- addCreateClauseForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbxezlborsug3dbovzwkrtpojaxi5dsnfrhk5dfhi)
> : [- columnTypeStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6y3pnr2w23supfygku3uojuw4z2gn5zec5duojuwe5lumu5a)
> : [- allowsNullClauseForConstraint:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnrxxo42oovwgyq3mmf2xgzkgn5zeg33oon2heyljnz2du)
> : [+ foreignKeyConstraintStatementsForRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tfnftw4s3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64ssmvwgc5djn5xhg2djoa5a)
> : [- prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfinxw443uojqws3tukn2gc5dfnvsw45cgn5zfezlmmf2gs33oonugs4b2onxxk4tdmvbw63dvnvxhgotemvzxi2lomf2gs33oinxwy5lnnzztu)
> : [- createDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsuiylumfrgc43fkn2gc5dfnvsw45dtizxxeq3pnzxgky3unfxw4rdjmn2gs33omfzhsotbmrwws3tjon2heylunf3gkq3pnzxgky3unfxw4rdjmn2gs33omfzhsoq)
> : [- dropDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qirqxiylcmfzwku3umf2gk3lfnz2hgrtpojbw63tomvrxi2lpnzcgsy3unfxw4ylspe5gczdnnfxgs43uojqxi2lwmvbw63tomvrxi2lpnzcgsy3unfxw4ylspe5a)
>
> **Synchronizing the database
> with a model**
> : [+ statementsToUpdateObjectStoreForModel:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxetlpmrswyotxnf2gqq3imfxgozkenfrxi2lpnzqxe6j2n5yhi2lpnzztu)
> : [+ statementsToUpdateObjectStoreForEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxerlooruxi6khojxxk4b2o5uxi2cdnbqw4z3firuwg5djn5xgc4tzhjxxa5djn5xhgoq)
> : [+ statementsToCopyTableNamed:intoTableForEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6q3pob4viylcnrsu4ylnmvsdu2loorxviylcnrsum33sivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi)
> : [+ phraseCastingColumnNamed:fromType:toType:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5ygq4tbonsugyltoruw4z2dn5whk3lojzqw2zlehjthe33nkr4xazj2orxvi6lqmu5g64dunfxw44z2)
> : [+ statementsToRenameTableNamed:newName:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6utfnzqw2zkumfrgyzkomfwwkzb2nzsxottbnvstu33qoruw63tthi)
> : [+ statementsToInsertColumnForAttribute:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6sloonsxe5cdn5whk3loizxxeqluorzgsytvorstu33qoruw63tthi)
> : [+ statementsToDeleteColumnNamed:inTableNamed:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6rdfnrsxizkdn5whk3lojzqw2zlehjuw4vdbmjwgkttbnvswiotpob2gs33oom5a)
> : [+ statementsToRenameColumnNamed:inTableNamed:newName:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6utfnzqw2zkdn5whk3lojzqw2zlehjuw4vdbmjwgkttbnvswiotomv3u4ylnmu5g64dunfxw44z2)
> : [+ statementsToModifyColumnNamed:inTableNamed:toNullRule:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6tlpmruwm6kdn5whk3lojzqw2zlehjuw4vdbmjwgkttbnvswiotun5hhk3dmkj2wyzj2)
> : [+ statementsToConvertColumnNamed:inTableNamed:fromType:toType:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6q3pnz3gk4tuinxwy5lnnzhgc3lfmq5gs3sumfrgyzkomfwwkzb2mzzg63kupfygkotun5khs4dfhjxxa5djn5xhgoq)
> : [+ isColumnType:equivalentToColumnType:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5uxgq3pnr2w23supfygkotfof2ws5tbnrsw45cun5bw63dvnvxfi6lqmu5g64dunfxw44z2)
> : [+ statementsToDropForeignKeyConstraintsOnEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6rdsn5yem33smvuwo3slmv4ug33oon2heyljnz2hgt3oivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi)
> : [+ statementsToDropPrimaryKeyConstraintsOnEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6rdsn5yfa4tjnvqxe6klmv4ug33oon2heyljnz2hgt3oivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi)
> : [+ statementsToDropPrimaryKeySupportForEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6rdsn5yfa4tjnvqxe6klmv4vg5lqobxxe5cgn5zek3tunf2hsr3sn52xaotxnf2gqq3imfxgozkenfrxi2lpnzqxe6j2n5yhi2lpnzztu)
> : [+ statementsToImplementForeignKeyConstraintsOnEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6slnobwgk3lfnz2em33smvuwo3slmv4ug33oon2heyljnz2hgt3oivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi)
> : [+ statementsToImplementPrimaryKeyConstraintsOnEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6slnobwgk3lfnz2fa4tjnvqxe6klmv4ug33oon2heyljnz2hgt3oivxhi2lupfdxe33voa5ho2lunbbwqylom5sui2ldoruw63tboj4tu33qoruw63tthi)
> : [+ statementsToImplementPrimaryKeySupportForEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6slnobwgk3lfnz2fa4tjnvqxe6klmv4vg5lqobxxe5cgn5zek3tunf2hsr3sn52xaotxnf2gqq3imfxgozkenfrxi2lpnzqxe6j2n5yhi2lpnzztu)
>
> **Querying about database
> synchronization support**
> : [+ supportsSchemaSynchronization](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42tmnugk3lbkn4w4y3iojxw42l2mf2gs33o)
> : [+ supportsDirectColumnCoercion](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42enfzgky3uinxwy5lnnzbw6zlsmnuw63q)
> : [+ supportsDirectColumnDeletion](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42enfzgky3uinxwy5lnnzcgk3dforuw63q)
> : [+ supportsDirectColumnInsertion](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42enfzgky3uinxwy5lnnzew443foj2gs33o)
> : [+ supportsDirectColumnNullRuleModification](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42enfzgky3uinxwy5lnnzhhk3dmkj2wyzknn5sgsztjmnqxi2lpny)
> : [+ supportsDirectColumnRenaming](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxk4dqn5zhi42enfzgky3uinxwy5lnnzjgk3tbnvuw4zy)

## Class Methods

---

### appendExpression:toScript:

`+ (void)appendExpression:(EOSQLExpression
*)anSQLExpression
toScript:(NSMutableString *)script`

Append's _anSQLExpression_'s [statement](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643umf2gk3lfnz2a) to _script_ along
with any necessary delimiter. EOSQLExpression's implementation
appends the SQL statement for _anSQLExpression_ to _script_ followed
by a semicolon and a newline. A subclass of EOSQLExpression only
needs to override this method if the delimiter for its database
server is different. For example, the Oracle and Informix use the default
implementation, whereas the Sybase adaptor appends the word "go"
instead of a semicolon.

__See Also:__  [+ createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a)

---

### createDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:

`+ (NSArray *)createDatabaseStatementsForConnectionDictionary:(NSDictionary
*)connectionDictionary
administrativeConnectionDictionary:(NSDictionary
*)adminDictionary`

Generates the SQL statements that will create
a database (or user, for Oracle) that can be accessed by the provided
connection dictionary and administrative connection dictionary.

__See
Also:__  [+ dropDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qirqxiylcmfzwku3umf2gk3lfnz2hgrtpojbw63tomvrxi2lpnzcgsy3unfxw4ylspe5gczdnnfxgs43uojqxi2lwmvbw63tomvrxi2lpnzcgsy3unfxw4ylspe5a)

---

### createTableStatementsForEntityGroup:

`+ (NSArray *)createTableStatementsForEntityGroup:(NSArray
*)entityGroup`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create a table for _entityGroup_,
an array of EOEntity objects that have the same [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk). Returns an empty array
if _entityGroup_ is nil or empty.

EOSQLExpression's
implementation does the following:

1. Creates
   an EOSQLExpression object.
2. Sets the expression's [entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlooruxi6i) to the first entity in _entityGroup_.
3. Adds a create clause for each Attribute in _entityGroup_'s
   Entities.
4. Sets the expression's [statement](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643umf2gk3lfnz2a) to CREATE TABLE _TABLE_NAME_ (_LIST_STRING_),
   where _TABLE_NAME_ is the __externalName__ of
   the Entity objects in _entityGroup_ and _LIST_STRING_ is
   the expression's [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo).
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

- [addCreateClauseForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbxezlborsug3dbovzwkrtpojaxi5dsnfrhk5dfhi)
- [columnTypeStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6y3pnr2w23supfygku3uojuw4z2gn5zec5duojuwe5lumu5a)
- [allowsNullClauseForConstraint:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnrxxo42oovwgyq3mmf2xgzkgn5zeg33oon2heyljnz2du)

__See
Also:__  [+ createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a), [+ dropTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkrqwe3dfkn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4b2)

---

### createTableStatementsForEntityGroups:

`+ (NSArray *)createTableStatementsForEntityGroups:(NSArray
*)entityGroups`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the tables specified in _entityGroups_.
An entity group is an array of Entity objects that have the same __externalName__, and _entityGroups_ is
an array of entity groups. Returns an empty array if _entityGroups_ is nil or
empty. EOSQLExpression's implementation invokes [createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [+ schemaCreationStatementsForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2)

---

### deleteStatementWithQualifier:entity:

`+ (EOSQLExpression *)deleteStatementWithQualifier:(EOQualifier
*)qualifier
entity:(id)entity`

Creates and returns an SQL DELETE expression
to delete the rows described by qualifier. Creates an instance of
EOSQLExpression, initializes it with _entity_ (an
EOEntity object), and sends it a [prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq) message. Raises an `NSInvalidArgumentException` if
qualifier is nil.

The expression created with this method does
not use table aliases because Enterprise Objects Framework assumes
that all INSERT, UPDATE, and DELETE statements are single-table
operations. As a result, all keys in _qualifier_ should
be simple key names; no key paths are allowed. To generate DELETE
statements that do use table aliases, you must override [prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq) to
send a [setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)`YES` message
prior to invoking `super`'s version.

---

### dropDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:

`+ (NSArray *)dropDatabaseStatementsForConnectionDictionary:(NSDictionary
*)connectionDictionary
administrativeConnectionDictionary:(NSDictionary
*)adminDictionary`

Generates the SQL statements to drop a database
(or user, for Oracle).

__See Also:__  [+ createDatabaseStatementsForConnectionDictionary:administrativeConnectionDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsuiylumfrgc43fkn2gc5dfnvsw45dtizxxeq3pnzxgky3unfxw4rdjmn2gs33omfzhsotbmrwws3tjon2heylunf3gkq3pnzxgky3unfxw4rdjmn2gs33omfzhsoq)

---

### dropPrimaryKeySupportStatementsForEntityGroup:

`+ (NSArray *)dropPrimaryKeySupportStatementsForEntityGroup:(NSArray
*)entityGroup`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the primary key generation
support for _entityGroup_, an array
of Entity objects that have the same __externalName__.
The drop statement generated by this method should be sufficient
to remove the primary key support created by [primaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovydu)'s
statements.

EOSQLExpression's implementation creates a statement
of the following form:

> ```
> drop sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is
the [primaryKeyRootName:](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfjg633ujzqw2zj2) for
the first entity in _entityGroup_ concatenated
with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass
uses a different primary key generation mechanism or if the subclass's
database server's drop semantics are different, the subclass should
override this method.

---

### dropPrimaryKeySupportStatementsForEntityGroups:

`+ (NSArray *)dropPrimaryKeySupportStatementsForEntityGroups:(NSArray
*)entityGroups`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the primary key generation
support for the entities specified in _entityGroups_.
An entity group is an array of EOEntity objects that have the same __externalName__,
and _entityGroups_ is an array of entity
groups. EOSQLExpression's implementation invokes [dropPrimaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkbzgs3lboj4uwzlzkn2xa4dpoj2fg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a) for each
entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [+ schemaCreationStatementsForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2)

---

### dropTableStatementsForEntityGroup:

`+ (NSArray *)dropTableStatementsForEntityGroup:(NSArray
*)entityGroup`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the table identified by _entityGroup_,
an array of Entity objects that have the same __externalName__.
The drop statement generated by this method should be sufficient
to remove the table created by [createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a)'s
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

### dropTableStatementsForEntityGroups:

`+ (NSArray *)dropTableStatementsForEntityGroups:(NSArray
*)entityGroups`

Returns an array of EOSQLExpression objects
that define the SQL necessary to drop the tables for _entityGroups_.
An entity group is an array of Entity objects that have the same __externalName__,
and _entityGroups_ is an array of entity
groups. EOSQLExpression's implementation invokes [dropTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkrqwe3dfkn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4b2) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

__See
Also:__  [+ schemaCreationStatementsForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2)

---

### expressionForString:

`+ (EOSQLExpression *)expressionForString:(NSString
*)string`

Creates and returns an SQL expression for _string_. _string_ should
be a valid expression in the target query language. This method
does not perform substitutions or formatting of any kind.

__See
Also:__  [- setStatement:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forjxiylumvwwk3tuhi)

---

### foreignKeyConstraintStatementsForRelationship:

`+ (NSArray *)foreignKeyConstraintStatementsForRelationship:(EORelationship
*)aRelationship`

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
  (if _aRelationship_'s [destinationEntity](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/destinationEntity) is
  in a different model than _aRelationship_'s
  source [entity](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOAccess.framework/ObjC_classic/Classes/EORelationship.html#//apple_ref/occ/instm/EORelationship/entity))
- _aRelationship_ is a to-many
  relationship, or if the inverse relationship of _aRelationship_ is
  not a to-many. In other words, foreign key constraint statements
  are only created for to-one relationships whose inverse is a to-many.

If
neither of the above are true, this method creates a new EOSQLExpression,
assigns its entity to _aRelationship_'s
entity, invokes [prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfinxw443uojqws3tukn2gc5dfnvsw45cgn5zfezlmmf2gs33oonugs4b2onxxk4tdmvbw63dvnvxhgotemvzxi2lomf2gs33oinxwy5lnnzztu),
and returns an array containing the expression.

If a
subclass's database server's foreign key constraint semantics
are different, the subclass should override this method or override
the method __prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:__.

__See
Also:__  [+ schemaCreationStatementsForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33okn2gc5dfnvsw45dtizxxerlooruxi2lfom5g64dunfxw44z2)

---

### formatSQLString:format:

`+ (NSString *)formatSQLString:(NSString
*)sqlString
format:(NSString *)format`

Applies _format_ (an
EOAttribute object's "read" or "write" format) to _sqlString_ (a
value for the attribute). If _format_ is nil,
this method returns _sqlString_ unchanged.

__See
Also:__  [- readFormat](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3smvqwirtpojwwc5a) (EOAttribute), [- writeFormat](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3xojuxizkgn5zg2ylu) (EOAttribute)

---

### formatStringValue:

`+ (NSString *)formatStringValue:(NSString
*)string`

Formats _string_ for
use as a string constant in a SQL statement. EOSQLExpression's
implementation encloses the string in single quotes, escaping any
single quotes already present in _string_. Raises an `NSInternalInconsistencyException` if _string_ is nil.

---

### formatValue:forAttribute:

`+ (NSString *)formatValue:(id)value
forAttribute:(EOAttribute *)attribute`

Overridden by subclasses to return a string
representation of _value_ suitable
for use in an SQL statement. EOSQLExpression's implementation
returns _value_ unchanged. A subclass
should override this method to format _value_ depending
on _attribute_'s [externalType](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3fpb2gk4tomfwfi6lqmu). For example, a subclass
might format a date using a special database-specific syntax or
standard form or truncate numbers to attribute's precision and
scale.

---

### insertStatementForRow:entity:

`+ (EOSQLExpression *)insertStatementForRow:(NSDictionary
*)row
entity:(EOEntity *)entity`

Creates and returns an SQL INSERT expression
to insert _row_. Creates an instance
of EOSQLExpression, initializes it with _entity_,
and sends it [prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq). Raises an `NSInvalidArgumentException` if
entity is nil.

The expression created with this method does
not use table aliases because Enterprise Objects Framework assumes
that all INSERT, UPDATE, and DELETE statements are single-table
operations. To generate INSERT statements that do use table aliases,
you must override [prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq) to
send a [setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)`YES` message
prior to invoking `super`'s version.

---

### isColumnType:equivalentToColumnType:options:

`+ (BOOL)isColumnType:(id
<EOColumnTypes>)columnTypeA
equivalentToColumnType:(id <EOColumnTypes>)columnTypeB
options:(NSDictionary *)options`

Returns YES if values in a column of _columnTypeA_ can
be copied into a column of _columnTypeB_ without the
use of a casting phrase, NO otherwise. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### phraseCastingColumnNamed:fromType:toType:options:

`+ (NSString *)phraseCastingColumnNamed:(NSString
*)columnName
fromType:(id <EOColumnTypes>)type
toType:(id <EOColumnTypes>)castType
options:(NSDictionary *)options`

Returns an SQL string to cast the values in
the column specified by _columnName_ to
a new type. This method is used when the adaptor doesn't support
in-place column type coercion, and the table has to be recreated.
To move data from the old table to the new table, sometimes a conversion
statement is needed (for example, to convert strings in a VARCHAR
column to numbers). The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### primaryKeyConstraintStatementsForEntityGroup:

`+ (NSArray *)primaryKeyConstraintStatementsForEntityGroup:(NSArray
*)entityGroup`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key constraints
for _entityGroup_, an array of EOEntity
objects that have the same [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk).
Returns an empty array if any of the primary key attributes in _entityGroup_ don't
have a [columnName](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3dn5whk3lojzqw2zi).

EOSQLExpression's
implementation creates a statement of the following form:

> ```
> ALTER TABLE TABLE_NAME ADD PRIMARY KEY (PRIMARY_KEY_COLUMN_NAMES)
> ```

Where _TABLE_NAME_ is
the [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk) for
the first entity in _entityGroup_ and _PRIMARY_KEY_COLUMN_NAMES_ is
a comma-separated list of the [columnName](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3dn5whk3lojzqw2zi)s of the first entity's [primaryKeyAttributes](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfaxi5dsnfrhk5dfom).

If
the subclass's database server's primary key constraint semantics
are different, the subclass should override this method.

---

### primaryKeyConstraintStatementsForEntityGroups:

`+ (NSArray *)primaryKeyConstraintStatementsForEntityGroups:(NSArray
*)entityGroups`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key constraints
for the Entities specified in _entityGroups_.
An entity group is an array of Entity objects that have the same [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk), and _entityGroups_ is
an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovydu) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

---

### primaryKeySupportStatementsForEntityGroup:

`+ (NSArray *)primaryKeySupportStatementsForEntityGroup:(NSArray
*)entityGroup`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key generation
support for _entityGroup_, an array
of EOEntity objects that have the same [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk). EOSQLExpression's
implementation creates a statement of the following form:
> ```
> create sequence SEQUENCE_NAME
> ```

Where _SEQUENCE_NAME_ is
the [primaryKeyRootName:](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5yhe2lnmfzhss3fpfjg633ujzqw2zj2) for
the first entity in _entityGroup_ concatenated
with "_SEQ" (EMP_ID_SEQ, for example).

If a subclass
uses a different primary key generation mechanism or if the subclass's
database server's drop semantics are different, the subclass should
override this method.

__See Also:__  [+ dropPrimaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkbzgs3lboj4uwzlzkn2xa4dpoj2fg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a), [- primaryKeyForNewRowWithEntity:](EOAdaptorChannel-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bmrqxa5dpojbwqylonzswyl3qojuw2ylspffwk6kgn5ze4zlxkjxxov3joruek3tunf2hsoq) (EOAdaptorChannel)

---

### primaryKeySupportStatementsForEntityGroups:

`+ (NSArray *)primaryKeySupportStatementsForEntityGroups:(NSArray
*)entityGroups`

Returns an array of EOSQLExpression objects
that define the SQL necessary to create the primary key generation
support for the Entities specified in _entityGroups_.
An entity group is an array of Entity objects that have the same [externalName](EOEntity-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2fnz2gs5dzf5sxq5dfojxgc3comfwwk), and _entityGroups_ is
an array of entity groups. EOSQLExpression's implementation invokes [primaryKeySupportStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovydu) for
each entity group in _entityGroups_ and
returns an array of all the resulting EOSQLExpressions.

---

### schemaCreationScriptForEntities:options:

`+ (NSArray *)schemaCreationScriptForEntities:(NSArray
*)entities
options:(NSDictionary *)options`

Returns a script of SQL statements suitable
to create the schema for the EOEntity objects in _entities_. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec). EOSQLExpression's
implementation invokes __schemaCreationStatementsForEntities:options:__ with _entities_ and _options_ and
then uses [appendExpression:toScript:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5qxa4dfnzsek6dqojsxg43jn5xdu5dpknrxe2lqoq5a) to
generate the script from the EOSQLExpressions generated by __schemaCreationStatementsForEntities:options:__.

---

### schemaCreationStatementsForEntities:options:

`+ (NSArray *)schemaCreationStatementsForEntities:(NSArray
*)entities
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions suitable
to create the schema for the Entity objects in _entities_. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

EOSQLExpression's
implementation uses the following methods:

- [createTableStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33vobztu)
- [dropTableStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkrqwe3dfkn2gc5dfnvsw45dtizxxerlooruxi6khojxxk4dthi)
- [primaryKeySupportStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfjxk4dqn5zhiu3umf2gk3lfnz2hgrtpojcw45djor4uo4tpovyhgoq)
- [dropPrimaryKeySupportStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5she33qkbzgs3lboj4uwzlzkn2xa4dpoj2fg5dborsw2zloorzum33sivxhi2lupfdxe33vobztu)
- [primaryKeyConstraintStatementsForEntityGroups:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5yhe2lnmfzhss3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64sfnz2gs5dzi5zg65lqom5a)
- [foreignKeyConstraintStatementsForRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tfnftw4s3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64ssmvwgc5djn5xhg2djoa5a)

to
generate EOSQLExpressions for the support identified in _options_.

__See
Also:__  [+ schemaCreationScriptForEntities:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwg2dfnvqug4tfmf2gs33oknrxe2lqordg64sfnz2gs5djmvztu33qoruw63tthi)

---

### selectStatementForAttributes:lock:fetchSpecification:entity:

`+ (EOSQLExpression *)selectStatementForAttributes:(NSArray
*)attributes
lock:(BOOL)flag
fetchSpecification:(EOFetchSpecification
*)fetchSpecification
entity:(EOEntity *)entity`

Creates and returns an SQL SELECT expression.
Creates an instance of EOSQLExpression, initializes it with _entity_,
and sends it [prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2).
The expression created with this method uses table aliases. Raises an `NSInvalidArgumentException` if attributes
is nil or empty, _fetchSpecification_ is nil,
or _entity_ is nil.

The expression
created with this method uses table aliases. To generate SELECT
statements that don't use them, you must override [prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2) to send
a [setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)`NO` message
prior to invoking `super`'s
version.

---

### setUseBindVariables:

`+ (void)setUseBindVariables:(BOOL)flag`

Sets according to _flag_ whether
all instances of EOSQLExpression subclasses use bind variables.
By default, instances don't use bind variables; if the value for
the global user default named `EOAdaptorUseBindVariables` is YES,
though, instances do use them. For more information on bind variables,
see the discussion in the class description.

__See
Also:__  [+ useBindVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkcnfxgivtbojuwcytmmvzq)

---

### setUseQuotedExternalNames:

`+ (void)setUseQuotedExternalNames:(BOOL)flag`

Sets whether all instances of EOSQLExpression
subclasses quote external names when they are referenced in SQL
statements. By setting _flag_ to YES,
you can access database tables with names such as "%return",
"1st year", and "TABLE" that you couldn't otherwise access.
By default, instances don't quote external names; if the value for
the global user default named `EOAdaptorQuotesExternalNames` is YES,
though, instances do use quotes.

__See Also:__  [+ useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkrovxxizleiv4hizlsnzqwyttbnvsxg), [- sqlStringForSchemaObjectName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknrwqzlnmfhwe2tfmn2e4ylnmu5a), [- externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlyorsxe3tbnrhgc3lfkf2w65dfinugc4tbmn2gk4q)

---

### sqlPatternFromShellPattern:

`+ (NSString *)sqlPatternFromShellPattern:(NSString
*)pattern`

Translates a "like" qualifier to an SQL
"like" expression. Invoked from [sqlStringForKeyValueQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjnsxsvtbnr2wkulvmfwgsztjmvzdu) when
the qualifier argument is an EOKeyValueQualifier object whose selector
is `EOQualifierOperatorLike`. EOSQLExpression's
implementation performs the following substitutions

|  |  |
| --- | --- |
| __Character in pattern__ | __Substitution string__ |
| \* | % |
| ? | _ |
| % | [%] _(unless the percent character appears in square brackets)_ |
| _ | [_] _(unless the underscore character appears in square brackets)_ |

__See Also:__  [+ sqlPatternFromShellPattern:withEscapeCharacter:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxc3cqmf2hizlsnzdhe33nknugk3dmkbqxi5dfojxdu53joruek43dmfygkq3imfzgcy3umvzdu)

---

### sqlPatternFromShellPattern:withEscapeCharacter:

`+ (NSString *)sqlPatternFromShellPattern:(NSString
*)pattern
withEscapeCharacter:(unichar)escapeCharacter`

Like [sqlPatternFromShellPattern:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxc3cqmf2hizlsnzdhe33nknugk3dmkbqxi5dfojxdu) except
the argument _escapeCharacter_ allows
you to specify a character for escaping the wild card characters
"%" and "_".

---

### statementsToConvertColumnNamed:inTableNamed:fromType:toType:options:

`+ (NSArray *)statementsToConvertColumnNamed:(NSString
*)columnName
inTableNamed:(NSString *)tableName
fromType:(id <EOColumnTypes>)type
toType:(id <EOColumnTypes>)newType
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to convert
in place the type of the specified column. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToCopyTableNamed:intoTableForEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToCopyTableNamed:(NSString
*)tableName
intoTableForEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to copy
the specified table into a new table, whose definition is provided
by _entityGroup_-an array of EOEntity
objects rooted to the table named _tableName_.
This method is used when the adaptor doesn't support the in-place
table modifications required to synchronize the database to a model.

The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToDeleteColumnNamed:inTableNamed:options:

`+ (NSArray *)statementsToDeleteColumnNamed:(NSString
*)columnName
inTableNamed:(NSString *)tableName
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to delete
in place the specified column from the specified table. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToDropForeignKeyConstraintsOnEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToDropForeignKeyConstraintsOnEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to drop
foreign key constraints for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToDropPrimaryKeyConstraintsOnEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToDropPrimaryKeyConstraintsOnEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to drop
primary key constraints for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToDropPrimaryKeySupportForEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToDropPrimaryKeySupportForEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to drop
the primary key support mechanism for the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToImplementForeignKeyConstraintsOnEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToImplementForeignKeyConstraintsOnEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to implement
foreign key constraints on the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToImplementPrimaryKeyConstraintsOnEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToImplementPrimaryKeyConstraintsOnEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to implement
primary key constraints on the table corresponding to _entityGroup_-an
array of EOEntity objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToImplementPrimaryKeySupportForEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToImplementPrimaryKeySupportForEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to implement
support mechanisms for primary key generation for the table corresponding
to _entityGroup_-an array of EOEntity
objects rooted to the same table. The _changes_ dictionary
identifies the changes to make to the database schema; for more
information, see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToInsertColumnForAttribute:options:

`+ (NSArray *)statementsToInsertColumnForAttribute:(EOAttribute
*)attribute
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to insert
in place a column for the specified attribute. The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToModifyColumnNamed:inTableNamed:toNullRule:

`+ (NSArray *)statementsToModifyColumnNamed:(NSString
*)columnName
inTableNamed:(NSString *)tableName
toNullRule:(BOOL)allowsNull
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to modify
in place the specified column to either allow or not allow NULL
values as specified by _allowsNull_.
The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToRenameColumnNamed:inTableNamed:newName:options:

`+ (NSArray *)statementsToRenameColumnNamed:(NSString
*)columnName
inTableNamed:(NSString *)tableName
newName:(NSString *)newName
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to rename
in place the specified column. The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToRenameTableNamed:newName:options:

`+ (NSArray *)statementsToRenameTableNamed:(NSString
*)tableName
newName:(NSString *)newName
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to rename
in place the specified table. The _options_ dictionary describes
the aspects of the schema for which to create SQL statements; for
more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToUpdateObjectStoreForEntityGroup:withChangeDictionary:options:

`+ (NSArray *)statementsToUpdateStoreForEntityGroup:(NSArray
*)entityGroup
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to update
the table that corresponds to _entityGroup_-an
array of EOEntity objects rooted to the same table. Inserts and
deletes columns, and updates modified columns. The _changes_ dictionary
identifies the changes to make to the database schema; for more information,
see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### statementsToUpdateObjectStoreForModel:withChangeDictionary:options:

`+ (NSArray *)statementsToUpdateObjectStoreForModel:(EOModel
*)model
withChangeDictionary:(NSDictionary
*)changes
options:(NSDictionary *)options`

Returns an array of EOSQLExpressions to synchronize
the database with _model_. Prepares
the statements to insert and delete new and deleted tables before
invoking [statementsToUpdateObjectStoreForEntityGroup:withChangeDictionary:options:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxiylumvwwk3tuonkg6vlqmrqxizkpmjvgky3ukn2g64tfizxxerlooruxi6khojxxk4b2o5uxi2cdnbqw4z3firuwg5djn5xgc4tzhjxxa5djn5xhgoq) for
each modified table. The _changes_ dictionary
identifies the changes to make to the database schema; for more information,
see ["The Change Dictionary"](EOSQLExpression-4.md#apple-ijeugskiifdeu). The _options_ dictionary
describes the aspects of the schema for which to create SQL statements;
for more information, see ["The Options Dictionary"](EOSQLExpression-4.md#apple-ijeugq2kjjfec).

---

### supportsDirectColumnCoercion

`+ (BOOL)supportsDirectColumnCoercion`

Returns YES if the adaptor can change the type
of an existing column in place, NO otherwise.

---

### supportsDirectColumnDeletion

`+ (BOOL)supportsDirectColumnDeletion`

Returns YES if the adaptor can delete columns, NO otherwise.

---

### supportsDirectColumnInsertion

`+ (BOOL)supportsDirectColumnInsertion`

Returns YES if the adaptor can add columns to
a table, NO otherwise.

---

### supportsDirectColumnNullRuleModification

`+ (BOOL)supportsDirectColumnNullRuleModification`

Returns YES if the adaptor can modify the null
rule of an existing column in place, NO otherwise.

---

### supportsDirectColumnRenaming

`+ (BOOL)supportsDirectColumnRenaming`

Returns YES if the adaptor can rename table
columns, NO otherwise.

---

### supportsSchemaSynchronization

`+ (BOOL)supportsSchemaSynchronization`

Returns YES if the adaptor can update the database
to reflect changes in a model, NO otherwise.

---

### updateStatementForRow:qualifier:entity:

`+ (EOSQLExpression *)updateStatementForRow:(NSDictionary
*)row
qualifier:(EOQualifier *)qualifier
entity:(EOEntity *)entity`

Creates and returns an SQL UPDATE expression
to update the row identified by _qualifier_ with
the values in _row_. _row_ should
only contain entries for values that have actually changed. Creates
an instance of EOSQLExpression, initializes it with _entity_,
and sends it [prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq).

Raises
an `NSInvalidArgumentException` if _row_ is `nil` or
empty, _qualifier_ is `nil`,
or _entity_ is `nil`.

The
expression created with this method does not use table aliases because
Enterprise Objects Framework assumes that all INSERT, UPDATE, and
DELETE statements are single-table operations. As a result, all
keys in _qualifier_ should be simple
key names; no key paths are allowed. To generate UPDATE statements
that do use table aliases, you must override [prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq) to
send a [setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)`YES` message
prior to invoking `super`'s
version.

__See Also:__  [- setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a)

---

### useBindVariables

`+ (BOOL)useBindVariables`

Returns YES if instances use bind variables, NO otherwise.
For more information on bind variables, see the discussion in the
class description.

__See Also:__  [+ setUseBindVariables:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk5cvonsue2lomrlgc4tjmfrgyzlthi)

---

### useQuotedExternalNames

`+ (BOOL)useQuotedExternalNames`

Returns YES if instances use quoted external
names, NO otherwise.

__See Also:__  [+ setUseQuotedExternalNames:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk5cvonsvc5lporswirlyorsxe3tbnrhgc3lfom5a), [- sqlStringForSchemaObjectName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknrwqzlnmfhwe2tfmn2e4ylnmu5a), [- externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlyorsxe3tbnrhgc3lfkf2w65dfinugc4tbmn2gk4q)

---

## Instance Methods

---

### addBindVariableDictionary:

`- (void)addBindVariableDictionary:(NSMutableDictionary
*)binding`

Adds _binding_ to
the receiver's array of bind variable dictionaries. _binding_ is
generally created using the method [bindVariableDictionaryForAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq) and
is added to the receiver's bind variable dictionaries in [sqlStringForValue:attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi) when
the receiver uses a bind variable for the specified attribute. See
the method description for __bindVariableDictionaryForAttribute:value:__ for
a description of the contents of a bind variable dictionary, and
for more information on bind variables, see the discussion in the
class description.

__See Also:__  [- bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tjmvzq)

---

### addCreateClauseForAttribute:

`- (void)addCreateClauseForAttribute:(EOAttribute
*)attribute`

Adds the SQL string for creating _attribute_ to
a comma-separated list of attribute creation clauses. The list is
constructed for use in a CREATE TABLE statement produced by [createTableStatementsForEntityGroup:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5rxezlborsviylcnrsvg5dborsw2zloorzum33sivxhi2lupfdxe33voa5a).
Use the method [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo) to
access creation clauses.

EOSQLExpression's implementation
creates clauses in the following form:

> ```
> COLUMN_NAME COLUMN_TYPE ALLOWS_NULL_CLAUSE
> ```

Where

- _COLUMN_TYPE_ is the string returned
  from [columnTypeStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6y3pnr2w23supfygku3uojuw4z2gn5zec5duojuwe5lumu5a) for _anAttribute._
- _ALLOWS_NULL_CLAUSE_ is the string
  returned from [allowsNullClauseForConstraint:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnrxxo42oovwgyq3mmf2xgzkgn5zeg33oon2heyljnz2du) with YES if _anAttribute_ [allowsNull](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3bnrwg653tjz2wy3a) or with NO if _anAttribute_ doesn't.

---

### addInsertListAttribute:value:

`- (void)addInsertListAttribute:(EOAttribute
*)attribute
value:(NSString *)value`

Adds the SQL string for _attribute_ to
a comma-separated list of attributes and _value_ to
a comma-separated list of values. Both lists are constructed for
use in an INSERT statement. Use the methods [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo) and [valueList](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65tbnr2wktdjon2a) to access the attributes
and value lists.

Invokes [appendItem:toListString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylqobsw4zcjorsw2otun5ggs43ukn2he2lom45a) to
add an SQL string for _attribute_ to
the receiver's [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo),
and again to add a formatted SQL string for _value_ to
the receiver's [valueList](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65tbnr2wktdjon2a).

__See
Also:__  [- sqlStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizj2), [- sqlStringForValue:attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi), [+ formatValue:forAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fmylmovstuztpojaxi5dsnfrhk5dfhi)

---

### addJoinClauseWithLeftName:rightName:joinSemantic:

`- (void)addJoinClauseWithLeftName:(NSString
*)leftName
rightName:(NSString *)rightName
joinSemantic:(EOJoinSemantic)semantic`

Creates a new join clause by invoking [assembleJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a) and adds
it to the receiver's join clause string. Separates join conditions
already in the join clause string with the word "and". Invoked
from [joinExpression](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxek6dqojsxg43jn5xa).

__See
Also:__  [- joinClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxeg3dbovzwku3uojuw4zy)

---

### addOrderByAttributeOrdering:

`- (void)addOrderByAttributeOrdering:(EOSortOrdering
*)sortOrdering`

Adds an attribute-direction pair ("LAST_NAME
asc", for example) to the receiver's ORDER BY string. If _sortOrdering_'s
selector is `EOCompareCaseInsensitiveAscending` or `EOCompareCaseInsensitiveAscending`,
the string generated has the format "upper(attribute) direction". Use
the method [orderByString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc633smrsxeqtzkn2he2lom4) to
access the ORDER BY string. [addOrderByAttributeOrdering:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrhxezdfojbhsqluorzgsytvorsu64temvzgs3thhi) invokes [appendItem:toListString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylqobsw4zcjorsw2otun5ggs43ukn2he2lom45a) to add the
attribute-direction pair.

__See Also:__  [- sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2)

---

### addSelectListAttribute:

`- (void)addSelectListAttribute:(EOAttribute
*)attribute`

Adds an SQL string for _attribute_ to
a comma-separated list of attribute names for use in a SELECT statement.
The SQL string for _attribute_ is formatted
with _attribute_'s "read" format.
Use [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo) to access
the list. __addSelectListAttribute:__ invokes [appendItem:toListString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylqobsw4zcjorsw2otun5ggs43ukn2he2lom45a) to add the
attribute name.

__See Also:__  [- sqlStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizj2), [+ formatSQLString:format:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq), [- readFormat](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3smvqwirtpojwwc5a) (EOAttribute)

---

### addUpdateListAttribute:value:

`- (void)addUpdateListAttribute:(EOAttribute
*)attribute
value:(NSString *)value`

Adds an attribute-value assignment ("LAST_NAME
= ‘Thomas'", for example) to a comma-separated list for use
in an UPDATE statement. Formats _value_ with _attribute_'s
"write" format. Use [listString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63djon2fg5dsnfxgo) to access
the list. __addUpdateListAttribute:value:__ invokes [appendItem:toListString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylqobsw4zcjorsw2otun5ggs43ukn2he2lom45a) to add the attribute-value
assignment.

__See Also:__  [+ formatSQLString:format:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq)

---

### aliasesByRelationshipPath

`- (NSMutableDictionary *)aliasesByRelationshipPath`

Returns a dictionary of table aliases. The keys
of the dictionary are relationship paths-"department" and
"department.location", for example. The values are the table
aliases for the corresponding table-"t1" and "t2", for
example. The [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq) dictionary
always has at least one entry: an entry for the EOSQLExpression's
entity. The key of this entry is the empty string (@"") and
the value is "t0". The dictionary returned from this method
is built up over time with successive calls to [sqlStringForAttributePath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkqmf2gqoq).

__See
Also:__  [- tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a)

---

### allowsNullClauseForConstraint:

`- (NSString *)allowsNullClauseForConstraint:(BOOL)flag`

Returns according to _flag_ an
adaptor specific string for use in a CREATE TABLE statement. The returned
string indicates whether a column allows null values. EOSQLExpression's
implementation returns the empty string if _flag_ is YES,
"NOT NULL" otherwise. A subclass should override this if its database
server's semantics are different. For example, the SybaseSLQExpression
returns "null" if _flag_ is YES,
the empty string otherwise.

__See Also:__  [+ addCreateClauseForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbxezlborsug3dbovzwkrtpojaxi5dsnfrhk5dfhi)

---

### appendItem:toListString:

`- (void)appendItem:(NSString
*)itemString
toListString:(NSMutableString
*)listString`

Adds _itemString_ to
a comma-separated list. If _listString_ already
has entries, this method appends a comma followed by _itemString_.
Invoked from [addSelectListAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5dfhi), [addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a), [addUpdateListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrkxazdborsuy2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a), and [addOrderByAttributeOrdering:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrhxezdfojbhsqluorzgsytvorsu64temvzgs3thhi)

---

### assembleDeleteStatementWithQualifier:tableList:whereClause:

`- (NSString *)assembleDeleteStatementWithQualifier:(EOQualifier
*)qualifier
tableList:(NSString *)tableList
whereClause:(NSString *)whereClause`

Invoked from [prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq) to
return an SQL DELETE statement of the form:
> ```
> DELETE FROM tableList
> SQL_WHERE whereClause
> ```

_qualifier_ is
the argument to [prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq) from
which _whereClause_ was derived. It
is provided for subclasses that need to generate the WHERE clause
in a particular way.

---

### assembleInsertStatementWithRow:tableList:columnList:valueList:

`- (NSString *)assembleInsertStatementWithRow:(NSDictionary
*)row
tableList:(NSString *)tableList
columnList:(NSString *)columnList
valueList:(NSString *)valueList`

Invoked from [prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq) to
return an SQL INSERT statement of the form:
> ```
> INSERT INTO tableList (columnList)
> VALUES valueList
> ```

or,
if _columnList_ is nil:

> ```
> INSERT INTO tableList
> VALUES valueList
> ```

_row_ is
the argument to [prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq) from
which _columnList_ and _valueList_ were derived.
It is provided for subclasses that need to generate the list of
columns and values in a particular way.

---

### assembleJoinClauseWithLeftName:rightName:joinSemantic:

`- (NSString *)assembleJoinClauseWithLeftName:(NSString
*)leftName
rightName:(NSString *)rightName
joinSemantic:(EOJoinSemantic)semantic`

Returns a join clause of the form:
> ```
> leftName operator rightName
> ```

Where
operator is "=" for an inner join, "\*=" for a left-outer
join, and "=\*" for a right-outer join. Invoked from [addJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a).

---

### assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder:selectString:columnList:tableList:whereClause:joinClause:orderByClause:lockClause:

`- (NSString *)assembleSelectStatementWithAttributes:(NSArray
*)attributes
lock:(BOOL)lock
qualifier:(EOQualifier *)qualifier
fetchOrder:(NSArray *)fetchOrder
selectString:(NSString *)selectString
columnList:(NSString *)columnList
tableList:(NSString *)tableList
whereClause:(NSString *)whereClause
joinClause:(NSString *)joinClause
orderByClause:(NSString *)orderByClause
lockClause:(NSString *)lockClause`

Invoked from [prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2) to
return an SQL SELECT statement of the form:
> ```
> SELECT columnList
> FROM tableList lockClause
> WHERE whereClause AND joinClause
> ORDER BY orderByClause
> ```

If _lockClause_ is nil,
it is omitted from the statement. Similarly, if _orderByClause_ is nil,
the "ORDER BY _orderByClause_"
is omitted. If either _whereClause_ or _joinClause_ is nil,
the "AND" and nil-valued argument are omitted. If both are nil,
the entire WHERE clause is omitted.

_attributes_, _lock_, _qualifier_,
and _fetchOrder_ are the arguments
to [prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2) from
which the other __assembleSelect...__ arguments
were derived. They are provided for subclasses that need to generate
the clauses of the SELECT statement in a particular way.

---

### assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:

`- (NSString *)assembleUpdateStatementWithRow:(NSDictionary
*)row
qualifier:(EOQualifier *)qualifier
tableList:(NSString *)tableList
updateList:(NSString *)updateList
whereClause:(NSString *)whereClause`

Invoked from [prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq) to
return an SQL UPDATE statement of the form:
> ```
> UPDATE tableList
> SET updateList
> WHERE whereClause
> ```

_row_ and _qualifier_ are
the arguments to [prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq) from
which _updateList_ and _whereClause_ were
derived. They are provided for subclasses that need to generate
the clauses of the UPDATE statement in a particular way.

---

### bindVariableDictionaries

`- (NSArray *)bindVariableDictionaries`

Returns the receiver's bind variable dictionaries.
For more information on bind variables, see the discussion in the
class description.

__See Also:__  [- addBindVariableDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbgs3tekzqxe2lbmjwgkrdjmn2gs33omfzhsoq)

---

### bindVariableDictionaryForAttribute:value:

`- (NSMutableDictionary *)bindVariableDictionaryForAttribute:(EOAttribute
*)attribute value:(id)value`

Implemented by subclasses to create and return
the bind variable dictionary for _attribute_ and _value_. The
dictionary returned from this method must contain the following
key-value pairs:

|  |  |
| --- | --- |
| __Key__ | __Corresponding Value__ |
| `EOBindVariableNameKey` | Name of the bind variable for _attribute_ |
| `EOBindVariablePlaceHolderKey` | Placeholder string used in the SQL statement |
| `EOBindVariableAttributeKey` | _attribute_ |
| `EOBindVariableValueKey` | _value_ |

An adaptor subclass may define additional entries
as required by its RDBMS.

Invoked from [sqlStringForValue:attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi) when
the message [mustUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)_attribute_ returns YES or
when the receiver's class uses bind variables and the message [shouldUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a)_attribute_ returns YES.
For more information on bind variables, see the discussion in the
class description.

A subclass that uses bind variables
should implement this method without invoking EOSQLExpression's
implementation. The subclass implementation must return a dictionary
with entries for the keys listed above and may add additional keys.

__See
Also:__  [- bindVariableDictionaryForAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq), [+ useBindVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkcnfxgivtbojuwcytmmvzq)

---

### columnTypeStringForAttribute:

`- (NSString *)columnTypeStringForAttribute:(EOAttribute
*)anAttribute`

Returns an adaptor specific type string for _anAttribute_ that's
suitable for use in a CREATE TABLE statement. EOSQLExpression's
implementation creates a string based on _anAttribute_'s [externalType](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3fpb2gk4tomfwfi6lqmu), [precision](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3qojswg2ltnfxw4), and [width](EOAttribute-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2bor2he2lcov2gkl3xnfshi2a) as follows:

|  |  |
| --- | --- |
| __If Condition__ | __Generated String__ |
| precision is non-zero | externalType(precision, scale) |
| precision is zero and width is non-zero | externalType(scale) |
| precision and width are zero | externalType |

A subclass should override the default implementation
if its database server requires column types in a different format.

__See
Also:__  [- addCreateClauseForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbxezlborsug3dbovzwkrtpojaxi5dsnfrhk5dfhi)

---

### entity

`- (EOEntity *)entity`

Returns the receiver's entity.

__See
Also:__  [- initWithEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62lonf2fo2lunbcw45djor4tu)

---

### externalNameQuoteCharacter

`- (NSString *)externalNameQuoteCharacter`

Returns the string ‘\"' (an escaped quote
character) if the receiver uses quoted external names, or the empty
string ("") otherwise.

__See Also:__  [+ useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkrovxxizleiv4hizlsnzqwyttbnvsxg), [- sqlStringForSchemaObjectName:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknrwqzlnmfhwe2tfmn2e4ylnmu5a)

---

### initWithEntity:

`- initWithEntity:(EOEntity
*)entity`

Initializes a new instance of EOSQLExpression
with _entity_.

__See
Also:__  [- entity](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlooruxi6i)

---

### joinClauseString

`- (NSMutableString *)joinClauseString`

Returns the part of the receiver's WHERE clause
that specifies join conditions. Together, the __joinExpression__ and
the [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th) make
up a statement's WHERE clause. If the receiver's statement doesn't
contain join conditions, this method returns an empty string.

An
EOSQLExpression's __joinClauseString__ is
generally set by invoking [joinExpression](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxek6dqojsxg43jn5xa).

__See
Also:__  [- addJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a)

---

### joinExpression

`- (void)joinExpression`

Builds up the [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxeg3dbovzwku3uojuw4zy) for use in a SELECT
statement. For each relationship path in the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq) dictionary,
this method invokes [addJoinClauseWithLeftName:rightName:joinSemantic:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrfg62loinwgc5ltmvlws5dijrswm5comfwwkotsnftwq5comfwwkotkn5uw4u3fnvqw45djmm5a) for
each of the relationship's EOJoin objects.

If the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq) dictionary
only has one entry (the entry for the EOSQLExpression's entity),
the __joinClauseString__ is empty.

You
must invoke this method after invoking [addSelectListAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5dfhi) for each
attribute to be selected and after sending __sqlStringForSQLExpression____:self__ to
the qualifier for the SELECT statement. (These methods build up
the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq) dictionary
by invoking [sqlStringForAttributePath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkqmf2gqoq).)

__See
Also:__  [- whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th), -
sqlStringForSQLExpression: (EOQualifierSQLGeneration protocol)

---

### listString

`- (NSMutableString *)listString`

Returns a comma-separated list of attributes
or "attribute = value" assignments. __listString__ is
built up with successive invocations of [addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a), [addSelectListAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5dfhi), or [addUpdateListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrkxazdborsuy2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a) for
INSERT statements, SELECT statements, and UPDATE statements, respectively.
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

`- (NSString *)lockClause`

Overridden by subclasses to return the SQL string
used in a SELECT statement to lock selected rows. A concrete subclass
of EOSQLExpression must override this method to return the string
used by its adaptor's RDBMS.

---

### mustUseBindVariableForAttribute:

`- (BOOL)mustUseBindVariableForAttribute:(EOAttribute
*)attribute`

Returns YES if the receiver must use bind variables
for _attribute_, NO otherwise. EOSQLExpression's implementation
returns NO. An SQL expression subclass that uses bind variables
should override this method to return YES if the underlying RDBMS
requires that bind variables be used for attributes with _attribute_'s
external type.

__See Also:__  [- shouldUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a), [- bindVariableDictionaryForAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tzizxxeqluorzgsytvorstu5tbnr2wkoq)

---

### orderByString

`- (NSMutableString *)orderByString`

Returns the comma-separated list of "attribute
direction" pairs ("LAST_NAME asc, FIRST_NAME asc", for example)
for use in a SELECT statement.

__See Also:__  [- addOrderByAttributeOrdering:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrhxezdfojbhsqluorzgsytvorsu64temvzgs3thhi)

---

### prepareConstraintStatementForRelationship:sourceColumns:destinationColumns:

`- (void)prepareConstraintStatementForRelationship:(EORelationship
*)relationship
sourceColumns:(NSArray *)sourceColumns
destinationColumns:(NSArray *)destinationColumns`

Sets the receiver's [statement](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643umf2gk3lfnz2a) to an adaptor specific
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
Also:__  [+ foreignKeyConstraintStatementsForRelationship:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tfnftw4s3fpfbw63ttorzgc2loorjxiylumvwwk3tuondg64ssmvwgc5djn5xhg2djoa5a)

---

### prepareDeleteExpressionForQualifier:

`- (void)prepareDeleteExpressionForQualifier:(EOQualifier
*)qualifier`

Generates a DELETE statement by performing the
following steps:

1. Sends an __sqlStringForSQLExpression__`:self` message
   to _qualifier_ to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th).
2. Invokes [tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a) to
   get the table name for the FROM clause.
3. Invokes [assembleDeleteStatementWithQualifier:tableList:whereClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvcgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2orqwe3dfjruxg5b2o5ugk4tfinwgc5ltmu5a).

__See
Also:__  [+ deleteStatementWithQualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sgk3dforsvg5dborsw2zloorlws5dikf2wc3djmzuwk4r2mvxhi2lupe5a)

---

### prepareInsertExpressionWithRow:

`- (void)prepareInsertExpressionWithRow:(NSDictionary
*)row`

Generates an INSERT statement by performing
the following steps:

1. Invokes [addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a) for
   each entry in _row_ to prepare the
   comma-separated list of attributes and the corresponding list of
   values.
2. Invokes [tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a) to
   get the table name.
3. Invokes [assembleInsertStatementWithRow:tableList:columnList:valueList:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvew443foj2fg5dborsw2zloorlws5dikjxxootumfrgyzkmnfzxiotdn5whk3lojruxg5b2ozqwy5lfjruxg5b2).

__See
Also:__  [+ insertStatementForRow:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5uw443foj2fg5dborsw2zloordg64ssn53tuzlooruxi6j2)

---

### prepareSelectExpressionWithAttributes:lock:fetchSpecification:

`- (void)prepareSelectExpressionWithAttributes:(NSArray
*)attributes
lock:(BOOL)flag
fetchSpecification:(EOFetchSpecification
*)fetchSpecification`

Generates a SELECT statement by performing the
following steps:

1. Invokes [addSelectListAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrjwk3dfmn2ey2ltoraxi5dsnfrhk5dfhi) for each
   entry in _attributes_ to prepare the
   comma-separated list of attributes.
2. Sends an __sqlStringForSQLExpression____:self__ message
   to _fetchSpecification_'s qualifier
   to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th).
3. Invokes [addOrderByAttributeOrdering:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrhxezdfojbhsqluorzgsytvorsu64temvzgs3thhi) for
   each EOAttributeOrdering object in fetchSpecification.First
   conjoins the qualifier in _fetchSpecification_ with
   the restricting qualifier, if any, of the receiver's entity.
4. Invokes [joinExpression](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxek6dqojsxg43jn5xa) to
   generate the receiver's [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxeg3dbovzwku3uojuw4zy).
5. Invokes [tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a) to
   get the comma-separated list of tables for the FROM clause.
6. If _flag_ is YES, invokes [lockClause](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63dpmnvug3dbovzwk) to get
   the SQL string to lock selected rows.
7. Invokes [assembleSelectStatementWithAttributes:lock:qualifier:fetchOrder:selectString:columnList:tableList:whereClause:joinClause:orderByClause:lockClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvjwk3dfmn2fg5dborsw2zloorlws5diif2hi4tjmj2xizlthjwg6y3lhjyxkylmnftgszlshjtgk5ddnbhxezdfoi5hgzlmmvrxiu3uojuw4zz2mnxwy5lnnzggs43uhj2gcytmmvggs43uhj3wqzlsmvbwyylvonstu2tpnfxeg3dbovzwkotpojsgk4scpfbwyylvonstu3dpmnvug3dbovzwkoq).

__See
Also:__  [+ selectStatementForAttributes:lock:fetchSpecification:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zwk3dfmn2fg5dborsw2zloordg64sbor2he2lcov2gk4z2nrxwg2z2mzsxiy3iknygky3jmzuwgylunfxw4otfnz2gs5dzhi)

---

### prepareUpdateExpressionWithRow:qualifier:

`- (void)prepareUpdateExpressionWithRow:(NSDictionary
*)row
qualifier:(EOQualifier *)qualifier`

Generates an UPDATE statement by performing
the following steps:

1. Invokes [addUpdateListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrkxazdborsuy2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a) for
   each entry in _row_ to prepare the
   comma-separated list of "attribute = value" assignments.
2. Sends an __sqlStringForSQLExpression____:self__ message
   to _qualifier_ to generate the receiver's [whereClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc653imvzgkq3mmf2xgzktorzgs3th).
3. Invokes [tableListWithRootEntity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65dbmjwgktdjon2fo2lunbjg633uivxhi2lupe5a) to
   get the table name for the FROM clause.
4. Invokes [assembleUpdateStatementWithRow:qualifier:tableList:updateList:whereClause:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6yltonsw2ytmmvkxazdborsvg5dborsw2zloorlws5dikjxxootrovqwy2lgnfsxeotumfrgyzkmnfzxiotvobsgc5dfjruxg5b2o5ugk4tfinwgc5ltmu5a).

__See
Also:__  [+ updateStatementForRow:qualifier:entity:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xazdborsvg5dborsw2zloordg64ssn53tu4lvmfwgsztjmvzduzlooruxi6j2)

---

### setStatement:

`- (void)setStatement:(NSString
*)string`

Sets the receiver's SQL statement to _string_,
which should be a valid expression in the target query language.
Use this method-instead of a __prepare...__ method-to
directly assign an SQL string to an EOSQLExpression object. This
method does not perform substitutions or formatting of any kind.

__See
Also:__  [+ expressionForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi), [- statement](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643umf2gk3lfnz2a)

---

### setUseAliases:

`- (void)setUseAliases:(BOOL)flag`

Tells the receiver whether or not to use table
aliases.

__See Also:__  [- useAliases](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65ltmvawy2lbonsxg)

---

### shouldUseBindVariableForAttribute:

`- (BOOL)shouldUseBindVariableForAttribute:(EOAttribute
*)attribute`

Returns YES if the receiver can provide a bind
variable dictionary for _attribute_, NO otherwise.
Bind variables aren't used for values associated with this attribute
when the class method [useBindVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkcnfxgivtbojuwcytmmvzq) returns NO. EOSQLExpression's
implementation returns NO. An SQL expression subclass should override
this method to return YES if the receiver should use bind variables
for attributes with _attribute_'s
external type. It should also return YES for any attribute for which
the receiver must use bind variables.

__See
Also:__  [- mustUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2)

---

### sqlStringForAttribute:

`- (NSString *)sqlStringForAttribute:(EOAttribute
*)attribute`

Returns the SQL string for attribute, complete
with a table alias if the receiver uses table aliases. Invoked from [sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2) when
the attribute name is not a path.

__See Also:__  [- sqlStringForAttributePath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkqmf2gqoq)

---

### sqlStringForAttributeNamed:

`- (NSString *)sqlStringForAttributeNamed:(NSString
*)name`

Returns the SQL string for the attribute named _name_,
complete with a table alias if the receiver uses table aliases.
Generates the return value using [sqlStringForAttributePath:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkqmf2gqoq) if _name_ is
an attribute path ("department.name", for example); otherwise,
uses [sqlStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizj2).

---

### sqlStringForAttributePath:

`- (NSString *)sqlStringForAttributePath:(NSArray
*)path`

Returns the SQL string for _path_,
complete with a table alias if the receiver uses table aliases.
Invoked from [sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2) when
the specified attribute name is a path ("department.location.officeNumber",
for example). _path_ is an array of
any number of EORelationship objects followed by an EOAttribute
object. The EORelationship and EOAttribute objects each correspond
to a component in path. For example, if the attribute name argument
to __sqlStringForAttributeNamed:__ is "department.location.officeNumber", _path_ is
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
of adding a "relationship path"-"alias name" entry to the [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq) dictionary.

__See
Also:__  [- sqlStringForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizj2), [- aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq)

---

### sqlStringFor:caseInsensitiveLike:

`- (NSString *)sqlStringForValue:(NSString
*)valueString
caseInsensitiveLikeKey:(NSString
*)keyString`

Overridden by subclasses to return a case insensitive
comparison of _valueString_ and _keyString_.
For example, a subclass implementation might return the string "UPPER(_keyString_)
LIKE UPPER(_valueString_)".

---

### sqlStringForConjoinedQualifiers:

`- (NSString *)sqlStringForConjoinedQualifiers:(NSArray
*)qualifiers`

Creates and returns an SQL string that is the
result of interposing the word "AND" between the SQL strings
for the qualifiers in _qualifiers_.
Generates an SQL string for each qualifier by sending [sqlStringForSQLExpression:](EOQualifierSQLGeneration.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu) messages
to the qualifiers with `self` as
the argument. If the SQL string for a qualifier contains only white
space, it isn't included in the return value. The return value
is enclosed in parentheses if the SQL strings for two or more qualifiers
were ANDed together.

---

### sqlStringForDisjoinedQualifiers:

`- (NSString *)sqlStringForDisjoinedQualifiers:(NSArray
*)qualifiers`

Creates and returns an SQL string that is the
result of interposing the word "OR" between the SQL strings
for the qualifiers in _qualifiers_.
Generates an SQL string for each qualifier by sending [sqlStringForSQLExpression:](EOQualifierSQLGeneration.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu) messages
to the qualifiers with self as the argument. If the SQL string for a
qualifier contains only white space, it isn't included in the
return value. The return value is enclosed in parentheses if the
SQL strings for two or more qualifiers were ORed together.

---

### sqlStringForKeyComparisonQualifier:

`- (NSString *)sqlStringForKeyComparisonQualifier:(EOKeyComparisonQualifier
*)qualifier`

Creates and returns an SQL string that is the
result of interposing an operator between the SQL strings for the
right and left keys in _qualifier_.
Determines the SQL operator by invoking [sqlStringForSelector:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknswyzldorxxeotwmfwhkzj2) with _qualifier_'s
selector and nil for the value. Generates SQL strings for _qualifier_'s
keys by invoking [sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2) to
get SQL strings. This method also formats the strings for the right
and left keys using [formatSQLString:format:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq) with
the corresponding attributes' "read" formats.

---

### sqlStringForKeyValueQualifier:

`- (NSString *)sqlStringForKeyValueQualifier:(EOKeyValueQualifier
*)qualifier`

Creates and returns an SQL string that is the
result of interposing an operator between the SQL strings for _qualifier_'s
key and value. Determines the SQL operator by invoking [sqlStringForSelector:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sknswyzldorxxeotwmfwhkzj2) with _qualifier_'s
selector and value. Generates an SQL string for _qualifier_'s
key by invoking [sqlStringForAttributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sif2hi4tjmj2xizkomfwwkzb2) to
get an SQL string and [formatSQLString:format:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fgukmkn2he2lom45gm33snvqxioq) with
the corresponding attribute's "read" format. Similarly, generates
an SQL string for qualifier's value by invoking [sqlStringForValue:attributeNamed:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33skzqwy5lfhjqxi5dsnfrhk5dfjzqw2zlehi) to
get an SQL string and [formatValue:forAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fmylmovstuztpojaxi5dsnfrhk5dfhi) to format
it. (First invokes [sqlPatternFromShellPattern:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5zxc3cqmf2hizlsnzdhe33nknugk3dmkbqxi5dfojxdu) for
the value if _qualifier_'s selector
is `EOQualifierOperatorLike`.)

---

### sqlStringForNegatedQualifier:

`- (NSString *)sqlStringForNegatedQualifier:(EOQualifier
*)qualifier`

Creates and returns an SQL string that is the
result of surrounding the SQL string for _qualifier_ in parentheses
and appending it to the word "not". For example, if the string
for _qualifier_ is "FIRST_NAME =
‘John'", __sqlStringForNegatedQualifier:__ returns
the string "not (FIRST_NAME = ‘John')".

Generates an
SQL string for _qualifier_ by sending
an [sqlStringForSQLExpression:](EOQualifierSQLGeneration.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu) message
to _qualifier_ with self as the argument.
If the SQL string for _qualifier_ contains
only white space, this method returns nil.

---

### sqlStringForSchemaObjectName:

`- (NSString *)sqlStringForSchemaObjectName:(NSString
*)name`

Returns _name_ enclosed
in the external name quote character if the receiver uses quoted
external names, otherwise simply returns _name_ unaltered.

__See
Also:__  [+ useQuotedExternalNames](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkrovxxizleiv4hizlsnzqwyttbnvsxg), [- externalNameQuoteCharacter](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6zlyorsxe3tbnrhgc3lfkf2w65dfinugc4tbmn2gk4q)

---

### sqlStringForSelector:value:

`- (NSString *)sqlStringForSelector:(SEL)selector
value:(id)value`

Returns an SQL operator for _selector_ and _value_.
The possible values for _selector_ are
defined as constants (in EOControl). The following table summarizes
EOSQLExpression's default mapping:

|  |  |
| --- | --- |
| __Selector (Constant)__ | __SQL Operator__ |
| `EOQualifierOperatorIsEqual` | "is" if value is an EONull, "=" otherwise |
| `EOQualifierOperatorNotEqual` | "is not" if _value_ is an EONull, "<>" otherwise |
| `EOQualifierOperatorLessThan` | "<" |
| `EOQualifierOperatorGreaterThan` | ">" |
| `EOQualifierOperatorLessThanOrEqualTo` | "<=" |
| `EOQualifierOperatorGreaterThanOrEqualTo` | ">=" |
| `EOQualifierOperatorLike` | "like" |

Raises an `NSInternalInconsistencyException` if _selector_ is
an unknown operator.

__See Also:__  [- sqlStringForKeyComparisonQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjnsxsq3pnvygc4tjonxw4ulvmfwgsztjmvzdu), [- sqlStringForKeyValueQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643rnrjxi4tjnztum33sjnsxsvtbnr2wkulvmfwgsztjmvzdu)

---

### sqlStringForValue:attributeNamed:

`- (NSString *)sqlStringForValue:(id)value
attributeNamed:(NSString *)name`

Returns a string for _value_ appropriate
for use in an SQL statement. If the receiver uses a bind variable for
the attribute named _name_, then __sqlStringForValue:attributeNamed:__ gets
the bind variable dictionary for the attribute, adds it to the receiver's
array of bind variables dictionaries, and returns the value for the
binding's [EOBindVariablePlaceHolderKey](#apple-ijduorkcincuq).
Otherwise, this method invokes [formatValue:forAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5tg64tnmf2fmylmovstuztpojaxi5dsnfrhk5dfhi) and
returns the formatted string for _value_.

__See
Also:__  [- mustUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc63lvon2fk43fijuw4zcwmfzgsylcnrsum33sif2hi4tjmj2xizj2), [- shouldUseBindVariableForAttribute:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643in52wyzcvonsue2lomrlgc4tjmfrgyzkgn5zec5duojuwe5lumu5a), [+ useBindVariables](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of52xgzkcnfxgivtbojuwcytmmvzq), [- bindVariableDictionaries](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ytjnzsfmylsnfqwe3dfiruwg5djn5xgc4tjmvzq), [- addBindVariableDictionary:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrbgs3tekzqxe2lbmjwgkrdjmn2gs33omfzhsoq)

---

### statement

`- (NSString *)statement`

Returns the complete SQL statement for the receiver.
An SQL statement can be assigned to an EOSQLExpression object directly
using the class method [expressionForString:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwy3jpivhvgukmiv4ha4tfonzws33of5sxq4dsmvzxg2lpnzdg64storzgs3thhi) or
using the instance method [setStatement:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forjxiylumvwwk3tuhi). Generally, however,
an EOSQLExpression's statement is built up using one of the following
methods:

- [- prepareSelectExpressionWithAttributes:lock:fetchSpecification:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfknswyzldorcxq4dsmvzxg2lpnzlws5diif2hi4tjmj2xizlthjwg6y3lhjtgk5ddnbjxazldnftgsy3boruw63r2)
- [- prepareInsertExpressionWithRow:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfjfxhgzlsorcxq4dsmvzxg2lpnzlws5dikjxxooq)
- [- prepareUpdateExpressionWithRow:qualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfkvygiylumvcxq4dsmvzxg2lpnzlws5dikjxxootrovqwy2lgnfsxeoq)
- [- prepareDeleteExpressionForQualifier:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc64dsmvygc4tfirswyzlumvcxq4dsmvzxg2lpnzdg64srovqwy2lgnfsxeoq)

---

### tableListWithRootEntity:

`- (NSString *)tableListWithRootEntity:(EOEntity
*)entity`

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

__tableListWithRootEntity:__ creates
a string containing the table name for _entity_ and
a corresponding table alias ("EMPLOYEE t0", for example). For
each entry in [aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq),
this method appends a new table name and table alias.

__See
Also:__  [- useAliases](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc65ltmvawy2lbonsxg), [- aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq)

---

### useAliases

`- (BOOL)useAliases`

Returns YES if the receiver generates statements
with table aliases, NO otherwise. For example, the following SELECT
statement uses table aliases:
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
Also:__  [- setUseAliases:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc643forkxgzkbnruwc43fom5a), [- aliasesByRelationshipPath](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylmnfqxgzltij4vezlmmf2gs33oonugs4cqmf2gq)

---

### valueList

`- (NSMutableString *)valueList`

Returns the comma-separated list of values used
in an INSERT statement. For example, the value list for the following
INSERT statement:
> ```
> INSERT EMPLOYEE (FIRST_NAME, LAST_NAME, EMPLOYEE_ID, DEPARTMENT_ID, SALARY)
> VALUES ('Shaun', 'Hayes', 1319, 23, 4600)
> ```

is
"‘Shaun', ‘Hayes', 1319, 23, 4600". An EOSQLExpression's `valueList` is
generated a value at a time with [addInsertListAttribute:value:](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc6ylemrew443foj2ey2ltoraxi5dsnfrhk5dfhj3gc3dvmu5a) messages.

---

### whereClauseString

`- (NSString *)whereClauseString`

Returns the part of the receiver's WHERE clause
that qualifies rows. The whereClauseString does not specify join
conditions; the [joinClauseString](#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw443unuxukt2tkfgek6dqojsxg43jn5xc62tpnfxeg3dbovzwku3uojuw4zy) does
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
generally set by sending a [sqlStringForSQLExpression:](EOQualifierSQLGeneration.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu) message
to an EOQualifier object.

__See Also:__  [- sqlStringForSQLExpression:](EOQualifierSQLGeneration.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5uw45dgnuxukt2rovqwy2lgnfsxeu2rjrdwk3tfojqxi2lpnyxxg4lmkn2he2lom5dg64stkfgek6dqojsxg43jn5xdu) (EOQualifierSQLGeneration
protocol)

---

[![Table of Contents](attachments/images/up.gif)](../EOAccessTOC.md)
