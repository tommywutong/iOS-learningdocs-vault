---
title: 'replaceChildCollections(at:withChildCollections:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/replacechildcollections(at:withchildcollections:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/replacechildcollections(at:withchildcollections:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/replacechildcollections%28at%3Awithchildcollections%3A%29.json'
content_hash: 'sha256:48287c18c1900a2d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# replaceChildCollections(at:withChildCollections:)

<sub>Instance Method</sub>

Replaces the child collections at the specified indexes in the collection list with the specified collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func replaceChildCollections(at indexes: IndexSet, withChildCollections collections: any NSFastEnumeration)
```

## Parameters

- `indexes` — The indexes of the child collections to be replaced in the collection list.

- `collections` — An array of [PHCollection](../phcollection.md) objects (asset collections or other collection lists) to be inserted into (or moved within) the collection list.

## Discussion

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method before rearranging child collections.

## See Also

### Managing Collections

- [- addChildCollections:](<addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- insertChildCollections:atIndexes:](<insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- moveChildCollectionsAtIndexes:toIndex:](<movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- removeChildCollections:](<removechildcollections(__).md>) — Removes the specified child collections from the collection list.
- [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.
