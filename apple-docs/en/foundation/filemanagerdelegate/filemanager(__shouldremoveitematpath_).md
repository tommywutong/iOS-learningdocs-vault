---
title: 'fileManager(_:shouldRemoveItemAtPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitematpath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitematpath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldremoveitematpath%3A%29.json'
content_hash: 'sha256:bb3a741ccd1cc6a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldRemoveItemAtPath:)

<sub>Instance Method</sub>

Asks the delegate whether the item at the specified path should be deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldRemoveItemAtPath path: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to remove the file or directory.

- `path` — The path to the file or directory that the file manager is attempting to delete.

## Return Value

[true](../../swift/true.md) if the specified item should be deleted or [false](../../swift/false.md) if it should not be deleted.

## Discussion

Removed items are deleted immediately and not placed in the Trash. If the specified item is a directory, returning [false](../../swift/false.md) prevents both the directory and its children from being deleted.

This method performs the same task as the [- fileManager:shouldRemoveItemAtURL:](<filemanager(__shouldremoveitemat_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<../filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- removeItemAtURL:error:](<../filemanager/removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Removing an Item

- [- fileManager:shouldRemoveItemAtURL:](<filemanager(__shouldremoveitemat_).md>) — Asks the delegate whether the item at the specified URL should be deleted.
- [- fileManager:shouldProceedAfterError:removingItemAtURL:](<filemanager(__shouldproceedaftererror_removingitemat_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [- fileManager:shouldProceedAfterError:removingItemAtPath:](<filemanager(__shouldproceedaftererror_removingitematpath_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.
