---
title: finishDeferredLightweightMigration()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator/finishdeferredlightweightmigration()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/finishdeferredlightweightmigration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/finishdeferredlightweightmigration%28%29.json'
content_hash: 'sha256:81ea5f1bce437016'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# finishDeferredLightweightMigration()

<sub>Instance Method</sub>

Executes all remaining tasks of a deferred lightweight migration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func finishDeferredLightweightMigration() throws
```

## Discussion

> [!note] Note
> Enable deferred lightweight migrations before using this method. For more information, see [NSPersistentStoreDeferredLightweightMigrationOptionKey](../nspersistentstoredeferredlightweightmigrationoptionkey.md).

## See Also

### Deferring a store’s migrations

- [NSPersistentStoreDeferredLightweightMigrationOptionKey](../nspersistentstoredeferredlightweightmigrationoptionkey.md) — The key for enabling deferred lightweight migrations.
- [- finishDeferredLightweightMigrationTask:](<finishdeferredlightweightmigrationtask().md>) — Executes a single pending task of a deferred lightweight migration.
