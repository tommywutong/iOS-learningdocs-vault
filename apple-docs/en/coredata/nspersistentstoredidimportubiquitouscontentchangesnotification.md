---
title: NSPersistentStoreDidImportUbiquitousContentChangesNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoredidimportubiquitouscontentchangesnotification.json'
content_hash: 'sha256:f09de072f5d0f293'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreDidImportUbiquitousContentChangesNotification

<sub>Global Variable</sub>

Posted after records are imported from the ubiquitous content store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```objc
extern NSString * const NSPersistentStoreDidImportUbiquitousContentChangesNotification;
```

## Discussion

The notification’s `object` is set to the `NSPersistentStoreCoordinator` instance which registered the store. The notification’s `userInfo` dictionary contains the same keys as the [NSManagedObjectContextObjectsDidChangeNotification](nsmanagedobjectcontextobjectsdidchangenotification.md) notification ([NSInsertedObjectsKey](nsinsertedobjectskey.md), [NSUpdatedObjectsKey](nsupdatedobjectskey.md), [NSDeletedObjectsKey](nsdeletedobjectskey.md)), however the values are sets of [NSManagedObjectID](nsmanagedobjectid.md) objects rather than sets of [NSManagedObject](nsmanagedobject.md) objects.
