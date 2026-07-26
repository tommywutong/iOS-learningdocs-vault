---
title: 'formIndex(_:offsetBy:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectionofone/formindex(_:offsetby:)'
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/formindex(_:offsetby:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/formindex%28_%3Aoffsetby%3A%29.json'
content_hash: 'sha256:82885d1f1bfe6108'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# formIndex(_:offsetBy:)

<sub>Instance Method</sub>

Offsets the given index by the specified distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func formIndex(_ i: inout Self.Index, offsetBy distance: Int)
```

## Parameters

- `i` — A valid index of the collection.

- `distance` — The distance to offset `i`. `distance` must not be negative unless the collection conforms to the `BidirectionalCollection` protocol.

## Discussion

The value passed as `distance` must not offset `i` beyond the bounds of the collection.

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the absolute value of `distance`.
