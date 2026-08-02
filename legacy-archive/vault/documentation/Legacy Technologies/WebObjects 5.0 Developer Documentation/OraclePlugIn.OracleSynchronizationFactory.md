---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/OraclePlugIn.OracleSynchr.html
archived_at: '2026-07-15T08:13:57.393710Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# OraclePlugIn.OracleSynchronizationFactory

> __Inherits from:__ com.webobjects.eoaccess.EOSynchronizationFactory : Object

> __Implements:__ EOSchemaGeneration, EOSchemaSynchronization

> __Package:__ com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Interfaces Implemented

---

> EOSynchronizationFactory createDatabaseStatementsForConnectionDictionary dropDatabaseStatementsForConnectionDictionary dropTableStatementsForEntityGroup appendExpressionToScript primaryKeySupportStatementsForEntityGroup supportsSchemaSynchronization EOSchemaGeneration

## Method Types

---

> All methods OraclePlugIn.OracleSynchronizationFactory

## Constructors

---

### OraclePlugIn.OracleSynchronizationFactory

`public OraclePlugIn.OracleSynchronizationFactory( com.webobjects.eoaccess.EOAdaptor anEOAdaptor)`

Description forthcoming.

---

## Instance Methods

---

### appendExpressionToScript

`public void appendExpressionToScript( com.webobjects.eoaccess.EOSQLExpression anEOSQLExpression, StringBuffer script)`

See the method description in the documentation for EOSynchronizationFactory.

---

### createDatabaseStatementsForConnectionDictionary

`public NSArray createDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

See the method description in the documentation for EOSynchronizationFactory.

---

### dropDatabaseStatementsForConnectionDictionary

`public NSArray dropDatabaseStatementsForConnectionDictionary( NSDictionary connectionDictionary, NSDictionary adminDictionary)`

See the method description in the documentation for EOSynchronizationFactory.

---

### dropTableStatementsForEntityGroup

`public NSArray dropTableStatementsForEntityGroup(NSArray entityGroup)`

See the method description in the documentation for EOSynchronizationFactory.

---

### primaryKeySupportStatementsForEntityGroup

`public NSArray primaryKeySupportStatementsForEntityGroup(NSArray entityGroup)`

See the method description in the documentation for EOSynchronizationFactory.

---

### supportsSchemaSynchronization

`public boolean supportsSchemaSynchronization()`

See the method description in the documentation for EOSynchronizationFactory.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
