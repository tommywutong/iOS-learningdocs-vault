---
title: 'fileManager(_:shouldProceedAfterError:linkingItemAtPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitematpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Alinkingitematpath%3Atopath%3A%29.json'
content_hash: 'sha256:ca4d4d4ff96fc512'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:linkingItemAtPath:toPath:)

<sub>Instance Method</sub>

Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, linkingItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to create the link.

- `error` — The error that occurred during the link attempt.

- `srcPath` — The path to the attempted link location.

- `dstPath` — The path to the file or directory that was the destination of the hard link.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem creating a hard link to the item at the specified location. If you return [true](../../swift/true.md), the file manager continues creating any other links associated with the current operation and ignores the error.

This method performs the same task as the [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- linkItemAtURL:toURL:error:](<../filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<../filemanager/linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.

### Linking an Item

- [- fileManager:shouldLinkItemAtURL:toURL:](<filemanager(__shouldlinkitemat_to_).md>) — Asks the delegate if a hard link should be created between the items at the two URLs.
- [- fileManager:shouldLinkItemAtPath:toPath:](<filemanager(__shouldlinkitematpath_topath_).md>) — Asks the delegate if a hard link should be created between the items at the two paths.
- [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
