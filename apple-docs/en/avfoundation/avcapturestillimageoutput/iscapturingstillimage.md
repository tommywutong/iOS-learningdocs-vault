---
title: isCapturingStillImage
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 5.0+（10.0 起废弃）, iPadOS 5.0+（10.0 起废弃）, Mac Catalyst 14.0+（13.1 起废弃）, macOS 10.8+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturestillimageoutput/iscapturingstillimage
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/iscapturingstillimage'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/iscapturingstillimage.json'
content_hash: 'sha256:7afb11a0cfebfc1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# isCapturingStillImage

<sub>Instance Property</sub>

Indicates whether a still image is being captured.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isCapturingStillImage: Bool { get }
```

## Discussion

The value of this property is [true](../../swift/true.md) when a still image is being captured, and [false](../../swift/false.md) when no still image capture is underway.

This property supports key-value observing.

## See Also

### Capturing an image

- [- captureStillImageAsynchronouslyFromConnection:completionHandler:](<capturestillimageasynchronously(from_completionhandler_).md>) — Initiates a still image capture and returns immediately. _(deprecated)_
