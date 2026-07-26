---
title: 'fileManager(_:shouldLinkItemAtPath:toPath:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 2.0+, iPadOS 2.0+, Mac Catalyst 13.0+, macOS 10.0+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanagerdelegate/filemanager(_:shouldlinkitematpath:topath:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanagerdelegate/filemanager%28_%3Ashouldlinkitematpath%3Atopath%3A%29.json'
content_hash: 'sha256:93fcb2ded07fcae4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManagerDelegate](../filemanagerdelegate.md)

# fileManager(_:shouldLinkItemAtPath:toPath:)

<sub>Instance Method</sub>

Asks the delegate if a hard link should be created between the items at the two paths.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
optional func fileManager(_ fileManager: FileManager, shouldLinkItemAtPath srcPath: String, toPath dstPath: String) -> Bool
```

## Parameters

- `fileManager` — The file manager object that is attempting to create the link.

- `srcPath` — The path or a file or directory that `fileManager` is about to attempt to link.

- `dstPath` — The path or a file or directory to which `fileManager` is about to attempt to link.

## Return Value

[true](../../swift/true.md) if the operation should proceed, otherwise [false](../../swift/false.md).

## Discussion

If the item specified by `destURL` is a directory, returning [false](../../swift/false.md) prevents links from being created to both the directory and its children.

This method performs the same task as the [- fileManager:shouldLinkItemAtURL:toURL:](<filemanager(__shouldlinkitemat_to_).md>) method, which is preferred over this method in macOS 10.6 and later.

## See Also

### Related Documentation

- [- linkItemAtURL:toURL:error:](<../filemanager/linkitem(at_to_).md>) — Creates a hard link between the items at the specified URLs.
- [- linkItemAtPath:toPath:error:](<../filemanager/linkitem(atpath_topath_).md>) — Creates a hard link between the items at the specified paths.

### Linking an Item

- [- fileManager:shouldLinkItemAtURL:toURL:](<filemanager(__shouldlinkitemat_to_).md>) — Asks the delegate if a hard link should be created between the items at the two URLs.
- [- fileManager:shouldProceedAfterError:linkingItemAtURL:toURL:](<filemanager(__shouldproceedaftererror_linkingitemat_to_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified URL.
- [- fileManager:shouldProceedAfterError:linkingItemAtPath:toPath:](<filemanager(__shouldproceedaftererror_linkingitematpath_topath_).md>) — Asks the delegate if the operation should continue after an error occurs while linking to the item at the specified path.
