---
title: 'moveItem(at:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/moveitem(at:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/moveitem(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/moveitem%28at%3Ato%3A%29.json'
content_hash: 'sha256:a23fdb44f6222405'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# moveItem(at:to:)

<sub>Instance Method</sub>

Moves the file or directory at the specified URL to a new location synchronously.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func moveItem(at srcURL: URL, to dstURL: URL) throws
```

## Parameters

- `srcURL` — The file URL that identifies the file or directory you want to move. The URL in this parameter must not be a file reference URL. This parameter must not be `nil`.

- `dstURL` — The new location for the item in `srcURL`. The URL in this parameter must not be a file reference URL and must include the name of the file or directory in its new location. This parameter must not be `nil`.

## Discussion

When moving items, the current process must have permission to read the item at `srcURL` and write the parent directory of `dstURL`. If the item at `srcURL` is a directory, this method moves the directory and all of its contents, including any hidden files. If an item with the same name already exists at `dstURL`, this method stops the move attempt and returns an appropriate error. If the last component of `srcURL` is a symbolic link, only the link is moved to the new path; the item pointed to by the link remains at its current location.

Prior to moving the item, the file manager asks its delegate if it should actually move it. It does this by calling the [- fileManager:shouldMoveItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldmoveitemat_to_).md>) method; if that method is not implemented it calls the [- fileManager:shouldMoveItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldmoveitematpath_topath_).md>) method instead. If the item being moved is a directory, the file manager notifies the delegate only for the directory itself and not for any of its contents. If the delegate method returns [true](../../swift/true.md), or if the delegate does not implement the appropriate methods, the file manager moves the file. If there is an error moving one out of several items, the file manager may also call the delegate’s [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_movingitemat_to_).md>) or [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) method to determine how to proceed.

If the source and destination of the move operation are not on the same volume, this method copies the item first and then removes it from its current location. This behavior may trigger additional delegate notifications related to copying and removing individual items.

> [!note] Handling Errors in Swift
> In Swift, this method returns `Void` and is marked with the `throws` keyword to indicate that it throws an error in cases of failure.
>
> You call this method in a `try` expression and handle any errors in the `catch` clauses of a `do` statement, as described in [Error Handling](https://docs.swift.org/swift-book/LanguageGuide/ErrorHandling.html) in [The Swift Programming Language](https://docs.swift.org/swift-book/) and `About Imported Cocoa Error Parameters`.

## See Also

### Related Documentation

- [- removeItemAtURL:error:](<removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Moving and copying items

- [- copyItemAtURL:toURL:error:](<copyitem(at_to_).md>) — Copies the file at the specified URL to a new location synchronously.
- [- copyItemAtPath:toPath:error:](<copyitem(atpath_topath_).md>) — Copies the item at the specified path to a new location synchronously.
- [- moveItemAtPath:toPath:error:](<moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
