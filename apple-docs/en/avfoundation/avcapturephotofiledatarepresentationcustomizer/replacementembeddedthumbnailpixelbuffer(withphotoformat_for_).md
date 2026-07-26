---
title: 'replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat:for:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat:for:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer%28withphotoformat%3Afor%3A%29.json'
content_hash: 'sha256:f61ee317939297aa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md)

# replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat:for:)

<sub>Instance Method</sub>

A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func replacementEmbeddedThumbnailPixelBuffer(withPhotoFormat replacementEmbeddedThumbnailPhotoFormatOut: AutoreleasingUnsafeMutablePointer<NSDictionary?>, for photo: AVCapturePhoto) -> Unmanaged<CVPixelBuffer>?
```

## Parameters

- `replacementEmbeddedThumbnailPhotoFormatOut` — A pointer to a dictionary of keys and values from `AVFoundation/AVVideoSettings.h`.  If you pass a non-nil dictionary, [AVVideoCodecKey](../avvideocodeckey.md) is required, with `width` and `height` keys optional.

- `photo` — The calling instance of [AVCapturePhoto](../avcapturephoto.md) whose file metadata you’re modifying.

## Return Value

A pixel buffer containing a source image to be encoded to the file as the replacement thumbnail image. To preserve the existing embedded thumbnail photo to the flattened data, set `replacementEmbeddedThumbnailPhotoFormatOut` to `photo.embeddedThumbnailPhotoFormat` and return `nil`. To replace the existing embedded thumbnail, pass a replacement photo format dictionary and return a non-`nil` replacement pixel buffer.  To remove the existing embedded thumbnail, set `replacementEmbeddedThumbnailPhotoFormatOut` to `nil` and return `nil`.

## Discussion

This callback is optional. If your delegate doesn’t implement this callback, the existing metadata in the in-memory [AVCapturePhoto](../avcapturephoto.md) container is written directly to the file data representation.

## See Also

### Replacing or removing metadata

- [- replacementMetadataForPhoto:](<replacementmetadata(for_).md>) — A callback in which you can provide replacement metadata or direct [AVCapturePhoto](../avcapturephoto.md) to strip existing metadata from the flattened file.
- [- replacementDepthDataForPhoto:](<replacementdepthdata(for_).md>) — A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [- replacementPortraitEffectsMatteForPhoto:](<replacementportraiteffectsmatte(for_).md>) — A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [- replacementSemanticSegmentationMatteOfType:forPhoto:](<replacementsemanticsegmentationmatte(oftype_for_).md>) — Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [- replacementAppleProRAWCompressionSettingsForPhoto:defaultSettings:maximumBitDepth:](<replacementappleprorawcompressionsettings(for_defaultsettings_maximumbitdepth_).md>) — Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.
