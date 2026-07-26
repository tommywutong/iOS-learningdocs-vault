---
title: 'moveChildCollections(at:to:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/movechildcollections(at:to:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/movechildcollections(at:to:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/movechildcollections%28at%3Ato%3A%29.json'
content_hash: 'sha256:2c412667780a4e12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# moveChildCollections(at:to:)

<sub>Instance Method</sub>

Moves the child collections at the specified indexes in the collection list to a new index.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func moveChildCollections(at indexes: IndexSet, to toIndex: Int)
```

## Parameters

- `indexes` — The indexes of the child collections to be moved in the collection list.

- `toIndex` — The index at which to place the moved child collections, relative to the collection list’s ordering after removing the items at `indexes`.

## Discussion

When you call this method, Photos first removes the items in the `indexes` parameter from the collection, and then inserts them at the location specified by the `toIndex` parameter.

To ensure that the index set you specify is valid even if the collection list has changed since you fetched it, create a change request with a snapshot of the collection list’s contents using the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method before rearranging child collections.

## See Also

### Managing Collections

- [- addChildCollections:](<addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- insertChildCollections:atIndexes:](<insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollections:](<removechildcollections(__).md>) — Removes the specified child collections from the collection list.
- [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.
