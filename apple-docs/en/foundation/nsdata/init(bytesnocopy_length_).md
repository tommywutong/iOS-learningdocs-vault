---
title: 'init(bytesNoCopy:length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(bytesnocopy:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(bytesnocopy:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28bytesnocopy%3Alength%3A%29.json'
content_hash: 'sha256:ed40c70b12553d8b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(bytesNoCopy:length:)

<sub>Initializer</sub>

Initializes a data object filled with a given number of bytes of data from a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytesNoCopy bytes: UnsafeMutableRawPointer, length: Int)
```

## Parameters

- `bytes` — A buffer containing data for the new object. `bytes` must point to a memory block allocated with `malloc`.

- `length` — The number of bytes to hold from `bytes`. This value must not exceed the length of `bytes`.

## Return Value

A data object initialized by adding to it `length` bytes of data from the buffer `bytes`. The returned object might be different than the original receiver.

## Discussion

The returned object takes ownership of the `bytes` pointer and frees it on deallocation. Therefore, `bytes` must point to a memory block allocated with `malloc`.

## See Also

### Creating Data

- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
