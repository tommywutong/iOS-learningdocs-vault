---
title: 'jpegStillImageNSDataRepresentation(_:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Type Method
platforms: [iOS 4.0+（10.0 起废弃）, iPadOS 4.0+（10.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, macOS 10.7+（10.15 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/avfoundation/avcapturestillimageoutput/jpegstillimagensdatarepresentation(_:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturestillimageoutput/jpegstillimagensdatarepresentation(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturestillimageoutput/jpegstillimagensdatarepresentation%28_%3A%29.json'
content_hash: 'sha256:382ef9a5831a356f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureStillImageOutput](../avcapturestillimageoutput.md)

# jpegStillImageNSDataRepresentation(_:)

<sub>Type Method</sub>

Returns an `NSData` representation of a still image data and metadata attachments in a JPEG sample buffer.

> [!warning] Deprecated
> Use AVCapturePhotoOutput instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
class func jpegStillImageNSDataRepresentation(_ jpegSampleBuffer: CMSampleBuffer) -> Data?
```

## Parameters

- `jpegSampleBuffer` — The sample buffer carrying JPEG image data, optionally with `Exif` metadata sample buffer attachments. This method throws an [invalidArgumentException](../../foundation/nsexceptionname/invalidargumentexception.md) if `jpegSampleBuffer` is `NULL` or not in the JPEG format.

## Return Value

An `NSData` representation of `jpegSampleBuffer`.

## Discussion

This method merges the image data and `Exif` metadata sample buffer attachments without recompressing the image.

The returned `NSData` object is suitable for writing to disk.
