---
title: NSManagedObjectContext.ScheduledTaskType.immediate
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/immediate
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/immediate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/scheduledtasktype/immediate.json'
content_hash: 'sha256:742409988cd01380'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Core Data](../../../coredata.md) · [NSManagedObjectContext](../../nsmanagedobjectcontext.md) · [ScheduledTaskType](../scheduledtasktype.md)

# NSManagedObjectContext.ScheduledTaskType.immediate

<sub>Case</sub>

The immediate scheduled task type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
case immediate
```

## Discussion

Immediate tasks execute right away if the context operates within the current scope; otherwise, the context enqueues the task. Tasks of this type are reentrant, nonblocking, and continuation-aware.

## See Also

### Scheduled Task Types

- [NSManagedObjectContext.ScheduledTaskType.enqueued](enqueued.md) — The enqueued scheduled task type.
