---
title: 'creationRequestForAsset(from:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/creationrequestforasset(from:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforasset(from:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/creationrequestforasset%28from%3A%29.json'
content_hash: 'sha256:0e9d3ba2d6dcebed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# creationRequestForAsset(from:)

<sub>Type Method</sub>

Creates a request for adding a new image asset to the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
class func creationRequestForAsset(from image: UIImage) -> Self
```

<sub>macOS</sub>

```swift
class func creationRequestForAsset(from image: NSImage) -> Self
```

## Parameters

- `image` — An image.

## Return Value

An asset creation request.

## Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

To reference the newly created asset later in the same change block or after the change block completes, use the [placeholderForCreatedAsset](placeholderforcreatedasset.md) property to retrieve a placeholder object.

> [!important] Important
> A [UIImage](../../uikit/uiimage.md) object does not contain all metadata associated with the image file it was originally loaded from (for example, Exif tags such as geographic location, camera model, and exposure parameters). To ensure such metadata is saved in the Photos library, instead use the [+ creationRequestForAssetFromImageAtFileURL:](<creationrequestforassetfromimage(atfileurl_).md>) method or the [PHAssetCreationRequest](../phassetcreationrequest.md) class. To copy metadata from one file to another, see [Image I/O](../../imageio.md).

## See Also

### Adding New Assets

- [+ creationRequestForAssetFromImageAtFileURL:](<creationrequestforassetfromimage(atfileurl_).md>) — Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [+ creationRequestForAssetFromVideoAtFileURL:](<creationrequestforassetfromvideo(atfileurl_).md>) — Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.
- [placeholderForCreatedAsset](placeholderforcreatedasset.md) — A placeholder object for the asset that the change request creates.
