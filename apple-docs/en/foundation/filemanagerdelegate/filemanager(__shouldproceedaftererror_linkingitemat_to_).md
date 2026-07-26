---
title: 'fileManager(_:shouldProceedAfterError:linkingItemAt:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldproceedaftererror:linkingitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldproceedaftererror%3Alinkingitemat%3Ato%3A%29.json'
content_hash: 'sha256:1d7c40762095aa53'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldProceedAfterError:linkingItemAt:to:)

<sub>Instance Method</sub>

Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldProceedAfterError error: any Error, linkingItemAt srcURL: URL, to dstURL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that attempted to create the link.

- `error` — The error that occurred during the link attempt.

- `srcURL` — The URL of the attempted link location.

- `dstURL` — The URL of the file or directory that was the destination of the hard link.

## Return Value

[true](../../swift/true.md) if the operation should proceed or [false](../../swift/false.md) if it should be aborted. If you do not implement this method, the file manager assumes a response of [false](../../swift/false.md).

## Discussion

The file manager calls this method when there is a problem creating a hard link to the item at the specified location. If you return [true](../../swift/true.md), the file manager continues creating any other links associated with the current operation and ignores the error.

This method performs the same task as the [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- linkItemAtURL:toURL:error:](<../filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<../filemanager/linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.

### Linking an Item

- [- fileManager:shouldLinkItemAtURL:toURL:](<filemanager(__shouldlinkitemat_to_).md>) — Asks the delegate if a hard link should be created between the items at the two URLs.
- [- fileManager:shouldLinkItemAtPath:toPath:](<filemanager(__shouldlinkitematpath_topath_).md>) — Asks the delegate if a hard link should be created between the items at the two paths.
- [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.
