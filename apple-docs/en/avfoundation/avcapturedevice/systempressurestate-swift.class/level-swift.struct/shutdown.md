---
title: shutdown
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct/shutdown.json'
content_hash: 'sha256:1f92a99a55442280'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Level](../level-swift.struct.md)

# shutdown

<sub>Type Property</sub>

System pressure is beyond critical, so the capture system has shut down.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static let shutdown: AVCaptureDevice.SystemPressureState.Level
```

## Discussion

When system pressure reaches this level, the capture system automatically shuts down, causing a session interruption. Use the [AVCaptureSessionInterruptionSystemPressureStateKey](../../../avcapturesessioninterruptionsystempressurestatekey.md) in the interruption notification’s [userInfo](../../../../foundation/notification/userinfo.md) dictionary to find details about the system pressure factors causing the interruption.

## See Also

### System pressure levels

- [AVCaptureSystemPressureLevelNominal](nominal.md) — A level that indicates the system pressure is normal and not under pressure.
- [AVCaptureSystemPressureLevelFair](fair.md) — A level that indicates that system pressure is slightly elevated.
- [AVCaptureSystemPressureLevelSerious](serious.md) — A level that indicates that system pressure is highly elevated.
- [AVCaptureSystemPressureLevelCritical](critical.md) — System pressure is critically elevated.
