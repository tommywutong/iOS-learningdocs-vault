---
title: removeFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/set/removefirst()
source_url: 'https://developer.apple.com/documentation/swift/set/removefirst()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/removefirst%28%29.json'
content_hash: 'sha256:4f02b7423859376c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# removeFirst()

<sub>Instance Method</sub>

Removes the first element of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeFirst() -> Element
```

## Return Value

A member of the set.

## Discussion

Because a set is not an ordered collection, the “first” element may not be the first element that was added to the set. The set must not be empty.

> [!abstract] Complexity
> Amortized O(1) if the set does not wrap a bridged `NSSet`. If the set wraps a bridged `NSSet`, the performance is unspecified.

## See Also

### Removing Elements

- [filter(_:)](<filter(__).md>) — Returns a new set containing the elements of the set that satisfy the given predicate.
- [remove(_:)](<remove(__)-8p2tv.md>) — Removes the specified element from the set.
- [remove(_:)](<remove(__)-4d3i1.md>)
- [remove(at:)](<remove(at_).md>) — Removes the element at the given index of the set.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all members from the set.
