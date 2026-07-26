---
title: 'remove(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/remove(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/remove(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/remove%28_%3A%29.json'
content_hash: 'sha256:842f2850d3e0797d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# remove(_:)

<sub>Instance Method</sub>

Removes a given object from the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func remove(_ object: Any)
```

## Parameters

- `object` — The object to remove from the set.

## See Also

### Related Documentation

- [- minusSet:](<minus(__).md>) — Removes each object in another given set from the receiving set, if present.
- [- intersectSet:](<intersect(__).md>) — Removes from the receiving set each object that isn’t a member of another given set.

### Adding and removing entries

- [- addObject:](<add(__).md>) — Adds a given object to the set, if it is not already a member.
- [- filterUsingPredicate:](<filter(using_).md>) — Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds to the set each object contained in a given array that is not already a member.
