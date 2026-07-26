---
title: peakPower
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/peakpower.json'
content_hash: 'sha256:3eeafa5e2e156951'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Factors](../factors-swift.struct.md)

# peakPower

<sub>Type Property</sub>

The system’s peak power requirements exceed the battery’s current capacity.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var peakPower: AVCaptureDevice.SystemPressureState.Factors { get }
```

## Discussion

Devices with chemically aged batteries are less able to respond to rapid increases in total power usage (CPU and GPU usage, I/O, camera systems, radios, etc). When a device detects such conditions, the system may limit capture sperformance to prevent an unexpected device shutdown.

## See Also

### System pressure factors

- [AVCaptureSystemPressureFactorSystemTemperature](systemtemperature.md) — The entire system is under elevated thermal load.
- [AVCaptureSystemPressureFactorDepthModuleTemperature](depthmoduletemperature.md) — The module capturing depth information is operating at an elevated temperature.
- [AVCaptureSystemPressureFactorCameraTemperature](cameratemperature.md) — The camera module is operating at an elevated temperature.
