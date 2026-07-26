---
title: 'init(changes:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectiondifference/init(changes:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(changes:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/init%28changes%3A%29.json'
content_hash: 'sha256:b07fb1665e5a603b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# init(changes:)

<sub>Initializer</sub>

Creates an ordered collection difference using an array of ordered collection changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
convenience init(changes: [NSOrderedCollectionChange])
```

## Parameters

- `changes` — An array of ordered collection changes.

## See Also

### Creating a Collection Difference Object

- [- initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:](<init(insert_insertedobjects_remove_removedobjects_).md>) — Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.
- [- initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:additionalChanges:](<init(insert_insertedobjects_remove_removedobjects_additionalchanges_).md>) — Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.
