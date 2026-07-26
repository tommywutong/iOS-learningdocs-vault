---
title: NSPersistentStore.StoreType
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstore/storetype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/storetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/storetype.json'
content_hash: 'sha256:2ba1e6f3f3e614c4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# NSPersistentStore.StoreType

<sub>Structure</sub>

The types of persistent stores that Core Data supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StoreType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Store Types

- [binary](storetype/binary.md) — A store that reads from and writes to a persistent binary file.
- [inMemory](storetype/inmemory.md) — An ephemeral store that reads from and writes to memory only.
- [sqlite](storetype/sqlite.md) — A store that reads from and writes to a persistent SQLite database.
- [xml](storetype/xml.md) — A store that reads from and writes to a persistent XML file.

## See Also

### Getting Store Configuration

- [configurationName](configurationname.md) — The name of the managed object model configuration that creates the persistent store.
- [options](options.md) — The options that Core Data uses to create the store.
- [persistentStoreCoordinator](persistentstorecoordinator.md) — The persistent store coordinator that loads the persistent store.
- [type](type.md) — The type string of the persistent store.
- [Persistent Store Types](../persistent-store-types.md) — Persist data through the available store types.
