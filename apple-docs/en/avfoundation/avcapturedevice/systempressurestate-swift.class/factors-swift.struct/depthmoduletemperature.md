---
title: depthModuleTemperature
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct/depthmoduletemperature.json'
content_hash: 'sha256:2d7e70f7fb03ec64'
translated: false
---

> Navigation: [Technologies](../../../../technologies.md) · [AVFoundation](../../../../avfoundation.md) · [AVCaptureDevice](../../../avcapturedevice.md) · [SystemPressureState](../../systempressurestate-swift.class.md) · [Factors](../factors-swift.struct.md)

# depthModuleTemperature

<sub>Type Property</sub>

The module capturing depth information is operating at an elevated temperature.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
static var depthModuleTemperature: AVCaptureDevice.SystemPressureState.Factors { get }
```

## Discussion

As system pressure increases, depth quality may become degraded. To reduce system pressure from this factor, reduce depth capture frame rate.

This factor applies only to [AVCaptureDeviceTypeBuiltInTrueDepthCamera](../../devicetype-swift.struct/builtintruedepthcamera.md) devices.

## See Also

### System pressure factors

- [AVCaptureSystemPressureFactorSystemTemperature](systemtemperature.md) — The entire system is under elevated thermal load.
- [AVCaptureSystemPressureFactorPeakPower](peakpower.md) — The system’s peak power requirements exceed the battery’s current capacity.
- [AVCaptureSystemPressureFactorCameraTemperature](cameratemperature.md) — The camera module is operating at an elevated temperature.
