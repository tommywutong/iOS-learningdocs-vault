---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/OpenBasePlugIn.OpenBaseSy.html
archived_at: '2026-07-15T08:13:57.345547Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# OpenBasePlugIn.OpenBaseSynchronizationFactory

> __Inherits from:__ com.webobjects.eoaccess.EOSynchronizationFactory : Object

> __Implements:__ EOSchemaGeneration, EOSchemaSynchronization

> __Package:__ com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Interfaces Implemented

---

> EOSchemaGeneration createTableStatementsForEntityGroup primaryKeyConstraintStatementsForEntityGroup primaryKeySupportStatementsForEntityGroup dropPrimaryKeySupportStatementsForEntityGroup EOSchemaSynchronization statementsToRenameTableNamed statementsToModifyColumnNullRule statementsToRenameColumnNamed statementsToDropForeignKeyConstraintsOnEntityGroups statementsToDropPrimaryKeyConstraintsOnEntityGroups statementsToImplementPrimaryKeyConstraintsOnEntityGroups supportsDirectColumnCoercion supportsDirectColumnDeletion supportsDirectColumnInsertion supportsDirectColumnNullRuleModification supportsDirectColumnRenaming supportsSchemaSynchronization

## Method Types

---

> All methods OpenBasePlugIn.OpenBaseSynchronizationFactory isColumnTypeEquivalentToColumnType objectStoreChangesFromAttributeToAttribute

## Constructors

---

### OpenBasePlugIn.OpenBaseSynchronizationFactory

`public OpenBasePlugIn.OpenBaseSynchronizationFactory( com.webobjects.eoaccess.EOAdaptor anEOAdaptor)`

Description forthcoming.

---

## Instance Methods

---

### createTableStatementsForEntityGroup

`public NSArray createTableStatementsForEntityGroup(NSArray aNSArray)`

See the method description in EOSchemaGeneration.

---

### dropPrimaryKeySupportStatementsForEntityGroup

`public NSArray dropPrimaryKeySupportStatementsForEntityGroup( NSArray entityGroup)`

See the method description in EOSchemaGeneration.

---

### isColumnTypeEquivalentToColumnType

`public boolean isColumnTypeEquivalentToColumnType( com.webobjects.eoaccess.EOSchemaSynchronization.ColumnTypes candidate, com.webobjects.eoaccess.EOSchemaSynchronization.ColumnTypes columnType, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### objectStoreChangesFromAttributeToAttribute

`public NSDictionary objectStoreChangesFromAttributeToAttribute( com.webobjects.eoaccess.EOAttribute schemaAttribute, com.webobjects.eoaccess.EOAttribute modelAttribute)`

Description forthcoming.

---

### primaryKeyConstraintStatementsForEntityGroup

`public NSArray primaryKeyConstraintStatementsForEntityGroup( NSArray entityGroup)`

See the method description in EOSchemaGeneration.

---

### primaryKeySupportStatementsForEntityGroup

`public NSArray primaryKeySupportStatementsForEntityGroup( NSArray entityGroup)`

See the method description in EOSchemaGeneration.

---

### statementsToDropForeignKeyConstraintsOnEntityGroups

`public NSArray statementsToDropForeignKeyConstraintsOnEntityGroups( NSArray entityGroups, NSDictionary changes, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### statementsToDropPrimaryKeyConstraintsOnEntityGroups

`public NSArray statementsToDropPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroups, NSDictionary changes, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### statementsToImplementPrimaryKeyConstraintsOnEntityGroups

`public NSArray statementsToImplementPrimaryKeyConstraintsOnEntityGroups( NSArray entityGroups, NSDictionary changes, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### statementsToModifyColumnNullRule

`public NSArray statementsToModifyColumnNullRule( String columnName, String tableName, boolean allowsNull, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### statementsToRenameColumnNamed

`public NSArray statementsToRenameColumnNamed( String columnName, String tableName, String newName, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### statementsToRenameTableNamed

`public NSArray statementsToRenameTableNamed( String tableName, String newName, NSDictionary options)`

See the method description in EOSchemaSynchronization.

---

### supportsDirectColumnCoercion

`public boolean supportsDirectColumnCoercion()`

See the method description in EOSchemaSynchronization.

---

### supportsDirectColumnDeletion

`public boolean supportsDirectColumnDeletion()`

See the method description in EOSchemaSynchronization.

---

### supportsDirectColumnInsertion

`public boolean supportsDirectColumnInsertion()`

See the method description in EOSchemaSynchronization.

---

### supportsDirectColumnNullRuleModification

`public boolean supportsDirectColumnNullRuleModification()`

See the method description in EOSchemaSynchronization.

---

### supportsDirectColumnRenaming

`public boolean supportsDirectColumnRenaming()`

See the method description in EOSchemaSynchronization.

---

### supportsSchemaSynchronization

`public boolean supportsSchemaSynchronization()`

See the method description in EOSchemaSynchronization.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
