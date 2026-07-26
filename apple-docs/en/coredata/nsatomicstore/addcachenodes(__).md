---
title: 'addCacheNodes(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/addcachenodes(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/addcachenodes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/addcachenodes%28_%3A%29.json'
content_hash: 'sha256:24f080770f816c4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# addCacheNodes(_:)

<sub>Instance Method</sub>

Registers a set of cache nodes with the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func addCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)
```

## Parameters

- `cacheNodes` — A set of cache nodes.

## Discussion

You should invoke this method in a subclass during the call to [- load:](<load().md>) to register the loaded information with the store.

## See Also

### Loading a Store

- [- load:](<load().md>) — Loads the cache nodes for the receiver.
- [- objectIDForEntity:referenceObject:](<objectid(for_withreferenceobject_).md>) — Returns a managed object ID from the reference data for a specified entity.
