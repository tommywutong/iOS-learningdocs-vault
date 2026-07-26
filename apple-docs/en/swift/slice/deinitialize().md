---
title: deinitialize()
framework: Swift
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/slice/deinitialize()
source_url: 'https://developer.apple.com/documentation/swift/slice/deinitialize()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/slice/deinitialize%28%29.json'
content_hash: 'sha256:3fe7270c71916532'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [Slice](../slice.md)

# deinitialize()

<sub>Instance Method</sub>

Deinitializes every instance in this buffer slice.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@discardableResult func deinitialize<Element>() -> UnsafeMutableRawBufferPointer where Base == UnsafeMutableBufferPointer<Element>
```

## Return Value

A raw buffer to the same range of memory as this buffer. The range of memory is still bound to `Element`.

## Discussion

The region of memory underlying this buffer slice must be fully initialized. After calling `deinitialize(count:)`, the memory is uninitialized, but still bound to the `Element` type.

> [!note] Note
> All buffer elements must already be initialized.
