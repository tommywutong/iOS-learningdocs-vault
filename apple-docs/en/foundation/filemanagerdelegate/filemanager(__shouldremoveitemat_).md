---
title: 'fileManager(_:shouldRemoveItemAt:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitemat:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldremoveitemat:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldremoveitemat%3A%29.json'
content_hash: 'sha256:d893985177039d64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldRemoveItemAt:)

<sub>Instance Method</sub>

Asks the delegate whether the item at the specified URL should be deleted.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldRemoveItemAt URL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to remove the file or directory.

- `URL` — The URL indicating the file or directory that the file manager is attempting to delete.

## Return Value

[true](../../swift/true.md) if the specified item should be removed or [false](../../swift/false.md) if it should not be removed.

## Discussion

Removed items are deleted immediately and not placed in the Trash. If the specified item is a directory, returning [false](../../swift/false.md) prevents both the directory and its children from being deleted.

This method performs the same task as the [- fileManager:shouldRemoveItemAtPath:](<filemanager(__shouldremoveitematpath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- removeItemAtPath:error:](<../filemanager/removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- removeItemAtURL:error:](<../filemanager/removeitem(at_).md>) — Removes the file or directory at the specified URL.

### Removing an Item

- [- fileManager:shouldRemoveItemAtPath:](<filemanager(__shouldremoveitematpath_).md>) — Asks the delegate whether the item at the specified path should be deleted.
- [- fileManager:shouldProceedAfterError:removingItemAtURL:](<filemanager(__shouldproceedaftererror_removingitemat_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified URL.
- [- fileManager:shouldProceedAfterError:removingItemAtPath:](<filemanager(__shouldproceedaftererror_removingitematpath_).md>) — Asks the delegate if the operation should continue after an error occurs while removing the item at the specified path.
