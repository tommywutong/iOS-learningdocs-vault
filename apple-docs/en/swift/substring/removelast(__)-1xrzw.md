---
title: 'removeLast(_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/substring/removelast(_:)-1xrzw'
source_url: 'https://developer.apple.com/documentation/swift/substring/removelast(_:)-1xrzw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/removelast%28_%3A%29-1xrzw.json'
content_hash: 'sha256:f9c4fd7db062f1aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# removeLast(_:)

<sub>Instance Method</sub>

Removes the specified number of elements from the end of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func removeLast(_ k: Int)
```

## Parameters

- `k` — The number of elements to remove from the collection. `k` must be greater than or equal to zero and must not exceed the number of elements in the collection.

## Discussion

Attempting to remove more elements than exist in the collection triggers a runtime error.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(_k_), where _k_ is the specified number of elements.
