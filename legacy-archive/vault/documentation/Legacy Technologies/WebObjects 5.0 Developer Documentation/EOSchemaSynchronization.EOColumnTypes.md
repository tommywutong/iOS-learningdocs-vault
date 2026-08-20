---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOAccessRef/Java/Protocols/EOSchemeSyn.EOColumnTypes.html
archived_at: '2026-07-15T08:13:42.090050Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

# EOSchemaSynchronization.EOColumnTypes

> **__Package:__**
> : com.webobjects.eoaccess

---

## Interface Description

---

You only need to know about this interface if you are implementing schema synchronization API for a custom adaptor. In that case, you don't have to implement a class that implements this interface; EOSQLExpression's implementation of the schema synchronization API uses a private class that implements it. You only need to know about the interface because your method implementations of the above methods needs to compare two objects that implement the protocol.

## Instance Methods

---

### name

`public abstract String name()`

Returns the receiver's name.

---

### precision

`public abstract int precision()`

Returns the receiver's precision.

---

### scale

`public abstract int scale()`

Returns the receiver's scale.

---

### width

`public abstract int width()`

Returns the receiver's width.

---

© 2001 Apple Computer, Inc. (Last Published April 13, 2001)

[![Table of Contents](attachments/EOAccessRef/Java/Art/up.gif)](../EOAccessTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
