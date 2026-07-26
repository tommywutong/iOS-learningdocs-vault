---
title: 'creationRequestForCollectionList(withTitle:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phcollectionlistchangerequest/creationrequestforcollectionlist(withtitle:)'
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/creationrequestforcollectionlist(withtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/creationrequestforcollectionlist%28withtitle%3A%29.json'
content_hash: 'sha256:22884bffe8d80f5b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# creationRequestForCollectionList(withTitle:)

<sub>Type Method</sub>

Creates a request for adding a new collection list to the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func creationRequestForCollectionList(withTitle title: String) -> Self
```

## Parameters

- `title` — A name for the new collection list.

## Return Value

A collection list creation request.

## Discussion

Call this method within a photo library change block to create a new collection list. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

To add collections to the newly created collection list or to change its title, use the methods listed in Managing Collections. To reference the newly created collection list later in the same change block or after the change block completes, use the [placeholderForCreatedCollectionList](placeholderforcreatedcollectionlist.md) property to retrieve a placeholder object.

## See Also

### Managing Collection Lists

- [placeholderForCreatedCollectionList](placeholderforcreatedcollectionlist.md) — A placeholder object for the collection list that the change request creates.
- [+ deleteCollectionLists:](<deletecollectionlists(__).md>) — Requests to delete the specified asset collections.
