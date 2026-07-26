---
title: sourceObject
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict/sourceobject
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/sourceobject'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/sourceobject.json'
content_hash: 'sha256:800e9ba92d520518'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# sourceObject

<sub>Instance Property</sub>

The source object for the conflict.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var sourceObject: NSManagedObject { get }
```

## See Also

### Accessing Merge Conflict Details

- [objectSnapshot](objectsnapshot.md) — A dictionary containing the values of the source object.
- [cachedSnapshot](cachedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [persistedSnapshot](persistedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store.
- [newVersionNumber](newversionnumber.md) — The new version number for the change.
- [oldVersionNumber](oldversionnumber.md) — The old version number for the change.
