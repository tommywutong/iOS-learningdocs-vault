---
title: close()
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/close()
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/close()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/close%28%29.json'
content_hash: 'sha256:3589a07b910fbf6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# close()

<sub>Instance Method</sub>

Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func close() throws
```

## Discussion

If the file handle object owns its file descriptor, it automatically closes that descriptor when deallocated. If you initialized the file handle object using the [- initWithFileDescriptor:](<init(filedescriptor_).md>) method, or you initialized it using the [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) and passed [false](../../swift/false.md) for the `flag` parameter, you can use this method to close the file descriptor; otherwise, you must close the file descriptor yourself.

After calling this method, you may still use the file handle object, but you must not attempt to read or write data or use the object to operate on the file descriptor. Attempts to read or write a closed file descriptor raise an exception.

## See Also

### Operating on a file

- [- synchronizeAndReturnError:](<synchronize().md>) — Causes all in-memory data and attributes of the file represented by the file handle to write to permanent storage.
- [- truncateAtOffset:error:](<truncate(atoffset_).md>) — Truncates or extends the file represented by the file handle to a specified offset within the file and puts the file pointer at that position.
