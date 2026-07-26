---
title: 'contentsEqual(atPath:andPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/contentsequal(atpath:andpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/contentsequal(atpath:andpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/contentsequal%28atpath%3Aandpath%3A%29.json'
content_hash: 'sha256:f5826ec392d85605'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# contentsEqual(atPath:andPath:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the files or directories in specified paths have the same contents.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func contentsEqual(atPath path1: String, andPath path2: String) -> Bool
```

## Parameters

- `path1` — The path of a file or directory to compare with the contents of `path2`.

- `path2` — The path of a file or directory to compare with the contents of `path1`.

## Return Value

[true](../../swift/true.md) if file or directory specified in `path1` has the same contents as that specified in `path2`, otherwise [false](../../swift/false.md).

## Discussion

If `path1` and `path2` are directories, the contents are the list of files and subdirectories each contains—contents of subdirectories are also compared. For files, this method checks to see if they’re the same file, then compares their size, and finally compares their contents. This method does not traverse symbolic links, but compares the links themselves.

## See Also

### Getting and comparing file contents

- [- contentsAtPath:](<contents(atpath_).md>) — Returns the contents of the file at the specified path.
