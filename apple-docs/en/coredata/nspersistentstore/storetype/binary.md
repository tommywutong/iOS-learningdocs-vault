---
title: binary
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/storetype/binary
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/binary'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/storetype/binary.json'
content_hash: 'sha256:23121a1b8e8a07e9'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSPersistentStore](../../nspersistentstore.md) · [StoreType](../storetype.md)

# binary

<sub>Type Property</sub>

A store that reads from and writes to a persistent binary file.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let binary: NSPersistentStore.StoreType
```

## Discussion

A binary store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [sqlite](sqlite.md) store, which you can partially modify.

## See Also

### Store Types

- [inMemory](inmemory.md) — An ephemeral store that reads from and writes to memory only.
- [sqlite](sqlite.md) — A store that reads from and writes to a persistent SQLite database.
- [xml](xml.md) — A store that reads from and writes to a persistent XML file.
