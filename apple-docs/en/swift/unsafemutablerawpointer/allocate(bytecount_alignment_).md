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
doc_path: '/documentation/swift/unsafemutablerawpointer/allocate(bytecount:alignment:)'
source_url: 'https://developer.apple.com/documentation/swift/unsafemutablerawpointer/allocate(bytecount:alignment:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/swift/unsafemutablerawpointer/allocate%28bytecount%3Aalignment%3A%29.json'
content_hash: 'sha256:84e38f1a36e9aa6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Swift](../../swift.md) · [UnsafeMutableRawPointer](../unsafemutablerawpointer.md)

# allocate(byteCount:alignment:)

<sub>Type Method</sub>

Allocates uninitialized memory with the specified size and alignment.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static func allocate(byteCount: Int, alignment: Int) -> UnsafeMutableRawPointer
```

## Parameters

- `byteCount` — The number of bytes to allocate. `byteCount` must not be negative.

- `alignment` — The alignment of the new region of allocated memory, in bytes. `alignment` must be a whole power of 2.

## Return Value

A pointer to a newly allocated region of memory. The memory is allocated, but not initialized.

## Discussion

You are in charge of managing the allocated memory. Be sure to deallocate any memory that you manually allocate.

The allocated memory is not bound to any specific type and must be bound before performing any typed operations. If you are using the memory for a specific type, allocate memory using the `UnsafeMutablePointer.allocate(capacity:)` static method instead.
