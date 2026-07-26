---
title: systemTemperature
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/systemtemperature.json'
content_hash: 'sha256:56785f8aab8ef0c9'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Factors](../factors-swift.struct.md)

# systemTemperature

<sub>Type Property</sub>

The entire system is under elevated thermal load.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var systemTemperature: AVCaptureDevice.SystemPressureState.Factors { get }
```

## See Also

### System pressure factors

- [AVCaptureSystemPressureFactorPeakPower](peakpower.md) — The system’s peak power requirements exceed the battery’s current capacity.
- [AVCaptureSystemPressureFactorDepthModuleTemperature](depthmoduletemperature.md) — The module capturing depth information is operating at an elevated temperature.
- [AVCaptureSystemPressureFactorCameraTemperature](cameratemperature.md) — The camera module is operating at an elevated temperature.
