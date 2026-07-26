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
doc_path: '/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-15ude'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-15ude'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/performandwait%28_%3A%29-15ude.json'
content_hash: 'sha256:72ddbadada8dff43'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# performAndWait(_:)

<sub>Instance Method</sub>

Executes the provided closure on the coordinator’s queue and waits for it to finish.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func performAndWait<T>(_ block: @Sendable () throws -> T) rethrows -> T
```

## Parameters

- `block` — The closure to execute.

## See Also

### Performing tasks

- [perform(_:)](<perform(__)-74udx.md>) — Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
- [- executeRequest:withContext:error:](<execute(__with_).md>) — Executes the specified request on each of the coordinator’s persistent stores.
