---
title: 'subscript(_:)'
framework: Swift
symbol_kind: subscript
role: symbol
role_heading: Instance Subscript
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/subscript(_:)-4dk2n'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/subscript(_:)-4dk2n'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/subscript%28_%3A%29-4dk2n.json'
content_hash: 'sha256:eb3bfeb8668b151e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the byte at the given offset in the memory region as a `UInt8` value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> UnsafeRawBufferPointer.Element { get }
```

## Parameters

- `i` — The offset of the byte to access. `i` must be in the range `0..<count`.
