---
title: 'init(object:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(object:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(object:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28object%3A%29.json'
content_hash: 'sha256:7fcc99ff655b7e8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(object:)

<sub>Initializer</sub>

Creates and returns a set that contains a single given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(object: Any)
```

## Parameters

- `object` — The object to add to the new set. `object` receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message after being added to the set.

## Return Value

A new set that contains a single member, `object`.

## See Also

### Creating a Set

- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
