---
title: count
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/lazysequence/count-1cggd
source_url: 'https://developer.apple.com/documentation/swift/lazysequence/count-1cggd'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/lazysequence/count-1cggd.json'
content_hash: 'sha256:78cbd51b8f17ece9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [LazySequence](../lazysequence.md)

# count

<sub>Instance Property</sub>

The number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var count: Int { get }
```

## Discussion

To check whether a collection is empty, use its `isEmpty` property instead of comparing `count` to zero. Unless the collection guarantees random-access performance, calculating `count` can be an O(_n_) operation.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.
