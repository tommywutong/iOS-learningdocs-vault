---
title: 'init(rawValue:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/foundation/filemanager/itemreplacementoptions/init(rawvalue:)'
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions/init(rawvalue:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/itemreplacementoptions/init%28rawvalue%3A%29.json'
content_hash: 'sha256:1d8c0d96eff3c0e7'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [FileManager](../../filemanager.md) · [ItemReplacementOptions](../itemreplacementoptions.md)

# init(rawValue:)

<sub>Initializer</sub>

Creates a value for a file replacement operation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(rawValue: UInt)
```

## Parameters

- `rawValue` — An initial value for the structure composed as the bitwise OR of zero or more of the valid values.

## See Also

### Using File Replacement Options

- [NSFileManagerItemReplacementUsingNewMetadataOnly](usingnewmetadataonly.md) — Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [NSFileManagerItemReplacementWithoutDeletingBackupItem](withoutdeletingbackupitem.md) — The backup item remains in place after a successful replacement.
