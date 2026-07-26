---
title: factors
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.property.json'
content_hash: 'sha256:3692fae1246bd38d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [SystemPressureState](../systempressurestate-swift.class.md)

# factors

<sub>Instance Property</sub>

The set of underlying causes for the system pressure level.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
var factors: AVCaptureDevice.SystemPressureState.Factors { get }
```

## Discussion

Increased system pressure may be due to one or more contributing causes; this set provides additional details for the overall performance characterization reported by the [level](level-swift.property.md) property.

When the system pressure level is high, you can use this information to choose how to mitigate the issue. For example, you can reduce high system pressure due to [AVCaptureSystemPressureFactorDepthModuleTemperature](factors-swift.struct/depthmoduletemperature.md) (on a [AVCaptureDeviceTypeBuiltInTrueDepthCamera](../devicetype-swift.struct/builtintruedepthcamera.md) device) by limiting the depth capture frame rate.

## See Also

### Contributing factors

- [Factors](factors-swift.struct.md) — A structure that defines the factors affecting capture system performance.
