---
title: NSPersistentStoreDidImportUbiquitousContentChanges
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, swift]
beta: false
deprecated: true
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nspersistentstoredidimportubiquitouscontentchanges.json'
content_hash: 'sha256:e49987367f5a1208'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSPersistentStoreDidImportUbiquitousContentChanges

<sub>Type Property</sub>

Posted after records are imported from the ubiquitous content store.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let NSPersistentStoreDidImportUbiquitousContentChanges: NSNotification.Name
```

## Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator` instance which registered the store. The notification’s `userInfo` dictionary contains the same keys as the [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) notification ([NSInsertedObjectsKey](../../../coredata/nsinsertedobjectskey.md), [NSUpdatedObjectsKey](../../../coredata/nsupdatedobjectskey.md)[NSDeletedObjectsKey](../../../coredata/nsdeletedobjectskey.md)), however the values are sets of [NSManagedObjectID](../../../coredata/nsmanagedobjectid.md) objects rather than sets of [NSManagedObject](../../../coredata/nsmanagedobject.md) objects.

## See Also

### Core Data

- [NSManagedObjectContextDidSave](nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSManagedObjectContextWillSave](nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSPersistentStoreCoordinatorStoresDidChange](nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChange](nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSCoreDataCoreSpotlightDelegateIndexDidUpdate](nscoredatacorespotlightdelegateindexdidupdate.md) — A notification that posts after Spotlight completes an index update.
- [NSManagedObjectContextDidMergeChangesObjectIDs](nsmanagedobjectcontextdidmergechangesobjectids.md) — A notification that posts after a context merges changes from a different notification.
- [NSManagedObjectContextDidSaveObjectIDs](nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
