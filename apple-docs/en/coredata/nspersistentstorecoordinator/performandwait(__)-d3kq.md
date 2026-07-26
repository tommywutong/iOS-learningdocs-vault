---
title: 'performAndWait(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift, occ, occ]
beta: false
deprecated: true
doc_path: '/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-d3kq'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/performandwait(_:)-d3kq'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/performandwait%28_%3A%29-d3kq.json'
content_hash: 'sha256:7a68ebf56d8e564c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# performAndWait(_:)

<sub>Instance Method</sub>

Executes the provided closure on the coordinator’s queue and waits for it to finish.

> [!warning] Deprecated
> Use [performAndWait(_:)](<performandwait(__)-15ude.md>) instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func performAndWait(_ block: @Sendable () -> Void)
```

## Parameters

- `block` — The closure to execute.

## See Also

### Performing tasks

- [perform(_:)](<perform(__)-74udx.md>) — Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [performAndWait(_:)](<performandwait(__)-15ude.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- executeRequest:withContext:error:](<execute(__with_).md>) — Executes the specified request on each of the coordinator’s persistent stores.
