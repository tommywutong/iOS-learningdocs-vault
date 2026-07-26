---
title: 'init(for:)'
framework: Photos
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/init(for:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/init(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/init%28for%3A%29.json'
content_hash: 'sha256:8aebd3ca612f22f5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# init(for:)

<sub>Initializer</sub>

Creates a request for modifying the specified collection list.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
convenience init?(for collectionList: PHCollectionList)
```

## Parameters

- `collectionList` — The collection list to be modified.

## Return Value

A collection list change request.

## Discussion

After you create a change request within a photo library change block, propose changes to the collection’s title or list of child collections with the properties and instance methods of the change request. After Photos runs your change block, the collection list reflects your changes. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

Use this method when modifying a collection list’s metadata or when adding or removing child collections without regard to their arrangement. To work with indexes in the list of child collections, use the [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) method instead.

## See Also

### Creating a Change Request

- [+ changeRequestForCollectionList:childCollections:](<init(for_childcollections_).md>) — Creates a request for modifying the specified collection list, with a fetch result for tracking changes.
- [+ changeRequestForTopLevelCollectionListUserCollections:](<init(fortoplevelcollectionlistusercollections_).md>) — Creates a request to add, remove, or rearrange child collections in the top-level collection list.
