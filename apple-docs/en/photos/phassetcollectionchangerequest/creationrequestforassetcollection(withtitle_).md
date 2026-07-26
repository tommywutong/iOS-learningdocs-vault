---
title: 'creationRequestForAssetCollection(withTitle:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetcollectionchangerequest/creationrequestforassetcollection(withtitle:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/creationrequestforassetcollection(withtitle:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/creationrequestforassetcollection%28withtitle%3A%29.json'
content_hash: 'sha256:c6b9c875eb0adee1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# creationRequestForAssetCollection(withTitle:)

<sub>Type Method</sub>

Creates a request for adding a new asset collection to the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func creationRequestForAssetCollection(withTitle title: String) -> Self
```

## Parameters

- `title` — A name for the new asset collection.

## Return Value

An asset collection creation request.

## Discussion

Call this method within a photo library change block to create a new asset collection. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

To add assets to the newly created asset collection or change its title, use the methods listed in Modifying Asset Collections. To reference the newly created asset collection later in the same change block or after the change block completes, use the [placeholderForCreatedAssetCollection](placeholderforcreatedassetcollection.md) property to retrieve a placeholder object.

## See Also

### Adding New Asset Collections

- [placeholderForCreatedAssetCollection](placeholderforcreatedassetcollection.md) — A placeholder object for the asset collection that the change request creates.
