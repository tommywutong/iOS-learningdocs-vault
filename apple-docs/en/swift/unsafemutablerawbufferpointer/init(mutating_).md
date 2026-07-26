---
title: 'init(mutating:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/init(mutating:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/init(mutating:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/init%28mutating%3A%29.json'
content_hash: 'sha256:048f9805e2d6002e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# init(mutating:)

<sub>Initializer</sub>

Creates a new mutable buffer over the same memory as the given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(mutating bytes: UnsafeRawBufferPointer)
```

## Parameters

- `bytes` — The buffer to convert.
