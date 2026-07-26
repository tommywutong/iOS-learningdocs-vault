---
title: previewPixelBuffer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/previewpixelbuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/previewpixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/previewpixelbuffer.json'
content_hash: 'sha256:1dd6039853f66cf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# previewPixelBuffer

<sub>Instance Property</sub>

The pixel data for a preview-sized version of the photo, if requested.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var previewPixelBuffer: CVPixelBuffer? { get }
```

## Discussion

If you requested a preview image by specifying the [previewPhotoFormat](../avcapturephotosettings/previewphotoformat.md) property of your photo settings when requesting capture, this property offers access to the resulting preview image pixel data. The pixel buffer contains only the minimal attachments required for correct display. If you did not request a preview image, this property’s value is `nil`.

## See Also

### Accessing preview photo data

- [embeddedThumbnailPhotoFormat](embeddedthumbnailphotoformat.md) — A dictionary describing the data format for a preview-sized image accompanying the captured photo.
