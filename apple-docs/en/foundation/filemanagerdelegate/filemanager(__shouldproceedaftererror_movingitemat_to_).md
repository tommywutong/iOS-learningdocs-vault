---
title: 'fileManager(_:shouldProceedAfterError:movingItemAt:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:movingitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Amovingitemat%3Ato%3A%29.json'
content_hash: 'sha256:5f8d81506db0c628'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:movingItemAt:to:)

<sub>Instance Method</sub>

Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, movingItemAt srcURL: URL, to dstURL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to move the item.

- `error` — The error that occurred while trying to move the item in `srcURL`.

- `srcURL` — The URL of the file or directory that the file manager tried to move.

- `dstURL` — The URL of the intended destination for the item in `srcURL`.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem moving the item to the specified location. If you return [true](../../swift/true.md), the file manager proceeds to remove the item from its current location as if the move operation had completed successfully.

This method performs the same task as the [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- moveItemAtPath:toPath:error:](<../filemanager/moveitem(atpath_topath_).md>) — Moves the file or directory at the specified path to a new location synchronously.
- [- moveItemAtURL:toURL:error:](<../filemanager/moveitem(at_to_).md>) — Moves the file or directory at the specified URL to a new location synchronously.

### Moving  an Item

- [- fileManager:shouldMoveItemAtURL:toURL:](<filemanager(__shouldmoveitemat_to_).md>) — Asks the delegate if the file manager should move the specified item to the new URL.
- [- fileManager:shouldMoveItemAtPath:toPath:](<filemanager(__shouldmoveitematpath_topath_).md>) — Asks the delegate if the file manager should move the specified item to the new path.
- [- fileManager:shouldProceedAfterError:movingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_movingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while moving the item at the specified path.
