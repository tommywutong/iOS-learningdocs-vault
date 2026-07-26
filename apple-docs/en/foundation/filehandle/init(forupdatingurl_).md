---
title: 'init(forUpdatingURL:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filehandle/init(forupdatingurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/init(forupdatingurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/init%28forupdatingurl%3A%29.json'
content_hash: 'sha256:74cbc9c6b75a8cd2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# init(forUpdatingURL:)

<sub>Initializer</sub>

Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(forUpdatingURL url: URL) throws
```

## Parameters

- `url` — The URL of the file, device, or named socket to access.

## Return Value

The initialized file handle object or `nil` if no file exists at `url`.

## Discussion

The file pointer is set to the beginning of the file. The returned object responds to both `NSFileHandle``read...` messages and [- writeData:](<write(__).md>).

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

> [!note] Handling Errors in Swift
> In Swift, this method returns a nonoptional result and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [availableData](availabledata.md) — The data currently available in the receiver.
- [- readDataOfLength:](<readdata(oflength_).md>) — Reads data synchronously up to the specified number of bytes. _(deprecated)_
- [- readDataToEndOfFile](<readdatatoendoffile().md>) — Reads the available data synchronously up to the end of file or maximum number of bytes. _(deprecated)_
- [- writeData:](<write(__).md>) — Writes the specified data synchronously to the file handle. _(deprecated)_

### Creating a file handle

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.
- [- initWithFileDescriptor:closeOnDealloc:](<init(filedescriptor_closeondealloc_).md>) — Creates and returns a file handle object associated with the specified file descriptor and deallocation policy.
- [+ fileHandleForReadingAtPath:](<init(forreadingatpath_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified path.
- [init(forReadingFromURL:)](<init(forreadingfromurl_).md>) — Returns a file handle initialized for reading the file, device, or named socket at the specified URL.
- [+ fileHandleForWritingAtPath:](<init(forwritingatpath_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified path.
- [init(forWritingToURL:)](<init(forwritingtourl_).md>) — Returns a file handle initialized for writing to the file, device, or named socket at the specified URL.
- [+ fileHandleForUpdatingAtPath:](<init(forupdatingatpath_).md>) — Returns a file handle initialized for reading and writing to the file, device, or named socket at the specified path.
- [- initWithCoder:](<init(coder_).md>) — Returns a file handle initialized from data in an unarchiver.
