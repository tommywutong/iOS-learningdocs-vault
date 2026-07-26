---
title: isStudioLightActive
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isstudiolightactive
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isstudiolightactive'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isstudiolightactive.json'
content_hash: 'sha256:91c090c60f3265c8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isStudioLightActive

<sub>Instance Property</sub>

A Boolean value that indicates whether Studio Light is active on a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isStudioLightActive: Bool { get }
```

## Discussion

When the value is [true](../../swift/true.md), the system artificially lights the subject’s face to simulate the presence of a studio light near the camera.

## See Also

### Configuring Studio Light

- [studioLightEnabled](isstudiolightenabled.md) — A Boolean value that indicates whether a user enabled Studio Light on a device.
