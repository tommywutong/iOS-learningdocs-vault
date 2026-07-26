---
title: 'assetResources(for:)'
framework: Photos
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/photos/phassetresource/assetresources(for:)-2fedw'
source_url: 'https://developer.apple.com/documentation/photos/phassetresource/assetresources(for:)-2fedw'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresource/assetresources%28for%3A%29-2fedw.json'
content_hash: 'sha256:cb482567434f5fd3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResource](../phassetresource.md)

# assetResources(for:)

<sub>Type Method</sub>

Returns the list of data resources associated with a Live Photo object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class func assetResources(for livePhoto: PHLivePhoto) -> [PHAssetResource]
```

## Parameters

- `livePhoto` — A Live Photo object.

## Return Value

The underlying resources that constitute the Live Photo.

## Discussion

A Live Photo is a picture, taken with a compatible device, that includes movement and sound from the moments just before and after its capture. A [PHLivePhoto](../phlivephoto.md) object represents the displayable combination of image, motion, and sound data. You can obtain such objects from the Photos library using the [PHImageManager](../phimagemanager.md) class or construct them from asset resources exported from a Photos library using the [PHLivePhoto](../phlivephoto.md) class.

Use this method to export the underlying resources that constitute a Live Photo. For example, a social networking app can retrieve those data files and upload them to a server. Then, on another user’s device, the app downloads those data files and uses the [PHLivePhoto](../phlivephoto.md) class to re-create a Live Photo object for display using the [PHLivePhotoView](../../photosui/phlivephotoview.md) class.

## See Also

### Retrieving an Asset’s Data Resources

- [+ assetResourcesForAsset:](<assetresources(for_)-27o4l.md>) — Returns the list of data resources associated with an asset.
