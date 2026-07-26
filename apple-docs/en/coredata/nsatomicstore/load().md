---
title: load()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstore/load()
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/load()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/load%28%29.json'
content_hash: 'sha256:60bf3900521e3b99'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# load()

<sub>Instance Method</sub>

Loads the cache nodes for the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func load() throws
```

## Discussion

You override this method to load the data from the URL specified in [- initWithPersistentStoreCoordinator:configurationName:URL:options:](<init(persistentstorecoordinator_configurationname_at_options_).md>) and create cache nodes for the represented objects. You must respect the configuration specified for the store, as well as the options.

Any subclass of `NSAtomicStore` must be able to handle being initialized with a URL pointing to a zero-length file. This serves as an indicator that a new store is to be constructed at the specified location and allows you to securely create reservation files in known locations which can then be passed to Core Data to construct stores. You may choose to create zero-length reservation files during [- initWithPersistentStoreCoordinator:configurationName:URL:options:](<init(persistentstorecoordinator_configurationname_at_options_).md>) or [- load:](<load().md>). If you do so, you must remove the reservation file if the store is removed from the coordinator before it is saved.

You must override this method in a subclass of `NSAtomicStore`.

## See Also

### Loading a Store

- [- objectIDForEntity:referenceObject:](<objectid(for_withreferenceobject_).md>) — Returns a managed object ID from the reference data for a specified entity.
- [- addCacheNodes:](<addcachenodes(__).md>) — Registers a set of cache nodes with the receiver.
