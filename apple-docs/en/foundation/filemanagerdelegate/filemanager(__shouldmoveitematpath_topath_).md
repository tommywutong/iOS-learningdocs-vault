---
title: 'fileManager(_:shouldMoveItemAtPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldmoveitematpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldmoveitematpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldmoveitematpath%3Atopath%3A%29.json'
content_hash: 'sha256:f6f570ad4ea27db6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldMoveItemAtPath:toPath:)

<sub>Instance Method</sub>

Asks the delegate if the file manager should move the specified item to the new path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldMoveItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to move the file or directory.

- `srcPath` — The path to the file or directory that the file manager wants to move.

- `dstPath` — The new path for the file or directory.

## Return Value

[true](../../swift/true.md) if the operation should proceed, otherwise [false](../../swift/false.md). If you do not implement this method, the file manager assumes a response of [true](../../swift/true.md).

## Discussion

This method is called only once for the item being moved, regardless of whether the item is a file, directory, or symbolic link.

This method performs the same task as the [- fileManager:shouldMoveItemAtURL:toURL:](<filemanager(__shouldmoveitemat_to_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- moveItemAtPath:toPath:error:](<../filemanager/moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<../filemanager/moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.

### Moving  an Item

- [- fileManager:shouldMoveItemAtURL:toURL:](<filemanager(__shouldmoveitemat_to_).md>) — Asks the delegate if the file manager should move the specified item to the new URL.
- [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_movingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
- [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.
