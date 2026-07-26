---
title: Notification keys
framework: Core Data
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/notification-keys
source_url: 'https://developer.apple.com/documentation/coredata/notification-keys'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/notification-keys.json'
content_hash: 'sha256:93dcd075e012d669'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md) · [Core Data stack](core-data-stack.md) · [NSPersistentStoreCoordinator](nspersistentstorecoordinator.md)

# Notification keys

<sub>API Collection</sub>

The keys you use to retrieve values from a notification’s user info dictionary.

## Topics

### Constants

- [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md) — Key for the array of stores that were added.
- [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) — Key for the array of stores that were removed.
- [NSUUIDChangedPersistentStoresKey](nsuuidchangedpersistentstoreskey.md) — Key for an array containing the old and new stores.
- [NSPersistentStoreConnectionPoolMaxSizeKey](nspersistentstoreconnectionpoolmaxsizekey.md) — The maximum connection pool size to use on a store that supports concurrent request handling.
- [NSPersistentStoreSaveConflictsErrorKey](nspersistentstoresaveconflictserrorkey.md) — The key for the array of merge conflict objects (instances of [NSMergeConflict](nsmergeconflict.md)).
- [NSPersistentStoreUbiquitousTransitionTypeKey](nspersistentstoreubiquitoustransitiontypekey.md) _(deprecated)_

## See Also

### Responding to changes of the coordinator’s registered stores

- [NSPersistentStoreCoordinatorStoresWillChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorStoresDidChange](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorWillRemoveStore](../foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
