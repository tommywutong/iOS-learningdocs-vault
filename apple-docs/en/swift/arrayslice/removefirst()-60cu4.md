---
title: removeFirst()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/arrayslice/removefirst()-60cu4
source_url: 'https://developer.apple.com/documentation/swift/arrayslice/removefirst()-60cu4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/arrayslice/removefirst%28%29-60cu4.json'
content_hash: 'sha256:c07476711684e2d3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [ArraySlice](../arrayslice.md)

# removeFirst()

<sub>Instance Method</sub>

Removes and returns the first element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult mutating func removeFirst() -> Self.Element
```

## Return Value

The first element of the collection.

## Discussion

The collection must not be empty.

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(1)
