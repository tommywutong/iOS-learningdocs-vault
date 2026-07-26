---
title: 'contains(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/contains(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/contains(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/contains%28_%3A%29.json'
content_hash: 'sha256:c6e747fb06204924'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# contains(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the hash table contains a given object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contains(_ anObject: ObjectType?) -> Bool
```

## Parameters

- `anObject` — The object to test for membership in the hash table.

## Return Value

[true](../../swift/true.md) if the hash table contains `anObject`, otherwise [false](../../swift/false.md).

## Discussion

The equality test used depends on the personality option selected. For instance, choosing the [NSPointerFunctionsObjectPersonality](../nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [Options](../nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## See Also

### Accessing Content

- [anyObject](anyobject.md) — One of the objects in the hash table.
- [allObjects](allobjects.md) — The hash table’s members.
- [setRepresentation](setrepresentation.md) — A set that contains the hash table’s members.
- [count](count.md) — The number of elements in the hash table.
- [- member:](<member(__).md>) — Determines whether the hash table contains a given object, and returns that object if it is present
- [- objectEnumerator](<objectenumerator().md>) — Returns an enumerator object that lets you access each object in the hash table.
