---
title: 'CFStringGetMaximumSizeOfFileSystemRepresentation(_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringgetmaximumsizeoffilesystemrepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringgetmaximumsizeoffilesystemrepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringgetmaximumsizeoffilesystemrepresentation%28_%3A%29.json'
content_hash: 'sha256:b50b28158f5aa866'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringGetMaximumSizeOfFileSystemRepresentation(_:)

<sub>Function</sub>

Determines the upper bound on the number of bytes required to hold the file system representation of the string.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringGetMaximumSizeOfFileSystemRepresentation(_ string: CFString!) -> CFIndex
```

## Parameters

- `string` — The string to convert.

## Return Value

The upper bound on the number of bytes required to hold the file system representation of the string.

## Discussion

The result is returned quickly as a rough approximation, and could be much larger than the actual space required. The result includes space for the zero termination. If you are allocating a buffer for long-term storage, you should reallocate it to be the right size after calling [CFStringGetFileSystemRepresentation](<cfstringgetfilesystemrepresentation(______).md>).

## See Also

### String File System Representations

- [CFStringCreateWithFileSystemRepresentation](<cfstringcreatewithfilesystemrepresentation(____).md>) — Creates a CFString from a zero-terminated POSIX file system representation.
- [CFStringGetFileSystemRepresentation](<cfstringgetfilesystemrepresentation(______).md>) — Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.
