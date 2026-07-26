---
title: xml
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 12.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/storetype/xml
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/storetype/xml'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/storetype/xml.json'
content_hash: 'sha256:425ef65b6b618918'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSPersistentStore](../../nspersistentstore.md) · [StoreType](../storetype.md)

# xml

<sub>Type Property</sub>

A store that reads from and writes to a persistent XML file.

<sub>macOS</sub>

```swift
static let xml: NSPersistentStore.StoreType
```

## Discussion

An XML store is atomic, which means Core Data reads and writes the file in its entirety. This behavior is different from a [sqlite](sqlite.md) store, which you can partially modify.

## See Also

### Store Types

- [binary](binary.md) — A store that reads from and writes to a persistent binary file.
- [inMemory](inmemory.md) — An ephemeral store that reads from and writes to memory only.
- [sqlite](sqlite.md) — A store that reads from and writes to a persistent SQLite database.
