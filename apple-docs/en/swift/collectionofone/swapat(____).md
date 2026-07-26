---
title: 'swapAt(_:_:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/collectionofone/swapat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/collectionofone/swapat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/collectionofone/swapat%28_%3A_%3A%29.json'
content_hash: 'sha256:6deb7a1e2490a3db'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [CollectionOfOne](../collectionofone.md)

# swapAt(_:_:)

<sub>Instance Method</sub>

Exchanges the values at the specified indices of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func swapAt(_ i: Self.Index, _ j: Self.Index)
```

## Parameters

- `i` — The index of the first value to swap.

- `j` — The index of the second value to swap.

## Discussion

Both parameters must be valid indices of the collection that are not equal to `endIndex`. Calling `swapAt(_:_:)` with the same index as both `i` and `j` has no effect.

> [!abstract] Complexity
> O(1)
