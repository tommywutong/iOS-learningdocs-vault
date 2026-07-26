---
title: 'init(for:childCollections:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/init(for:childcollections:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(for:childcollections:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/init%28for%3Achildcollections%3A%29.json'
content_hash: 'sha256:e04ac182275f9fe1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# init(for:childCollections:)

<sub>Initializer</sub>

Creates a request for modifying the specified collection list, with a fetch result for tracking changes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(for collectionList: PHCollectionList, childCollections: PHFetchResult<PHCollection>)
```

## Parameters

- `collectionList` — The collection list to be modified.

- `childCollections` — A fetch result listing the child collections in the collection.

## Return Value

A collection list change request.

## Discussion

After you create a change request within a photo library change block, propose changes to the collection’s title or list of child collections with the properties and instance methods of the change request. After Photos runs your change block, the collection list reflects your changes. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

Use this method when you need to insert, remove, or rearrange collections at specified indexes in the collection list. By passing in a fetch result reflecting what your app sees as the current state of the collection’s membership, the Photos framework can ensure that the indexes you specify are valid even if the collection has changed since you last fetched it. If you don’t need to work with indexes in the list of child collections, you can use the [+ changeRequestForCollectionList:](<init(for_).md>) method instead.

## See Also

### Creating a Change Request

- [+ changeRequestForCollectionList:](<init(for_).md>) — Creates a request for modifying the specified collection list.
- [+ changeRequestForTopLevelCollectionListUserCollections:](<init(fortoplevelcollectionlistusercollections_).md>) — Creates a request to add, remove, or rearrange child collections in the top-level collection list.
