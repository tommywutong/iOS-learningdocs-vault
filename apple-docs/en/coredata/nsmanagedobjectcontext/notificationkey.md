---
title: NSManagedObjectContext.NotificationKey
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 3.0+, macOS 10.4+, tvOS 3.0+, visionOS, watchOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontext/notificationkey
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontext/notificationkey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontext/notificationkey.json'
content_hash: 'sha256:b5d93ec45b24dd94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSManagedObjectContext](../nsmanagedobjectcontext.md)

# NSManagedObjectContext.NotificationKey

<sub>Enumeration</sub>

Keys to access details in user info dictionaries of managed object context notifications.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NotificationKey
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md)

## Topics

### Constants

- [NSManagedObjectContext.NotificationKey.deletedObjectIDs](notificationkey/deletedobjectids.md) — A key for the set of deleted object identifiers.
- [NSManagedObjectContext.NotificationKey.deletedObjects](notificationkey/deletedobjects.md) — A key for the context’s set of deleted objects.
- [NSManagedObjectContext.NotificationKey.insertedObjectIDs](notificationkey/insertedobjectids.md) — A key for the set of inserted object identifiers.
- [NSManagedObjectContext.NotificationKey.insertedObjects](notificationkey/insertedobjects.md) — A key for the context’s set of inserted objects.
- [NSManagedObjectContext.NotificationKey.invalidatedAllObjects](notificationkey/invalidatedallobjects.md) — A key for the context’s set of all invalidated objects.
- [NSManagedObjectContext.NotificationKey.invalidatedObjectIDs](notificationkey/invalidatedobjectids.md) — A key for the set of invalidated object identifiers.
- [NSManagedObjectContext.NotificationKey.invalidatedObjects](notificationkey/invalidatedobjects.md) — A key for the context’s set of invalidated objects.
- [NSManagedObjectContext.NotificationKey.queryGeneration](notificationkey/querygeneration.md) — A key for the token that indicates which generation of the persistent store Core Data is accessing
- [NSManagedObjectContext.NotificationKey.refreshedObjectIDs](notificationkey/refreshedobjectids.md) — A key for the set of refreshed object identifiers.
- [NSManagedObjectContext.NotificationKey.refreshedObjects](notificationkey/refreshedobjects.md) — A key for the context’s set of refreshed objects.
- [NSManagedObjectContext.NotificationKey.updatedObjectIDs](notificationkey/updatedobjectids.md) — A key for the set of updated object identifiers.
- [NSManagedObjectContext.NotificationKey.updatedObjects](notificationkey/updatedobjects.md) — A key for the context’s set of updated objects.

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
- [didMergeChangesObjectIDsNotification](didmergechangesobjectidsnotification.md) — A notification that posts after a context finishes merging changes from another notification.
- [didSaveObjectIDsNotification](didsaveobjectidsnotification.md) — A notification that posts after a context finishes saving changes to its managed objects.
