---
title: 'CFStringGetFileSystemRepresentation(_:_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetfilesystemrepresentation(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetfilesystemrepresentation(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetfilesystemrepresentation%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:035b54fe401e6709'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetFileSystemRepresentation(_:_:_:)

<sub>Function</sub>

Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetFileSystemRepresentation(_ string: CFString!, _ buffer: UnsafeMutablePointer<CChar>!, _ maxBufLen: CFIndex) -> Bool
```

## Parameters

- `string` — The string to convert.

- `buffer` — The C string buffer into which to copy the string. The buffer must be at least `maxBufLen` bytes in length. On return, the buffer contains the converted characters.

- `maxBufLen` — The maximum length of the buffer.

## Return Value

`true` if the string is correctly converted; `false` if the conversion fails, or the results don’t fit into the buffer.

## Discussion

You can use [CFStringGetMaximumSizeOfFileSystemRepresentation](<cfstringgetmaximumsizeoffilesystemrepresentation(__).md>) if you want to make sure the buffer is of sufficient length.

## See Also

### String File System Representations

- [CFStringCreateWithFileSystemRepresentation](<cfstringcreatewithfilesystemrepresentation(____).md>) — Creates a CFString from a zero-terminated POSIX file system representation.
- [CFStringGetMaximumSizeOfFileSystemRepresentation](<cfstringgetmaximumsizeoffilesystemrepresentation(__).md>) — Determines the upper bound on the number of bytes required to hold the file system representation of the string.
