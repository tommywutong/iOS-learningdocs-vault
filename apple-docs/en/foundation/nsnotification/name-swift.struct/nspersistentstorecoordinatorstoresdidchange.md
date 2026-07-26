---
title: NSPersistentStoreCoordinatorStoresDidChange
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nspersistentstorecoordinatorstoresdidchange.json'
content_hash: 'sha256:c777825867b4ebe1'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSPersistentStoreCoordinatorStoresDidChange

<sub>Type Property</sub>

A notification that the coordinator posts after its registered stores change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSPersistentStoreCoordinatorStoresDidChange: NSNotification.Name
```

## Discussion

This notification’s `object` is the changed store coordinator. The framework posts the notification to an internal thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains information about the added, updated, and removed persistent stores, which you access with the [NSAddedPersistentStoresKey](../../../coredata/nsaddedpersistentstoreskey.md), [NSUUIDChangedPersistentStoresKey](../../../coredata/nsuuidchangedpersistentstoreskey.md), and [NSRemovedPersistentStoresKey](../../../coredata/nsremovedpersistentstoreskey.md) keys. Don’t capture the dictionary’s contents.

## See Also

### Core Data

- [NSManagedObjectContextDidSave](nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSManagedObjectContextWillSave](nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSPersistentStoreCoordinatorStoresWillChange](nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSCoreDataCoreSpotlightDelegateIndexDidUpdate](nscoredatacorespotlightdelegateindexdidupdate.md) — A notification that posts after Spotlight completes an index update.
- [NSManagedObjectContextDidMergeChangesObjectIDs](nsmanagedobjectcontextdidmergechangesobjectids.md) — A notification that posts after a context merges changes from a different notification.
- [NSManagedObjectContextDidSaveObjectIDs](nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
- [NSPersistentStoreDidImportUbiquitousContentChanges](nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_
