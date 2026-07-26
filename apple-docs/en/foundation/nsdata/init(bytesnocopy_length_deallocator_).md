---
title: 'init(bytesNoCopy:length:deallocator:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(bytesnocopy:length:deallocator:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:deallocator:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28bytesnocopy%3Alength%3Adeallocator%3A%29.json'
content_hash: 'sha256:39ac96a807cf7d2e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(bytesNoCopy:length:deallocator:)

<sub>Initializer</sub>

Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int, deallocator: ((UnsafeMutableRawPointer, Int) -> Void)? = nil)
```

## Parameters

- `bytes` — A buffer containing data for the new object.

- `length` — The number of bytes to hold from `bytes`. This value must not exceed the length of `bytes`.

- `deallocator` — A block to invoke when the resulting `NSData` object is deallocated.

## Return Value

A data object initialized by adding to it `length` bytes of data from the buffer `bytes`. The returned object might be different than the original receiver.

## Discussion

Use this method to define your own deallocation behavior for the data buffer you provide.

In order to avoid any inadvertent strong reference cycles, you should avoid capturing pointers to any objects that may in turn maintain strong references to the `NSData` object. This includes explicit references to `self`, and implicit references to `self` due to direct instance variable access. To make it easier to avoid these references, the `deallocator` block takes two parameters, a pointer to the `buffer`, and its length; you should always use these values instead of trying to use references from outside the block.

## See Also

### Creating Data

- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
