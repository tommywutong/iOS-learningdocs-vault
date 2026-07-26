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
doc_path: '/documentation/coredata/nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/init(persistentstorecoordinator:configurationname:at:options:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/init%28persistentstorecoordinator%3Aconfigurationname%3Aat%3Aoptions%3A%29.json'
content_hash: 'sha256:59dc7843ec80f781'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# init(persistentStoreCoordinator:configurationName:at:options:)

<sub>Initializer</sub>

Creates an atomic store at the specified location.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(persistentStoreCoordinator coordinator: NSPersistentStoreCoordinator?, configurationName: String?, at url: URL, options: [AnyHashable : Any]? = nil)
```

## Parameters

- `coordinator` — The persistent store coordinator.

- `configurationName` — The name of the store’s configuration in the managed object model.

- `url` — The URL of the store to load. This value can’t be `nil`.

- `options` — A dictionary that contains the store’s options. For possible values, see [Store options](../store-options.md).

## Discussion

Typically, you don’t invoke this method yourself; instead, the persistent store coordinator invokes the method when it creates a new store or adds an existing one.

In your implementation, check whether a file exists at `url`. If it doesn’t exist, create a zero-length file at `url` so that the file exists before the coordinator calls the store’s [- load:](<load().md>) method. A zero-length file indicates to the system that it should create a new store at that location. If the coordinator removes the store without first calling [- save:](<save().md>), delete the zero-length file.

It’s your responsibility to load the store’s metadata during initialization and set it using the [+ setMetadata:forPersistentStoreWithURL:error:](<../nspersistentstore/setmetadata(__forpersistentstoreat_).md>) method.

> [!important] Important
> If you override this method, you must invoke the superclass implementation to ensure that Core Data correctly initializes the store.
