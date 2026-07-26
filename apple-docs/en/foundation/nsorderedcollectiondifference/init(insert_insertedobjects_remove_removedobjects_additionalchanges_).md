---
title: 'init(insert:insertedObjects:remove:removedObjects:additionalChanges:)'
framework: Foundation
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ, occ, occ]
beta: false
deprecated: false
doc_path: '/documentation/foundation/nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:)'
source_url: 'https://developer.apple.com/documentation/foundation/nsorderedcollectiondifference/init(insert:insertedobjects:remove:removedobjects:additionalchanges:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/foundation/nsorderedcollectiondifference/init%28insert%3Ainsertedobjects%3Aremove%3Aremovedobjects%3Aadditionalchanges%3A%29.json'
content_hash: 'sha256:9d138913b8dd0a2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Foundation](../../foundation.md) · [NSOrderedCollectionDifference](../nsorderedcollectiondifference.md)

# init(insert:insertedObjects:remove:removedObjects:additionalChanges:)

<sub>Initializer</sub>

Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices, in addition to an array of ordered collection changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(insert inserts: IndexSet, insertedObjects: [Any]?, remove removes: IndexSet, removedObjects: [Any]?, additionalChanges changes: [NSOrderedCollectionChange])
```

## Parameters

- `inserts` — An index set that represents the index values to associate with the objects in the provided array of inserted objects.

- `insertedObjects` — An array of objects the ordered collection difference will insert.

- `removes` — An index set that represents the index values to associate with the objects in the provided array of removed objects.

- `removedObjects` — An array of objects the ordered collection difference will remove.

- `changes` — An array of ordered collection changes.

## See Also

### Creating a Collection Difference Object

- [- initWithChanges:](<init(changes_).md>) — Creates an ordered collection difference using an array of ordered collection changes.
- [- initWithInsertIndexes:insertedObjects:removeIndexes:removedObjects:](<init(insert_insertedobjects_remove_removedobjects_).md>) — Creates an ordered collection difference from arrays of inserted and removed objects with corresponding sets of indices.
