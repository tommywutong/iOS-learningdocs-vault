---
title: WebObjects 4.5 Developer Documentation
apple_id: TP40006775
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.5/System/Library/Frameworks/EOControl.framework/ObjC_classic/Classes/EOArrayDataSource.html
archived_at: '2026-07-15T08:11:39.155740Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.5 Developer Documentation](webobjects.md)


__PATH__
[Documentation](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/index.html) __>__ [WebObjects 4.5](webobjects.md) __>__
EOControl Reference

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)

# EOArrayDataSource

> **__Inherits
> from:__**
> : [EODataSource](EODataSource-3.md#apple-f4xwc4dqnrsv64tfmyxw6y3df5rwyl2fj5cgc5dbknxxk4tdmu) : NSObject

> **__Conforms to:__**
> : NSCoding
> : NSObject (NSObject)

> __Declared in:__ : EOControl/EOArrayDataSource.h

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

## Adopted Protocols

---

> NSCoding: __- encodeWithCoder:__
> : __- initWithCoder:__

## Instance Methods

---

### initWithClassDescription:editingContext:

`- initWithClassDescription:(EOClassDescription
*)classDescription editingContext:(EOEditingContext
*)editingContext`

The designated initializer of the EOArrayDataSource
class, this method initializes a newly allocated EOArrayDataSource
object with _classDescription_ and _editingContext_,
both of which it retains. _classDescription_ contains
information about the objects provided by the EOArrayDataSource
and _editingContext_ is the EOArrayDataSource's
EOEditingContext. Either argument may be `nil`.
Returns `self`.

---

### setArray:

`- (void)setArray:(NSArray
*)array`

Sets the receiver's array of objects to _array_.

---

[![Table of Contents](attachments/images/up.gif)](../EOControlTOC.md)
