---
title: lock()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+（8.0 起废弃）, iPadOS 3.0+（8.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.4+（10.10 起废弃）, visionOS 1.0+（1.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/coredata/nspersistentstorecoordinator/lock()
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstorecoordinator/lock()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstorecoordinator/lock%28%29.json'
content_hash: 'sha256:64da6527ac4439ad'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md)

# lock()

<sub>Instance Method</sub>

Attempts to acquire a lock.

> [!warning] Deprecated
> Use -performBlockAndWait: instead

<sub>iOS, iPadOS, Mac Catalyst, macOS, visionOS</sub>

```swift
func lock()
```

## Discussion

This method blocks a thread’s execution until the lock can be acquired. An application protects a critical section of code by requiring a thread to acquire a lock before executing the code. Once the critical section is past, the thread relinquishes the lock by invoking unlock.

## See Also

### Deprecated instance methods

- [- addPersistentStoreWithType:configuration:URL:options:error:](<addpersistentstore(oftype_configurationname_at_options_).md>) — Adds a specific type of persistent store at the provided location. _(deprecated)_
- [- destroyPersistentStoreAtURL:withType:options:error:](<destroypersistentstore(at_oftype_options_).md>) — Deletes a specific type of persistent store at the provided location. _(deprecated)_
- [- importStoreWithIdentifier:fromExternalRecordsDirectory:toURL:options:withType:error:](<importstore(withidentifier_fromexternalrecordsdirectoryat_to_options_oftype_).md>) — Creates and populates a store with the external records found at a given URL. _(deprecated)_
- [- migratePersistentStore:toURL:options:withType:error:](<migratepersistentstore(__to_options_withtype_).md>) — Changes the location and, if necessary, the store type of the specified persistent store. _(deprecated)_
- [- replacePersistentStoreAtURL:destinationOptions:withPersistentStoreFromURL:sourceOptions:storeType:error:](<replacepersistentstore(at_destinationoptions_withpersistentstorefrom_sourceoptions_oftype_).md>) — Replaces one persistent store with another. _(deprecated)_
- [- tryLock](<trylock().md>) — Attempts to acquire a lock. _(deprecated)_
- [- unlock](<unlock().md>) — Relinquishes a previously acquired lock. _(deprecated)_
- [- performBlock:](<perform(__)-7jqb.md>) — Executes the provided closure asynchronously on the coordinator’s queue. _(deprecated)_
- [- performBlockAndWait:](<performandwait(__)-d3kq.md>) — Executes the provided closure on the coordinator’s queue and waits for it to finish. _(deprecated)_
