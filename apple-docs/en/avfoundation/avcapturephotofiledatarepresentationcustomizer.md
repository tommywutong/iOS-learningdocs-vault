---
title: AVCapturePhotoFileDataRepresentationCustomizer
framework: AVFoundation
symbol_kind: protocol
role: symbol
role_heading: Protocol
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotofiledatarepresentationcustomizer.json'
content_hash: 'sha256:ed09674e224a0f14'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md)

# AVCapturePhotoFileDataRepresentationCustomizer

<sub>Protocol</sub>

A protocol that defines the methods to implement to customize the packaging of photo data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
protocol AVCapturePhotoFileDataRepresentationCustomizer : NSObjectProtocol
```

## Overview

AVCapturePhoto is a wrapper representing a photo in a file container. To flatten the photo to an [NSData](../foundation/nsdata.md) object to write to file, call [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>). For more complex flattening operations such as replacing or stripping metadata, call [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>) and provide a delegate for customized replacement or stripping behavior. This delegate’s methods are called synchronously before the flattening process begins.

## Relationships

- **Inherits From**: [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Replacing or removing metadata

- [- replacementMetadataForPhoto:](<avcapturephotofiledatarepresentationcustomizer/replacementmetadata(for_).md>) — A callback in which you can provide replacement metadata or direct [AVCapturePhoto](avcapturephoto.md) to strip existing metadata from the flattened file.
- [- replacementEmbeddedThumbnailPixelBufferWithPhotoFormat:forPhoto:](<avcapturephotofiledatarepresentationcustomizer/replacementembeddedthumbnailpixelbuffer(withphotoformat_for_).md>) — A callback in which you can provide a replacement embedded thumbnail image with compression settings, or strip the existing embedded thumbnail image from the flattened file.
- [- replacementDepthDataForPhoto:](<avcapturephotofiledatarepresentationcustomizer/replacementdepthdata(for_).md>) — A callback in which you can provide replacement depth data or strip existing depth data from the file.
- [- replacementPortraitEffectsMatteForPhoto:](<avcapturephotofiledatarepresentationcustomizer/replacementportraiteffectsmatte(for_).md>) — A callback in which you can provide a replacement portrait effects matte, or strip the existing portrait effects matte from the file.
- [- replacementSemanticSegmentationMatteOfType:forPhoto:](<avcapturephotofiledatarepresentationcustomizer/replacementsemanticsegmentationmatte(oftype_for_).md>) — Replaces or removes the semantic segmentation matte of the specified type from the flattened file data representation.
- [- replacementAppleProRAWCompressionSettingsForPhoto:defaultSettings:maximumBitDepth:](<avcapturephotofiledatarepresentationcustomizer/replacementappleprorawcompressionsettings(for_defaultsettings_maximumbitdepth_).md>) — Replaces the compression settings the system uses when writing Apple ProRAW data to a Linear DNG file.

## See Also

### Packaging data for file output

- [- fileDataRepresentationWithCustomizer:](<avcapturephoto/filedatarepresentation(with_).md>) — Gets a customized representation of the photo data.
- [- fileDataRepresentation](<avcapturephoto/filedatarepresentation().md>) — Generates and returns a flat data representation of the photo and its attachments.
- [- CGImageRepresentation](<avcapturephoto/cgimagerepresentation().md>) — Extracts and returns the captured photo’s primary image as a Core Graphics image object.
- [- previewCGImageRepresentation](<avcapturephoto/previewcgimagerepresentation().md>) — Extracts and returns the captured photo’s preview image as a Core Graphics image object.
- [- fileDataRepresentationWithReplacementMetadata:replacementEmbeddedThumbnailPhotoFormat:replacementEmbeddedThumbnailPixelBuffer:replacementDepthData:](<avcapturephoto/filedatarepresentation(withreplacementmetadata_replacementembeddedthumbnailphotoformat_replacementembeddedthumbnailpixelbuffer_replacementdepthdata_).md>) — Generates and returns a flat data representation of the photo using the specified replacements for some or all of its attachments. _(deprecated)_
