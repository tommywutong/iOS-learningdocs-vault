---
title: 'CFStringCreateWithFileSystemRepresentation(_:_:)'
framework: Core Foundation
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/corefoundation/cfstringcreatewithfilesystemrepresentation(_:_:)'
source_url: 'https://developer.apple.com/documentation/corefoundation/cfstringcreatewithfilesystemrepresentation(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/corefoundation/cfstringcreatewithfilesystemrepresentation%28_%3A_%3A%29.json'
content_hash: 'sha256:38ddd7b97c0e975f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Foundation](../corefoundation.md)

# CFStringCreateWithFileSystemRepresentation(_:_:)

<sub>Function</sub>

Creates a CFString from a zero-terminated POSIX file system representation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func CFStringCreateWithFileSystemRepresentation(_ alloc: CFAllocator!, _ buffer: UnsafePointer<CChar>!) -> CFString!
```

## Parameters

- `alloc` — The allocator to use to allocate memory for the new string. Pass `NULL` or [kCFAllocatorDefault](kcfallocatordefault.md) to use the current default allocator.

- `buffer` — The C string that you want to convert.

## Return Value

A string that represents `buffer`. The result is `NULL` if there was a problem in creating the string (possible if the conversion fails due to bytes in the buffer not being a valid sequence of bytes for the appropriate character encoding). Ownership follows the [The Create Rule](https://developer.apple.com/library/archive/documentation/CoreFoundation/Conceptual/CFMemoryMgmt/Concepts/Ownership.html#//apple_ref/doc/uid/20001148-103029).

## See Also

### String File System Representations

- [CFStringGetFileSystemRepresentation](<cfstringgetfilesystemrepresentation(______).md>) — Extracts the contents of a string as a `NULL`-terminated 8-bit string appropriate for passing to POSIX APIs.
- [CFStringGetMaximumSizeOfFileSystemRepresentation](<cfstringgetmaximumsizeoffilesystemrepresentation(__).md>) — Determines the upper bound on the number of bytes required to hold the file system representation of the string.
