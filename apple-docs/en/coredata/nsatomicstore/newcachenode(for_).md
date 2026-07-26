---
title: 'newCacheNode(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/newcachenode(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/newcachenode(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/newcachenode%28for%3A%29.json'
content_hash: 'sha256:072c1bf2ebb85b8e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# newCacheNode(for:)

<sub>Instance Method</sub>

Returns a new cache node for a given managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newCacheNode(for managedObject: NSManagedObject) -> NSAtomicStoreCacheNode
```

## Parameters

- `managedObject` — A managed object.

## Return Value

A new cache node for `managedObject`.

## Discussion

This method is invoked by the framework during a save operation, once for each newly-inserted managed object. It should pull information from the managed object and return a cache node containing the information (the node will be registered by the framework).

### Special Considerations

You must override this method.

## See Also

### Updating Cache Nodes

- [- newReferenceObjectForManagedObject:](<newreferenceobject(for_).md>) — Returns a new reference object for a given managed object.
- [- updateCacheNode:fromManagedObject:](<updatecachenode(__from_).md>) — Updates the given cache node using the values in a given managed object.
- [- willRemoveCacheNodes:](<willremovecachenodes(__).md>) — Method invoked before the store removes the given collection of cache nodes.
