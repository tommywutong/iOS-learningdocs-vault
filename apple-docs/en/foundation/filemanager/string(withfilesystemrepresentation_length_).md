---
title: 'string(withFileSystemRepresentation:length:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/string(withfilesystemrepresentation:length:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/string(withfilesystemrepresentation:length:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/string%28withfilesystemrepresentation%3Alength%3A%29.json'
content_hash: 'sha256:a45c5d7adb52ef9e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# string(withFileSystemRepresentation:length:)

<sub>Instance Method</sub>

Returns an [NSString](../nsstring.md) object whose contents are derived from the specified C-string path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func string(withFileSystemRepresentation str: UnsafePointer<CChar>, length len: Int) -> String
```

## Parameters

- `str` — A C string representation of a pathname.

- `len` — The number of characters in `string`.

## Return Value

An [NSString](../nsstring.md) object converted from the C-string representation `string` with length `len` of a pathname in the current file system.

## Discussion

Use this method if your code receives paths as C strings from system routines.

## See Also

### Converting file paths to strings

- [- fileSystemRepresentationWithPath:](<filesystemrepresentation(withpath_).md>) — Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.
