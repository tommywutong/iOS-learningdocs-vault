---
title: 'updateCacheNode(_:from:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/updatecachenode(_:from:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/updatecachenode(_:from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/updatecachenode%28_%3Afrom%3A%29.json'
content_hash: 'sha256:270a81ee423be7e1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# updateCacheNode(_:from:)

<sub>Instance Method</sub>

Updates the given cache node using the values in a given managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func updateCacheNode(_ node: NSAtomicStoreCacheNode, from managedObject: NSManagedObject)
```

## Parameters

- `node` — The cache node to update.

- `managedObject` — The managed object with which to update `node`.

## Discussion

This method is invoked by the framework after a save operation on a managed object context, once for each updated `NSManagedObject` instance.

You override this method in a subclass to take the information from `managedObject` and update `node`.

### Special Considerations

You must override this method.

## See Also

### Updating Cache Nodes

- [- newCacheNodeForManagedObject:](<newcachenode(for_).md>) — Returns a new cache node for a given managed object.
- [- newReferenceObjectForManagedObject:](<newreferenceobject(for_).md>) — Returns a new reference object for a given managed object.
- [- willRemoveCacheNodes:](<willremovecachenodes(__).md>) — Method invoked before the store removes the given collection of cache nodes.
