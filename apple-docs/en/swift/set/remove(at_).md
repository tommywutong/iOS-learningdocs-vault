---
title: 'remove(at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/set/remove(at:)'
source_url: 'https://developer.apple.com/documentation/swift/set/remove(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/set/remove%28at%3A%29.json'
content_hash: 'sha256:af21dbf7b2bbb266'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Set](../set.md)

# remove(at:)

<sub>Instance Method</sub>

Removes the element at the given index of the set.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func remove(at position: Set<Element>.Index) -> Element
```

## Parameters

- `position` — The index of the member to remove. `position` must be a valid index of the set, and must not be equal to the set’s end index.

## Return Value

The element that was removed from the set.

## See Also

### Removing Elements

- [filter(_:)](<filter(__).md>) — Returns a new set containing the elements of the set that satisfy the given predicate.
- [remove(_:)](<remove(__)-8p2tv.md>) — Removes the specified element from the set.
- [remove(_:)](<remove(__)-4d3i1.md>)
- [removeFirst()](<removefirst().md>) — Removes the first element of the set.
- [removeAll(keepingCapacity:)](<removeall(keepingcapacity_).md>) — Removes all members from the set.
