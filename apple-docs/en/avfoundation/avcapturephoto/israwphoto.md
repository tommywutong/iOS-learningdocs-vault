---
title: isRawPhoto
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/israwphoto
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/israwphoto'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/israwphoto.json'
content_hash: 'sha256:c2a0f5f389d449be'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# isRawPhoto

<sub>Instance Property</sub>

A Boolean value indicating whether this photo object contains RAW format data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isRawPhoto: Bool { get }
```

## Discussion

When you request capture in RAW format, the capture output calls your delegate’s [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method one or more times, delivering both the RAW photo data and (if requested) equivalent processed photos. Use this property to distinguish between the RAW and processed results from the same capture.

## See Also

### Accessing photo pixel data

- [pixelBuffer](pixelbuffer.md) — The uncompressed or RAW image sample buffer for the photo, if requested.
