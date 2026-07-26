---
title: NSPersistentStoreCoordinator.StoresDidChangeMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator/storesdidchangemessage
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/storesdidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/storesdidchangemessage.json'
content_hash: 'sha256:491ef106657e6358'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# NSPersistentStoreCoordinator.StoresDidChangeMessage

<sub>Structure</sub>

Posted when stores are added to or removed from the persistent store coordinator on the main queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct StoresDidChangeMessage
```

## Relationships

- **Conforms To**: [NotificationCenter.MainActorMessage](../../foundation/notificationcenter/mainactormessage.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [addedStores](storesdidchangemessage/addedstores.md) — Stores that were added during this change.
- [persistentStoreCoordinator](storesdidchangemessage/persistentstorecoordinator.md)
- [removedStores](storesdidchangemessage/removedstores.md) — Stores that were removed during this change.
- [uuidChangedStores](storesdidchangemessage/uuidchangedstores.md)
