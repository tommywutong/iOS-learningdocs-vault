---
title: 'isSubset(of:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/issubset(of:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/issubset(of:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/issubset%28of%3A%29.json'
content_hash: 'sha256:c7f7488317f72d97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# isSubset(of:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isSubset(of otherSet: Set<AnyHashable>) -> Bool
```

## Parameters

- `otherSet` — The set with which to compare the receiving set.

## Return Value

[true](../../swift/true.md) if every object in the receiving set is also present in `otherSet`, otherwise [false](../../swift/false.md).

## Discussion

Object equality is tested using isEqual:.

## See Also

### Comparing Sets

- [- intersectsSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [- isEqualToSet:](<isequal(to_).md>) — Compares the receiving set to another set.
- [- valueForKey:](<value(forkey_).md>) — Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the set’s members.
