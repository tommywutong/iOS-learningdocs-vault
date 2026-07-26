---
title: 'adding(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/adding(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/adding(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/adding%28_%3A%29.json'
content_hash: 'sha256:e1c2eff8e435e45d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# adding(_:)

<sub>Instance Method</sub>

Returns a new set formed by adding a given object to the receiving set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func adding(_ anObject: Any) -> Set<AnyHashable>
```

## Parameters

- `anObject` — The object to add to the set.

## Return Value

A new set formed by adding `anObject` to the receiving set.

## See Also

### Creating a Set

- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
