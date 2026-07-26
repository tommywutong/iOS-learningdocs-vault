---
title: 'initializeElement(at:to:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/initializeelement(at:to:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/initializeelement(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/initializeelement%28at%3Ato%3A%29.json'
content_hash: 'sha256:661d339db49a4ba9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# initializeElement(at:to:)

<sub>Instance Method</sub>

Initializes the element at `index` to the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initializeElement(at index: UnsafeMutableBufferPointer<Element>.Index, to value: consuming Element)
```

## Parameters

- `index` — The index of the element to initialize

- `value` — The value used to initialize the buffer element’s memory.

## Discussion

The memory underlying the destination element must be uninitialized, or `Element` must be a trivial type. After a call to `initialize(to:)`, the memory underlying this element of the buffer is initialized.
