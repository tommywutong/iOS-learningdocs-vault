---
title: 'init(start:count:)'
framework: Swift
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsaferawbufferpointer/init(start:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsaferawbufferpointer/init(start:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsaferawbufferpointer/init%28start%3Acount%3A%29.json'
content_hash: 'sha256:6add166a4c364b41'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeRawBufferPointer](../unsaferawbufferpointer.md)

# init(start:count:)

<sub>Initializer</sub>

Creates a buffer over the specified number of contiguous bytes starting at the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(start: UnsafeRawPointer?, count: Int)
```

## Parameters

- `start` — The address of the memory that starts the buffer. If `starts` is `nil`, `count` must be zero. However, `count` may be zero even for a non-`nil` `start`.

- `count` — The number of bytes to include in the buffer. `count` must not be negative.
