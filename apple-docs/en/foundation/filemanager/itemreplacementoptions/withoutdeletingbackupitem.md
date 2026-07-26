---
title: withoutDeletingBackupItem
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/itemreplacementoptions/withoutdeletingbackupitem
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/withoutdeletingbackupitem'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/itemreplacementoptions/withoutdeletingbackupitem.json'
content_hash: 'sha256:ff5d6d32802c8651'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [ItemReplacementOptions](../itemreplacementoptions.md)

# withoutDeletingBackupItem

<sub>Type Property</sub>

The backup item remains in place after a successful replacement.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var withoutDeletingBackupItem: FileManager.ItemReplacementOptions { get }
```

## See Also

### Using File Replacement Options

- [init(rawValue:)](<init(rawvalue_).md>) — Creates a value for a file replacement operation.
- [NSFileManagerItemReplacementUsingNewMetadataOnly](usingnewmetadataonly.md) — Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
