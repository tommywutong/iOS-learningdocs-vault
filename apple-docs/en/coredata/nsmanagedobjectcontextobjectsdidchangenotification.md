---
title: NSManagedObjectContextObjectsDidChangeNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsmanagedobjectcontextobjectsdidchangenotification
source_url: 'https://developer.apple.com/documentation/coredata/nsmanagedobjectcontextobjectsdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsmanagedobjectcontextobjectsdidchangenotification.json'
content_hash: 'sha256:eb4b3cd5d6ab060c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSManagedObjectContextObjectsDidChangeNotification

<sub>Global Variable</sub>

A notification that posts when there are changes to context’s registered managed objects.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSManagedObjectContextObjectsDidChangeNotification;
```

## Discussion

> [!note] Note
> This notification posts only when there are changes to the context’s registered managed objects. It doesn’t post when a fetch adds managed objects to the context.

This notification’s `object` property is the changed managed object context. Don’t peform any asynchronous work or block the calling thread. [NSManagedObjectContext](nsmanagedobjectcontext.md) posts notifications to the same thread that creates it.

The `userInfo` dictionary contains the inserted, updated, deleted, and invalidated managed objects. For the keys to access those objects, see [NotificationKey](nsmanagedobjectcontext/notificationkey.md). Don’t capture the dictionary’s contents.
