---
title: duration
framework: Photos
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.13+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phasset/duration
source_url: 'https://developer.apple.com/documentation/photos/phasset/duration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/duration.json'
content_hash: 'sha256:eae4fa59a3f5e05b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# duration

<sub>Instance Property</sub>

The duration, in seconds, of the video asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var duration: TimeInterval { get }
```

## Discussion

For photo assets, the duration is always zero.

## See Also

### Reading Asset Metadata

- [contentType](contenttype.md) — The type of image or video data that is presented for the asset
- [mediaType](mediatype.md) — The type of the asset, such as video or audio.
- [PHAssetMediaType](../phassetmediatype.md) — Identifies the general type of an asset, such as image or video.
- [mediaSubtypes](mediasubtypes.md) — The subtypes of the asset, identifying special kinds of assets, such as panoramic photo or high-frame-rate video.
- [PHAssetMediaSubtype](../phassetmediasubtype.md) — Constants identifying specific variations of asset media, such as panorama or screenshot photos, and time-lapse or high-frame-rate video.
- [sourceType](sourcetype.md) — The means by which the asset enters the user’s Photos library.
- [PHAssetSourceType](../phassetsourcetype.md) — The means by which an asset enters the Photos library.
- [pixelWidth](pixelwidth.md) — The width, in pixels, of the asset’s image or video data.
- [pixelHeight](pixelheight.md) — The height, in pixels, of the asset’s image or video data.
- [addedDate](addeddate.md) — The date and time this asset was added to the photo library (from the device that was used to add this asset)
- [creationDate](creationdate.md) — The date and time of the asset’s creation.
- [modificationDate](modificationdate.md) — The date and time of the asset’s last modification.
- [location](location.md) — The location information for the asset.
- [favorite](isfavorite.md) — A Boolean value that indicates whether the user marks the asset as a favorite.
- [hidden](ishidden.md) — A Boolean value that indicates whether the user hides the asset.
