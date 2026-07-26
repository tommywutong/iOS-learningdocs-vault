---
title: PHAssetResourceType
framework: Photos
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 9.0+, iPadOS 9.0+, Mac Catalyst 13.1+, macOS 10.11+, tvOS 10.0+, visionOS 1.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/photos/phassetresourcetype
source_url: 'https://developer.apple.com/documentation/photos/phassetresourcetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/photos/phassetresourcetype.json'
content_hash: 'sha256:34731d8acb4afc1c'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Photos](../photos.md)

# PHAssetResourceType

<sub>Enumeration</sub>

Describes the relationship of an asset resource to its owning asset.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
enum PHAssetResourceType
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Resource Types

- [PHAssetResourceTypePhoto](phassetresourcetype/photo.md) — Provides the original photo data for its asset.
- [PHAssetResourceTypeVideo](phassetresourcetype/video.md) — Provides the original video data for its asset.
- [PHAssetResourceTypeAudio](phassetresourcetype/audio.md) — Provides the original audio data for its asset.
- [PHAssetResourceTypeAlternatePhoto](phassetresourcetype/alternatephoto.md) — Provides photo data that isn’t the primary form of its asset.
- [PHAssetResourceTypeFullSizePhoto](phassetresourcetype/fullsizephoto.md) — Provides a modified version of the original photo asset.
- [PHAssetResourceTypeFullSizeVideo](phassetresourcetype/fullsizevideo.md) — Provides a modified version of the original video asset.
- [PHAssetResourceTypeAdjustmentData](phassetresourcetype/adjustmentdata.md) — Provides data for use in reconstructing recent edits to its asset.
- [PHAssetResourceTypeAdjustmentBasePhoto](phassetresourcetype/adjustmentbasephoto.md) — Provides an unaltered version of its photo asset for use in for use in reconstructing recent edits.
- [PHAssetResourceTypePairedVideo](phassetresourcetype/pairedvideo.md) — Provides the original video data component of a Live Photo asset.
- [PHAssetResourceTypeFullSizePairedVideo](phassetresourcetype/fullsizepairedvideo.md) — Provides the current video data component of a Live Photo asset.
- [PHAssetResourceTypeAdjustmentBaseVideo](phassetresourcetype/adjustmentbasevideo.md) — Provides an unaltered version of its video asset.
- [PHAssetResourceTypeAdjustmentBasePairedVideo](phassetresourcetype/adjustmentbasepairedvideo.md) — Provides an unaltered version of the video data for a Live Photo asset for use in reconstructing recent edits.

### Enumeration Cases

- [PHAssetResourceTypePhotoProxy](phassetresourcetype/photoproxy.md)

### Initializers

- [init(rawValue:)](<phassetresourcetype/init(rawvalue_).md>)

## See Also

### Inspecting an Asset Resource

- [type](phassetresource/type.md) — The relationship of an asset resource to its owning asset.
- [contentType](phassetresource/contenttype.md) — The content type of the data associated with this asset resource (the data can be retrieved via `PHAssetResourceManager`)
- [assetLocalIdentifier](phassetresource/assetlocalidentifier.md) — The unique identifier the system associates for a local asset object.
- [uniformTypeIdentifier](phassetresource/uniformtypeidentifier.md) — The uniform type identifier for the asset resource’s image or video data. _(deprecated)_
- [originalFilename](phassetresource/originalfilename.md) — The original filename of the asset resource from when it was created or imported.
- [pixelHeight](phassetresource/pixelheight.md) — The height of the resource, in pixels.
- [pixelWidth](phassetresource/pixelwidth.md) — The width of the resource, in pixels.
