---
title: NSPersistentStoreCoordinatorStoresDidChangeNotification
framework: Core Data
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.4+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nspersistentstorecoordinatorstoresdidchangenotification
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinatorstoresdidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinatorstoresdidchangenotification.json'
content_hash: 'sha256:afecf6377e75543f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreCoordinatorStoresDidChangeNotification

<sub>Global Variable</sub>

A notification that the coordinator posts after its registered stores change.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```objc
extern NSString * const NSPersistentStoreCoordinatorStoresDidChangeNotification;
```

## Discussion

This notification’s `object` is the changed store coordinator. The framework posts the notification to an internal thread. Move to a known thread before peforming any work.

The `userInfo` dictionary contains information about the added, updated, and removed persistent stores, which you access with the [NSAddedPersistentStoresKey](nsaddedpersistentstoreskey.md), [NSUUIDChangedPersistentStoresKey](nsuuidchangedpersistentstoreskey.md), and [NSRemovedPersistentStoresKey](nsremovedpersistentstoreskey.md) keys. Don’t capture the dictionary’s contents.

## See Also

### Notifications

- [NSPersistentStoreCoordinatorStoresWillChangeNotification](nspersistentstorecoordinatorstoreswillchangenotification.md) — A notification that posts before a coordinator changes its registered stores.
- [NSPersistentStoreCoordinatorWillRemoveStoreNotification](nspersistentstorecoordinatorwillremovestorenotification.md) — A notification that posts before a coordinator removes a store.
