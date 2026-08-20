---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/Java/Classes/EOArrayDataSource.html
archived_at: '2026-07-15T08:11:37.060054Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOArrayDataSource

> **__Inherits
> from:__**
> : [(com.apple.client.eocontrol) EODataSource](EODataSource.md#apple-f4xwc4dqnrsv64tfmyxwuylwmexwg3bpivhuiylumfjw65lsmnsq) : Object
> (com.apple.yellow.eocontrol) EODataSource : NSObject

> **__Package:__**
> : com.apple.client.eocontrol
> : com.apple.yellow.eocontrol

---

## Class Description

---

EOArrayDataSource is a concrete subclass of EODataSource that
can be used to provide enterprise objects to a display group (EODisplayGroup
from EOInterface or WODisplayGroup from WebObjects) without having
to fetch them from the database. In an EOArrayDataSource, objects
are maintained in an in-memory NSArray.

EOArrayDataSource can fetch, insert, and delete objects-operations
it performs directly with its array. It can also provide a detail
data source.

## Constructors

---

### EOArrayDataSource

`public EOArrayDataSource(
EOClassDescription classDescription,
EOEditingContext editingContext)`

Creates and returns an EOArrayDataSource object
where _classDescription_ contains information
about the objects provided by the EOArrayDataSource and _editingContext_ is
the EOArrayDataSource's editing context. Either argument may be
null

---

## Instance Methods

---

### setArray

`public void setArray(foundation.NSArray array)`

Sets the receiver's array of objects to _array._

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
