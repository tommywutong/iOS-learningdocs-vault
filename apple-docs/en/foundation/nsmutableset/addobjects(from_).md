---
title: 'addObjects(from:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsmutableset/addobjects(from:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsmutableset/addobjects(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsmutableset/addobjects%28from%3A%29.json'
content_hash: 'sha256:6a00ba9feb8bf0c5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSMutableSet](../nsmutableset.md)

# addObjects(from:)

<sub>Instance Method</sub>

Adds to the set each object contained in a given array that is not already a member.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addObjects(from array: [Any])
```

## Parameters

- `array` — An array of objects to add to the set.

## See Also

### Related Documentation

- [- unionSet:](<union(__).md>) — Adds each object in another given set to the receiving set, if not present.

### Adding and removing entries

- [- addObject:](<add(__).md>) — Adds a given object to the set, if it is not already a member.
- [- filterUsingPredicate:](<filter(using_).md>) — Evaluates a given predicate against the set’s content and removes from the set those objects for which the predicate returns false.
- [- removeObject:](<remove(__).md>) — Removes a given object from the set.
- [- removeAllObjects](<removeallobjects().md>) — Empties the set of all of its members.
