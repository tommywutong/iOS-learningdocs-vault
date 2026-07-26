---
title: 'referenceObject(for:)'
framework: Core Data
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 3.0+, iPadOS 3.0+, Mac Catalyst 13.1+, macOS 10.5+, tvOS, visionOS 1.0+, watchOS 2.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/coredata/nsatomicstore/referenceobject(for:)'
source_url: 'https://developer.apple.com/documentation/coredata/nsatomicstore/referenceobject(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/coredata/nsatomicstore/referenceobject%28for%3A%29.json'
content_hash: 'sha256:b86f25a3380e2216'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Core Data](../../coredata.md) · [NSAtomicStore](../nsatomicstore.md)

# referenceObject(for:)

<sub>Instance Method</sub>

Returns the reference object for a given managed object ID.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func referenceObject(for objectID: NSManagedObjectID) -> Any
```

## Parameters

- `objectID` — A managed object ID.

## Return Value

The reference object for `objectID`.

## Discussion

Subclasses should invoke this method to extract the reference data from the object ID for each cache node if the data is to be made persistent.

## See Also

### Utility Methods

- [- cacheNodes](<cachenodes().md>) — Returns the set of cache nodes registered with the receiver.
- [- cacheNodeForObjectID:](<cachenode(for_).md>) — Returns the cache node for a given managed object ID.
