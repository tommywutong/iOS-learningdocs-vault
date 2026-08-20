---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Classes/EOArrayDataSource.html
archived_at: '2026-07-18T01:28:33.900841Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](The%20EOControl%20Framework-2.md)
[!](EOAndQualifier-2.md)

---

# EOArrayDataSource

__Inherits From:__
EODataSource : NSObject

__Conforms To:__ NSCoding
NSObject (NSObject)

__Declared in:__ EOControl/EOArrayDataSource.h

EOArrayDataSource is a concrete subclass of EODataSource that can be used to provide enterprise objects to a display group (EODisplayGroup from EOInterface or WODisplayGroup from WebObjects) without having to fetch them from the database. In an EOArrayDataSource, objects are maintained in an in-memory NSArray.

EOArrayDataSource can fetch, insert, and delete objects-operations it performs directly with its array. It can also provide a detail data source.

---

## Adopted Protocols

**NSCoding**

**encodeWithCoder:

**initWithCoder:****

---

#### initWithClassDescription:editingContext:

- `initWithClassDescription:`(EOClassDescription \*)_classDescription_`editingContext:`(EOEditingContext \*)_editingContext_

The designated initializer of the EOArrayDataSource class, this method initializes a newly allocated EOArrayDataSource object with _classDescription_ and _editingContext_, both of which it retains. _classDescription_ contains information about the objects provided by the EOArrayDataSource and editingContext is the EOArrayDataSource's EOEditingContext. Either argument may be nil. Returns `self`.

---

#### setArray:

- (void)`setArray:`(NSArray \*)_array_

Sets the receiver's array of objects to _array_.

---

[!](The%20EOControl%20Framework-2.md)
[!](EOAndQualifier-2.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
