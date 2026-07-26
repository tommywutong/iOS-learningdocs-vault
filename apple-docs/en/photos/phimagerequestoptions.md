---
title: PHImageRequestOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phimagerequestoptions
source_url: 'https://developer.apple.com/documentation/photos/phimagerequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phimagerequestoptions.json'
content_hash: 'sha256:d4b8bb4f4fd4ab9d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHImageRequestOptions

<sub>Class</sub>

A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHImageRequestOptions
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Scheduling an Image Request

- [synchronous](phimagerequestoptions/issynchronous.md) — A Boolean value that determines whether Photos processes the image request synchronously.

### Specifying Image Request Options

- [version](phimagerequestoptions/version.md) — The version of the image to be requested.
- [PHImageRequestOptionsVersion](phimagerequestoptionsversion.md) — Options for requesting an image asset with or without adjustments, used by the [version](phimagerequestoptions/version.md) property.
- [deliveryMode](phimagerequestoptions/deliverymode.md) — The requested image quality and delivery priority.
- [PHImageRequestOptionsDeliveryMode](phimagerequestoptionsdeliverymode.md) — Options for delivering requested image data, used by the [deliveryMode](phimagerequestoptions/deliverymode.md) property.
- [resizeMode](phimagerequestoptions/resizemode.md) — A mode that specifies how to resize the requested image.
- [PHImageRequestOptionsResizeMode](phimagerequestoptionsresizemode.md) — Options for how to resize the requested image to fit a target size, used by the [resizeMode](phimagerequestoptions/resizemode.md) property.
- [normalizedCropRect](phimagerequestoptions/normalizedcroprect.md) — A rectangle for requesting a cropped version of the original image.

### Fetching Image Data from iCloud

- [networkAccessAllowed](phimagerequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested image from iCloud.
- [progressHandler](phimagerequestoptions/progresshandler.md) — A block that Photos calls periodically while downloading the image.
- [PHAssetImageProgressHandler](phassetimageprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](phimagerequestoptions/progresshandler.md) property.

### Instance Properties

- [allowSecondaryDegradedImage](phimagerequestoptions/allowsecondarydegradedimage.md)
- [preferHDR](phimagerequestoptions/preferhdr.md) — Request HDR image data if available (such as PQ/HLG formats).
- [targetHDRHeadroom](phimagerequestoptions/targethdrheadroom.md) — Target HDR headroom for image rendering.

## See Also

### Asset loading

- [Loading and Caching Assets and Thumbnails](../photokit/loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [PHImageManager](phimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails and asset data.
- [PHCachingImageManager](phcachingimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [PHVideoRequestOptions](phvideorequestoptions.md) — A set of options affecting the delivery of video asset data that you request from an image manager.
- [PHLivePhotoRequestOptions](phlivephotorequestoptions.md) — A set of options affecting the delivery of Live Photo assets you request from an image manager.
