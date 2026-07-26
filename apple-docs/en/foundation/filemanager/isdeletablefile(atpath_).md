---
title: 'isDeletableFile(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/isdeletablefile(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/isdeletablefile(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/isdeletablefile%28atpath%3A%29.json'
content_hash: 'sha256:9af7b49b8b9eba32'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# isDeletableFile(atPath:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isDeletableFile(atPath path: String) -> Bool
```

## Parameters

- `path` — A file path.

## Return Value

[true](../../swift/true.md) if the current process has delete privileges for the file at `path`; otherwise [false](../../swift/false.md) if the process does not have delete privileges or the existence of the file could not be determined.

## Discussion

For a directory or file to be deletable, the current process must either be able to write to the parent directory of `path` or it must have the same owner as the item at `path`. If `path` is a directory, every item contained in `path` must be deletable by the current process.

If the file at `path` is inaccessible to your app, perhaps because it does not have search privileges for one or more parent directories, this method returns [false](../../swift/false.md). If the item at `path` is a symbolic link, it is not traversed.

> [!note] Note
> Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file system race conditions, see [Race Conditions and Secure File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## See Also

### Determining access to files

- [- fileExistsAtPath:](<fileexists(atpath_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- fileExistsAtPath:isDirectory:](<fileexists(atpath_isdirectory_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- isReadableFileAtPath:](<isreadablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [- isWritableFileAtPath:](<iswritablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.
- [- isExecutableFileAtPath:](<isexecutablefile(atpath_).md>) — Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
