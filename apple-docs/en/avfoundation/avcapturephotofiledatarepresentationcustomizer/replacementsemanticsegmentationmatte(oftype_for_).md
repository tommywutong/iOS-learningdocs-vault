---
title: 'replacementSemanticSegmentationMatte(ofType:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte%28oftype%3Afor%3A%29.json'
content_hash: 'sha256:c0b39423931597b3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md)

# replacementSemanticSegmentationMatte(ofType:for:)

<sub>Instance Method</sub>

Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func replacementSemanticSegmentationMatte(ofType semanticSegmentationMatteType: AVSemanticSegmentationMatte.MatteType, for photo: AVCapturePhoto) -> AVSemanticSegmentationMatte?
```

## Parameters

- `semanticSegmentationMatteType` — The type of semantic segmentation matte to be replaced or stripped.

- `photo` — The calling instance of [AVCapturePhoto](../avcapturephoto.md).

## Return Value

An instance of [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md). To preserve the existing matte, return `photo.```AVCapturePhoto/semanticSegmentationMatte(for:)``. To strip the existing one, return `nil`. To replace, provide a replacement [AVSemanticSegmentationMatte](../avsemanticsegmentationmatte.md) instance.

## Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing semantic segmentation matte of the specified type in the in-memory [AVCapturePhoto](../avcapturephoto.md) container is written to the file data representation.

## See Also

### Replacing or removing metadata

- [- replacementMetadataForPhoto:](<replacementmetadata(for_).md>) — A callback in which you can provide replacement metadata or direct [AVCapturePhoto](../avcapturephoto.md) to strip existing metadata from the flattened file.
- [- replacementEmbeddedThumbnailPixelBufferWithPhotoFormat:forPhoto:](<replacementembeddedthumbnailpixelbuffer(withphotoformat_for_).md>) — A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [- replacementDepthDataForPhoto:](<replacementdepthdata(for_).md>) — A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [- replacementPortraitEffectsMatteForPhoto:](<replacementportraiteffectsmatte(for_).md>) — A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [- replacementAppleProRAWCompressionSettingsForPhoto:defaultSettings:maximumBitDepth:](<replacementappleprorawcompressionsettings(for_defaultsettings_maximumbitdepth_).md>) — Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.
