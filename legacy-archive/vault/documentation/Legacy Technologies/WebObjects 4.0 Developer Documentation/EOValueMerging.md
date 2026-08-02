---
title: WebObjects 4.0 Developer Documentation
apple_id: TP40006774
resource_type: Guide
platform: macOS
topic: null
technology: null
published: '2007-12-11'
source_url: https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/Protocols/EOValueMerging.html
archived_at: '2026-07-18T01:28:41.899553Z'
---
> 导航：[总目录](../../../README.md) · [documentation](../../../_indexes/documentation.md) · [WebObjects 4.0 Developer Documentation](webobjects.md)


__PATH__
[WebObjects 4.0 Documentation](webobjects.md) __>__
[EOControl Reference](https://developer.apple.com/library/archive/documentation/LegacyTechnologies/WebObjects/WebObjects_4.0/System/Library/Frameworks/EOControl.framework/Resources/English.lproj/Documentation/Reference/ObjC_classic/frameset.html)

[!](EOValidation-4.md)

---

# EOValueMerging

---

#### (informal protocol)

__Category Of:__ NSObject

__Declared in:__ EOControl/EOClassDescription.h

## Instance Methods

**Merging values**

**- changesFromSnapshot:

**- reapplyChangesFromDictionary:****

---

#### changesFromSnapshot:

- (NSDictionary \*)__changesFromSnapshot:__ (NSDictionary \*)_snapshot_

The result is like a snapshot except that it contains only those keys that refer to uncommitted changes in the object relative to the given snapshot. For to-many keys, the uncommitted value is an array of two arrays: uncommitted additions and uncommitted deletions. The return value is autoreleased.

---

#### reapplyChangesFromDictionary:

- (void)__reapplyChangesFromDictionary:__ (NSDictionary \*)_changes_

Similar to __takeValuesFromDictionary:__ but the _changes_ dictionary is not quite the same as a snapshot. For to-many relationship keys, the value is an array with exactly two arrays in it: the first is an array of objects to be added to the relation, and the second is an array of objects to be removed from the relation. Attribute and to-one relationship keys refer to values that should replace the current value. An instance of EONull is used in the _changes_ dictionary as a placeholder for nil.

---

[!](EOValidation-4.md)

---

_Copyright © 1998, Apple Computer, Inc. All rights reserved._
