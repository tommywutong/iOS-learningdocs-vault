---
title: fileHandleForReading
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/pipe/filehandleforreading
source_url: 'https://developer.apple.com/documentation/foundation/pipe/filehandleforreading'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/pipe/filehandleforreading.json'
content_hash: 'sha256:e874b64c3dc36624'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [Pipe](../pipe.md)

# fileHandleForReading

<sub>Instance Property</sub>

The receiver’s read file handle.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileHandleForReading: FileHandle { get }
```

## Discussion

The descriptor represented by this object is deleted, and the object itself is automatically deallocated when the receiver is deallocated.

You use the returned file handle to read from the pipe using `NSFileHandle`’s read methods—[availableData](../filehandle/availabledata.md), [- readDataToEndOfFile](<../filehandle/readdatatoendoffile().md>), and [- readDataOfLength:](<../filehandle/readdata(oflength_).md>).

You don’t need to send [- closeFile](<../filehandle/closefile().md>) to this object or explicitly release the object after you have finished using it.

## See Also

### Getting the File Handles for a Pipe

- [fileHandleForWriting](filehandleforwriting.md) — The receiver’s write file handle.
