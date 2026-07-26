---
title: highResolutionStillImageDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 8.0+（16.0 起废弃）, iPadOS 8.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturedevice/format/highresolutionstillimagedimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/highresolutionstillimagedimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/highresolutionstillimagedimensions.json'
content_hash: 'sha256:6611ea13a4f4ac3d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# highResolutionStillImageDimensions

<sub>Instance Property</sub>

The highest resolution still image the system can produce for this format.

> [!warning] Deprecated
> Use [supportedMaxPhotoDimensions](../../avcapturedeviceformat/supportedmaxphotodimensions.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var highResolutionStillImageDimensions: CMVideoDimensions { get }
```

## Discussion

Normally, the [AVCaptureStillImageOutput](../../avcapturestillimageoutput.md) class emits images with the same dimensions as the source [AVCaptureDevice](../../avcapturedevice.md) instance’s [activeFormat](../activeformat.md). However, if you set `highResolutionStillImageOutputEnabled` to [true](../../../swift/true.md), [AVCaptureStillImageOutput](../../avcapturestillimageoutput.md) emits still images with its source [AVCaptureDevice](../../avcapturedevice.md) instance’s `activeFormat.highResolutionStillImageDimensions` dimensions.
