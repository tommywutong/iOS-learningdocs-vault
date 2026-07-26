---
title: spatialCaptureDiscomfortReasons
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 18.0+, iPadOS 18.0+, Mac Catalyst 18.0+, macOS 15.0+, tvOS 18.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/spatialcapturediscomfortreasons
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/spatialcapturediscomfortreasons'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/spatialcapturediscomfortreasons.json'
content_hash: 'sha256:684f77f0d444584d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# spatialCaptureDiscomfortReasons

<sub>Instance Property</sub>

Reasons why current environmental conditions aren’t suitable to capturing spatial videos that are comfortable to view.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var spatialCaptureDiscomfortReasons: Set<AVSpatialCaptureDiscomfortReason> { get }
```

## Discussion

You can monitor this property to determine whether to present UI that recommends a person reframe their scene for more pleasing spatial capture. For example, you could show a message that indicates the subject is too close or the scene is too dark.

## See Also

### Supporting spatial capture

- [AVSpatialCaptureDiscomfortReason](../avspatialcapturediscomfortreason.md) — Constants that indicate the suitability of the current scene to create a comfortable viewing experience.
