---
title: 'perform(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 15.0+, visionOS, watchOS 8.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/perform(_:)-74udx'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/perform(_:)-74udx'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/perform%28_%3A%29-74udx.json'
content_hash: 'sha256:3fd0bad42d6be7e8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# perform(_:)

<sub>Instance Method</sub>

Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency func perform<T>(_ block: @escaping @Sendable () throws -> T) async rethrows -> T
```

## Parameters

- `block` — The closure to execute.

## See Also

### Performing tasks

- [performAndWait(_:)](<performandwait(__)-15ude.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
- [- executeRequest:withContext:error:](<execute(__with_).md>) — Executes the specified request on each of the coordinator’s persistent stores.
