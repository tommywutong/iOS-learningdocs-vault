---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/JDBCAdaptorRef/Java/Classes/OraclePlugIn.html
archived_at: '2026-07-15T08:13:57.410072Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

# OraclePlugIn

> **__Inherits from:__**
> : [JDBCPlugIn](JDBCPlugIn.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpjjceeq2qnr2woslo) : Object

> **__Package:__**
> : com.webobjects.jdbcadaptor

---

## Class Description

---

Documentation for this class is forthcoming.

## Method Types

---

> **All methods**
> : [OraclePlugIn](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5hxeyldnrsva3dvm5ew4): [createSynchronizationFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5rxezlborsvg6lomnuhe33onf5gc5djn5xemyldorxxe6i): [databaseProductName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5sgc5dbmjqxgzkqojxwi5ldorhgc3lf): [defaultDriverName](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5sgkztbovwhirdsnf3gk4somfwwk): [defaultExpressionClass](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5sgkztbovwhirlyobzgk43tnfxw4q3mmfzxg): [fetchBLOB](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5tgk5ddnbbeyt2c): [fetchCLOB](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5tgk5ddnbbuyt2c): [newPrimaryKeys](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5xgk52qojuw2ylspffwk6lt): [schemaNameForEntity](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5zwg2dfnvqu4ylnmvdg64sfnz2gs5dz): [sqlStatementForGettingTableNames](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof5zxc3ctorqxizlnmvxhirtpojdwk5dunfxgovdbmjwgkttbnvsxg): [updateLOBs](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof52xazdborsuyt2com): [wildcardPatternForAttributes](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6t3smfrwyzkqnr2woslof53ws3demnqxezcqmf2hizlsnzdg64sbor2he2lcov2gk4y)

## Constructors

---

### OraclePlugIn

`public OraclePlugIn(JDBCAdaptor aJDBCAdaptor)`

Description forthcoming.

---

## Instance Methods

---

### createSynchronizationFactory

`protected com.webobjects.eoaccess.EOSynchronizationFactory createSynchronizationFactory()`

Description forthcoming.

---

### databaseProductName

`public String databaseProductName()`

Description forthcoming.

---

### defaultDriverName

`public String defaultDriverName()`

Description forthcoming.

---

### defaultExpressionClass

`public Class defaultExpressionClass()`

Description forthcoming.

---

### fetchBLOB

`protected Object fetchBLOB( java.sql.ResultSet aResultSet, int column, com.webobjects.eoaccess.EOAttribute anEOAttribute, boolean materialize)`

Description forthcoming.

---

### fetchCLOB

`protected Object fetchCLOB( java.sql.ResultSet aResultSet, int column, com.webobjects.eoaccess.EOAttribute anEOAttribute, boolean materialize)`

Description forthcoming.

---

### newPrimaryKeys

`protected NSDictionary newPrimaryKeys( int count com.webobjects.eoaccess.EOEntity anEOEntity, JDBCChannel aJDBCChannel)`

Description forthcoming.

---

### schemaNameForEntity

`protected String schemaNameForEntity(com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### sqlStatementForGettingTableNames

`protected String sqlStatementForGettingTableNames()`

Description forthcoming.

---

### updateLOBs

`protected void updateLOBs( JDBCChannel aJDBCChannel, JDBCExpression aJDBCExpression, NSDictionary row, com.webobjects.eoaccess.EOEntity anEOEntity)`

Description forthcoming.

---

### wildcardPatternForAttributes

`protected String wildcardPatternForAttributes()`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 15, 2001)

[![Table of Contents](attachments/JDBCAdaptorRef/Java/Art/up.gif)](../TOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
