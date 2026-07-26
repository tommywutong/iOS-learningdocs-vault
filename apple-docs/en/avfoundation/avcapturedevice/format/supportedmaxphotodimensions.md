---
title: supportedMaxPhotoDimensions
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/format/supportedmaxphotodimensions
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/format/supportedmaxphotodimensions'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/format/supportedmaxphotodimensions.json'
content_hash: 'sha256:077d75a3b2c1e114'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [Format](../format.md)

# supportedMaxPhotoDimensions

<sub>Instance Property</sub>

The maximum photo dimension this format supports.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
@nonobjc var supportedMaxPhotoDimensions: [CMVideoDimensions] { get }
```

## See Also

### Determining photo quality

- [highPhotoQualitySupported](ishighphotoqualitysupported.md) — A Boolean value that indicates whether this format supports high-quality capture with the current quality prioritization setting.
- [highestPhotoQualitySupported](ishighestphotoqualitysupported.md) — A Boolean value that indicates whether this format supports the highest photo quality that the platform delivers.
