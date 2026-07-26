---
title: 'init(persistentStoreCoordinator:configurationName:at:options:)'
framework: Core Data
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nspersistentstore/init(persistentstorecoordinator:configurationname:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nspersistentstore/init(persistentstorecoordinator:configurationname:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nspersistentstore/init%28persistentstorecoordinator%3Aconfigurationname%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:38bfab5dd579315d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSPersistentStore](../nspersistentstore.md)

# init(persistentStoreCoordinator:configurationName:at:options:)

<sub>Initializer</sub>

Returns a store initialized with the given arguments.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(persistentStoreCoordinator root: NSPersistentStoreCoordinator?, configurationName name: String?, at url: URL, options: [AnyHashable : Any]? = nil)
```

## Parameters

- `root` — A persistent store coordinator.

- `name` — The name of the managed object model configuration to use. Pass `nil` if you do not want to specify a configuration.

- `url` — The URL of the store to load.

- `options` — A dictionary containing configuration options. See [NSPersistentStoreCoordinator](../nspersistentstorecoordinator.md) for a list of key names for options in this dictionary.

## Return Value

A new store object, associated with `coordinator`, that represents a persistent store at url using the options in `options` and—if it is not `nil`—the managed object model configuration `configurationName`.

## Discussion

You must ensure that you load metadata during initialization and set it using [metadata](metadata.md).

### Special Considerations

This is the designated initializer for persistent stores.

## See Also

### Related Documentation

- [metadata](metadata.md) — The metadata for the persistent store.
- [Core Data Programming Guide](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/CoreData/index.html#//apple_ref/doc/uid/TP40001075)
- [Atomic Store Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004521)
- [Incremental Store Programming Guide](https://developer.apple.com/library/archive/documentation/DataManagement/Conceptual/IncrementalStorePG/Introduction/Introduction.html#//apple_ref/doc/uid/TP40010706)
