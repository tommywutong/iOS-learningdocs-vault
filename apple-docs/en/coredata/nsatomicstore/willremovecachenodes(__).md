---
title: 'willRemoveCacheNodes(_:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/willremovecachenodes(_:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/willremovecachenodes(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/willremovecachenodes%28_%3A%29.json'
content_hash: 'sha256:2e22c68d489f694d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# willRemoveCacheNodes(_:)

<sub>Instance Method</sub>

Method invoked before the store removes the given collection of cache nodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func willRemoveCacheNodes(_ cacheNodes: Set<NSAtomicStoreCacheNode>)
```

## Parameters

- `cacheNodes` — The set of cache nodes to remove.

## Discussion

This method is invoked by the store before the call to [- save:](<save().md>) with the collection of cache nodes marked as deleted by a managed object context.  You can override this method to track the nodes which will not be made persistent in the [- save:](<save().md>) method.

You should not invoke this method directly in a subclass.

## See Also

### Related Documentation

- [- save:](<save().md>) — Saves the cache nodes.

### Updating Cache Nodes

- [- newCacheNodeForManagedObject:](<newcachenode(for_).md>) — Returns a new cache node for a given managed object.
- [- newReferenceObjectForManagedObject:](<newreferenceobject(for_).md>) — Returns a new reference object for a given managed object.
- [- updateCacheNode:fromManagedObject:](<updatecachenode(__from_).md>) — Updates the given cache node using the values in a given managed object.
