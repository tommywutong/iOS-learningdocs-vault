---
title: 'fileManager(_:shouldLinkItemAt:to:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitemat:to:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitemat:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldlinkitemat%3Ato%3A%29.json'
content_hash: 'sha256:3fd69b3b24b15f1b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldLinkItemAt:to:)

<sub>Instance Method</sub>

Asks the delegate if a hard link should be created between the items at the two URLs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldLinkItemAt srcURL: URL, to dstURL: URL) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to create the link.

- `srcURL` — The URL identifying the new hard link to be created.

- `dstURL` — The URL identifying the destination of the link.

## Return Value

[true](../../swift/true.md) if the link should be created or [false](../../swift/false.md) if it should not be created.

## Discussion

If the item specified by `destURL` is a directory, returning [false](../../swift/false.md) prevents links from being created to both the directory and its children.

This method performs the same task as the [- fileManager:shouldLinkItemAtPath:toPath:](<filemanager(__shouldlinkitematpath_topath_).md>) method and is preferred over that method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- linkItemAtURL:toURL:error:](<../filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<../filemanager/linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.

### Linking an Item

- [- fileManager:shouldLinkItemAtPath:toPath:](<filemanager(__shouldlinkitematpath_topath_).md>) — Asks the delegate if a hard link should be created between the items at the two paths.
- [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.
