---
title: 'changeCurrentDirectoryPath(_:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/changecurrentdirectorypath(_:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/changecurrentdirectorypath(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/changecurrentdirectorypath%28_%3A%29.json'
content_hash: 'sha256:56f11557998cbb19'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# changeCurrentDirectoryPath(_:)

<sub>Instance Method</sub>

Changes the path of the current working directory to the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func changeCurrentDirectoryPath(_ path: String) -> Bool
```

## Parameters

- `path` — The path of the directory to which to change.

## Return Value

[true](../../swift/true.md) if successful, otherwise [false](../../swift/false.md).

## Discussion

All relative pathnames refer implicitly to the current working directory.

> [!warning] Warning
> This method changes the current working directory for the current process, not just the receiver.

## See Also

### Related Documentation

- [- fileExistsAtPath:isDirectory:](<fileexists(atpath_isdirectory_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- contentsOfDirectoryAtPath:error:](<contentsofdirectory(atpath_).md>) — Performs a shallow search of the specified directory and returns the paths of any contained items.

### Managing the current directory

- [currentDirectoryPath](currentdirectorypath.md) — The path to the program’s current directory.
