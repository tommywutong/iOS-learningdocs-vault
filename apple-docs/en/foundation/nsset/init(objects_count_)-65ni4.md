---
title: 'init(objects:count:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/init(objects:count:)-65ni4'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/init(objects:count:)-65ni4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/init%28objects%3Acount%3A%29-65ni4.json'
content_hash: 'sha256:9be30417c2d87ebe'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# init(objects:count:)

<sub>Initializer</sub>

Creates and returns a set containing a specified number of objects from a given C array of objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(objects: UnsafePointer<AnyObject>, count cnt: Int)
```

## Parameters

- `objects` — A C array of objects to add to the new set. If the same object appears more than once in `objects`, it is added only once to the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

- `cnt` — The number of objects from `objects` to add to the new set.

## Return Value

A new set containing `cnt` objects from the list of objects specified by `objects`.

## See Also

### Creating a Set

- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
