---
title: PHAssetResourceType.adjustmentData
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcetype/adjustmentdata
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcetype/adjustmentdata'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcetype/adjustmentdata.json'
content_hash: 'sha256:2af3d37323777c8d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceType](../phassetresourcetype.md)

# PHAssetResourceType.adjustmentData

<sub>Case</sub>

Provides data for use in reconstructing recent edits to its asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case adjustmentData
```

## Discussion

When you edit the asset, Photos provides this data in the form of a [PHAdjustmentData](../phadjustmentdata.md) object.

## See Also

### Resource Types

- [PHAssetResourceTypePhoto](photo.md) — Provides the original photo data for its asset.
- [PHAssetResourceTypeVideo](video.md) — Provides the original video data for its asset.
- [PHAssetResourceTypeAudio](audio.md) — Provides the original audio data for its asset.
- [PHAssetResourceTypeAlternatePhoto](alternatephoto.md) — Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceTypeFullSizePhoto](fullsizephoto.md) — Provides a modified version of the original photo asset.
- [PHAssetResourceTypeFullSizeVideo](fullsizevideo.md) — Provides a modified version of the original video asset.
- [PHAssetResourceTypeAdjustmentBasePhoto](adjustmentbasephoto.md) — Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceTypePairedVideo](pairedvideo.md) — Provides the original video data component of a Live Photo asset.
- [PHAssetResourceTypeFullSizePairedVideo](fullsizepairedvideo.md) — Provides the current video data component of a Live Photo asset.
- [PHAssetResourceTypeAdjustmentBaseVideo](adjustmentbasevideo.md) — Provides an unaltered version of its video asset.
- [PHAssetResourceTypeAdjustmentBasePairedVideo](adjustmentbasepairedvideo.md) — Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.
