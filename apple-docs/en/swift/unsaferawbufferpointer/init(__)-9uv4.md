---
title: 'init(_:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/init(_:)-9uv4'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/init(_:)-9uv4'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/init%28_%3A%29-9uv4.json'
content_hash: 'sha256:054fc3f6019fdd58'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# init(_:)

<sub>Initializer</sub>

Creates a raw buffer over the contiguous bytes in the given typed buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init<T>(_ buffer: UnsafeBufferPointer<T>) where T : ~Copyable
```

## Parameters

- `buffer` — The typed buffer to convert to a raw buffer. The buffer’s type `T` must be a trivial type.
