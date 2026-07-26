---
title: usingNewMetadataOnly
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/itemreplacementoptions/usingnewmetadataonly
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/usingnewmetadataonly'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/itemreplacementoptions/usingnewmetadataonly.json'
content_hash: 'sha256:8f9a1f85e25a6414'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [ItemReplacementOptions](../itemreplacementoptions.md)

# usingNewMetadataOnly

<sub>Type Property</sub>

Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var usingNewMetadataOnly: FileManager.ItemReplacementOptions { get }
```

## See Also

### Using File Replacement Options

- [init(rawValue:)](<init(rawvalue_).md>) — Creates a value for a file replacement operation.
- [NSFileManagerItemReplacementWithoutDeletingBackupItem](withoutdeletingbackupitem.md) — The backup item remains in place after a successful replacement.
