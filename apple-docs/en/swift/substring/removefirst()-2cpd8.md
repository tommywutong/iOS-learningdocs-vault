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
doc_path: /documentation/swift/substring/removefirst()-2cpd8
source_url: 'https://developer.apple.com/documentation/swift/substring/removefirst()-2cpd8'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/removefirst%28%29-2cpd8.json'
content_hash: 'sha256:3b7aa36889ff2844'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

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
