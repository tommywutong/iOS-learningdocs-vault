---
title: isHighestPhotoQualitySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/ishighestphotoqualitysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/ishighestphotoqualitysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/ishighestphotoqualitysupported.json'
content_hash: 'sha256:a4c9d38fda05d850'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# isHighestPhotoQualitySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isHighestPhotoQualitySupported: Bool { get }
```

## Discussion

The simplest way to capture the highest quality photos is to set [AVCaptureSessionPresetPhoto](../../avcapturesession/preset/photo.md) as your session’s preset. If you’re instead manually setting the capture device’s [activeFormat](../activeformat.md) value, select the format whose [highestPhotoQualitySupported](ishighestphotoqualitysupported.md) property is [true](../../../swift/true.md).

## See Also

### Determining photo quality

- [supportedMaxPhotoDimensions](supportedmaxphotodimensions.md) — The maximum photo dimension this format supports.
- [highPhotoQualitySupported](ishighphotoqualitysupported.md) — A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
