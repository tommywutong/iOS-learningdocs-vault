---
title: 'initialize(repeating:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablebufferpointer/initialize(repeating:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablebufferpointer/initialize(repeating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablebufferpointer/initialize%28repeating%3A%29.json'
content_hash: 'sha256:b7f75bf180578680'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableBufferPointer](../unsafemutablebufferpointer.md)

# initialize(repeating:)

<sub>Instance Method</sub>

Initializes every element in this buffer’s memory to a copy of the given value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func initialize(repeating repeatedValue: Element)
```

## Parameters

- `repeatedValue` — The instance to initialize this buffer’s memory with.

## Discussion

The destination memory must be uninitialized or the buffer’s `Element` must be a trivial type. After a call to `initialize(repeating:)`, the entire region of memory referenced by this buffer is initialized.
