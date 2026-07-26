---
title: progress
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.10+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreasynchronousresult/progress
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreasynchronousresult/progress'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreasynchronousresult/progress.json'
content_hash: 'sha256:c35a3d6dfffd6fd5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreAsynchronousResult](../nspersistentstoreasynchronousresult.md)

# progress

<sub>Instance Property</sub>

An object that reports progress for the asynchronous fetch request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var progress: Progress? { get }
```

## See Also

### Inspecting the Result

- [managedObjectContext](managedobjectcontext.md) — The managed object context for the result.
- [operationError](operationerror.md) — An error that contains details if the asynchronous fetch request fails.
