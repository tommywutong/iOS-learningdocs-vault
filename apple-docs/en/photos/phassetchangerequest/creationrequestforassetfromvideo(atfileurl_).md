---
title: 'creationRequestForAssetFromVideo(atFileURL:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo(atfileurl:)'
source_url: 'https://developer.apple.com/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo(atfileurl:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetchangerequest/creationrequestforassetfromvideo%28atfileurl%3A%29.json'
content_hash: 'sha256:8d0a512760250545'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetChangeRequest](../phassetchangerequest.md)

# creationRequestForAssetFromVideo(atFileURL:)

<sub>Type Method</sub>

Creates a request for adding a new video asset to the Photos library, using the video file at the specified URL.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func creationRequestForAssetFromVideo(atFileURL fileURL: URL) -> Self?
```

## Parameters

- `fileURL` — A URL for a video file.

## Return Value

An asset creation request.

## Discussion

Call this method within a photo library change block to create a new asset. For details on change blocks, see [PHPhotoLibrary](../phphotolibrary.md).

To set metadata properties of the newly created asset, use the corresponding properties of the change request (listed in Modifying Assets). To reference the newly created asset later in the same change block or after the change block completes, use the [placeholderForCreatedAsset](placeholderforcreatedasset.md) property to retrieve a placeholder object.

## See Also

### Adding New Assets

- [+ creationRequestForAssetFromImage:](<creationrequestforasset(from_).md>) — Creates a request for adding a new image asset to the Photos library.
- [+ creationRequestForAssetFromImageAtFileURL:](<creationrequestforassetfromimage(atfileurl_).md>) — Creates a request for adding a new image asset to the Photos library, using the image file at the specified URL.
- [placeholderForCreatedAsset](placeholderforcreatedasset.md) — A placeholder object for the asset that the change request creates.
