---
title: PHAssetMediaType
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetmediatype
source_url: 'https://developer.apple.com/documentation/photos/phassetmediatype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetmediatype.json'
content_hash: 'sha256:37659edfba7812df'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetMediaType

<sub>Enumeration</sub>

Identifies the general type of an asset, such as image or video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAssetMediaType
```

## Overview

You use these constants with the [PHAsset](phasset.md) and [PHContentEditingInput](phcontenteditinginput.md) classes to fetch specific types of assets or to identify an asset being edited.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Constants

- [PHAssetMediaTypeUnknown](phassetmediatype/unknown.md) — The asset’s type is unknown.
- [PHAssetMediaTypeImage](phassetmediatype/image.md) — The asset is a photo or other static image.
- [PHAssetMediaTypeVideo](phassetmediatype/video.md) — The asset is a video file.
- [PHAssetMediaTypeAudio](phassetmediatype/audio.md) — The asset is an audio file.

### Initializers

- [init(rawValue:)](<phassetmediatype/init(rawvalue_).md>)

## See Also

### Reading Asset Metadata

- [contentType](phasset/contenttype.md) — The type of image or video data that is presented for the asset
- [mediaType](phasset/mediatype.md) — The type of the asset, such as video or audio.
- [mediaSubtypes](phasset/mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [PHAssetMediaSubtype](phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [sourceType](phasset/sourcetype.md) — The means by which the asset enters the user’s Photos library.
- [PHAssetSourceType](phassetsourcetype.md) — The means by which an asset enters the Photos library.
- [pixelWidth](phasset/pixelwidth.md) — The width, in pixels, of the asset’s image or video data.
- [pixelHeight](phasset/pixelheight.md) — The height, in pixels, of the asset’s image or video data.
- [addedDate](phasset/addeddate.md) — The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [creationDate](phasset/creationdate.md) — The date and time of the asset’s creation.
- [modificationDate](phasset/modificationdate.md) — The date and time of the asset’s last modification.
- [location](phasset/location.md) — The location information for the asset.
- [duration](phasset/duration.md) — The duration, in seconds, of the video asset.
- [favorite](phasset/isfavorite.md) — A Boolean value that indicates whether the user marks the asset as a favorite.
- [hidden](phasset/ishidden.md) — A Boolean value that indicates whether the user hides the asset.
