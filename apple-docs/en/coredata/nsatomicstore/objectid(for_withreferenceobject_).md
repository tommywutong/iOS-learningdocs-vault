---
title: 'objectID(for:withReferenceObject:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/objectid(for:withreferenceobject:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/objectid(for:withreferenceobject:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/objectid%28for%3Awithreferenceobject%3A%29.json'
content_hash: 'sha256:2ea7b19510bdae1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# objectID(for:withReferenceObject:)

<sub>Instance Method</sub>

Returns a managed object ID from the reference data for a specified entity.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func objectID(for entity: NSEntityDescription, withReferenceObject data: Any) -> NSManagedObjectID
```

## Parameters

- `entity` — An entity description object.

- `data` — Reference data for which the managed object ID is required.

## Return Value

The managed object ID from the reference data for a specified entity

## Discussion

You use this method to create managed object IDs which are then used to create cache nodes for information being loaded into the store.

### Special Considerations

You should not override this method.

## See Also

### Loading a Store

- [- load:](<load().md>) — Loads the cache nodes for the receiver.
- [- addCacheNodes:](<addcachenodes(__).md>) — Registers a set of cache nodes with the receiver.
