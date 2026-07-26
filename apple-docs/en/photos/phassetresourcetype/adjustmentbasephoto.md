---
title: PHAssetResourceType.adjustmentBasePhoto
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcetype/adjustmentbasephoto
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcetype/adjustmentbasephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcetype/adjustmentbasephoto.json'
content_hash: 'sha256:33fd1bc2fc09bae2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceType](../phassetresourcetype.md)

# PHAssetResourceType.adjustmentBasePhoto

<sub>Case</sub>

Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case adjustmentBasePhoto
```

## Discussion

When you edit an asset, you have the option of resuming the most recent edit made. This process uses a [PHAdjustmentData](../phadjustmentdata.md) object to describe the edit, and an extra copy of the photo data representing the state of the asset before the edit. For details, see [PHAsset](../phasset.md).

## See Also

### Resource Types

- [PHAssetResourceTypePhoto](photo.md) — Provides the original photo data for its asset.
- [PHAssetResourceTypeVideo](video.md) — Provides the original video data for its asset.
- [PHAssetResourceTypeAudio](audio.md) — Provides the original audio data for its asset.
- [PHAssetResourceTypeAlternatePhoto](alternatephoto.md) — Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceTypeFullSizePhoto](fullsizephoto.md) — Provides a modified version of the original photo asset.
- [PHAssetResourceTypeFullSizeVideo](fullsizevideo.md) — Provides a modified version of the original video asset.
- [PHAssetResourceTypeAdjustmentData](adjustmentdata.md) — Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceTypePairedVideo](pairedvideo.md) — Provides the original video data component of a Live Photo asset.
- [PHAssetResourceTypeFullSizePairedVideo](fullsizepairedvideo.md) — Provides the current video data component of a Live Photo asset.
- [PHAssetResourceTypeAdjustmentBaseVideo](adjustmentbasevideo.md) — Provides an unaltered version of its video asset.
- [PHAssetResourceTypeAdjustmentBasePairedVideo](adjustmentbasepairedvideo.md) — Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.
