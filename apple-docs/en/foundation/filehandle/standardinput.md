---
title: standardInput
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/standardinput
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/standardinput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/standardinput.json'
content_hash: 'sha256:7ef938dc79a5fad0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# standardInput

<sub>Type Property</sub>

The file handle associated with the standard input file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var standardInput: FileHandle { get }
```

## Return Value

The shared file handle associated with the standard input file.

## Discussion

Conventionally this is a terminal device on which the user enters a stream of data. There’s one standard input file handle per process; it’s a shared instance.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.

### Getting a file handle

- [fileHandleWithStandardError](standarderror.md) — The file handle associated with the standard error file.
- [fileHandleWithStandardOutput](standardoutput.md) — The file handle associated with the standard output file.
- [fileHandleWithNullDevice](nulldevice.md) — The file handle associated with a null device.
