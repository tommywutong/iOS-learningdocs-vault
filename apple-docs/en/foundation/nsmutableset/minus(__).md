---
title: 'minus(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/minus(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/minus(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/minus%28_%3A%29.json'
content_hash: 'sha256:5c704c88b822689a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# minus(_:)

<sub>Instance Method</sub>

Removes each object in another given set from the receiving set, if present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func minus(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet` — The set of objects to remove from the receiving set.

## See Also

### Related Documentation

- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.

### Combining and recombining sets

- [- unionSet:](<union(__).md>) — Adds each object in another given set to the receiving set, if not present.
- [- intersectSet:](<intersect(__).md>) — Removes from the receiving set each object that isn’t a member of another given set.
- [- setSet:](<setset(__).md>) — Empties the receiving set, then adds each object contained in another given set.
