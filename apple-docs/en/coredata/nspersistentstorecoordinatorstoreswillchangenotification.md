---
title: NSPersistentStoreCoordinatorStoresWillChangeNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 13.1+, macOS 10.9+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinatorstoreswillchangenotification
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorstoreswillchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinatorstoreswillchangenotification.json'
content_hash: 'sha256:b5d0049c3456b7d5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreCoordinatorStoresWillChangeNotification

<sub>Global Variable</sub>

A notification that posts before a coordinator changes its registered stores.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSPersistentStoreCoordinatorStoresWillChangeNotification;
```

## Discussion

This notification’s `object` is the store coordinator that’s about to change. The framework posts the notification to an internal thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains information about the added and removed persistent stores, which you access with the [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md) and [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) keys. Don’t capture the dictionary’s contents.

## See Also

### Notifications

- [NSPersistentStoreCoordinatorStoresDidChangeNotification](nspersistentstorecoordinatorstoresdidchangenotification.md) — A notification that the coordinator posts after its registered stores change.
- [NSPersistentStoreCoordinatorWillRemoveStoreNotification](nspersistentstorecoordinatorwillremovestorenotification.md) — A notification that posts before a coordinator removes a store.
