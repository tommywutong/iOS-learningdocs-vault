---
title: 'addingObjects(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/addingobjects(from:)-2i31h'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/addingobjects(from:)-2i31h'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/addingobjects%28from%3A%29-2i31h.json'
content_hash: 'sha256:0d78afb8586c7dba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# addingObjects(from:)

<sub>Instance Method</sub>

Returns a new set formed by adding the objects in a given set to the receiving set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addingObjects(from other: Set<AnyHashable>) -> Set<AnyHashable>
```

## Parameters

- `other` — The set of objects to add to the receiving set.

## Return Value

A new set formed by adding the objects in `other` to the receiving set.

## See Also

### Creating a Set

- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
