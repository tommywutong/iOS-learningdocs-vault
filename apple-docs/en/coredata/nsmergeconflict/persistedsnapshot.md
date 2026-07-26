---
title: persistedSnapshot
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict/persistedsnapshot
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/persistedsnapshot'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/persistedsnapshot.json'
content_hash: 'sha256:f24d32470d5982b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# persistedSnapshot

<sub>Instance Property</sub>

A dictionary containing the values of the source object held in the persistent store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var persistedSnapshot: [String : Any]? { get }
```

## See Also

### Accessing Merge Conflict Details

- [sourceObject](sourceobject.md) — The source object for the conflict.
- [objectSnapshot](objectsnapshot.md) — A dictionary containing the values of the source object.
- [cachedSnapshot](cachedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [newVersionNumber](newversionnumber.md) — The new version number for the change.
- [oldVersionNumber](oldversionnumber.md) — The old version number for the change.
