---
title: embeddedThumbnailPhotoFormat
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/embeddedthumbnailphotoformat
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/embeddedthumbnailphotoformat'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/embeddedthumbnailphotoformat.json'
content_hash: 'sha256:4c369c6beeaeb49a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# embeddedThumbnailPhotoFormat

<sub>Instance Property</sub>

A dictionary describing the data format for a preview-sized image accompanying the captured photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var embeddedThumbnailPhotoFormat: [String : Any]? { get }
```

## Discussion

See [Video settings](../video-settings.md) for possible keys and values.

If you requested an embedded thumbnail image by specifying the [embeddedThumbnailPhotoFormat](../avcapturephotosettings/embeddedthumbnailphotoformat.md) property of your photo settings when requesting capture, this property’s value is the resolved video settings dictionary for the embedded thumbnail image. If you did not request an embedded thumbnail image, this property’s value is `nil`.

## See Also

### Accessing preview photo data

- [previewPixelBuffer](previewpixelbuffer.md) — The pixel data for a preview-sized version of the photo, if requested.
