---
title: NSPersistentStoreCoordinator.RemoteChangeMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinator/remotechangemessage
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/remotechangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/remotechangemessage.json'
content_hash: 'sha256:544602b895764faa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# NSPersistentStoreCoordinator.RemoteChangeMessage

<sub>Structure</sub>

Posted when a store receives a remote change notification from another process.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RemoteChangeMessage
```

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [historyToken](remotechangemessage/historytoken.md) — The persistent history token representing the state after the remote change.
- [persistentStoreCoordinator](remotechangemessage/persistentstorecoordinator.md)
- [storeURL](remotechangemessage/storeurl.md) — The URL of the store that changed.
- [storeUUID](remotechangemessage/storeuuid.md) — The UUID of the store that changed.
