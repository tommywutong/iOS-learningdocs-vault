---
title: baseAddress
framework: Swift
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/swift/unsaferawbufferpointer/baseaddress
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/baseaddress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/baseaddress.json'
content_hash: 'sha256:7dc73a4bf7c66672'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# baseAddress

<sub>Instance Property</sub>

A pointer to the first byte of the buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var baseAddress: UnsafeRawPointer? { get }
```

## Discussion

If the `baseAddress` of this buffer is `nil`, the count is zero. However, a buffer can have a `count` of zero even with a non-`nil` base address.
