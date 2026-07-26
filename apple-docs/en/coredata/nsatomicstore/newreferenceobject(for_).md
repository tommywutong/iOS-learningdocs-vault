---
title: 'newReferenceObject(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/newreferenceobject(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/newreferenceobject(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/newreferenceobject%28for%3A%29.json'
content_hash: 'sha256:5ef1997050a6d33b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# newReferenceObject(for:)

<sub>Instance Method</sub>

Returns a new reference object for a given managed object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func newReferenceObject(for managedObject: NSManagedObject) -> Any
```

## Parameters

- `managedObject` — A managed object. At the time this method is called, it has a temporary ID.

## Return Value

A new reference object for `managedObject`.

## Discussion

This method is invoked by the framework after a save operation on a managed object context, once for each newly-inserted managed object. The value returned is used to create a permanent ID for the object and must be unique for an instance within its entity’s inheritance hierarchy (in this store).

### Special Considerations

You must override this method.

This method must return a stable (unchanging) value for a given object, otherwise Save As and migration will not work correctly. This means that you can use arbitrary numbers, UUIDs, or other random values only if they are persisted with the raw data. If you cannot save the originally-assigned reference object with the data, then the method must derive the reference object from the managed object’s values. For more details, see [Atomic Store Programming Topics](https://developer.apple.com/library/archive/documentation/Cocoa/Conceptual/AtomicStore_Concepts/Introduction/Introduction.html#//apple_ref/doc/uid/TP40004521).

## See Also

### Updating Cache Nodes

- [- newCacheNodeForManagedObject:](<newcachenode(for_).md>) — Returns a new cache node for a given managed object.
- [- updateCacheNode:fromManagedObject:](<updatecachenode(__from_).md>) — Updates the given cache node using the values in a given managed object.
- [- willRemoveCacheNodes:](<willremovecachenodes(__).md>) — Method invoked before the store removes the given collection of cache nodes.
