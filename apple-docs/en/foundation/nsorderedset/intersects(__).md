---
title: 'intersects(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/intersects(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/intersects(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/intersects%28_%3A%29.json'
content_hash: 'sha256:ed46955cffe5a8b5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# intersects(_:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersects(_ other: NSOrderedSet) -> Bool
```

## Parameters

- `other` — The other ordered set.

## Return Value

[true](../../swift/true.md) if at least one object in the receiving ordered set is also present in `other`, otherwise [false](../../swift/false.md).

## See Also

### Comparing Sets

- [- isEqualToOrderedSet:](<isequal(to_).md>) — Compares the receiving ordered set to another ordered set.
- [- intersectsSet:](<intersectsset(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [- isSubsetOfOrderedSet:](<issubset(of_)-7brc.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [- isSubsetOfSet:](<issubset(of_)-8zx9x.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.
