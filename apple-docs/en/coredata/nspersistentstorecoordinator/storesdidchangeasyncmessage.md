---
title: NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/storesdidchangeasyncmessage.json'
content_hash: 'sha256:eee30174f16ea4d1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# NSPersistentStoreCoordinator.StoresDidChangeAsyncMessage

<sub>Structure</sub>

Posted when stores are added to or removed from the persistent store coordinator on a background queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StoresDidChangeAsyncMessage
```

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [addedStores](storesdidchangeasyncmessage/addedstores.md) — Stores that were added during this change.
- [persistentStoreCoordinator](storesdidchangeasyncmessage/persistentstorecoordinator.md)
- [removedStores](storesdidchangeasyncmessage/removedstores.md) — Stores that were removed during this change.
- [uuidChangedStores](storesdidchangeasyncmessage/uuidchangedstores.md)
