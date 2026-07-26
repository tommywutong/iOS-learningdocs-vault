---
title: AVCaptureDevice.SystemPressureState.Factors
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/factors-swift.struct.json'
content_hash: 'sha256:493a6bf3956a183d'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [SystemPressureState](../systempressurestate-swift.class.md)

# AVCaptureDevice.SystemPressureState.Factors

<sub>Structure</sub>

A structure that defines the factors affecting capture system performance.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Factors
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../../swift/bitwisecopyable.md), [Equatable](../../../swift/equatable.md), [ExpressibleByArrayLiteral](../../../swift/expressiblebyarrayliteral.md), [OptionSet](../../../swift/optionset.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md), [SetAlgebra](../../../swift/setalgebra.md)

## Topics

### System pressure factors

- [AVCaptureSystemPressureFactorSystemTemperature](factors-swift.struct/systemtemperature.md) — The entire system is under elevated thermal load.
- [AVCaptureSystemPressureFactorPeakPower](factors-swift.struct/peakpower.md) — The system’s peak power requirements exceed the battery’s current capacity.
- [AVCaptureSystemPressureFactorDepthModuleTemperature](factors-swift.struct/depthmoduletemperature.md) — The module capturing depth information is operating at an elevated temperature.
- [AVCaptureSystemPressureFactorCameraTemperature](factors-swift.struct/cameratemperature.md) — The camera module is operating at an elevated temperature.

### Initializers

- [init(rawValue:)](<factors-swift.struct/init(rawvalue_).md>) — Creates a system pressure factor from its raw string value.

### Type Properties

- [AVCaptureSystemPressureFactorSystemStress](factors-swift.struct/systemstress.md) — Indicates that the system is 30 seconds away from unexpected power off. _(beta)_

## See Also

### Contributing factors

- [factors](factors-swift.property.md) — The set of underlying causes for the system pressure level.
