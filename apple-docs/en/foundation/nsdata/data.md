---
title: data
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsdata/data
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/data'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/data.json'
content_hash: 'sha256:0c104725b084efdf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# data

<sub>Type Method</sub>

Creates an empty data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
+ (instancetype) data;
```

## Discussion

This method is declared primarily for the use of mutable subclasses of [NSData](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/OldStylePlists/OldStylePLists.html#//apple_ref/doc/uid/20001012-47169).

## See Also

### Related Documentation

- [Binary Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/BinaryData/BinaryData.html#//apple_ref/doc/uid/10000037i)
- [Property List Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/PropertyLists/Introduction/Introduction.html#//apple_ref/doc/uid/10000048i)

### Creating Data

- [dataWithBytes:length:](datawithbytes_length_.md) — Creates a data object containing a given number of bytes copied from a given buffer.
- [dataWithBytesNoCopy:length:](datawithbytesnocopy_length_.md) — Creates a data object that holds a given number of bytes from a given buffer.
- [dataWithBytesNoCopy:length:freeWhenDone:](datawithbytesnocopy_length_freewhendone_.md) — Creates a data object that holds a given number of bytes from a given buffer.
- [dataWithData:](datawithdata_.md) — Creates a data object containing the contents of another data object.
- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
- [- initWithData:](<init(data_).md>) — Initializes a data object with the contents of another data object.
