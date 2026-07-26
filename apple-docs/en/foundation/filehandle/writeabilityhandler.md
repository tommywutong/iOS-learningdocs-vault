---
title: writeabilityHandler
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/writeabilityhandler
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/writeabilityhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/writeabilityhandler.json'
content_hash: 'sha256:5ce39d3f1cfce3ba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# writeabilityHandler

<sub>Instance Property</sub>

The block to use for writing the contents of the file handle asynchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var writeabilityHandler: (@Sendable (FileHandle) -> Void)? { get set }
```

## Discussion

The default value of this property is `nil`. Assigning a valid [Block object](https://developer.apple.com/library/archive/documentation/General/Conceptual/DevPedia-CocoaCore/Block.html#//apple_ref/doc/uid/TP40008195-CH3) to this property creates a dispatch source for writing the contents of the file or socket. Your block is submitted to the file handle’s dispatch queue when there is room available to write more data. When writing a file, your handler block is typically executed repeatedly until the entire contents of the file have been written. When writing data to a socket, your handler block is executed whenever the socket is ready to accept more data.

The block you provide must accept a single parameter that is the current file handle. The return type of your block should be `void`.

To stop writing data to the file or socket, set the value of this property to `nil`. Doing so cancels the dispatch source and cleans up the file handle’s structures appropriately.

## See Also

### Monitoring for readability and writability

- [readabilityHandler](readabilityhandler.md) — The block to use for reading the contents of the file handle asynchronously.
