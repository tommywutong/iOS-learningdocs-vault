---
title: 'init(forReadingAtPath:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(forreadingatpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(forreadingatpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28forreadingatpath%3A%29.json'
content_hash: 'sha256:5e4f8efc792c658b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(forReadingAtPath:)

<sub>Initializer</sub>

Returns a file handle initialized for reading the file, device, or named socket at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init?(forReadingAtPath path: String)
```

## Parameters

- `path` — The path to the file, device, or named socket to access.

## Return Value

The initialized file handle object or `nil` if no file exists at `path`.

## Discussion

The system sets the file pointer to the beginning of the file. You can’t write data to the returned file handle object. Use the [- readDataToEndOfFile](<readdatatoendoffile().md>) or [- readDataOfLength:](<readdata(oflength_).md>) methods to read data from it.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_

### Creating a file handle

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
- [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) — Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [init(forReadingFromURL:)](<init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingAtPath:](<init(forwritingatpath_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [init(forWritingToURL:)](<init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [init(forUpdatingURL:)](<init(forupdatingurl_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.
- [- initWithCoder:](<init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.
