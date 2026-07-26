---
title: 'fileManager(_:shouldMoveItemAt:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldmoveitemat:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldmoveitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldmoveitemat%3Ato%3A%29.json'
content_hash: 'sha256:56f88a27d69b59b7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldMoveItemAt:to:)

<sub>Instance Method</sub>

Asks the delegate if the file manager should move the specified item to the new URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldMoveItemAt srcURL: URL, to dstURL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to move the file or directory.

- `srcURL` — The URL of the file or directory that the file manager wants to move.

- `dstURL` — The URL specifying the new location for the file or directory.

## Return Value

[true](../../swift/true.md) if the item should be moved or [false](../../swift/false.md) if it should not be moved. If you do not implement this method, the file manager assumes a response of [true](../../swift/true.md).

## Discussion

This method is called only once for the item being moved, regardless of whether the item is a file, directory, or symbolic link.

This method performs the same task as the [- fileManager:shouldMoveItemAtPath:toPath:](<filemanager(__shouldmoveitematpath_topath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- moveItemAtPath:toPath:error:](<../filemanager/moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<../filemanager/moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.

### Moving  an Item

- [- fileManager:shouldMoveItemAtPath:toPath:](<filemanager(__shouldmoveitematpath_topath_).md>) — Asks the delegate if the file manager should move the specified item to the new path.
- [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_movingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
- [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.
