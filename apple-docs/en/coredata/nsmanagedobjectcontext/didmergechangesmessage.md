---
title: NSManagedObjectContext.DidMergeChangesMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didmergechangesmessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didmergechangesmessage.json'
content_hash: 'sha256:520f6a442d5b7435'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.DidMergeChangesMessage

<sub>Structure</sub>

Posted after a main queue context merges changes from another context, containing object IDs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidMergeChangesMessage
```

## Overview

Only use this message type for contexts with `NSMainQueueConcurrencyType`. For private queue contexts, use [DidMergeChangesAsyncMessage](didmergechangesasyncmessage.md).

## Relationships

- **Conforms To**: [NotificationCenter.MainActorMessage](../../foundation/notificationcenter/mainactormessage.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](didmergechangesmessage/context.md)
- [deletedIDs](didmergechangesmessage/deletedids.md) — Object IDs of objects that were deleted during the merge.
- [historyToken](didmergechangesmessage/historytoken.md) — The persistent history token representing the state after the merge.
- [insertedIDs](didmergechangesmessage/insertedids.md) — Object IDs of objects that were inserted during the merge.
- [invalidatedIDs](didmergechangesmessage/invalidatedids.md) — Object IDs of objects that were invalidated during the merge.
- [queryGeneration](didmergechangesmessage/querygeneration.md) — Query generation token after the merge.
- [refreshedIDs](didmergechangesmessage/refreshedids.md) — Object IDs of objects that were refreshed during the merge.
- [updatedIDs](didmergechangesmessage/updatedids.md) — Object IDs of objects that were updated during the merge.
