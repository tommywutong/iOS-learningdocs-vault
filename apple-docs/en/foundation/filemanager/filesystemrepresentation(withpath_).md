---
title: 'fileSystemRepresentation(withPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/filesystemrepresentation(withpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/filesystemrepresentation(withpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/filesystemrepresentation%28withpath%3A%29.json'
content_hash: 'sha256:7db032bdf3943a6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# fileSystemRepresentation(withPath:)

<sub>Instance Method</sub>

Returns a C-string representation of a given path that properly encodes Unicode strings for use by the file system.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func fileSystemRepresentation(withPath path: String) -> UnsafePointer<CChar>
```

## Parameters

- `path` — A string object containing a path to a file. This parameter must not be `nil` or contain the empty string.

## Return Value

A C-string representation of `path` that properly encodes Unicode strings for use by the file system.

## Discussion

Use this method if your code calls system routines that expect C-string path arguments. If you use the C string beyond the scope of the current autorelease pool, you must copy it.

This method raises an exception if `path` is `nil` or contains the empty string. This method also throws an exception if the conversion of the string fails.

## See Also

### Converting file paths to strings

- [- stringWithFileSystemRepresentation:length:](<string(withfilesystemrepresentation_length_).md>) — Returns an [NSString](../nsstring.md) object whose contents are derived from the specified C-string path.
