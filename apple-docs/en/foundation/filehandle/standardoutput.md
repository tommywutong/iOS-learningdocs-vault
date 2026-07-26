---
title: standardOutput
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filehandle/standardoutput
source_url: 'https://developer.apple.com/documentation/foundation/filehandle/standardoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filehandle/standardoutput.json'
content_hash: 'sha256:8de5e3e7d751480f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileHandle](../filehandle.md)

# standardOutput

<sub>Type Property</sub>

The file handle associated with the standard output file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class var standardOutput: FileHandle { get }
```

## Return Value

The shared file handle associated with the standard output file.

## Discussion

Conventionally this is a terminal device that receives a stream of data from a program. There’s one standard output file handle per process; it’s a shared instance.

When using this method to create a file handle object, the file handle owns its associated file descriptor and is responsible for closing it.

## See Also

### Related Documentation

- [- initWithFileDescriptor:](<init(filedescriptor_).md>) — Creates and returns a file handle object associated with the specified file descriptor.

### Getting a file handle

- [fileHandleWithStandardError](standarderror.md) — The file handle associated with the standard error file.
- [fileHandleWithStandardInput](standardinput.md) — The file handle associated with the standard input file.
- [fileHandleWithNullDevice](nulldevice.md) — The file handle associated with a null device.
