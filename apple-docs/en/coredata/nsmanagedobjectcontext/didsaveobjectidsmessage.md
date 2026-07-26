---
title: NSManagedObjectContext.DidSaveObjectIDsMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsmessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didsaveobjectidsmessage.json'
content_hash: 'sha256:11046b2436d05ef6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.DidSaveObjectIDsMessage

<sub>Structure</sub>

Posted after a main queue context saves, containing object IDs rather than full objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidSaveObjectIDsMessage
```

## Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Relationships

- **Conforms To**: [NotificationCenter.MainActorMessage](../../foundation/notificationcenter/mainactormessage.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](didsaveobjectidsmessage/context.md)
- [deletedIDs](didsaveobjectidsmessage/deletedids.md) — Object IDs of objects that were deleted during this save.
- [historyToken](didsaveobjectidsmessage/historytoken.md) — The persistent history token representing the state after the save.
- [insertedIDs](didsaveobjectidsmessage/insertedids.md) — Object IDs of objects that were inserted during this save.
- [invalidatedIDs](didsaveobjectidsmessage/invalidatedids.md) — Object IDs of objects that were invalidated during this save.
- [queryGeneration](didsaveobjectidsmessage/querygeneration.md) — Query generation token after the save.
- [refreshedIDs](didsaveobjectidsmessage/refreshedids.md) — Object IDs of objects that were refreshed during this save.
- [updatedIDs](didsaveobjectidsmessage/updatedids.md) — Object IDs of objects that were updated during this save.
