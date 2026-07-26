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
doc_path: /documentation/swift/uint8/words-swift.struct/count
source_url: 'https://developer.apple.com/documentation/swift/uint8/words-swift.struct/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint8/words-swift.struct/count.json'
content_hash: 'sha256:349a46a79aea3cec'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt8](../../uint8.md) · [Words](../words-swift.struct.md)

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
