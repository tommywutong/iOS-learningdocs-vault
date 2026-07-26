---
title: NSPersistentStoreConnectionPoolMaxSizeKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.12+, tvOS 10.0+, visionOS 1.0+, watchOS 3.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoreconnectionpoolmaxsizekey
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreconnectionpoolmaxsizekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreconnectionpoolmaxsizekey.json'
content_hash: 'sha256:5ac2fe06a583d3c4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreConnectionPoolMaxSizeKey

<sub>Global Variable</sub>

The maximum connection pool size to use on a store that supports concurrent request handling.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSPersistentStoreConnectionPoolMaxSizeKey: String
```

## Discussion

Values that you specify for this key are of type [NSNumber](../foundation/nsnumber.md). The connection pool size determines the number of requests a store can handle concurrently, and is a function of how many contexts attempt to access store data at any time. Generally, you don’t set this, and use the default value instead.

The default connection pool size is implementation-dependent and may vary by store type or platform.

## See Also

### Constants

- [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md) — Key for the array of stores that were added.
- [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) — Key for the array of stores that were removed.
- [NSUUIDChangedPersistentStoresKey](nsuuidchangedpersistentstoreskey.md) — Key for an array containing the old and new stores.
- [NSPersistentStoreSaveConflictsErrorKey](nspersistentstoresaveconflictserrorkey.md) — The key for the array of merge conflict objects (instances of [NSMergeConflict](nsmergeconflict.md)).
- [NSPersistentStoreUbiquitousTransitionTypeKey](nspersistentstoreubiquitoustransitiontypekey.md) _(deprecated)_
