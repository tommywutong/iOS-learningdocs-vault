---
title: NSManagedObjectContext.DidSaveMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didsavemessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didsavemessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didsavemessage.json'
content_hash: 'sha256:14df7e8a40881e4d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.DidSaveMessage

<sub>Structure</sub>

Posted after a main queue context saves.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidSaveMessage
```

## Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`.

## Relationships

- **Conforms To**: [NotificationCenter.MainActorMessage](../../foundation/notificationcenter/mainactormessage.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](didsavemessage/context.md)
- [deleted](didsavemessage/deleted.md) — Managed objects that were deleted during this save.
- [historyToken](didsavemessage/historytoken.md)
- [inserted](didsavemessage/inserted.md) — Managed objects that were inserted during this save.
- [queryGeneration](didsavemessage/querygeneration.md) — Query generation token after the save.
- [updated](didsavemessage/updated.md) — Managed objects that were updated during this save.
