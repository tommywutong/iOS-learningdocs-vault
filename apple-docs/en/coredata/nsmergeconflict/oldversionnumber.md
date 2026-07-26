---
title: oldVersionNumber
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 13.1+, macOS 10.7+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmergeconflict/oldversionnumber
source_url: 'https://developer.apple.com/documentation/coredata/nsmergeconflict/oldversionnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmergeconflict/oldversionnumber.json'
content_hash: 'sha256:cdecf7e81846a5e2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSMergeConflict](../nsmergeconflict.md)

# oldVersionNumber

<sub>Instance Property</sub>

The old version number for the change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var oldVersionNumber: Int { get }
```

## See Also

### Accessing Merge Conflict Details

- [sourceObject](sourceobject.md) — The source object for the conflict.
- [objectSnapshot](objectsnapshot.md) — A dictionary containing the values of the source object.
- [cachedSnapshot](cachedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store coordinator layer.
- [persistedSnapshot](persistedsnapshot.md) — A dictionary containing the values of the source object held in the persistent store.
- [newVersionNumber](newversionnumber.md) — The new version number for the change.
