---
title: 'insertChildCollections(_:at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/insertchildcollections(_:at:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/insertchildcollections(_:at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/insertchildcollections%28_%3Aat%3A%29.json'
content_hash: 'sha256:927f0e8d8eb975dc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# insertChildCollections(_:at:)

<sub>Instance Method</sub>

Inserts the specified collections into the collection list at the specified indexes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func insertChildCollections(_ collections: any NSFastEnumeration, at indexes: IndexSet)
```

## Parameters

- `collections` — An array of [PHCollection](../phcollection.md) objects (asset collections or other collection lists) to be inserted into the collection list.

- `indexes` — The indexes at which the collections should be inserted. The count of locations in this index set must equal the count of collections.

## Discussion

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method before inserting child collections.

For a detailed discussion of how the index set you specify maps to insertions in the collection list, see the similar [NSMutableArray](../../foundation/nsmutablearray.md) method `insert`.

## See Also

### Managing Collections

- [- addChildCollections:](<addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- moveChildCollectionsAtIndexes:toIndex:](<movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollections:](<removechildcollections(__).md>) — Removes the specified child collections from the collection list.
- [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.
