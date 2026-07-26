---
title: 'intersects(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 6.0+, iPadOS 6.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nshashtable/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nshashtable/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nshashtable/intersects%28_%3A%29.json'
content_hash: 'sha256:ec55aeaa9e924225'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSHashTable](../nshashtable.md)

# intersects(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether a given hash table intersects with the receiving hash table.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects(_ other: NSHashTable<ObjectType>) -> Bool
```

## Parameters

- `other` — The hash table with which to compare the receiving hash table.

## Return Value

[true](../../swift/true.md) if `other` intersects with the receiving hash table, otherwise [false](../../swift/false.md).

## Discussion

The equality test used for members depends on the personality option selected. For instance, choosing the [NSPointerFunctionsObjectPersonality](../nspointerfunctions/options/objectpersonality.md) option will use `isEqual:` to determine equality. See [Options](../nspointerfunctions/options.md) for more information on personality options and their corresponding equality tests.

## See Also

### Comparing Hash Tables

- [- intersectHashTable:](<intersect(__).md>) — Removes from the receiving hash table each element that isn’t a member of another given hash table.
- [- isSubsetOfHashTable:](<issubset(of_).md>) — Returns a Boolean value that indicates whether every element in the receiving hash table is also present in another given hash table.
- [- isEqualToHashTable:](<isequal(to_).md>) — Returns a Boolean value that indicates whether a given hash table is equal to the receiving hash table.
