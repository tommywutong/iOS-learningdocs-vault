---
title: 'copyItem(atPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/copyitem(atpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/copyitem(atpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/copyitem%28atpath%3Atopath%3A%29.json'
content_hash: 'sha256:863dbbfc8fa848de'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# copyItem(atPath:toPath:)

<sub>Instance Method</sub>

Copies the item at the specified path to a new location synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func copyItem(atPath srcPath: String, toPath dstPath: String) throws
```

## Parameters

- `srcPath` — The path to the file or directory you want to move. This parameter must not be `nil`.

- `dstPath` — The path at which to place the copy of `srcPath`. This path must include the name of the file or directory in its new location. This parameter must not be `nil`.

## Discussion

When copying items, the current process must have permission to read the file or directory at `srcPath` and write the parent directory of `dstPath`. If the item at `srcPath` is a directory, this method copies the directory and all of its contents, including any hidden files. If a file with the same name already exists at `dstPath`, this method stops the copy attempt and returns an appropriate error. If the last component of `srcPath` is a symbolic link, only the link is copied to the new path.

Prior to copying an item, the file manager asks its delegate if it should actually do so for each item. It does this by calling the [- fileManager:shouldCopyItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldcopyitemat_to_).md>) method; if that method is not implemented it calls the [- fileManager:shouldCopyItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldcopyitematpath_topath_).md>) method instead. If the delegate method returns [true](../../swift/true.md), or if the delegate does not implement the appropriate methods, the file manager copies the given file or directory. If there is an error copying an item, the file manager may also call the delegate’s [- fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_copyingitemat_to_).md>) or [- fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_copyingitematpath_topath_).md>) method to determine how to proceed.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Moving and copying items

- [- copyItemAtURL:toURL:error:](<copyitem(at_to_).md>) — Copies the file at the specified URL to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.
- [- moveItemAtPath:toPath:error:](<moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
