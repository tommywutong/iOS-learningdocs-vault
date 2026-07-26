---
title: 'deleteCollectionLists(_:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/deletecollectionlists(_:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/deletecollectionlists(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/deletecollectionlists%28_%3A%29.json'
content_hash: 'sha256:e50a6b0049868f64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# deleteCollectionLists(_:)

<sub>Type Method</sub>

Requests to delete the specified asset collections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func deleteCollectionLists(_ collectionLists: any NSFastEnumeration)
```

## Parameters

- `collectionLists` — An array of [PHCollectionList](../phcollectionlist.md) objects to be deleted.

## Discussion

Call this method within a photo library change block to delete collection lists. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

> [!important] Important
> Deleting a collection list also deletes any child collections it contains. To preserve those collections, remove them from the collection list (with the [- removeChildCollections:](<removechildcollections(__).md>) or [- removeChildCollectionsAtIndexes:](<removechildcollections(at_).md>) method) before deleting it. Deleting a collection list does not delete assets contained in its child collections.

## See Also

### Managing Collection Lists

- [+ creationRequestForCollectionListWithTitle:](<creationrequestforcollectionlist(withtitle_).md>) — Creates a request for adding a new collection list to the Photos library.
- [placeholderForCreatedCollectionList](placeholderforcreatedcollectionlist.md) — A placeholder object for the collection list that the change request creates.
