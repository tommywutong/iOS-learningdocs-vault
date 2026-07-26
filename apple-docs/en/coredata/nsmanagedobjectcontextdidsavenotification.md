---
title: NSManagedObjectContextDidSaveNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextdidsavenotification
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsavenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextdidsavenotification.json'
content_hash: 'sha256:cc48ce2e67c6f933'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextDidSaveNotification

<sub>Global Variable</sub>

A notification that posts after a context finishes writing unsaved changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSManagedObjectContextDidSaveNotification;
```

## Discussion

> [!important] Important
> Use [NSManagedObjectContextDidSaveObjectIDsNotification](nsmanagedobjectcontextdidsaveobjectidsnotification.md) instead of this notification.

This notification’s `object` is the saved context. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the inserted, updated, and deleted managed objects of the completed save. For the keys to access those objects, see [NotificationKey](nsmanagedobjectcontext/notificationkey.md). Don’t capture the dictionary’s contents.

To safely use the provided managed objects on the current thread, create a new context and use its [- mergeChangesFromContextDidSaveNotification:](<nsmanagedobjectcontext/mergechanges(fromcontextdidsave_).md>) method to merge in the notification’s changes.
