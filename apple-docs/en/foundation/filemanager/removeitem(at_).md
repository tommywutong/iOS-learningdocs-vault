---
title: 'removeItem(at:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/removeitem(at:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/removeitem(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/removeitem%28at%3A%29.json'
content_hash: 'sha256:167027fb0cac749c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# removeItem(at:)

<sub>Instance Method</sub>

Removes the file or directory at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func removeItem(at URL: URL) throws
```

## Parameters

- `URL` — A file URL specifying the file or directory to remove. If the URL specifies a directory, the contents of that directory are recursively removed. You may specify `nil` for this parameter in Objective-C.

## Discussion

Prior to removing each item, the file manager asks its delegate if it should actually do so. It does this by calling the [- fileManager:shouldRemoveItemAtURL:](<../filemanagerdelegate/filemanager(__shouldremoveitemat_).md>) method; if that method is not implemented (or the process is running in OS X 10.5 or earlier) it calls the [- fileManager:shouldRemoveItemAtPath:](<../filemanagerdelegate/filemanager(__shouldremoveitematpath_).md>) method instead. If the delegate method returns [true](../../swift/true.md), or if the delegate does not implement the appropriate methods, the file manager proceeds to remove the file or directory. If there is an error removing an item, the file manager may also call the delegate’s [- fileManager:shouldProceedAfterError:removingItemAtURL:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_removingitemat_).md>) or [- fileManager:shouldProceedAfterError:removingItemAtPath:](<../filemanagerdelegate/filemanager(__shouldproceedaftererror_removingitematpath_).md>) method to determine how to proceed.

Removing an item also removes all old versions of that item, invalidating any URLs returned by the [- URLForPublishingUbiquitousItemAtURL:expirationDate:error:](<url(forpublishingubiquitousitemat_expiration_).md>) method to old versions.

## See Also

### Creating and deleting items

- [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<createdirectory(at_withintermediatedirectories_attributes_).md>) — Creates a directory with the given attributes at the specified URL.
- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.
- [- createFileAtPath:contents:attributes:](<createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.
- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.
- [- trashItemAtURL:resultingItemURL:error:](<trashitem(at_resultingitemurl_).md>) — Moves an item to the trash.
