---
title: 'isEqual(to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedset/isequal(to:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedset/isequal(to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedset/isequal%28to%3A%29.json'
content_hash: 'sha256:7f4bec63fba00be0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedSet](../nsorderedset.md)

# isEqual(to:)

<sub>Instance Method</sub>

Compares the receiving ordered set to another ordered set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isEqual(to other: NSOrderedSet) -> Bool
```

## Parameters

- `other` — The ordered set with which to compare the receiving ordered set.

## Return Value

[true](../../swift/true.md) if the contents of `other` are equal to the contents of the receiving ordered set, otherwise [false](../../swift/false.md).

## Discussion

Two ordered sets have equal contents if they each have the same number of members, if each member of one ordered set is present in the other, and the members are in the same order.

## See Also

### Related Documentation

- [isEqual(_:)](<../../objectivec/nsobjectprotocol/isequal(__).md>) — Returns a Boolean value that indicates whether the receiver and a given object are equal.

### Comparing Sets

- [- intersectsOrderedSet:](<intersects(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given ordered set.
- [- intersectsSet:](<intersectsset(__).md>) — Returns a Boolean value that indicates whether at least one object in the receiving ordered set is also present in another given set.
- [- isSubsetOfOrderedSet:](<issubset(of_)-7brc.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given ordered set.
- [- isSubsetOfSet:](<issubset(of_)-8zx9x.md>) — Returns a Boolean value that indicates whether every object in the receiving ordered set is also present in another given set.
