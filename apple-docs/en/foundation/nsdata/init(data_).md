---
title: 'init(data:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsdata/init(data:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsdata/init(data:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsdata/init%28data%3A%29.json'
content_hash: 'sha256:bc3ca999d0fd472c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSData](../nsdata.md)

# init(data:)

<sub>Initializer</sub>

Initializes a data object with the contents of another data object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(data: Data)
```

## Parameters

- `data` — A data object.

## Return Value

A data object initialized with the contents `data`.

## See Also

### Creating Data

- [- initWithBytes:length:](<init(bytes_length_).md>) — Initializes a data object filled with a given number of bytes copied from a given buffer.
- [- initWithBytesNoCopy:length:](<init(bytesnocopy_length_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer.
- [- initWithBytesNoCopy:length:deallocator:](<init(bytesnocopy_length_deallocator_).md>) — Initializes a data object filled with a given number of bytes of data from a given buffer, with a custom deallocator block.
- [- initWithBytesNoCopy:length:freeWhenDone:](<init(bytesnocopy_length_freewhendone_).md>) — Initializes a newly allocated data object by adding the given number of bytes from the given buffer.
