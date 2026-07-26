---
title: availableEmbeddedThumbnailPhotoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/availableembeddedthumbnailphotocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availableembeddedthumbnailphotocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/availableembeddedthumbnailphotocodectypes.json'
content_hash: 'sha256:aef0af2776b6384f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# availableEmbeddedThumbnailPhotoCodecTypes

<sub>Instance Property</sub>

An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType] { get }
```

## Discussion

To enable embedding thumbnail images in photo file output, set the [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) property using one of the codec types listed in this array.

The order of this array is such that the most backward-compatible codec is listed first.

## See Also

### Enabling preview and thumbnail delivery

- [previewPhotoFormat](previewphotoformat.md) — A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-30d9.md) — An array of available of pixel format types available to specify a preview photo format.
- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [availableRawEmbeddedThumbnailPhotoCodecTypes](availablerawembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [rawEmbeddedThumbnailPhotoFormat](rawembeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
