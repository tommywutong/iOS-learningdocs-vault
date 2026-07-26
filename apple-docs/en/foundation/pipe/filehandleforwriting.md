---
title: fileHandleForWriting
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/pipe/filehandleforwriting
source_url: 'https://developer.apple.com/documentation/foundation/pipe/filehandleforwriting'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pipe/filehandleforwriting.json'
content_hash: 'sha256:250d53cc94bb49cd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Pipe](../pipe.md)

# fileHandleForWriting

<sub>Instance Property</sub>

The receiver’s write file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileHandleForWriting: FileHandle { get }
```

## Discussion

This object is automatically deallocated when the receiver is deallocated.

You use the returned file handle to write to the pipe using `NSFileHandle`’s [- writeData:](<../filehandle/write(__).md>) method. When you are finished writing data to this object, send it a [- closeFile](<../filehandle/closefile().md>) message to delete the descriptor. Deleting the descriptor causes the reading process to receive an end-of-data signal (an empty `NSData` object).

## See Also

### Getting the File Handles for a Pipe

- [fileHandleForReading](filehandleforreading.md) — The receiver’s read file handle.
