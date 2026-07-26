---
title: isStudioLightEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isstudiolightenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isstudiolightenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isstudiolightenabled.json'
content_hash: 'sha256:6a00e0164e35366f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isStudioLightEnabled

<sub>Type Property</sub>

A Boolean value that indicates whether a user enabled Studio Light on a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isStudioLightEnabled: Bool { get }
```

## Discussion

When the value is [true](../../swift/true.md), the system artificially lights the subject’s face to simulate the presence of a studio light near the camera.

This property is key-value observable.

## See Also

### Configuring Studio Light

- [studioLightActive](isstudiolightactive.md) — A Boolean value that indicates whether Studio Light is active on a device.
