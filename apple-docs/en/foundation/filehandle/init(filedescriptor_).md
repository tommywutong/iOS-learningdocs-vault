---
title: 'init(fileDescriptor:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(filedescriptor:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(filedescriptor:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28filedescriptor%3A%29.json'
content_hash: 'sha256:1a44a39ff15875ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(fileDescriptor:)

<sub>Initializer</sub>

Creates and returns a file handle object associated with the specified file descriptor.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(fileDescriptor fd: Int32)
```

## Parameters

- `fd` — The POSIX file descriptor with which to initialize the file handle. This descriptor represents an open file or socket that you created previously. For example, when creating a file handle for a socket, you’d pass the value returned by the socket function.

## Return Value

A file handle initialized with `fileDescriptor`.

## Discussion

The file descriptor you pass in to this method isn’t owned by the file handle object. Therefore, you’re responsible for closing the file descriptor at some point after disposing of the file handle object.

You can create a file handle for a socket by using the result of a `socket` call as `fileDescriptor`.

## See Also

### Related Documentation

- [- closeFile](<closefile().md>) — Disallows further access to the represented file or communications channel and signals end of file on communications channels that permit writing. _(deprecated)_

### Creating a file handle

- [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) — Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [+ fileHandleForReadingAtPath:](<init(forreadingatpath_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [init(forReadingFromURL:)](<init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingAtPath:](<init(forwritingatpath_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [init(forWritingToURL:)](<init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [init(forUpdatingURL:)](<init(forupdatingurl_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [- initWithCoder:](<init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.
