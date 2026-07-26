---
title: NSPersistentStoreCoordinatorWillRemoveStoreNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinatorwillremovestorenotification
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorwillremovestorenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinatorwillremovestorenotification.json'
content_hash: 'sha256:8d96c5db0332706d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreCoordinatorWillRemoveStoreNotification

<sub>Global Variable</sub>

A notification that posts before a coordinator removes a store.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSPersistentStoreCoordinatorWillRemoveStoreNotification;
```

## Discussion

This notification’s `object` is the changed store coordinator. The framework posts the notification to an internal thread. Don’t peform any asynchronous work or block the calling thread.

There is no `userInfo` dictionary.

## See Also

### Notifications

- [NSPersistentStoreCoordinatorStoresDidChangeNotification](nspersistentstorecoordinatorstoresdidchangenotification.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorStoresWillChangeNotification](nspersistentstorecoordinatorstoreswillchangenotification.md) — A notification that posts before a coordinator changes its registered stores.
