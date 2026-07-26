---
title: NSManagedObjectContextWillSave
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS 9.0+, visionOS 1.0+, watchOS 2.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.json'
content_hash: 'sha256:c866d387253deb67'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSManagedObjectContextWillSave

<sub>Type Property</sub>

A notification that posts before a context writes unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let NSManagedObjectContextWillSave: NSNotification.Name
```

## Discussion

This notification’s `object` is the context that’s about to save. Only use the notification to operate on the in-process save operation. For example, to insert additional managed objects. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](../../../coredata/nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

There is no `userInfo` dictionary.

## See Also

### Core Data

- [NSManagedObjectContextDidSave](nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSPersistentStoreCoordinatorStoresDidChange](nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChange](nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSCoreDataCoreSpotlightDelegateIndexDidUpdate](nscoredatacorespotlightdelegateindexdidupdate.md) — A notification that posts after Spotlight completes an index update.
- [NSManagedObjectContextDidMergeChangesObjectIDs](nsmanagedobjectcontextdidmergechangesobjectids.md) — A notification that posts after a context merges changes from a different notification.
- [NSManagedObjectContextDidSaveObjectIDs](nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
- [NSPersistentStoreDidImportUbiquitousContentChanges](nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_
