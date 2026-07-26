---
title: 'fileManager(_:shouldProceedAfterError:removingItemAt:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Aremovingitemat%3A%29.json'
content_hash: 'sha256:380bd3c43f06f48b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:removingItemAt:)

<sub>Instance Method</sub>

Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, removingItemAt URL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to remove the item.

- `error` — The error that occurred while attempting to remove the item at `URL`.

- `URL` — The URL for the file or directory that the file manager tried to delete.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem deleting the item to the specified location. If you return [true](../../swift/true.md), the file manager continues deleting any remaining items and ignores the error.

This method performs the same task as the [- fileManager:shouldProceedAfterError:removingItemAtPath:](<filemanager(__shouldproceedaftererror_removingitematpath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<../filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- removeItemAtURL:error:](<../filemanager/removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Removing an Item

- [- fileManager:shouldRemoveItemAtURL:](<filemanager(__shouldremoveitemat_).md>) — Asks the delegate whether the item at the specified URL should be deleted.
- [- fileManager:shouldRemoveItemAtPath:](<filemanager(__shouldremoveitematpath_).md>) — Asks the delegate whether the item at the specified path should be deleted.
- [- fileManager:shouldProceedAfterError:removingItemAtPath:](<filemanager(__shouldproceedaftererror_removingitematpath_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.
