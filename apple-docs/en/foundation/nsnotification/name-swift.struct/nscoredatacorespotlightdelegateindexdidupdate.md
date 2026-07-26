---
title: NSCoreDataCoreSpotlightDelegateIndexDidUpdate
framework: Foundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/foundation/nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate
source_url: 'https://developer.apple.com/documentation/foundation/nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsnotification/name-swift.struct/nscoredatacorespotlightdelegateindexdidupdate.json'
content_hash: 'sha256:bdf10656dfe57a4e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Foundation](../../../foundation.md) · [NSNotification](../../nsnotification.md) · [Name](../name-swift.struct.md)

# NSCoreDataCoreSpotlightDelegateIndexDidUpdate

<sub>Type Property</sub>

A notification that posts after Spotlight completes an index update.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
static let NSCoreDataCoreSpotlightDelegateIndexDidUpdate: NSNotification.Name
```

## Discussion

This notification’s `object` is the Core Spotlight delegate. The framework posts the notification to a private thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains the persistent store’s unique identifier and the most recent history token, which you access with the [NSStoreUUIDKey](../../../coredata/nsstoreuuidkey.md) and [NSPersistentHistoryTokenKey](../../../coredata/nspersistenthistorytokenkey.md) keys. It’s safe to capture the dictionary’s contents.

## See Also

### Core Data

- [NSManagedObjectContextDidSave](nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [NSManagedObjectContextObjectsDidChange](nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [NSManagedObjectContextWillSave](nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSPersistentStoreCoordinatorStoresDidChange](nspersistentstorecoordinatorstoresdidchange.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChange](nspersistentstorecoordinatorstoreswillchange.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStore](nspersistentstorecoordinatorwillremovestore.md) — A notification that posts before a coordinator removes a store.
- [NSManagedObjectContextDidMergeChangesObjectIDs](nsmanagedobjectcontextdidmergechangesobjectids.md) — A notification that posts after a context merges changes from a different notification.
- [NSManagedObjectContextDidSaveObjectIDs](nsmanagedobjectcontextdidsaveobjectids.md) — A notification that posts after a context finishes writing changes.
- [NSPersistentStoreRemoteChange](nspersistentstoreremotechange.md) — A notification that posts after another process writes to a persistent store.
- [NSPersistentStoreDidImportUbiquitousContentChanges](nspersistentstoredidimportubiquitouscontentchanges.md) — Posted after records are imported from the ubiquitous content store. _(deprecated)_
