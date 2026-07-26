---
title: PHAsset.Rating
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 27.0+ beta, iPadOS 27.0+ beta, Mac Catalyst 27.0+ beta, macOS 27.0+ beta, tvOS 27.0+ beta, visionOS 27.0+ beta]
languages: [swift]
beta: true
deprecated: false
doc_path: /documentation/photos/phasset/rating-swift.enum
source_url: 'https://developer.apple.com/documentation/photos/phasset/rating-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phasset/rating-swift.enum.json'
content_hash: 'sha256:86bfb8159deddcfc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAsset](../phasset.md)

# PHAsset.Rating

<sub>Enumeration</sub>

A rating for an asset, from unset (no rating chosen) up to five stars.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum Rating
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Ratings

- [PHAssetRatingUnset](rating-swift.enum/unset.md)
- [PHAssetRatingOne](rating-swift.enum/one.md)
- [PHAssetRatingTwo](rating-swift.enum/two.md)
- [PHAssetRatingThree](rating-swift.enum/three.md)
- [PHAssetRatingFour](rating-swift.enum/four.md)
- [PHAssetRatingFive](rating-swift.enum/five.md)

### Initializers

- [init(rawValue:)](<rating-swift.enum/init(rawvalue_).md>) _(beta)_

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
- [duration](duration.md) — The duration, in seconds, of the video asset.
- [favorite](isfavorite.md) — A Boolean value that indicates whether the user marks the asset as a favorite.
