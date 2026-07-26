---
title: 'intersect(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/intersect(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/intersect(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/intersect%28_%3A%29.json'
content_hash: 'sha256:7e1bad6e2d2e83e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# intersect(_:)

<sub>Instance Method</sub>

Removes from the receiving set each object that isn’t a member of another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func intersect(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet` — The set with which to perform the intersection.

## See Also

### Related Documentation

- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.

### Combining and recombining sets

- [- unionSet:](<union(__).md>) — Adds each object in another given set to the receiving set, if not present.
- [- minusSet:](<minus(__).md>) — Removes each object in another given set from the receiving set, if present.
- [- setSet:](<setset(__).md>) — Empties the receiving set, then adds each object contained in another given set.
