---
title: 'removeChildCollections(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/removechildcollections(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/removechildcollections(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/removechildcollections%28_%3A%29.json'
content_hash: 'sha256:1fbc58afb68e9f52'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# removeChildCollections(_:)

<sub>Instance Method</sub>

Removes the specified child collections from the collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func removeChildCollections(_ collections: any NSFastEnumeration)
```

## Parameters

- `collections` — An array of [PHCollection](../phcollection.md) objects (asset collections or other collection lists) to be removed from the collection list.

## Discussion

This method removes child collections from the collection list based on their identity (determined by the [localIdentifier](../phobject/localidentifier.md) property of each collection). To remove objects at specified indexes, use the [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) method.

## See Also

### Managing Collections

- [- addChildCollections:](<addchildcollections(__).md>) — Adds the specified collections as children of the collection list.
- [- insertChildCollections:atIndexes:](<insertchildcollections(__at_).md>) — Inserts the specified collections into the collection list at the specified indexes.
- [- moveChildCollectionsAtIndexes:toIndex:](<movechildcollections(at_to_).md>) — Moves the child collections at the specified indexes in the collection list to a new index.
- [- replaceChildCollectionsAtIndexes:withChildCollections:](<replacechildcollections(at_withchildcollections_).md>) — Replaces the child collections at the specified indexes in the collection list with the specified collections.
- [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) — Removes the child collections at the specified indexes from the collection list.
