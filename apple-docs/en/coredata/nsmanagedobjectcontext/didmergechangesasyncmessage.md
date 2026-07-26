---
title: NSManagedObjectContext.DidMergeChangesAsyncMessage
framework: Core Data
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta, watchOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didmergechangesasyncmessage
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesasyncmessage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didmergechangesasyncmessage.json'
content_hash: 'sha256:d4686e89698cca9b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.DidMergeChangesAsyncMessage

<sub>Structure</sub>

Posted after a private queue context merges changes from another context, containing object IDs.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct DidMergeChangesAsyncMessage
```

## Overview

Only use this message type for contexts with `NSPrivateQueueConcurrencyType`. For main queue contexts, use [DidMergeChangesMessage](didmergechangesmessage.md).

## Relationships

- **Conforms To**: [NotificationCenter.AsyncMessage](../../foundation/notificationcenter/asyncmessage.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Instance Properties

- [context](didmergechangesasyncmessage/context.md)
- [deletedIDs](didmergechangesasyncmessage/deletedids.md) — Object IDs of objects that were deleted during the merge.
- [historyToken](didmergechangesasyncmessage/historytoken.md) — The persistent history token representing the state after the merge.
- [insertedIDs](didmergechangesasyncmessage/insertedids.md) — Object IDs of objects that were inserted during the merge.
- [invalidatedIDs](didmergechangesasyncmessage/invalidatedids.md) — Object IDs of objects that were invalidated during the merge.
- [queryGeneration](didmergechangesasyncmessage/querygeneration.md) — Query generation token after the merge.
- [refreshedIDs](didmergechangesasyncmessage/refreshedids.md) — Object IDs of objects that were refreshed during the merge.
- [updatedIDs](didmergechangesasyncmessage/updatedids.md) — Object IDs of objects that were updated during the merge.
