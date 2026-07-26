---
title: PHAssetResourceType.fullSizePairedVideo
framework: Photos
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 13.1+, macOS 10.15+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcetype/fullsizepairedvideo
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcetype/fullsizepairedvideo'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcetype/fullsizepairedvideo.json'
content_hash: 'sha256:cc8329cceca416e0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Photos](../../photos.md) · [PHAssetResourceType](../phassetresourcetype.md)

# PHAssetResourceType.fullSizePairedVideo

<sub>Case</sub>

Provides the current video data component of a Live Photo asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
case fullSizePairedVideo
```

## Discussion

This asset resource type appears when fetching the asset resources associated with a Live Photo asset. This resource type represents the current rendered output, if any, for an edited Live Photo asset. The corresponding still image can be found in the [PHAssetResourceTypeFullSizePhoto](fullsizephoto.md) resource type.

## See Also

### Resource Types

- [PHAssetResourceTypePhoto](photo.md) — Provides the original photo data for its asset.
- [PHAssetResourceTypeVideo](video.md) — Provides the original video data for its asset.
- [PHAssetResourceTypeAudio](audio.md) — Provides the original audio data for its asset.
- [PHAssetResourceTypeAlternatePhoto](alternatephoto.md) — Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceTypeFullSizePhoto](fullsizephoto.md) — Provides a modified version of the original photo asset.
- [PHAssetResourceTypeFullSizeVideo](fullsizevideo.md) — Provides a modified version of the original video asset.
- [PHAssetResourceTypeAdjustmentData](adjustmentdata.md) — Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceTypeAdjustmentBasePhoto](adjustmentbasephoto.md) — Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceTypePairedVideo](pairedvideo.md) — Provides the original video data component of a Live Photo asset.
- [PHAssetResourceTypeAdjustmentBaseVideo](adjustmentbasevideo.md) — Provides an unaltered version of its video asset.
- [PHAssetResourceTypeAdjustmentBasePairedVideo](adjustmentbasepairedvideo.md) — Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.
