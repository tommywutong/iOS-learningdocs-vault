---
title: set
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsset/set
source_url: 'https://developer.apple.com/documentation/foundation/nsset/set'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/set.json'
content_hash: 'sha256:817f073aa4752881'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# set

<sub>Type Method</sub>

Creates and returns an empty set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) set;
```

## Return Value

A new empty set.

## Discussion

This method is declared primarily for the use of mutable subclasses of `NSSet`.

## See Also

### Related Documentation

- [Collections Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/Collections/Collections.html#//apple_ref/doc/uid/10000034i)

### Creating a Set

- [setWithArray:](setwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [setWithObjects:](setwithobjects_.md) — Creates and returns a set containing the objects in a given argument list.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [setWithSet:](setwithset_.md) — Creates and returns a set containing the objects from another set.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
