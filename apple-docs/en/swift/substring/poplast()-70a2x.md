---
title: popLast()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/swift/substring/poplast()-70a2x
source_url: 'https://developer.apple.com/documentation/swift/substring/poplast()-70a2x'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/substring/poplast%28%29-70a2x.json'
content_hash: 'sha256:0ce9283be0857061'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Substring](../substring.md)

# popLast()

<sub>Instance Method</sub>

Removes and returns the last element of the collection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func popLast() -> Self.Element?
```

## Return Value

The last element of the collection if the collection is not empty; otherwise, `nil`.

## Discussion

Calling this method may invalidate all saved indices of this collection. Do not rely on a previously stored index value after altering a collection with any operation that can change its length.

> [!abstract] Complexity
> O(1)
