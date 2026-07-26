---
title: 'intersect(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableorderedset/intersect(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableorderedset/intersect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableorderedset/intersect%28_%3A%29.json'
content_hash: 'sha256:6fdd306109ea97b9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableOrderedSet](../nsmutableorderedset.md)

# intersect(_:)

<sub>Instance Method</sub>

Removes from the receiving ordered set each object that isn’t a member of another ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersect(_ other: NSOrderedSet)
```

## Parameters

- `other` — The ordered set with which to perform the intersection.

## See Also

### Combining and Recombining Entries

- [- intersectSet:](<intersectset(__).md>) — Removes from the receiving ordered set each object that isn’t a member of another set.
- [- minusOrderedSet:](<minus(__).md>) — Removes each object in another given ordered set from the receiving mutable ordered set, if present.
- [- minusSet:](<minusset(__).md>) — Removes each object in another given set from the receiving mutable ordered set, if present.
- [- unionOrderedSet:](<union(__).md>) — Adds each object in another given ordered set to the receiving mutable ordered set, if not present.
- [- unionSet:](<unionset(__).md>) — Adds each object in another given set to the receiving mutable ordered set, if not present.
