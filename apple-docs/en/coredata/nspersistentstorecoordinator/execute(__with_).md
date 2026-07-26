---
title: 'execute(_:with:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstorecoordinator/execute(_:with:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/execute(_:with:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/execute%28_%3Awith%3A%29.json'
content_hash: 'sha256:16c03968fe4becc8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# execute(_:with:)

<sub>Instance Method</sub>

Executes the specified request on each of the coordinator’s persistent stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func execute(_ request: NSPersistentStoreRequest, with context: NSManagedObjectContext) throws -> Any
```

## Parameters

- `request` — A fetch or save request.

- `context` — The context against which `request` should be executed.

## Return Value

An array containing managed objects, managed object IDs, or dictionaries as appropriate for a fetch request; an empty array if `request` is a save request, or `nil` if an error occurred.

## Discussion

User defined requests return arrays of arrays, where a nested array is the result returned from a single store.

## See Also

### Performing tasks

- [perform(_:)](<perform(__)-74udx.md>) — Executes the provided closure asynchronously on the coordinator’s queue and awaits the result.
- [performAndWait(_:)](<performandwait(__)-15ude.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish.
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
