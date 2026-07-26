---
title: 'performAndWait(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-ypye'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/performandwait(_:)-ypye'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/performandwait%28_%3A%29-ypye.json'
content_hash: 'sha256:07f4cc34a6d0292d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# performAndWait(_:)

<sub>Instance Method</sub>

Synchronously performs the specified closure on the context’s queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performAndWait(_ block: @Sendable () -> Void)
```

## Parameters

- `block` — The closure to perform.

## Discussion

This method supports _reentrancy_ — meaning it’s safe to call the method again, from within the closure, before the previous invocation completes.

## See Also

### Performing block operations

- [- performBlock:](<perform(__).md>) — Asynchronously performs the specified closure on the context’s queue.
- [perform(schedule:_:)](<perform(schedule___).md>) — Submits a closure to the context’s queue for asynchronous execution.
- [performAndWait(_:)](<performandwait(__)-6aaf1.md>) — Submits a closure to the context’s queue for synchronous execution.
- [ScheduledTaskType](scheduledtasktype.md) — The different types of scheduled tasks.
