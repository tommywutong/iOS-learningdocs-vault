---
title: rawEmbeddedThumbnailPhotoFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/rawembeddedthumbnailphotoformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/rawembeddedthumbnailphotoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/rawembeddedthumbnailphotoformat.json'
content_hash: 'sha256:e0bcaa5cd02deb82'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# rawEmbeddedThumbnailPhotoFormat

<sub>Instance Property</sub>

A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var rawEmbeddedThumbnailPhotoFormat: [String : Any]? { get set }
```

## See Also

### Enabling preview and thumbnail delivery

- [previewPhotoFormat](previewphotoformat.md) — A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [availablePreviewPhotoPixelFormatTypes](availablepreviewphotopixelformattypes-30d9.md) — An array of available of pixel format types available to specify a preview photo format.
- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [availableRawEmbeddedThumbnailPhotoCodecTypes](availablerawembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
