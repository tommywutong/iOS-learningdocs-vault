---
title: NSManagedObjectContextDidSaveObjectIDsNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 10.3+, iPadOS 10.3+, Mac Catalyst 13.1+, macOS 10.12.4+, tvOS 10.2+, visionOS 1.0+, watchOS 3.2+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextdidsaveobjectidsnotification
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextdidsaveobjectidsnotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextdidsaveobjectidsnotification.json'
content_hash: 'sha256:0f957547d5e4d231'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextDidSaveObjectIDsNotification

<sub>Global Variable</sub>

A notification that posts after a context finishes writing changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSManagedObjectContextDidSaveObjectIDsNotification;
```

## Discussion

This notification’s `object` is the saved context. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the identifiers of the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [NotificationKey](nsmanagedobjectcontext/notificationkey.md). It’s safe to capture the dictionary’s contents.

Use this notification instead of [NSManagedObjectContextDidSaveNotification](nsmanagedobjectcontextdidsavenotification.md) if you intend to process the changed managed object on a different thread. It’s safe to pass instances of [NSManagedObjectID](nsmanagedobjectid.md) across thread boundaries.
