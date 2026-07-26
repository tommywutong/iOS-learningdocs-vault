---
title: 'add(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/add(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/add(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/add%28_%3A%29.json'
content_hash: 'sha256:11f35df367aa238c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# add(_:)

<sub>Instance Method</sub>

Adds a given object to the set, if it is not already a member.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func add(_ object: Any)
```

## Parameters

- `object` — The object to add to the set.

## See Also

### Related Documentation

- [- unionSet:](<union(__).md>) — Adds each object in another given set to the receiving set, if not present.

### Adding and removing entries

- [- filterUsingPredicate:](<filter(using_).md>) — Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.
- [- addObjectsFromArray:](<addobjects(from_).md>) — Adds to the set each object contained in a given array that is not already a member.
