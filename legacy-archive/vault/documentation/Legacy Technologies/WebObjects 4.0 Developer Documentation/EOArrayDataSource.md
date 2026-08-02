---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/Classes/EOArrayDataSource.html
archived_at: '2026-07-18T01:28:24.467968Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/Java/frameset.html)

[!](The%20EOControl%20Framework.md)
[!](EOAndQualifier.md)

---

# EOArrayDataSource

__Inherits From:__
EODataSource : Object (Java Client)
EODataSource : NSObject (Yellow Box)

__Package:__
com.apple.client.eocontrol (Java Client)
com.apple.yellow.eocontrol (Yellow Box)

## Class Description

EOArrayDataSource is a concrete subclass of EODataSource that can be used to provide enterprise objects to a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) without having to fetch them from the database. In an EOArrayDataSource, objects are maintained in an in-memory NSArray.

EOArrayDataSource can fetch, insert, and delete objects-operations it performs directly with its array. It can also provide a detail data source.

## Constructors

---

#### EOArrayDataSource

public __EOArrayDataSource__ (
EOClassDescription _classDescription_,
EOEditingContext _editingContext_)

Creates and returns an EOArrayDataSource object where _classDescription_ contains information about the objects provided by the EOArrayDataSource and _editingContext_ is the EOArrayDataSource's editing context. Either argument may be null

## Instance Methods

---

#### setArray

public void __setArray__ (foundation.NSArray _array_)

Sets the receiver's array of objects to _array_.

---

[!](The%20EOControl%20Framework.md)
[!](EOAndQualifier.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
