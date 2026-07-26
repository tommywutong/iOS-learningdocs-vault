---
title: PHAssetMediaSubtype
framework: Photos
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetmediasubtype
source_url: 'https://developer.apple.com/documentation/photos/phassetmediasubtype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetmediasubtype.json'
content_hash: 'sha256:9e067b54bf851431'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetMediaSubtype

<sub>Structure</sub>

Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct PHAssetMediaSubtype
```

## Overview

You use these constants with the [PHAsset](phasset.md) and [PHContentEditingInput](phcontenteditinginput.md) classes to fetch specific types of assets or to identify an asset being edited.

Media subtypes are [OptionSet](../swift/optionset.md) values, so you can combine them using set literal syntax to test for multiple subtypes.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<phassetmediasubtype/init(rawvalue_).md>) — Initializes a media subtype from a raw value.

### Media Subtypes

- [PHAssetMediaSubtypePhotoPanorama](phassetmediasubtype/photopanorama.md) — The asset is a large-format panorama photo.
- [PHAssetMediaSubtypePhotoHDR](phassetmediasubtype/photohdr.md) — The asset is a high-dynamic range photo.
- [PHAssetMediaSubtypePhotoScreenshot](phassetmediasubtype/photoscreenshot.md) — The asset is an image captured with the device’s screenshot feature.
- [PHAssetMediaSubtypePhotoLive](phassetmediasubtype/photolive.md) — The asset is a Live Photo that includes movement and sounds from the moments just before and after its capture.
- [PHAssetMediaSubtypeVideoCinematic](phassetmediasubtype/videocinematic.md) — The asset is a cinematic video.
- [PHAssetMediaSubtypeVideoStreamed](phassetmediasubtype/videostreamed.md) — The asset is a video with contents that always stream over a network connection.
- [PHAssetMediaSubtypeVideoHighFrameRate](phassetmediasubtype/videohighframerate.md) — The asset is a high-frame-rate video.
- [PHAssetMediaSubtypeVideoTimelapse](phassetmediasubtype/videotimelapse.md) — The asset is a time-lapse video.
- [PHAssetMediaSubtypePhotoDepthEffect](phassetmediasubtype/photodeptheffect.md) — The asset is a photo captured with the Camera app’s Portrait mode depth effect.

### Type Properties

- [PHAssetMediaSubtypePhotoAnimation](phassetmediasubtype/photoanimation.md)
- [PHAssetMediaSubtypeSpatialMedia](phassetmediasubtype/spatialmedia.md)
- [PHAssetMediaSubtypeVideoScreenRecording](phassetmediasubtype/videoscreenrecording.md) — The media subtype is a photo animation such as a GIF, animated PNGs, etc.

## See Also

### Reading Asset Metadata

- [contentType](phasset/contenttype.md) — The type of image or video data that is presented for the asset
- [mediaType](phasset/mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](phasset/mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
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
