---
title: didMergeChangesObjectIDsNotification
framework: Core Data
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 10.3+, macOS 10.12+, tvOS 10.2+, visionOS, watchOS 3.2+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/didmergechangesobjectidsnotification
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/didmergechangesobjectidsnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/didmergechangesobjectidsnotification.json'
content_hash: 'sha256:cfca0c034ef743f2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# didMergeChangesObjectIDsNotification

<sub>Type Property</sub>

A notification that posts after a context finishes merging changes from another notification.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static let didMergeChangesObjectIDsNotification: Notification.Name
```

## Discussion

This notification’s `object` is the merged context. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](../nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, refreshed, and invalidated managed objects. For the keys to access those objects, see [NotificationKey](notificationkey.md). It’s safe to capture the dictionary’s contents.

## See Also

### Managing notifications

- [didChangeObjectsNotification](didchangeobjectsnotification.md) — A notification that posts when a context makes changes to its registered objects.
- [NSManagedObjectContextObjectsDidChange](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [didSaveObjectsNotification](didsaveobjectsnotification.md) — A notification that posts after a context completes a save.
- [NSManagedObjectContextDidSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [willSaveObjectsNotification](willsaveobjectsnotification.md) — A notification that posts before a context writes pending changes to disk.
- [NSManagedObjectContextWillSave](../../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSInsertedObjectsKey](../nsinsertedobjectskey.md) — A key for the set of objects that were inserted into the context.
- [NSUpdatedObjectsKey](../nsupdatedobjectskey.md) — A key for the set of objects that were updated.
- [NSDeletedObjectsKey](../nsdeletedobjectskey.md) — A key for the set of objects that were marked for deletion during the previous event.
- [NSRefreshedObjectsKey](../nsrefreshedobjectskey.md) — A key for the set of objects that were refreshed but were not dirtied in the scope of this context.
- [NSInvalidatedObjectsKey](../nsinvalidatedobjectskey.md) — A key for the set of objects that were invalidated.
- [NSInvalidatedAllObjectsKey](../nsinvalidatedallobjectskey.md) — A key that specifies that all objects in the context have been invalidated.
- [didSaveObjectIDsNotification](didsaveobjectidsnotification.md) — A notification that posts after a context finishes saving changes to its managed objects.
- [NotificationKey](notificationkey.md) — Keys to access details in user info dictionaries of managed object context notifications.
