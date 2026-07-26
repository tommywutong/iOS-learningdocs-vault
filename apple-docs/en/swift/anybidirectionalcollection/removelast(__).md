---
title: 'removeLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/anybidirectionalcollection/removelast(_:)'
source_url: 'https://developer.apple.com/documentation/swift/anybidirectionalcollection/removelast(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/anybidirectionalcollection/removelast%28_%3A%29.json'
content_hash: 'sha256:9f8dc3cd0b4d3117'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [AnyBidirectionalCollection](../anybidirectionalcollection.md)

# removeLast(_:)

<sub>Instance Method</sub>

Removes the given number of elements from the end of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ k: Int)
```

## Parameters

- `k` — The number of elements to remove. `k` must be greater than or equal to zero, and must be less than or equal to the number of elements in the collection.

## Discussion

> [!abstract] Complexity
> O(1) if the collection conforms to `RandomAccessCollection`; otherwise, O(_k_), where _k_ is the number of elements to remove.
