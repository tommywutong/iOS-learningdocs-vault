---
title: 'intersectsSet(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/intersectsset(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/intersectsset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/intersectsset%28_%3A%29.json'
content_hash: 'sha256:66c840b85e41014d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# intersectsSet(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersectsSet(_ set: Set<AnyHashable>) -> Bool
```

## Parameters

- `set` — The set.

## Return Value

[true](../../swift/true.md) if at least one object in the receiving ordered set is also present in `other`, otherwise [false](../../swift/false.md).

## See Also

### Comparing Sets

- [- isEqualToOrderedSet:](<isequal(to_).md>) — Compares the receiving ordered set to another ordered set.
- [- intersectsOrderedSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [- isSubsetOfOrderedSet:](<issubset(of_)-7brc.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [- isSubsetOfSet:](<issubset(of_)-8zx9x.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.
