---
title: 'dataWithBytesNoCopy:length:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithbytesnocopy:length:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithbytesnocopy:length:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithbytesnocopy%3Alength%3A.json'
content_hash: 'sha256:0cfd5794db9a958d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithBytesNoCopy:length:

<sub>Type Method</sub>

Creates a data object that holds a given number of bytes from a given buffer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithBytesNoCopy:(void *) bytes length:(NSUInteger) length;
```

## Parameters

- `bytes` — A buffer containing data for the new object. `bytes` must point to a memory block allocated with `malloc`.

- `length` — The number of bytes to hold from `bytes`. This value must not exceed the length of `bytes`.

## Discussion

The returned object takes ownership of the `bytes` pointer and frees it on deallocation. Therefore, `bytes` must point to a memory block allocated with `malloc`.

## See Also

### Creating Data

- [data](data.md) — Creates an empty data object.
- [dataWithBytes:length:](datawithbytes_length_.md) — Creates a data object containing a given number of bytes copied from a given buffer.
- [dataWithBytesNoCopy:length:freeWhenDone:](datawithbytesnocopy_length_freewhendone_.md) — Creates a data object that holds a given number of bytes from a given buffer.
- [dataWithData:](datawithdata_.md) — Creates a data object containing the contents of another data object.
- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
