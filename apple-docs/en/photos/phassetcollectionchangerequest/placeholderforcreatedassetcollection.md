---
title: placeholderForCreatedAssetCollection
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetcollectionchangerequest/placeholderforcreatedassetcollection
source_url: 'https://developer.apple.com/documentation/photos/phassetcollectionchangerequest/placeholderforcreatedassetcollection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetcollectionchangerequest/placeholderforcreatedassetcollection.json'
content_hash: 'sha256:0ccd74ecc67fcd98'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetCollectionChangeRequest](../phassetcollectionchangerequest.md)

# placeholderForCreatedAssetCollection

<sub>Instance Property</sub>

A placeholder object for the asset collection that the change request creates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var placeholderForCreatedAssetCollection: PHObjectPlaceholder { get }
```

## Discussion

Use this property if you need to reference the asset collection created by a change request within the same change block. For example, the following code, when included in a photo library change block, creates an asset collection and then adds it to a collection list.

**Swift**

```swift
let createAlbumRequest = PHAssetCollectionChangeRequest.creationRequestForAssetCollection(withTitle: "New Album")
let albumPlaceholder = createAlbumRequest.placeholderForCreatedAssetCollection
let folderChangeRequest = PHCollectionListChangeRequest(for: folder)
folderChangeRequest!.addChildCollections([albumPlaceholder] as NSFastEnumeration)
```

**Objective-C**

```objc
PHAssetCollectionChangeRequest *createAlbumRequest =
    [PHAssetCollectionChangeRequest creationRequestForAssetCollectionWithTitle:@"New Album"];
PHObjectPlaceholder *albumPlaceholder = createAlbumRequest.placeholderForCreatedAssetCollection;
PHCollectionListChangeRequest *folderChangeRequest =
    [PHCollectionListChangeRequest changeRequestForCollectionList:folder];
[folderChangeRequest addChildCollections:@[ albumPlaceholder ]];
```

For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

## See Also

### Adding New Asset Collections

- [+ creationRequestForAssetCollectionWithTitle:](<creationrequestforassetcollection(withtitle_).md>) — Creates a request for adding a new asset collection to the Photos library.
