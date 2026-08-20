---
title: WebObjects 5.0 Developer Documentation
apple_id: TP40006776
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_5/EOControlRef/Java/Classes/EOArrayDataSource.html
archived_at: '2026-07-15T08:13:46.131400Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 5.0 Developer Documentation](webobjects.md)


|  |
| --- |
| __PATH__[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects](webobjects.md) |

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

# EOArrayDataSource

> **__Inherits from:__**
> : [EODataSource](EODataSource.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuiylumfjw65lsmnsq)

> **__Implements:__**
> : Serializable

> **__Package:__**
> : com.webobjects.eocontrol

---

## Class Description

---

EOArrayDataSource is a concrete subclass of EODataSource that can be used to provide enterprise objects to a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) without having to fetch them from the database. In an EOArrayDataSource, objects are maintained in an in-memory NSArray.

EOArrayDataSource can fetch, insert, and delete objects-operations it performs directly with its array. It can also provide a detail data source.

## Constructors

---

### EOArrayDataSource

`public EOArrayDataSource( EOClassDescription classDescription, EOEditingContext editingContext)`

Creates and returns an EOArrayDataSource object where _classDescription_ contains information about the objects provided by the EOArrayDataSource and _editingContext_ is the EOArrayDataSource's editing context. Either argument may be `null`.

---

## Instance Methods

---

### classDescriptionForObjects

`public EOClassDescription classDescriptionForObjects()`

Description forthcoming.

---

### createObject

`public Object createObject()`

Description forthcoming.

---

### dataSourceQualifiedByKey

`public EODataSource dataSourceQualifiedByKey(String aString)`

Description forthcoming.

---

### deleteObject

`public void deleteObject(Object anObject)`

Description forthcoming.

---

### editingContext

`public EOEditingContext editingContext()`

Description forthcoming.

---

### fetchObjects

`public NSArray fetchObjects()`

Description forthcoming.

---

### insertObject

`public void insertObject(Object anObject)`

Description forthcoming.

---

### qualifyWithRelationshipKey

`public void qualifyWithRelationshipKey( String aString, Object anObject)`

Description forthcoming.

---

### setArray

`public void setArray(foundation.NSArray array)`

Sets the receiver's array of objects to _array_.

---

© 2001 Apple Computer, Inc. (Last Published April 19, 2001)

[![Table of Contents](attachments/EOControlRef/Java/Art/up.gif)](../EOControlTOC.md)

Copyright © 2016 Apple Inc. All rights reserved.

- [Terms of Use](http://www.apple.com/legal/internet-services/terms/site.html)
- [Privacy Policy](http://www.apple.com/privacy/)
