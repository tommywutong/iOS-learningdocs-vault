---
title: save()
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/coredata/nsatomicstore/save()
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/save()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/save%28%29.json'
content_hash: 'sha256:f1c0cc8c3ce5dc6e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# save()

<sub>Instance Method</sub>

Saves the cache nodes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func save() throws
```

## Discussion

You override this method to make persistent the necessary information from the cache nodes to the URL specified for the receiver.

### Special Considerations

You must override this method.

## See Also

### Related Documentation

- [- updateCacheNode:fromManagedObject:](<updatecachenode(__from_).md>) — Updates the given cache node using the values in a given managed object.
- [- willRemoveCacheNodes:](<willremovecachenodes(__).md>) — Method invoked before the store removes the given collection of cache nodes.
- [- newReferenceObjectForManagedObject:](<newreferenceobject(for_).md>) — Returns a new reference object for a given managed object.
