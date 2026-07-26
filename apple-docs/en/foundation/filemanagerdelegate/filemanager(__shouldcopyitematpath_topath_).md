---
title: 'fileManager(_:shouldCopyItemAtPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldcopyitematpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldcopyitematpath%3Atopath%3A%29.json'
content_hash: 'sha256:051c70f3512ec742'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldCopyItemAtPath:toPath:)

<sub>Instance Method</sub>

Asks the delegate if the file manager should copy the specified item to the new path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldCopyItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to copy the file or directory.

- `srcPath` — The path to the file or directory that the file manager wants to copy.

- `dstPath` — The new path for the copied file or directory.

## Return Value

[true](../../swift/true.md) if the item should be copied or [false](../../swift/false.md) if the file manager should stop copying items associated with the current operation. If you do not implement this method, the file manager assumes a response of [true](../../swift/true.md).

## Discussion

This method is called once for each item that needs to be copied. Thus, for a directory, this method is called once for the directory and once for each item in the directory.

This method performs the same task as the [- fileManager:shouldCopyItemAtURL:toURL:](<filemanager(__shouldcopyitemat_to_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- copyItemAtPath:toPath:error:](<../filemanager/copyitem(atpath_topath_).md>) — Copies the item at the specified path to a new location synchronously.
- [- copyItemAtURL:toURL:error:](<../filemanager/copyitem(at_to_).md>) — Copies the file at the specified URL to a new location synchronously.

### Copying  an Item

- [- fileManager:shouldCopyItemAtURL:toURL:](<filemanager(__shouldcopyitemat_to_).md>) — Asks the delegate if the file manager should copy the specified item to the new URL.
- [- fileManager:shouldProceedAfterError:copyingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_copyingitemat_to_).md>) — Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.
- [- fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_copyingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.
