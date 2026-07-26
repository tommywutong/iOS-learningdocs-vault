---
title: NSPersistentStoreUbiquitousTransitionTypeKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstoreubiquitoustransitiontypekey
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreubiquitoustransitiontypekey.json'
content_hash: 'sha256:7590d5cdfe4ebc9e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreUbiquitousTransitionTypeKey

<sub>Global Variable</sub>

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
let NSPersistentStoreUbiquitousTransitionTypeKey: String
```

## Description

In the [NSPersistentStoreCoordinatorStoresWillChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md) and [NSPersistentStoreCoordinatorStoresDidChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md) userInfo dictionaries, this identifies the type of event. The corresponding value is one of the [NSPersistentStoreUbiquitousTransitionType](nspersistentstoreubiquitoustransitiontype.md) enum values as an `NSNumber` object.

## See Also

### Constants

- [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md) — Key for the array of stores that were added.
- [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) — Key for the array of stores that were removed.
- [NSUUIDChangedPersistentStoresKey](nsuuidchangedpersistentstoreskey.md) — Key for an array containing the old and new stores.
- [NSPersistentStoreConnectionPoolMaxSizeKey](nspersistentstoreconnectionpoolmaxsizekey.md) — The maximum connection pool size to use on a store that supports concurrent request handling.
- [NSPersistentStoreSaveConflictsErrorKey](nspersistentstoresaveconflictserrorkey.md) — The key for the array of merge conflict objects (instances of [NSMergeConflict](nsmergeconflict.md)).
