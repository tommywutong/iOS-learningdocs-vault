---
title: level
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.property.json'
content_hash: 'sha256:788d0f1f52e70ffc'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [SystemPressureState](../systempressurestate-swift.class.md)

# level

<sub>Instance Property</sub>

The overall level of performance constraints on the capture system.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var level: AVCaptureDevice.SystemPressureState.Level { get }
```

## Discussion

Several aspects of OS and hardware status affect capture system performance and availability (see [Factors](factors-swift.struct.md)). The overall system pressure level represents the most critical of underlying factors.

## See Also

### Overall level

- [Level](level-swift.struct.md) — A structure that defines system pressure state levels.
