---
title: placeholderForCreatedCollectionList
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phcollectionlistchangerequest/placeholderforcreatedcollectionlist
source_url: 'https://developer.apple.com/documentation/photos/phcollectionlistchangerequest/placeholderforcreatedcollectionlist'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phcollectionlistchangerequest/placeholderforcreatedcollectionlist.json'
content_hash: 'sha256:c1ac2f39edc443e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHCollectionListChangeRequest](../phcollectionlistchangerequest.md)

# placeholderForCreatedCollectionList

<sub>Instance Property</sub>

A placeholder object for the collection list that the change request creates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var placeholderForCreatedCollectionList: PHObjectPlaceholder { get }
```

## Discussion

Use this property if you need to reference the collection created by a change request within the same change block. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

## See Also

### Managing Collection Lists

- [+ creationRequestForCollectionListWithTitle:](<creationrequestforcollectionlist(withtitle_).md>) — Creates a request for adding a new collection list to the Photos library.
- [+ deleteCollectionLists:](<deletecollectionlists(__).md>) — Requests to delete the specified asset collections.
