---
title: 'fileManager(_:shouldProceedAfterError:removingItemAtPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:removingitematpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Aremovingitematpath%3A%29.json'
content_hash: 'sha256:18151abee1ec5589'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:removingItemAtPath:)

<sub>Instance Method</sub>

Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, removingItemAtPath path: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to remove the item.

- `error` — The error that occurred during the attempt to copy.

- `path` — The path for the file or directory that the file manager tried to delete.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem deleting the item to the specified location. If you return [true](../../swift/true.md), the file manager continues deleting any remaining items and ignores the error.

This method performs the same task as the [- fileManager:shouldProceedAfterError:removingItemAtURL:](<filemanager(__shouldproceedaftererror_removingitemat_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<../filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- removeItemAtURL:error:](<../filemanager/removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Removing an Item

- [- fileManager:shouldRemoveItemAtURL:](<filemanager(__shouldremoveitemat_).md>) — Asks the delegate whether the item at the specified URL should be deleted.
- [- fileManager:shouldRemoveItemAtPath:](<filemanager(__shouldremoveitematpath_).md>) — Asks the delegate whether the item at the specified path should be deleted.
- [- fileManager:shouldProceedAfterError:removingItemAtURL:](<filemanager(__shouldproceedaftererror_removingitemat_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
