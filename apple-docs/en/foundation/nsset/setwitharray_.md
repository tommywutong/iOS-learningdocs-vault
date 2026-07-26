---
title: 'setWithArray:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/setwitharray:'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/setwitharray:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/setwitharray%3A.json'
content_hash: 'sha256:ed0905a99810c55c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# setWithArray:

<sub>Type Method</sub>

Creates and returns a set containing a uniqued collection of the objects contained in a given array.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) setWithArray:(NSArray<id> *) array;
```

## Parameters

- `array` — An array containing the objects to add to the new set. If the same object appears more than once in `array`, it is added only once to the returned set. Each object receives a [retain](../../objectivec/nsobject-c.protocol/retain.md) message as it is added to the set.

## Return Value

A new set containing a uniqued collection of the objects contained in `array`.

## See Also

### Creating a Set

- [set](set.md) — Creates and returns an empty set.
- [+ setWithObject:](<init(object_).md>) — Creates and returns a set that contains a single given object.
- [setWithObjects:](setwithobjects_.md) — Creates and returns a set containing the objects in a given argument list.
- [+ setWithObjects:count:](<init(objects_count_)-65ni4.md>) — Creates and returns a set containing a specified number of objects from a given C array of objects.
- [setWithSet:](setwithset_.md) — Creates and returns a set containing the objects from another set.
- [- setByAddingObject:](<adding(__).md>) — Returns a new set formed by adding a given object to the receiving set.
- [- setByAddingObjectsFromSet:](<addingobjects(from_)-2i31h.md>) — Returns a new set formed by adding the objects in a given set to the receiving set.
- [- setByAddingObjectsFromArray:](<addingobjects(from_)-544m9.md>) — Returns a new set formed by adding the objects in a given array to the receiving set.
