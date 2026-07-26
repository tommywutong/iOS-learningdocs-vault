---
title: nullDevice
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/nulldevice
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/nulldevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/nulldevice.json'
content_hash: 'sha256:3bb737cd1f2a5616'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# nullDevice

<sub>Type Property</sub>

The file handle associated with a null device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var nullDevice: FileHandle { get }
```

## Return Value

A file handle associated with a null device.

## Discussion

You can use null-device file handles as “placeholders” for standard-device file handles or in collection objects to avoid exceptions and other errors resulting from messages being sent to invalid file handles. Read messages sent to a null-device file handle return an end-of-file indicator (an empty `NSData` object) rather than raise an exception. Write messages are no-ops, whereas [fileDescriptor](filedescriptor.md) returns an illegal value. Other methods are no-ops or return “sensible” values.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.

### Getting a file handle

- [fileHandleWithStandardError](standarderror.md) — The file handle associated with the standard error file.
- [fileHandleWithStandardInput](standardinput.md) — The file handle associated with the standard input file.
- [fileHandleWithStandardOutput](standardoutput.md) — The file handle associated with the standard output file.
