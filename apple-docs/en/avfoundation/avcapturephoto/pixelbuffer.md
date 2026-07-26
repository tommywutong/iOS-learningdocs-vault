---
title: pixelBuffer
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, macOS 10.15+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/pixelbuffer
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/pixelbuffer'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/pixelbuffer.json'
content_hash: 'sha256:549b8eb95eb719be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# pixelBuffer

<sub>Instance Property</sub>

The uncompressed or RAW image sample buffer for the photo, if requested.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var pixelBuffer: CVPixelBuffer? { get }
```

## Discussion

If you requested photo capture in a RAW format, or in a processed format without compression such as TIFF, you can use this property to access the underlying sample buffer.

If you requested capture in a compressed format such as JPEG or HEVC/HEIF, this property’s value is `nil`. Use the [- fileDataRepresentation](<filedatarepresentation().md>) or [- CGImageRepresentation](<cgimagerepresentation().md>) method to obtain compressed image data.

## See Also

### Accessing photo pixel data

- [rawPhoto](israwphoto.md) — A Boolean value indicating whether this photo object contains RAW format data.
