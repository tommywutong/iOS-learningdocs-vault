---
title: 'replacementAppleProRAWCompressionSettings(for:defaultSettings:maximumBitDepth:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 14.3+, iPadOS 14.3+, Mac Catalyst 14.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for:defaultsettings:maximumbitdepth:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings%28for%3Adefaultsettings%3Amaximumbitdepth%3A%29.json'
content_hash: 'sha256:ba3ab5425110dc4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoFileDataRepresentationCustomizer](../avcapturephotofiledatarepresentationcustomizer.md)

# replacementAppleProRAWCompressionSettings(for:defaultSettings:maximumBitDepth:)

<sub>Instance Method</sub>

Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
optional func replacementAppleProRAWCompressionSettings(for photo: AVCapturePhoto, defaultSettings: [String : Any], maximumBitDepth: Int) -> [String : Any]
```

## Parameters

- `photo` — The calling photo instance.

- `defaultSettings` — The default settings to use, if not overridden.

- `maximumBitDepth` — The maximum bit depth you can specify in the returned settings dictionary.

## Return Value

A dictionary that contains the replacement compression settings.

## Discussion

The system calls this method when writing an Apple ProRAW image to a DNG file. To configure the compression settings the system uses when writing the file, return a dictionary that contains values for the following keys:

- [AVVideoQualityKey](../avvideoqualitykey.md). A floating-point value from 0.0 to 1.0. Specify a value of 1.0 to use lossless compression, or less than 1.0 for lossy compression.
- [AVVideoAppleProRAWBitDepthKey](../avvideoappleprorawbitdepthkey.md). An integer value from 8 to `maximumBitDepth`. Setting this key to a value less than the value specified in `defaultSettings` may result in quantization losses.

Any keys not specified in the returned dictionary use the values from the `defaultSettings` dictionary. If your delegate object doesn’t implement this method, the system uses the default compression settings for DNG files.

## See Also

### Replacing or removing metadata

- [- replacementMetadataForPhoto:](<replacementmetadata(for_).md>) — A callback in which you can provide replacement metadata or direct [AVCapturePhoto](../avcapturephoto.md) to strip existing metadata from the flattened file.
- [- replacementEmbeddedThumbnailPixelBufferWithPhotoFormat:forPhoto:](<replacementembeddedthumbnailpixelbuffer(withphotoformat_for_).md>) — A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [- replacementDepthDataForPhoto:](<replacementdepthdata(for_).md>) — A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [- replacementPortraitEffectsMatteForPhoto:](<replacementportraiteffectsmatte(for_).md>) — A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [- replacementSemanticSegmentationMatteOfType:forPhoto:](<replacementsemanticsegmentationmatte(oftype_for_).md>) — Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
