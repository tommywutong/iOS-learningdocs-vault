---
title: PHAssetSourceType
framework: Photos
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetsourcetype
source_url: 'https://developer.apple.com/documentation/photos/phassetsourcetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetsourcetype.json'
content_hash: 'sha256:2558ce9eeefafa61'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetSourceType

<sub>Structure</sub>

The means by which an asset enters the Photos library.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
struct PHAssetSourceType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [ExpressibleByArrayLiteral](../swift/expressiblebyarrayliteral.md), [OptionSet](../swift/optionset.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md), [SetAlgebra](../swift/setalgebra.md)

## Topics

### Initializers

- [init(rawValue:)](<phassetsourcetype/init(rawvalue_).md>) — Initializes an asset source type from a raw value.

### Constants

- [PHAssetSourceTypeUserLibrary](phassetsourcetype/typeuserlibrary.md) — The asset is part of the user’s main Photos library.
- [PHAssetSourceTypeCloudShared](phassetsourcetype/typecloudshared.md) — The asset originates from an iCloud Shared Album.
- [PHAssetSourceTypeiTunesSynced](phassetsourcetype/typeitunessynced.md) — The asset originates from a Mac or PC and is present on the device through iTunes sync.

## See Also

### Reading Asset Metadata

- [contentType](phasset/contenttype.md) — The type of image or video data that is presented for the asset
- [mediaType](phasset/mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](phasset/mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [PHAssetMediaSubtype](phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [sourceType](phasset/sourcetype.md) — The means by which the asset enters the user’s Photos library.
- [pixelWidth](phasset/pixelwidth.md) — The width, in pixels, of the asset’s image or video data.
- [pixelHeight](phasset/pixelheight.md) — The height, in pixels, of the asset’s image or video data.
- [addedDate](phasset/addeddate.md) — The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [creationDate](phasset/creationdate.md) — The date and time of the asset’s creation.
- [modificationDate](phasset/modificationdate.md) — The date and time of the asset’s last modification.
- [location](phasset/location.md) — The location information for the asset.
- [duration](phasset/duration.md) — The duration, in seconds, of the video asset.
- [favorite](phasset/isfavorite.md) — A Boolean value that indicates whether the user marks the asset as a favorite.
- [hidden](phasset/ishidden.md) — A Boolean value that indicates whether the user hides the asset.
