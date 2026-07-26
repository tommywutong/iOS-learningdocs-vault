---
title: availableRawEmbeddedThumbnailPhotoCodecTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/availablerawembeddedthumbnailphotocodectypes.json'
content_hash: 'sha256:571fa8b0dca6b065'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# availableRawEmbeddedThumbnailPhotoCodecTypes

<sub>Instance Property</sub>

An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var availableRawEmbeddedThumbnailPhotoCodecTypes: [AVVideoCodecType] { get }
```

## See Also

### Enabling preview and thumbnail delivery

- [previewPhotoFormat](previewphotoformat.md) — A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-30d9.md) — An array of available of pixel format types available to specify a preview photo format.
- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [rawEmbeddedThumbnailPhotoFormat](rawembeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
