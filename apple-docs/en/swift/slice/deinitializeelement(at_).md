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
doc_path: '/documentation/swift/slice/deinitializeelement(at:)'
source_url: 'https://developer.apple.com/documentation/swift/slice/deinitializeelement(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/deinitializeelement%28at%3A%29.json'
content_hash: 'sha256:c251a5c3fa9dd56f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# deinitializeElement(at:)

<sub>Instance Method</sub>

Deinitializes the memory underlying the element at `index`.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func deinitializeElement<Element>(at index: UnsafeMutableBufferPointer<Element>.Index) where Base == UnsafeMutableBufferPointer<Element>
```

## Parameters

- `index` — The index of the buffer element to deinitialize.

## Discussion

The memory underlying the element at `index` must be initialized. After calling `deinitializeElement()`, the memory underlying this element of the buffer slice is uninitialized, and still bound to type `Element`.
