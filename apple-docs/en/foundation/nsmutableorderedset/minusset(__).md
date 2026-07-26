---
title: 'minusSet(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/minusset(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/minusset(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/minusset%28_%3A%29.json'
content_hash: 'sha256:02ca289edab56b45'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# minusSet(_:)

<sub>Instance Method</sub>

Removes each object in another given set from the receiving mutable ordered set, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minusSet(_ other: Set<AnyHashable>)
```

## Parameters

- `other` — The set of objects to remove from the receiving set.

## See Also

### Combining and Recombining Entries

- [- intersectOrderedSet:](<intersect(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another ordered set.
- [- intersectSet:](<intersectset(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another set.
- [- minusOrderedSet:](<minus(__).md>) — Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [- unionOrderedSet:](<union(__).md>) — Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [- unionSet:](<unionset(__).md>) — Adds each object in another given set to the receiving mutable ordered set, if not present.
