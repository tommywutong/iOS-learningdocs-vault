---
title: FileManager.ItemReplacementOptions
framework: Foundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 13.1+, macOS 10.6+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: false
doc_path: /documentation/foundation/filemanager/itemreplacementoptions
source_url: 'https://developer.apple.com/documentation/foundation/filemanager/itemreplacementoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/filemanager/itemreplacementoptions.json'
content_hash: 'sha256:4b436321b0adc6df'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [FileManager](../filemanager.md)

# FileManager.ItemReplacementOptions

<sub>Structure</sub>

Options for specifying the behavior of file replacement operations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ItemReplacementOptions
```

## Overview

These options are used by [- replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:](<replaceitem(at_withitemat_backupitemname_options_resultingitemurl_).md>).

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Using File Replacement Options

- [init(rawValue:)](<itemreplacementoptions/init(rawvalue_).md>) — Creates a value for a file replacement operation.
- [NSFileManagerItemReplacementUsingNewMetadataOnly](itemreplacementoptions/usingnewmetadataonly.md) — Only metadata from the new item is used, and metadata from the original item isn’t preserved (default).
- [NSFileManagerItemReplacementWithoutDeletingBackupItem](itemreplacementoptions/withoutdeletingbackupitem.md) — The backup item remains in place after a successful replacement.

## See Also

### Replacing items

- [replaceItemAt(_:withItemAt:backupItemName:options:)](<replaceitemat(__withitemat_backupitemname_options_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
- [- replaceItemAtURL:withItemAtURL:backupItemName:options:resultingItemURL:error:](<replaceitem(at_withitemat_backupitemname_options_resultingitemurl_).md>) — Replaces the contents of the item at the specified URL in a manner that ensures no data loss occurs.
