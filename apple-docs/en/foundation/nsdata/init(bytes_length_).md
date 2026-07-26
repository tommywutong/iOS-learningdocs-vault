---
title: 'init(bytes:length:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(bytes:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(bytes:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28bytes%3Alength%3A%29.json'
content_hash: 'sha256:ca0be7a871472a46'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(bytes:length:)

<sub>Initializer</sub>

Initializes a data object filled with a given number of bytes copied from a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(bytes: UnsafeRawPointer?, length: Int)
```

## Discussion

A data object initialized by adding to it `length` bytes of data copied from the buffer `bytes`. The returned object might be different than the original receiver.

## See Also

### Creating Data

- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
