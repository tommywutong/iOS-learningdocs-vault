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
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/subscript(_:)-u791'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/subscript(_:)-u791'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/subscript%28_%3A%29-u791.json'
content_hash: 'sha256:394c308a67470a69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# subscript(_:)

<sub>Instance Subscript</sub>

Accesses the byte at the given offset in the memory region as a `UInt8` value.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
subscript(i: Int) -> UnsafeMutableRawBufferPointer.Element { get nonmutating set }
```

## Parameters

- `i` — The offset of the byte to access. `i` must be in the range `0..<count`.
