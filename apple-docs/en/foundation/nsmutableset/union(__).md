---
title: 'union(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/union(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/union(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/union%28_%3A%29.json'
content_hash: 'sha256:1f574e40222df152'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# union(_:)

<sub>Instance Method</sub>

Adds each object in another given set to the receiving set, if not present.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func union(_ otherSet: Set<AnyHashable>)
```

## Parameters

- `otherSet` — The set of objects to add to the receiving set.

## See Also

### Related Documentation

- [- addObject:](<add(__).md>) — Adds a given object to the set, if it is not already a member.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds to the set each object contained in a given array that is not already a member.

### Combining and recombining sets

- [- minusSet:](<minus(__).md>) — Removes each object in another given set from the receiving set, if present.
- [- intersectSet:](<intersect(__).md>) — Removes from the receiving set each object that isn’t a member of another given set.
- [- setSet:](<setset(__).md>) — Empties the receiving set, then adds each object contained in another given set.
