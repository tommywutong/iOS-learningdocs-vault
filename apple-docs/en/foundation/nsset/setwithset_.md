---
title: 'setWithSet:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/setwithset:'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/setwithset:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/setwithset%3A.json'
content_hash: 'sha256:d5fac26e92bae182'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# setWithSet:

<sub>Type Method</sub>

Creates and returns a set containing the objects from another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) setWithSet:(NSSet<id> *) set;
```

## Parameters

- `set` — A set containing the objects to add to the new set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the new set.

## Return Value

A new set containing the objects from `set`.

## See Also

### Creating a Set

- [set](set.md) — Creates and returns an empty set.
- [setWithArray:](setwitharray_.md) — Creates and returns a set containing a uniqued collection of the objects contained in a given array.
- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [setWithObjects:](setwithobjects_.md) — Creates and returns a set containing the objects in a given argument list.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
