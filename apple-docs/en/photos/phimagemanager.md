---
title: PHImageManager
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagemanager
source_url: 'https://developer.apple.com/documentation/photos/phimagemanager'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagemanager.json'
content_hash: 'sha256:ecaee30b11d43ef2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageManager

<sub>Class</sub>

An object that facilitates retrieving or generating preview thumbnails and asset data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHImageManager
```

## Overview

Use these methods to fetch full-size photo assets or thumbnail images, or to retrieve AVFoundation objects for playing, exporting, and manipulating video assets.

To load image or video data:

1. Use the [PHAsset](phasset.md) class to fetch the asset you’re interested in.
2. Call the [+ defaultManager](<phimagemanager/default().md>) method to retrieve the shared image manager object.
3. Use one of the methods listed in the Requesting groups below to load the asset’s image or video data.

The image manager caches the asset images and data it provides, so later requests for the same assets with similar parameters will return results more quickly.

If you need to load image data for many assets together, use the [PHCachingImageManager](phcachingimagemanager.md) class to “preheat” the cache by loading images you expect to need soon. For example, when populating a collection view with photo asset thumbnails, you can cache images ahead of the current scroll position.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Inherited By**: [PHCachingImageManager](phcachingimagemanager.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Getting the Image Manager

- [+ defaultManager](<phimagemanager/default().md>) — Returns the shared image manager object.

### Requesting Images

- [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) — Requests an image representation for the specified asset.
- [- requestImageDataAndOrientationForAsset:options:resultHandler:](<phimagemanager/requestimagedataandorientation(for_options_resulthandler_).md>) — Requests the largest represented image as data bytes and EXIF orientation for the specified asset.
- [PHImageManagerMaximumSize](phimagemanagermaximumsize.md) — A special value for requesting original image data or the largest rendered image available. .

### Requesting Video Objects

- [- requestPlayerItemForVideo:options:resultHandler:](<phimagemanager/requestplayeritem(forvideo_options_resulthandler_).md>) — Requests a representation of the video asset for playback, to be loaded asynchronously.
- [- requestExportSessionForVideo:options:exportPreset:resultHandler:](<phimagemanager/requestexportsession(forvideo_options_exportpreset_resulthandler_).md>) — Requests an export session for writing the video asset’s data to a file, to be loaded asynchronously.
- [- requestAVAssetForVideo:options:resultHandler:](<phimagemanager/requestavasset(forvideo_options_resulthandler_).md>) — Requests AVFoundation objects representing the video asset’s content and state, to be loaded asynchronously.

### Requesting Live Photos

- [- requestLivePhotoForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestlivephoto(for_targetsize_contentmode_options_resulthandler_).md>) — Requests a Live Photo representation for the specified asset.

### Canceling a Request

- [- cancelImageRequest:](<phimagemanager/cancelimagerequest(__).md>) — Cancels an asynchronous request
- [PHImageRequestID](phimagerequestid.md) — A numeric identifier for an asynchronous image request.
- [PHInvalidImageRequestID](phinvalidimagerequestid.md) — A special value provided for asynchronous image requests that cannot be canceled.

### Constants

- [PHImageContentMode](phimagecontentmode.md) — Options for fitting an image’s aspect ratio to a requested size, used by the [- requestImageForAsset:targetSize:contentMode:options:resultHandler:](<phimagemanager/requestimage(for_targetsize_contentmode_options_resulthandler_).md>) method.
- [Image Result Info Keys](../photokit/image-result-info-keys.md) — Keys identifying information about an image loading result, used in the `resultHandler` block with image request methods.

## See Also

### Asset loading

- [Loading and Caching Assets and Thumbnails](../photokit/loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [PHCachingImageManager](phcachingimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [PHImageRequestOptions](phimagerequestoptions.md) — A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [PHVideoRequestOptions](phvideorequestoptions.md) — A set of options affecting the delivery of video asset data that you request from an image manager.
- [PHLivePhotoRequestOptions](phlivephotorequestoptions.md) — A set of options affecting the delivery of Live Photo assets you request from an image manager.
