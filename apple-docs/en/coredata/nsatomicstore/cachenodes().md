---
title: cacheNodes()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstore/cachenodes()
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/cachenodes()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/cachenodes%28%29.json'
content_hash: 'sha256:7ba5b8dc01a85f4e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# cacheNodes()

<sub>Instance Method</sub>

Returns the set of cache nodes registered with the receiver.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func cacheNodes() -> Set<NSAtomicStoreCacheNode>
```

## Return Value

The set of cache nodes registered with the receiver.

## Discussion

You should modify this collection using [- addCacheNodes:](<addcachenodes(__).md>): and [- willRemoveCacheNodes:](<willremovecachenodes(__).md>).

## See Also

### Utility Methods

- [- cacheNodeForObjectID:](<cachenode(for_).md>) — Returns the cache node for a given managed object ID.
- [- referenceObjectForObjectID:](<referenceobject(for_).md>) — Returns the reference object for a given managed object ID.
