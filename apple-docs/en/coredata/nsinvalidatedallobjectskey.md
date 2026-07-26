---
title: NSInvalidatedAllObjectsKey
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsinvalidatedallobjectskey
source_url: 'https://developer.apple.com/documentation/coredata/nsinvalidatedallobjectskey'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsinvalidatedallobjectskey.json'
content_hash: 'sha256:fb83947ee0b27847'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSInvalidatedAllObjectsKey

<sub>Global Variable</sub>

A key that specifies that all objects in the context have been invalidated.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
let NSInvalidatedAllObjectsKey: String
```

## See Also

### Managing notifications

- [didChangeObjectsNotification](nsmanagedobjectcontext/didchangeobjectsnotification.md) — A notification that posts when a context makes changes to its registered objects.
- [NSManagedObjectContextObjectsDidChange](../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextobjectsdidchange.md) — A notification that posts when there are changes to context’s registered managed objects.
- [didSaveObjectsNotification](nsmanagedobjectcontext/didsaveobjectsnotification.md) — A notification that posts after a context completes a save.
- [NSManagedObjectContextDidSave](../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextdidsave.md) — A notification that posts after a context finishes writing unsaved changes.
- [willSaveObjectsNotification](nsmanagedobjectcontext/willsaveobjectsnotification.md) — A notification that posts before a context writes pending changes to disk.
- [NSManagedObjectContextWillSave](../foundation/nsnotification/name-swift.struct/nsmanagedobjectcontextwillsave.md) — A notification that posts before a context writes unsaved changes.
- [NSInsertedObjectsKey](nsinsertedobjectskey.md) — A key for the set of objects that were inserted into the context.
- [NSUpdatedObjectsKey](nsupdatedobjectskey.md) — A key for the set of objects that were updated.
- [NSDeletedObjectsKey](nsdeletedobjectskey.md) — A key for the set of objects that were marked for deletion during the previous event.
- [NSRefreshedObjectsKey](nsrefreshedobjectskey.md) — A key for the set of objects that were refreshed but were not dirtied in the scope of this context.
- [NSInvalidatedObjectsKey](nsinvalidatedobjectskey.md) — A key for the set of objects that were invalidated.
- [didMergeChangesObjectIDsNotification](nsmanagedobjectcontext/didmergechangesobjectidsnotification.md) — A notification that posts after a context finishes merging changes from another notification.
- [didSaveObjectIDsNotification](nsmanagedobjectcontext/didsaveobjectidsnotification.md) — A notification that posts after a context finishes saving changes to its managed objects.
- [NotificationKey](nsmanagedobjectcontext/notificationkey.md) — Keys to access details in user info dictionaries of managed object context notifications.
