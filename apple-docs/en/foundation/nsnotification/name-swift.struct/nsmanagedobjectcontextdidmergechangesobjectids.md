---
title: NSManagedObjectContextDidMergeChangesObjectIDs
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidmergechangesobjectids.json'
content_hash: 'sha256:80b0549cd3d1b4f2'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSManagedObjectContextDidMergeChangesObjectIDs

<sub>Type Property</sub>

A notification that posts after a context merges changes from a different notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSManagedObjectContextDidMergeChangesObjectIDs: NSNotification.Name
```

## Discussion

This notification’s `object` is the merged context. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](../../../coredata/nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, refreshed, and invalidated managed objects. For the keys to access those objects, see [NSManagedObjectContext.NotificationKey](../../../coredata/nsmanagedobjectcontext/notificationkey.md). It’s safe to capture the dictionary’s contents.

## See Also

### Core Data

- [NSManagedObjectContextDidSave](nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSManagedObjectContextWillSave](nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSPersistentStoreCoordinatorStoresDidChange](nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChange](nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSCoreDataCoreSpotlightDelegateIndexDidUpdate](nscoredatacorespotlightdelegateindexdidupdate.md) — A notification that posts after Spotlight completes an index update.
- [NSManagedObjectContextDidSaveObjectIDs](nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
- [NSPersistentStoreDidImportUbiquitousContentChanges](nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_
