---
title: 'allocate(byteCount:alignment:)'
framework: Swift
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.0+, macOS 10.10+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/swift/unsafemutablerawbufferpointer/allocate(bytecount:alignment:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawbufferpointer/allocate(bytecount:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawbufferpointer/allocate%28bytecount%3Aalignment%3A%29.json'
content_hash: 'sha256:72cf39a3544dc101'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawBufferPointer](../unsafemutablerawbufferpointer.md)

# allocate(byteCount:alignment:)

<sub>Type Method</sub>

Allocates uninitialized memory with the specified size and alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func allocate(byteCount: Int, alignment: Int) -> UnsafeMutableRawBufferPointer
```

## Parameters

- `byteCount` — The number of bytes to allocate. `byteCount` must not be negative.

- `alignment` — The alignment of the new region of allocated memory, in bytes. `alignment` must be a whole power of 2.

## Return Value

A buffer pointer to a newly allocated region of memory aligned to `alignment`.

## Discussion

You are in charge of managing the allocated memory. Be sure to deallocate any memory that you manually allocate.

The allocated memory is not bound to any specific type and must be bound before performing any typed operations. If you are using the memory for a specific type, allocate memory using the `UnsafeMutablePointerBuffer.allocate(capacity:)` static method instead.
