---
title: 'dataWithData:'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/datawithdata:'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/datawithdata:'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/datawithdata%3A.json'
content_hash: 'sha256:8e1a4c053853cff1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# dataWithData:

<sub>Type Method</sub>

Creates a data object containing the contents of another data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) dataWithData:(NSData *) data;
```

## Parameters

- `data` — A data object.

## See Also

### Creating Data

- [data](data.md) — Creates an empty data object.
- [dataWithBytes:length:](datawithbytes_length_.md) — Creates a data object containing a given number of bytes copied from a given buffer.
- [dataWithBytesNoCopy:length:](datawithbytesnocopy_length_.md) — Creates a data object that holds a given number of bytes from a given buffer.
- [dataWithBytesNoCopy:length:freeWhenDone:](datawithbytesnocopy_length_freewhendone_.md) — Creates a data object that holds a given number of bytes from a given buffer.
- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
