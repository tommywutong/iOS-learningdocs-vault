---
title: cachedSnapshot
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict/cachedsnapshot
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/cachedsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/cachedsnapshot.json'
content_hash: 'sha256:5f43f733f480f4c7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# cachedSnapshot

<sub>Instance Property</sub>

A dictionary containing the values of the source object held in the persistent store coordinator layer.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var cachedSnapshot: [String : Any]? { get }
```

## See Also

### Accessing Merge Conflict Details

- [sourceObject](sourceobject.md) — The source object for the conflict.
- [objectSnapshot](objectsnapshot.md) — A dictionary containing the values of the source object.
- [persistedSnapshot](persistedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store.
- [newVersionNumber](newversionnumber.md) — The new version number for the change.
- [oldVersionNumber](oldversionnumber.md) — The old version number for the change.
