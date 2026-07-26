---
title: 'trashItem(at:resultingItemURL:)'
framework: Foundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 13.1+, macOS 10.8+, visionOS 1.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/trashitem(at:resultingitemurl:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/trashitem(at:resultingitemurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/trashitem%28at%3Aresultingitemurl%3A%29.json'
content_hash: 'sha256:f33855ddd8b148bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# trashItem(at:resultingItemURL:)

<sub>Instance Method</sub>

Moves an item to the trash.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func trashItem(at url: URL, resultingItemURL outResultingURL: AutoreleasingUnsafeMutablePointer<NSURL?>?) throws
```

## Parameters

- `url` — The item to move to the trash.

- `outResultingURL` — On input, a pointer to a URL object. On output, this pointer is set to the item’s location in the trash. The actual name of the item may be changed when moving it to the trash, so use this URL to access it. You may specify `nil` for this parameter if you do not want the information.

## See Also

### Creating and deleting items

- [- createDirectoryAtURL:withIntermediateDirectories:attributes:error:](<createdirectory(at_withintermediatedirectories_attributes_).md>) — Creates a directory with the given attributes at the specified URL.
- [- createDirectoryAtPath:withIntermediateDirectories:attributes:error:](<createdirectory(atpath_withintermediatedirectories_attributes_).md>) — Creates a directory with given attributes at the specified path.
- [- createFileAtPath:contents:attributes:](<createfile(atpath_contents_attributes_).md>) — Creates a file with the specified content and attributes at the given location.
- [- removeItemAtURL:error:](<removeitem(at_).md>) — Removes the file or directory at the specified URL.
- [- removeItemAtPath:error:](<removeitem(atpath_).md>) — Removes the file or directory at the specified path.
