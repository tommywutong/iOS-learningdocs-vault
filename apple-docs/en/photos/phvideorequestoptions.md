---
title: PHVideoRequestOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phvideorequestoptions
source_url: 'https://developer.apple.com/documentation/photos/phvideorequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phvideorequestoptions.json'
content_hash: 'sha256:e677b1d7118d9a20'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHVideoRequestOptions

<sub>Class</sub>

A set of options affecting the delivery of video asset data that you request from an image manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHVideoRequestOptions
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying Video Request Options

- [version](phvideorequestoptions/version.md) — The version of the video to request.
- [PHVideoRequestOptionsVersion](phvideorequestoptionsversion.md) — Options for requesting a video asset with or without adjustments, used by the [version](phvideorequestoptions/version.md) property.
- [deliveryMode](phvideorequestoptions/deliverymode.md) — A mode specifying the requested video quality and delivery priority.
- [PHVideoRequestOptionsDeliveryMode](phvideorequestoptionsdeliverymode.md) — Options for delivering requested video data, used by the [deliveryMode](phvideorequestoptions/deliverymode.md) property.

### Fetching Video Data from iCloud

- [networkAccessAllowed](phvideorequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested video from iCloud.
- [progressHandler](phvideorequestoptions/progresshandler.md) — A block Photos calls periodically while downloading the video.
- [PHAssetVideoProgressHandler](phassetvideoprogresshandler.md) — The signature for a block that Photos calls while downloading asset data from iCloud. Used by the [progressHandler](phvideorequestoptions/progresshandler.md) property.

## See Also

### Asset loading

- [Loading and Caching Assets and Thumbnails](../photokit/loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [PHImageManager](phimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails and asset data.
- [PHCachingImageManager](phcachingimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [PHImageRequestOptions](phimagerequestoptions.md) — A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [PHLivePhotoRequestOptions](phlivephotorequestoptions.md) — A set of options affecting the delivery of Live Photo assets you request from an image manager.
