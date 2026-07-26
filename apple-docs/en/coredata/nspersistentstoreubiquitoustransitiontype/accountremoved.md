---
title: NSPersistentStoreUbiquitousTransitionType.accountRemoved
framework: Core Data
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 7.0+（10.0 起废弃）, iPadOS 7.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.9+（10.12 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountremoved
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountremoved'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstoreubiquitoustransitiontype/accountremoved.json'
content_hash: 'sha256:4c7c01257fd30f8c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreUbiquitousTransitionType](../nspersistentstoreubiquitoustransitiontype.md)

# NSPersistentStoreUbiquitousTransitionType.accountRemoved

<sub>Case</sub>

This value indicates that no iCloud account is available, and the persistent store in use will or did transition to the “local” store.

> [!warning] Deprecated
> Please see the release notes and Core Data documentation.

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
case accountRemoved
```

## Discussion

It is only possible to discern this state when the application is running, and therefore this transition type will only be posted if the account is removed while the application is running or in the background.

## See Also

### Constants

- [NSPersistentStoreUbiquitousTransitionTypeAccountAdded](accountadded.md) — This value indicates that a new iCloud account is available, and the persistent store in use will or did transition to the new account. _(deprecated)_
- [NSPersistentStoreUbiquitousTransitionTypeContentRemoved](contentremoved.md) — This value indicates that the user has wiped the contents of the iCloud account, usually using Delete All from Documents & Data in Settings. _(deprecated)_
- [NSPersistentStoreUbiquitousTransitionTypeInitialImportCompleted](initialimportcompleted.md) — This value indicates that the Core Data integration has finished building a store file that is consistent with the contents of the iCloud account, and is ready to replace the fallback store with that file. _(deprecated)_
