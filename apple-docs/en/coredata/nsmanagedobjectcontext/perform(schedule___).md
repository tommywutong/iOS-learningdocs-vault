---
title: 'perform(schedule:_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/perform(schedule:_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(schedule:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/perform%28schedule%3A_%3A%29.json'
content_hash: 'sha256:a04a43d61a013db2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# perform(schedule:_:)

<sub>Instance Method</sub>

Submits a closure to the context’s queue for asynchronous execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated func perform<T>(schedule: NSManagedObjectContext.ScheduledTaskType = .immediate, _ block: @escaping @Sendable () throws -> T) async rethrows -> T
```

## Parameters

- `schedule` — The required execution schedule. For more information, see [ScheduledTaskType](scheduledtasktype.md).

- `block` — The closure to perform.

## See Also

### Performing block operations

- [- performBlock:](<perform(__).md>) — Asynchronously performs the specified closure on the context’s queue.
- [- performBlockAndWait:](<performandwait(__)-ypye.md>) — Synchronously performs the specified closure on the context’s queue.
- [performAndWait(_:)](<performandwait(__)-6aaf1.md>) — Submits a closure to the context’s queue for synchronous execution.
- [ScheduledTaskType](scheduledtasktype.md) — The different types of scheduled tasks.
