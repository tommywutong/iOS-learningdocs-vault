---
title: PHLivePhotoRequestOptions
framework: Photos
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 9.1+, iPadOS 9.1+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phlivephotorequestoptions
source_url: 'https://developer.apple.com/documentation/photos/phlivephotorequestoptions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phlivephotorequestoptions.json'
content_hash: 'sha256:b6d5ccccfd04880d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHLivePhotoRequestOptions

<sub>Class</sub>

A set of options affecting the delivery of Live Photo assets you request from an image manager.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class PHLivePhotoRequestOptions
```

## Overview

A Live Photo is a picture that includes movement and sound from the moments just before and after its capture.

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Specifying Image Request Options

- [version](phlivephotorequestoptions/version.md) — The version of the Live Photo to be requested.
- [deliveryMode](phlivephotorequestoptions/deliverymode.md) — The requested Live Photo quality and delivery priority.

### Fetching Image Data from iCloud

- [networkAccessAllowed](phlivephotorequestoptions/isnetworkaccessallowed.md) — A Boolean value that specifies whether Photos can download the requested Live Photo data from iCloud.
- [progressHandler](phlivephotorequestoptions/progresshandler.md) — A block that Photos calls periodically while downloading the Live Photo.

### Instance Properties

- [preferHDR](phlivephotorequestoptions/preferhdr.md) — Request HDR image data if available (such as PQ/HLG formats).

## See Also

### Asset loading

- [Loading and Caching Assets and Thumbnails](../photokit/loading-and-caching-assets-and-thumbnails.md) — Request image, video, or Live Photos content, and cache for quick reuse.
- [PHImageManager](phimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails and asset data.
- [PHCachingImageManager](phcachingimagemanager.md) — An object that facilitates retrieving or generating preview thumbnails, optimized for batch preloading large numbers of assets.
- [PHImageRequestOptions](phimagerequestoptions.md) — A set of options affecting the delivery of still image representations of Photos assets you request from an image manager.
- [PHVideoRequestOptions](phvideorequestoptions.md) — A set of options affecting the delivery of video asset data that you request from an image manager.
