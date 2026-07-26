---
title: 'init(fileDescriptor:closeOnDealloc:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(filedescriptor:closeondealloc:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(filedescriptor:closeondealloc:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28filedescriptor%3Acloseondealloc%3A%29.json'
content_hash: 'sha256:d3c39a4b9df7789d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(fileDescriptor:closeOnDealloc:)

<sub>Initializer</sub>

Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(fileDescriptor fd: Int32, closeOnDealloc closeopt: Bool)
```

## Parameters

- `fd` — The POSIX file descriptor with which to initialize the file handle.

- `closeopt` — [true](../../swift/true.md) if the returned file handle object should take ownership of the file descriptor and close it for you or [false](../../swift/false.md) if you want to maintain ownership of the file descriptor.

## Return Value

An initialized file handle object.

## Discussion

If `flag` is [false](../../swift/false.md), the file descriptor you pass in to this method isn’t owned by the file handle object. In such a case, you’re responsible for closing the file descriptor at some point after disposing of the file handle object. If you want the file handle object to close the descriptor for you automatically, pass [true](../../swift/true.md) for the `flag` parameter.

## See Also

### Related Documentation

- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_

### Creating a file handle

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
- [+ fileHandleForReadingAtPath:](<init(forreadingatpath_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [init(forReadingFromURL:)](<init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingAtPath:](<init(forwritingatpath_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [init(forWritingToURL:)](<init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [init(forUpdatingURL:)](<init(forupdatingurl_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [- initWithCoder:](<init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.
