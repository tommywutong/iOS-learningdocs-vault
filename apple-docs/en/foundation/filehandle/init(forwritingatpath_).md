---
title: 'init(forWritingAtPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(forwritingatpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(forwritingatpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28forwritingatpath%3A%29.json'
content_hash: 'sha256:655bcf3f6a224b7d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(forWritingAtPath:)

<sub>Initializer</sub>

Returns a file handle initialized for writing to the file, device, or named socket at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(forWritingAtPath path: String)
```

## Parameters

- `path` — The path to the file, device, or named socket to access.

## Return Value

The initialized file handle object or `nil` if no file exists at `path`.

## Discussion

The file pointer is set to the beginning of the file. You cannot read data from the returned file handle object. Use the [- writeData:](<write(__).md>) method to write data to the file handle.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation

- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_

### Creating a file handle

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
- [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) — Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [+ fileHandleForReadingAtPath:](<init(forreadingatpath_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [init(forReadingFromURL:)](<init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [init(forWritingToURL:)](<init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [init(forUpdatingURL:)](<init(forupdatingurl_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [- initWithCoder:](<init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.
