---
title: 'perform(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsmanagedobjectcontext/perform(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/perform(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/perform%28_%3A%29.json'
content_hash: 'sha256:08e71431ed09d77f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# perform(_:)

<sub>Instance Method</sub>

Asynchronously performs the specified closure on the context’s queue.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func perform(_ block: @escaping @Sendable () -> Void)
```

## Parameters

- `block` — The closure to perform.

## Discussion

This method encapsulates an autorelease pool and a call to [- processPendingChanges](<processpendingchanges().md>).

## See Also

### Performing block operations

- [perform(schedule:_:)](<perform(schedule___).md>) — Submits a closure to the context’s queue for asynchronous execution.
- [- performBlockAndWait:](<performandwait(__)-ypye.md>) — Synchronously performs the specified closure on the context’s queue.
- [performAndWait(_:)](<performandwait(__)-6aaf1.md>) — Submits a closure to the context’s queue for synchronous execution.
- [ScheduledTaskType](scheduledtasktype.md) — The different types of scheduled tasks.
