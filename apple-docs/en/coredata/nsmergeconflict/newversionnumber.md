---
title: newVersionNumber
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict/newversionnumber
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/newversionnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/newversionnumber.json'
content_hash: 'sha256:1ac173a49e199662'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# newVersionNumber

<sub>Instance Property</sub>

The new version number for the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var newVersionNumber: Int { get }
```

## Discussion

A new version number of 0 means the object was deleted and the corresponding snapshot is `nil`.

## See Also

### Accessing Merge Conflict Details

- [sourceObject](sourceobject.md) — The source object for the conflict.
- [objectSnapshot](objectsnapshot.md) — A dictionary containing the values of the source object.
- [cachedSnapshot](cachedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [persistedSnapshot](persistedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store.
- [oldVersionNumber](oldversionnumber.md) — The old version number for the change.
