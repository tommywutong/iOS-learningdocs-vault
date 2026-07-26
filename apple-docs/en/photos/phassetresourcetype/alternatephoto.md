---
title: PHAssetResourceType.alternatePhoto
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcetype/alternatephoto
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcetype/alternatephoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcetype/alternatephoto.json'
content_hash: 'sha256:17afd509d9cf921e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceType](../phassetresourcetype.md)

# PHAssetResourceType.alternatePhoto

<sub>Case</sub>

Provides photo data that isn’t the primary form of its asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case alternatePhoto
```

## Discussion

For example, a photo asset imported from an external camera may contain both a JPEG file (the primary form of the asset) and a RAW file (the alternate photo).

## See Also

### Resource Types

- [PHAssetResourceTypePhoto](photo.md) — Provides the original photo data for its asset.
- [PHAssetResourceTypeVideo](video.md) — Provides the original video data for its asset.
- [PHAssetResourceTypeAudio](audio.md) — Provides the original audio data for its asset.
- [PHAssetResourceTypeFullSizePhoto](fullsizephoto.md) — Provides a modified version of the original photo asset.
- [PHAssetResourceTypeFullSizeVideo](fullsizevideo.md) — Provides a modified version of the original video asset.
- [PHAssetResourceTypeAdjustmentData](adjustmentdata.md) — Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceTypeAdjustmentBasePhoto](adjustmentbasephoto.md) — Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceTypePairedVideo](pairedvideo.md) — Provides the original video data component of a Live Photo asset.
- [PHAssetResourceTypeFullSizePairedVideo](fullsizepairedvideo.md) — Provides the current video data component of a Live Photo asset.
- [PHAssetResourceTypeAdjustmentBaseVideo](adjustmentbasevideo.md) — Provides an unaltered version of its video asset.
- [PHAssetResourceTypeAdjustmentBasePairedVideo](adjustmentbasepairedvideo.md) — Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.
