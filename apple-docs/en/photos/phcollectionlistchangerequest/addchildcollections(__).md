---
title: 'addChildCollections(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/addchildcollections(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/addchildcollections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/addchildcollections%28_%3A%29.json'
content_hash: 'sha256:6109ccdc887404ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# addChildCollections(_:)

<sub>Instance Method</sub>

Adds the specified collections as children of the collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func addChildCollections(_ collections: any NSFastEnumeration)
```

## Parameters

- `collections` — An array of [PHCollection](../phcollection.md) objects (asset collections or other collection lists) to be added to the collection list.

## Discussion

If you created the change request with a snapshot of the collection list’s contents using the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method, Photos inserts the new children after the existing child collections in the collection list. Otherwise, the arrangement of the new children relative to others in the collection is undefined.

## See Also

### Managing Collections

- [- insertChildCollections:atIndexes:](<insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- moveChildCollectionsAtIndexes:toIndex:](<movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollections:](<removechildcollections(__).md>) — Removes the specified child collections from the collection list.
- [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.
