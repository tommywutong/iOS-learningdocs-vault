---
title: NSPersistentStoreUbiquitousTransitionType
framework: Core Data
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstoreubiquitoustransitiontype
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreubiquitoustransitiontype.json'
content_hash: 'sha256:484ced1fd71fd74f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Core Data](../coredata.md)

# NSPersistentStoreUbiquitousTransitionType

<sub>Enumeration</sub>

These constants are used as the value corresponding to the [NSPersistentStoreUbiquitousTransitionTypeKey](nspersistentstoreubiquitoustransitiontypekey.md) in the user info dictionary of [NSPersistentStoreCoordinatorStoresWillChangeNotification](nspersistentstorecoordinatorstoreswillchangenotification.md) and [NSPersistentStoreCoordinatorStoresDidChangeNotification](nspersistentstorecoordinatorstoresdidchangenotification.md) notifications to identify the type of event leading to a change.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
enum NSPersistentStoreUbiquitousTransitionType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [NSPersistentStoreUbiquitousTransitionTypeAccountAdded](nspersistentstoreubiquitoustransitiontype/accountadded.md) — This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account. _(deprecated)_
- [NSPersistentStoreUbiquitousTransitionTypeAccountRemoved](nspersistentstoreubiquitoustransitiontype/accountremoved.md) — This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store. _(deprecated)_
- [NSPersistentStoreUbiquitousTransitionTypeContentRemoved](nspersistentstoreubiquitoustransitiontype/contentremoved.md) — This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings. _(deprecated)_
- [NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted](nspersistentstoreubiquitoustransitiontype/initialimportcompleted.md) — This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file. _(deprecated)_

### Initializers

- [init(rawValue:)](<nspersistentstoreubiquitoustransitiontype/init(rawvalue_).md>) _(deprecated)_
