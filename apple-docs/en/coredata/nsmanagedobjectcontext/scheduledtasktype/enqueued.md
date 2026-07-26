---
title: NSManagedObjectContext.ScheduledTaskType.enqueued
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/enqueued
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/enqueued'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/enqueued.json'
content_hash: 'sha256:fcaf6259ba3f6c52'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSManagedObjectContext](../../nsmanagedobjectcontext.md) · [ScheduledTaskType](../scheduledtasktype.md)

# NSManagedObjectContext.ScheduledTaskType.enqueued

<sub>Case</sub>

The enqueued scheduled task type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case enqueued
```

## Discussion

Enqueued tasks execute asynchronously on the context’s queue. An enqueued task encapsulates an autorelease pool and a call to [- processPendingChanges](<../processpendingchanges().md>), and its behavior is analogous to [- performBlock:](<../perform(__).md>). The context’s queue executes tasks in the order you add them.

## See Also

### Scheduled Task Types

- [NSManagedObjectContext.ScheduledTaskType.immediate](immediate.md) — The immediate scheduled task type.
