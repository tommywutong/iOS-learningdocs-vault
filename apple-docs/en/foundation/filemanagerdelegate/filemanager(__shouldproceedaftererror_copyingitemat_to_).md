---
title: 'fileManager(_:shouldProceedAfterError:copyingItemAt:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:copyingitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Acopyingitemat%3Ato%3A%29.json'
content_hash: 'sha256:feef1e34fc9d915c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:copyingItemAt:to:)

<sub>Instance Method</sub>

Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, copyingItemAt srcURL: URL, to dstURL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to copy the item.

- `error` — The error that occurred during the attempt to copy.

- `srcURL` — The URL or a file or directory that `fileManager` is attempting to copy.

- `dstURL` — The URL or a file or directory to which `fileManager` is attempting to copy.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem copying the item to the specified location. If you return [true](../../swift/true.md), the file manager continues copying any other items and ignores the error.

This method performs the same task as the [- fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_copyingitematpath_topath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- copyItemAtPath:toPath:error:](<../filemanager/copyitem(atpath_topath_).md>) — Copies the item at the specified path to a new location synchronously.
- [- copyItemAtURL:toURL:error:](<../filemanager/copyitem(at_to_).md>) — Copies the file at the specified URL to a new location synchronously.

### Copying  an Item

- [- fileManager:shouldCopyItemAtURL:toURL:](<filemanager(__shouldcopyitemat_to_).md>) — Asks the delegate if the file manager should copy the specified item to the new URL.
- [- fileManager:shouldCopyItemAtPath:toPath:](<filemanager(__shouldcopyitematpath_topath_).md>) — Asks the delegate if the file manager should copy the specified item to the new path.
- [- fileManager:shouldProceedAfterError:copyingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_copyingitematpath_topath_).md>) — Asks the delegate if the move operation should continue after an error occurs while copying the item at the specified path.
