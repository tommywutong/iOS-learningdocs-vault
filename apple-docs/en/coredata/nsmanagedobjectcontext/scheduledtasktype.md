---
title: NSManagedObjectContext.ScheduledTaskType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/scheduledtasktype
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype.json'
content_hash: 'sha256:e9b7b41eacccd4a9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.ScheduledTaskType

<sub>Enumeration</sub>

The different types of scheduled tasks.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum ScheduledTaskType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md)

## Topics

### Scheduled Task Types

- [NSManagedObjectContext.ScheduledTaskType.enqueued](scheduledtasktype/enqueued.md) — The enqueued scheduled task type.
- [NSManagedObjectContext.ScheduledTaskType.immediate](scheduledtasktype/immediate.md) — The immediate scheduled task type.

## See Also

### Performing block operations

- [- performBlock:](<perform(__).md>) — Asynchronously performs the specified closure on the context’s queue.
- [perform(schedule:_:)](<perform(schedule___).md>) — Submits a closure to the context’s queue for asynchronous execution.
- [- performBlockAndWait:](<performandwait(__)-ypye.md>) — Synchronously performs the specified closure on the context’s queue.
- [performAndWait(_:)](<performandwait(__)-6aaf1.md>) — Submits a closure to the context’s queue for synchronous execution.
