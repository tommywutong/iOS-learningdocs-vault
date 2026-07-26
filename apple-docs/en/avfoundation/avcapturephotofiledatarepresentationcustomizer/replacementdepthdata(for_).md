---
title: 'replacementDepthData(for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementdepthdata%28for%3A%29.json'
content_hash: 'sha256:55f8aed7ec503004'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md)

# replacementDepthData(for:)

<sub>Instance Method</sub>

A callback in which you can provide replacement depth data or strip existing depth data from the file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func replacementDepthData(for photo: AVCapturePhoto) -> AVDepthData?
```

## Parameters

- `photo` — The calling instance of [AVCapturePhoto](../avcapturephoto.md) whose file metadata you’re modifying.

## Return Value

An instance of [AVDepthData](../avdepthdata.md).  To preserve the existing depth data, return `photo.depthData`. To strip existing depth data, provide a replacement [AVDepthData](../avdepthdata.md) instance.

## Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing metadata in the in-memory [AVCapturePhoto](../avcapturephoto.md) container is written directly to the file data representation.

## See Also

### Replacing or removing metadata

- [- replacementMetadataForPhoto:](<replacementmetadata(for_).md>) — A callback in which you can provide replacement metadata or direct [AVCapturePhoto](../avcapturephoto.md) to strip existing metadata from the flattened file.
- [- replacementEmbeddedThumbnailPixelBufferWithPhotoFormat:forPhoto:](<replacementembeddedthumbnailpixelbuffer(withphotoformat_for_).md>) — A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [- replacementPortraitEffectsMatteForPhoto:](<replacementportraiteffectsmatte(for_).md>) — A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [- replacementSemanticSegmentationMatteOfType:forPhoto:](<replacementsemanticsegmentationmatte(oftype_for_).md>) — Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [- replacementAppleProRAWCompressionSettingsForPhoto:defaultSettings:maximumBitDepth:](<replacementappleprorawcompressionsettings(for_defaultsettings_maximumbitdepth_).md>) — Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.
