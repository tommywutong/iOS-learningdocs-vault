---
title: NSManagedObjectContext.DidSaveObjectIDsAsyncMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsasyncmessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsasyncmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsasyncmessage.json'
content_hash: 'sha256:f0bc428e0a165f69'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.DidSaveObjectIDsAsyncMessage

<sub>Structure</sub>

Posted after a private queue context saves, containing object IDs rather than full objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidSaveObjectIDsAsyncMessage
```

## Overview

Only use this message type for contexts with `NSPrivateQueueConcurrencyType`. For main queue contexts, use [DidSaveObjectIDsMessage](didsaveobjectidsmessage.md).

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](didsaveobjectidsasyncmessage/context.md)
- [deletedIDs](didsaveobjectidsasyncmessage/deletedids.md) — Object IDs of objects that were deleted during this save.
- [historyToken](didsaveobjectidsasyncmessage/historytoken.md) — The persistent history token representing the state after the save.
- [insertedIDs](didsaveobjectidsasyncmessage/insertedids.md) — Object IDs of objects that were inserted during this save.
- [invalidatedIDs](didsaveobjectidsasyncmessage/invalidatedids.md) — Object IDs of objects that were invalidated during this save.
- [queryGeneration](didsaveobjectidsasyncmessage/querygeneration.md) — Query generation token after the save.
- [refreshedIDs](didsaveobjectidsasyncmessage/refreshedids.md) — Object IDs of objects that were refreshed during this save.
- [updatedIDs](didsaveobjectidsasyncmessage/updatedids.md) — Object IDs of objects that were updated during this save.
