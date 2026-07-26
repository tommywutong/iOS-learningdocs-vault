---
title: DISPATCH_IO_STREAM
framework: Dispatch
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/dispatch/dispatch_io_stream
source_url: 'https://developer.apple.com/documentation/dispatch/dispatch_io_stream'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/dispatch/dispatch_io_stream.json'
content_hash: 'sha256:4f1d1316497cb145'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Dispatch](../dispatch.md)

# DISPATCH_IO_STREAM

<sub>Global Variable</sub>

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var DISPATCH_IO_STREAM: Int32 { get }
```

## Discussion

The channel represents a linear stream of bytes. Read and write operations are performed serially in the order they were started. Operations always read or write data at the file pointer position that is current when the read or write begins. Read and write operations may be performed simultaneously on the same channel.

Offset values are ignored for channels of this type.

## See Also

### Initializing the Type

- [DISPATCH_IO_RANDOM](dispatch_io_random.md)
