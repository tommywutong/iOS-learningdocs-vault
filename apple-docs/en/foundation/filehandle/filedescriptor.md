---
title: fileDescriptor
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/filedescriptor
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/filedescriptor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/filedescriptor.json'
content_hash: 'sha256:01eb5e6daac14f3e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# fileDescriptor

<sub>Instance Property</sub>

The POSIX file descriptor associated with the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var fileDescriptor: Int32 { get }
```

## Discussion

You can use this method to retrieve the file descriptor while it is open. If the file handle object owns the file descriptor, you must not close it yourself. However, you can use the [- closeFile](<closefile().md>) method to close the file descriptor programmatically. If you do call the [- closeFile](<closefile().md>) method, subsequent calls to this method raise an exception.

## See Also

### Related Documentation

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
