---
title: underestimatedCount
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/uint64/words-swift.struct/underestimatedcount
source_url: 'https://developer.apple.com/documentation/swift/uint64/words-swift.struct/underestimatedcount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/uint64/words-swift.struct/underestimatedcount.json'
content_hash: 'sha256:0b1f7df07f37ec53'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Swift](../../../swift.md) · [UInt64](../../uint64.md) · [Words](../words-swift.struct.md)

# underestimatedCount

<sub>Instance Property</sub>

A value less than or equal to the number of elements in the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var underestimatedCount: Int { get }
```

## Discussion

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_n_), where _n_ is the length of the collection.
