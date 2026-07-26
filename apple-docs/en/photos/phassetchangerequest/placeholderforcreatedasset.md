---
title: placeholderForCreatedAsset
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetchangerequest/placeholderforcreatedasset
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/placeholderforcreatedasset'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/placeholderforcreatedasset.json'
content_hash: 'sha256:2965c9170d9a6cbd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# placeholderForCreatedAsset

<sub>Instance Property</sub>

A placeholder object for the asset that the change request creates.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var placeholderForCreatedAsset: PHObjectPlaceholder? { get }
```

## Discussion

Use this property if you need to reference the asset created by a change request within the same change block. For example, the following code, when included in a photo library change block, creates an asset and then adds it to a collection.

**Swift**

```swift
let createAssetRequest = PHAssetChangeRequest.creationRequestForAsset(from: image)
let assetPlaceholder = createAssetRequest.placeholderForCreatedAsset!
let albumChangeRequest = PHAssetCollectionChangeRequest(for: album)
albumChangeRequest!.addAssets([assetPlaceholder] as NSFastEnumeration)
```

**Objective-C**

```objc
PHAssetChangeRequest *createAssetRequest = [PHAssetChangeRequest creationRequestForAssetFromImage:image];
PHObjectPlaceholder *assetPlaceholder = createAssetRequest.placeholderForCreatedAsset;
PHAssetCollectionChangeRequest *albumChangeRequest =
    [PHAssetCollectionChangeRequest changeRequestForAssetCollection:album];
[albumChangeRequest addAssets:@[ assetPlaceholder ]];
```

For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

## See Also

### Adding New Assets

- [+ creationRequestForAssetFromImage:](<creationrequestforasset(from_).md>) — Creates a request for adding a new image asset to the Photos library.
- [+ creationRequestForAssetFromImageAtFileURL:](<creationrequestforassetfromimage(atfileurl_).md>) — Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [+ creationRequestForAssetFromVideoAtFileURL:](<creationrequestforassetfromvideo(atfileurl_).md>) — Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.
