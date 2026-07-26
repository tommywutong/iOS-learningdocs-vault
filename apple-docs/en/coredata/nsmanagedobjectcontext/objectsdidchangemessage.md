---
title: NSManagedObjectContext.ObjectsDidChangeMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/objectsdidchangemessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/objectsdidchangemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/objectsdidchangemessage.json'
content_hash: 'sha256:dbbab78460386798'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.ObjectsDidChangeMessage

<sub>Structure</sub>

Posted when objects in a main queue context change (inserted, updated, deleted, refreshed, or invalidated).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ObjectsDidChangeMessage
```

## Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Relationships

- **Conforms To**: [NotificationCenter.MainActorMessage](../../foundation/notificationcenter/mainactormessage.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](objectsdidchangemessage/context.md)
- [deleted](objectsdidchangemessage/deleted.md) — Objects that were deleted.
- [inserted](objectsdidchangemessage/inserted.md) — Objects that were inserted.
- [invalidated](objectsdidchangemessage/invalidated.md) — Objects that were invalidated.
- [invalidatedAll](objectsdidchangemessage/invalidatedall.md) — True if all objects in the context were invalidated.
- [refreshed](objectsdidchangemessage/refreshed.md) — Objects that were refreshed.
- [updated](objectsdidchangemessage/updated.md) — Objects that were updated.
