---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Classes/EOSQLExpressionFactory.html
archived_at: '2026-07-15T08:13:41.712452Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md) 

# EOSQLExpression

> **__Inherits from:__**
> : Object

> **__Package:__**
> : com.webobjects.eoaccess

---

## Class Description

---

This class has been introduced to create instances of EOSQLExpressions. Very little of the API is new. Rather, most of it was moved EOSQLExpressionFactory from EOSQLExpression. The API is essentially the same except that in 4.5, the methods were static methods. In 5.0 the methods on EOSQLExpressionFactory are instance methods.

## Method Types

---

> **Constructors**
> : [EOSQLExpressionFactory](#apple-f4xwc4dqnrsv64tfmyxwuylwmexws3ttorws6rkpkniuyrlyobzgk43tnfxw4l2fj5jvctcfpbyhezltonuw63sgmfrxi33spe)

## Constructors

---

### EOSQLExpressionFactory

`EOSQLExpressionFactory(EOAdaptor adaptor)`

Creates an EOSQLExpressionFactory for the specified EOAdaptor.

---

## Instance Methods

---

### createExpression

`public EOSQLExpression createExpression()`

Creates a new instance of the factory's EOSQLExpression class.

---

### deleteStatementWithQualifier

`public EOSQLExpression deleteStatementWithQualifier(EOQualifier qualifier, EOEntity entity)`

---

### expressionClass

`public Class expressionClass()`

Returns the factory's EOSQLExpression class.

---

### expressionForEntity

`public EOSQLExpression expressionForEntity(EOEntity entity)`

Creates a new instance of the factory's EOSQLExpression class and assigns the specified entity to that expression.

---

### expressionForString

`public EOSQLExpression expressionForString(String astring)`

Description forthcoming.

---

### insertStatementForRow

`public EOSQLExpression insertStatementForRow(NSDictionary row, EOEntity entity)`

Description forthcoming.

---

### selectStatementForAttributes

`public EOSQLExpression selectStatementForAttributes( NSArray attributes, boolean aboolean, EOFetchSpecification fetchSpec, EOEntity entity)`

Description forthcoming.

---

### updateStatementForRow

`public EOSQLExpression updateStatementForRow(NSDictionary row, EOQualifier qualifier, EOEntity entity)`

Description forthcoming.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
