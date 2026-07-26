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
doc_path: '/documentation/swift/unsafemutablebufferpointer/swapat(_:_:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/swapat(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/swapat%28_%3A_%3A%29.json'
content_hash: 'sha256:d3ca7221e0d8eb68'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# swapAt(_:_:)

<sub>Instance Method</sub>

Exchanges the values at the specified indices of the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func swapAt(_ i: Int, _ j: Int)
```

## Parameters

- `i` — The index of the first value to swap.

- `j` — The index of the second value to swap.

## Discussion

Both parameters must be valid indices of the buffer, and not equal to `endIndex`. Passing the same index as both `i` and `j` has no effect.
