---
title: 'deinitializeElement(at:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/deinitializeelement(at:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/deinitializeelement(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/deinitializeelement%28at%3A%29.json'
content_hash: 'sha256:3386150cd4c88a4b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# deinitializeElement(at:)

<sub>Instance Method</sub>

Deinitializes the memory underlying the element at `index`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deinitializeElement(at index: UnsafeMutableBufferPointer<Element>.Index)
```

## Parameters

- `index` — The index of the buffer element to deinitialize.

## Discussion

The memory underlying the element at `index` must be initialized. After calling `deinitializeElement()`, the memory underlying this element of the buffer is uninitialized, and still bound to type `Element`.
