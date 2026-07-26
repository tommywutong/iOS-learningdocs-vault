---
title: cameraTemperature
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/cameratemperature.json'
content_hash: 'sha256:ebb5d9837c41871d'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Factors](../factors-swift.struct.md)

# cameraTemperature

<sub>Type Property</sub>

The camera module is operating at an elevated temperature.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var cameraTemperature: AVCaptureDevice.SystemPressureState.Factors { get }
```

## See Also

### System pressure factors

- [AVCaptureSystemPressureFactorSystemTemperature](systemtemperature.md) — The entire system is under elevated thermal load.
- [AVCaptureSystemPressureFactorPeakPower](peakpower.md) — The system’s peak power requirements exceed the battery’s current capacity.
- [AVCaptureSystemPressureFactorDepthModuleTemperature](depthmoduletemperature.md) — The module capturing depth information is operating at an elevated temperature.
