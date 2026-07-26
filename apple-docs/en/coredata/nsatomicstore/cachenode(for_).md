---
title: 'cacheNode(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/cachenode(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/cachenode(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/cachenode%28for%3A%29.json'
content_hash: 'sha256:41a7ee51bf302c3c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# cacheNode(for:)

<sub>Instance Method</sub>

Returns the cache node for a given managed object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cacheNode(for objectID: NSManagedObjectID) -> NSAtomicStoreCacheNode?
```

## Parameters

- `objectID` — A managed object ID.

## Return Value

The cache node for `objectID`.

## Discussion

This method is normally used by cache nodes to locate related cache nodes (by relationships).

## See Also

### Utility Methods

- [- cacheNodes](<cachenodes().md>) — Returns the set of cache nodes registered with the receiver.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference object for a given managed object ID.
