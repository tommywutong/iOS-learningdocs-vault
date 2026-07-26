---
title: NSUUIDChangedPersistentStoresKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsuuidchangedpersistentstoreskey
source_url: 'https://developer.apple.com/documentation/coredata/nsuuidchangedpersistentstoreskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsuuidchangedpersistentstoreskey.json'
content_hash: 'sha256:0277c389d4930680'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSUUIDChangedPersistentStoresKey

<sub>Global Variable</sub>

Key for an array containing the old and new stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSUUIDChangedPersistentStoresKey: String
```

## Discussion

The object at index `0` is the old store instance, and the object at index `1` the new. When migration happens, the array contains a third object (at index `2`) that is an array containing the new objectIDs for all the migrated objects.

## See Also

### Constants

- [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md) — Key for the array of stores that were added.
- [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) — Key for the array of stores that were removed.
- [NSPersistentStoreConnectionPoolMaxSizeKey](nspersistentstoreconnectionpoolmaxsizekey.md) — The maximum connection pool size to use on a store that supports concurrent request handling.
- [NSPersistentStoreSaveConflictsErrorKey](nspersistentstoresaveconflictserrorkey.md) — The key for the array of merge conflict objects (instances of [NSMergeConflict](nsmergeconflict.md)).
- [NSPersistentStoreUbiquitousTransitionTypeKey](nspersistentstoreubiquitoustransitiontypekey.md) _(deprecated)_
