---
title: 'fileManager(_:shouldProceedAfterError:movingItemAtPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitematpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Amovingitematpath%3Atopath%3A%29.json'
content_hash: 'sha256:471419c1c22ea085'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:movingItemAtPath:toPath:)

<sub>Instance Method</sub>

Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, movingItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to move the item.

- `error` — The error that occurred while trying to move the item in `srcPath`.

- `srcPath` — The path of the file or directory that the file manager tried to move.

- `dstPath` — The path of the intended destination for the item in `srcPath`.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem moving the item to the specified location. If you return [true](../../swift/true.md), the file manager proceeds to remove the item from its current location as if the move operation had completed successfully.

This method performs the same task as the [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_movingitemat_to_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- moveItemAtPath:toPath:error:](<../filemanager/moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<../filemanager/moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.

### Moving  an Item

- [- fileManager:shouldMoveItemAtURL:toURL:](<filemanager(__shouldmoveitemat_to_).md>) — Asks the delegate if the file manager should move the specified item to the new URL.
- [- fileManager:shouldMoveItemAtPath:toPath:](<filemanager(__shouldmoveitematpath_topath_).md>) — Asks the delegate if the file manager should move the specified item to the new path.
- [- fileManager:shouldProceedAfterError:movingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_movingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.
