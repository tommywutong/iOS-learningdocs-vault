---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsset/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsset/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsset/isequal%28to%3A%29.json'
content_hash: 'sha256:207b2cb60bb9e1f8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSSet](../nsset.md)

# isEqual(to:)

<sub>Instance Method</sub>

Compares the receiving set to another set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to otherSet: Set<AnyHashable>) -> Bool
```

## Parameters

- `otherSet` — The set with which to compare the receiving set.

## Return Value

[true](../../swift/true.md) if the contents of `otherSet` are equal to the contents of the receiving set, otherwise [false](../../swift/false.md).

## Discussion

Two sets have equal contents if they each have the same number of members and if each member of one set is present in the other. Object equality is tested using isEqual:.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.

### Comparing Sets

- [- isSubsetOfSet:](<issubset(of_).md>) — Returns a Boolean value that indicates whether every object in the receiving set is also present in another given set.
- [- intersectsSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving set is also present in another given set.
- [- valueForKey:](<value(forkey_).md>) — Return a set containing the results of invoking `valueForKey:` on each of the receiving set’s members.
- [- setValue:forKey:](<setvalue(__forkey_).md>) — Invokes `setValue:forKey:` on each of the set’s members.
