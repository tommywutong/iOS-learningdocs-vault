---
title: next()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/stridetoiterator/next()
source_url: 'https://developer.apple.com/documentation/swift/stridetoiterator/next()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/stridetoiterator/next%28%29.json'
content_hash: 'sha256:c648c0e0bbbe2a12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [StrideToIterator](../stridetoiterator.md)

# next()

<sub>Instance Method</sub>

Advances to the next element and returns it, or `nil` if no next element exists.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
mutating func next() -> Element?
```

## Discussion

Once `nil` has been returned, all subsequent calls return `nil`.
