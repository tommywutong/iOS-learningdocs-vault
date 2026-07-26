---
title: critical
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/critical
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/critical'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/critical.json'
content_hash: 'sha256:379359d76c6f1327'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Level](../level-swift.struct.md)

# critical

<sub>Type Property</sub>

System pressure is critically elevated.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let critical: AVCaptureDevice.SystemPressureState.Level
```

## Discussion

Capture quality and performance are significantly impacted. Reduce the frame rate until system pressure state improves.

## See Also

### System pressure levels

- [AVCaptureSystemPressureLevelNominal](nominal.md) — A level that indicates the system pressure is normal and not under pressure.
- [AVCaptureSystemPressureLevelFair](fair.md) — A level that indicates that system pressure is slightly elevated.
- [AVCaptureSystemPressureLevelSerious](serious.md) — A level that indicates that system pressure is highly elevated.
- [AVCaptureSystemPressureLevelShutdown](shutdown.md) — System pressure is beyond critical, so the capture system has shut down.
