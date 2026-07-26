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
doc_path: '/documentation/swift/unsafebufferpointer/init(start:count:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafebufferpointer/init(start:count:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafebufferpointer/init%28start%3Acount%3A%29.json'
content_hash: 'sha256:7859a4b677da45a6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeBufferPointer](../unsafebufferpointer.md)

# init(start:count:)

<sub>Initializer</sub>

Creates a new buffer pointer over the specified number of contiguous instances beginning at the given pointer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(start: UnsafePointer<Element>?, count: Int)
```

## Parameters

- `start` — A pointer to the start of the buffer, or `nil`. If `start` is `nil`, `count` must be zero. However, `count` may be zero even for a non-`nil` `start`. The pointer passed as `start` must be aligned to `MemoryLayout<Element>.alignment`.

- `count` — The number of instances in the buffer. `count` must not be negative.
