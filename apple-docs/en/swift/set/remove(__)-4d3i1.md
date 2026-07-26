---
title: 'remove(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/remove(_:)-4d3i1'
source_url: 'https://developer.apple.com/documentation/swift/set/remove(_:)-4d3i1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/remove%28_%3A%29-4d3i1.json'
content_hash: 'sha256:1a148f20700bde11'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# remove(_:)

<sub>Instance Method</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove<ConcreteElement>(_ member: ConcreteElement) -> ConcreteElement? where ConcreteElement : Hashable
```

## See Also

### Removing Elements

- [filter(_:)](<filter(__).md>) — Returns a new set containing the elements of the set that satisfy the given predicate.
- [remove(_:)](<remove(__)-8p2tv.md>) — Removes the specified element from the set.
- [removeFirst()](<removefirst().md>) — Removes the first element of the set.
- [remove(at:)](<remove(at_).md>) — Removes the element at the given index of the set.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all members from the set.
