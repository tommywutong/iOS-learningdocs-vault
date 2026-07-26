---
title: 'performAndWait(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-6aaf1'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-6aaf1'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/performandwait%28_%3A%29-6aaf1.json'
content_hash: 'sha256:94871350c098b099'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# performAndWait(_:)

<sub>Instance Method</sub>

Submits a closure to the context’s queue for synchronous execution.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency nonisolated func performAndWait<T>(_ block: @Sendable () throws -> T) rethrows -> T
```

## Parameters

- `block` — The closure to perform.

## Discussion

This method supports _reentrancy_ — meaning it’s safe to call the method again, from within the closure, before the previous invocation completes.

## See Also

### Performing block operations

- [- performBlock:](<perform(__).md>) — Asynchronously performs the specified closure on the context’s queue.
- [perform(schedule:_:)](<perform(schedule___).md>) — Submits a closure to the context’s queue for asynchronous execution.
- [- performBlockAndWait:](<performandwait(__)-ypye.md>) — Synchronously performs the specified closure on the context’s queue.
- [ScheduledTaskType](scheduledtasktype.md) — The different types of scheduled tasks.
