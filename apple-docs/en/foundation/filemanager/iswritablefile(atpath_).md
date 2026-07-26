---
title: 'isWritableFile(atPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/iswritablefile(atpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/iswritablefile(atpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/iswritablefile%28atpath%3A%29.json'
content_hash: 'sha256:0032b157d383bf97'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# isWritableFile(atPath:)

<sub>Instance Method</sub>

Returns a Boolean value that indicates whether the invoking object appears able to write to a specified file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func isWritableFile(atPath path: String) -> Bool
```

## Parameters

- `path` — A file path.

## Return Value

[true](../../swift/true.md) if the current process has write privileges for the file at `path`; otherwise [false](../../swift/false.md) if the process does not have write privileges or the existence of the file could not be determined.

## Discussion

If the file at `path` is inaccessible to your app, perhaps because it does not have search privileges for one or more parent directories, this method returns [false](../../swift/false.md). This method traverses symbolic links in the path. This method also uses the real user ID and group ID, as opposed to the effective user and group IDs, to determine if the file is writable.

> [!note] Note
> Attempting to predicate behavior based on the current state of the file system or a particular file on the file system is not recommended. Doing so can cause odd behavior or race conditions. It’s far better to attempt an operation (such as loading a file or creating a directory), check for errors, and handle those errors gracefully than it is to try to figure out ahead of time whether the operation will succeed. For more information on file system race conditions, see [Race Conditions and Secure File Operations](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Articles/RaceConditions.html#//apple_ref/doc/uid/TP40002585) in [Secure Coding Guide](https://developer.apple.com/library/archive/documentation/Security/Conceptual/SecureCodingGuide/Introduction.html#//apple_ref/doc/uid/TP40002415).

## See Also

### Determining access to files

- [- fileExistsAtPath:](<fileexists(atpath_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- fileExistsAtPath:isDirectory:](<fileexists(atpath_isdirectory_).md>) — Returns a Boolean value that indicates whether a file or directory exists at a specified path.
- [- isReadableFileAtPath:](<isreadablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to read a specified file.
- [- isExecutableFileAtPath:](<isexecutablefile(atpath_).md>) — Returns a Boolean value that indicates whether the operating system appears able to execute a specified file.
- [- isDeletableFileAtPath:](<isdeletablefile(atpath_).md>) — Returns a Boolean value that indicates whether the invoking object appears able to delete a specified file.
