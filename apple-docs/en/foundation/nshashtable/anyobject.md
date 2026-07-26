---
title: anyObject
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nshashtable/anyobject
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/anyobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/anyobject.json'
content_hash: 'sha256:ac0633667b2534dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# anyObject

<sub>Instance Property</sub>

One of the objects in the hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var anyObject: ObjectType? { get }
```

## Discussion

One of the objects in the hash table, or `nil` if the hash table contains no objects.

The object returned is chosen at the hash table’s convenience—the selection is not guaranteed to be random.

## See Also

### Accessing Content

- [allObjects](allobjects.md) — The hash table’s members.
- [setRepresentation](setrepresentation.md) — A set that contains the hash table’s members.
- [count](count.md) — The number of elements in the hash table.
- [- containsObject:](<contains(__).md>) — Returns a Boolean value that indicates whether the hash table contains a given object.
- [- member:](<member(__).md>) — Determines whether the hash table contains a given object, and returns that object if it is present
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the hash table.
