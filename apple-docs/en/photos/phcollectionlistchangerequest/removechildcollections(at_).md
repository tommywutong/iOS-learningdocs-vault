---
title: 'removeChildCollections(at:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/removechildcollections(at:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/removechildcollections(at:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/removechildcollections%28at%3A%29.json'
content_hash: 'sha256:e1dbd4e9584ea222'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# removeChildCollections(at:)

<sub>Instance Method</sub>

Removes the child collections at the specified indexes from the collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeChildCollections(at indexes: IndexSet)
```

## Parameters

- `indexes` — The indexes of the child collections to be removed from the collection list.

## Discussion

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method before removing child collections. To remove objects based on their identities (without regard to their indexes in the collection), use the [- removeChildCollections:](<removechildcollections(__).md>) method.

## See Also

### Managing Collections

- [- addChildCollections:](<addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- insertChildCollections:atIndexes:](<insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- moveChildCollectionsAtIndexes:toIndex:](<movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollections:](<removechildcollections(__).md>) — Removes the specified child collections from the collection list.
