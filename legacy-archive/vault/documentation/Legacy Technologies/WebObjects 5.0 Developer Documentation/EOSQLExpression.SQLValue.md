---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOSQLExpression.SQLValue.html
archived_at: '2026-07-15T08:13:42.075968Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

# EOSQLExpression.SQLValue

> __Implemented by:__ : EOAttribute, EOEntity, EORelationship, EOSQLQualifier

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

Defines API for objects that can provide values for themselves to be used in SQL statements. Classes that implement the method-EOAttribute, EOEntity, EORelationship, and EOSQLQualifier-declare that they implement this method.

## Instance Methods

---

### valueForSQLExpression

`public abstract String valueForSQLExpression(EOSQLExpression context)`

Returns a String to be used to represent the receiver in an SQL statement.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
