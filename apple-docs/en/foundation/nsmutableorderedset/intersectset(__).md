---
title: 'intersectSet(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/intersectset(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/intersectset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/intersectset%28_%3A%29.json'
content_hash: 'sha256:ab6ce2f6dbf0bdf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# intersectSet(_:)

<sub>Instance Method</sub>

Removes from the receiving ordered set each object that isn’t a member of another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersectSet(_ other: Set<AnyHashable>)
```

## Parameters

- `other` — The set with which to perform the intersection.

## See Also

### Combining and Recombining Entries

- [- intersectOrderedSet:](<intersect(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another ordered set.
- [- minusOrderedSet:](<minus(__).md>) — Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [- minusSet:](<minusset(__).md>) — Removes each object in another given set from the receiving mutable ordered set, if present.
- [- unionOrderedSet:](<union(__).md>) — Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [- unionSet:](<unionset(__).md>) — Adds each object in another given set to the receiving mutable ordered set, if not present.
