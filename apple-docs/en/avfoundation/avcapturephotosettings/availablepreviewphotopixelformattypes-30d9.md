---
title: availablePreviewPhotoPixelFormatTypes
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-30d9
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-30d9'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/availablepreviewphotopixelformattypes-30d9.json'
content_hash: 'sha256:d7cb4f2f81999fc1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# availablePreviewPhotoPixelFormatTypes

<sub>Instance Property</sub>

An array of available of pixel format types available to specify a preview photo format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var availablePreviewPhotoPixelFormatTypes: [OSType] { get }
```

## Discussion

The array is sorted so that preview formats requiring fewer conversions come first.

## See Also

### Enabling preview and thumbnail delivery

- [previewPhotoFormat](previewphotoformat.md) — A dictionary describing the format for delivery of preview-sized images alongside the main photo.
- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of thumbnail images embedded in photo file output.
- [availableRawEmbeddedThumbnailPhotoCodecTypes](availablerawembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding raw thumbnail images in photo file output.
- [rawEmbeddedThumbnailPhotoFormat](rawembeddedthumbnailphotoformat.md) — A dictionary describing the format for delivery of raw thumbnail images embedded in photo file output.
- [availableEmbeddedThumbnailPhotoCodecTypes](availableembeddedthumbnailphotocodectypes.md) — An array of video codec types compatible with the photo settings for embedding thumbnail images in photo file output.
