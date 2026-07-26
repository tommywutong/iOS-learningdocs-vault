---
title: AVCaptureDevice.SystemPressureState.Level
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/systempressurestate-swift.class/level-swift.struct.json'
content_hash: 'sha256:5c5860eca8ec05ba'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [SystemPressureState](../systempressurestate-swift.class.md)

# AVCaptureDevice.SystemPressureState.Level

<sub>Structure</sub>

A structure that defines system pressure state levels.

<sub>iOS, iPadOS, Mac Catalyst, tvOS, visionOS</sub>

```swift
struct Level
```

## Relationships

- **Conforms To**: [Equatable](../../../swift/equatable.md), [Hashable](../../../swift/hashable.md), [RawRepresentable](../../../swift/rawrepresentable.md), [Sendable](../../../swift/sendable.md), [SendableMetatype](../../../swift/sendablemetatype.md)

## Topics

### System pressure levels

- [AVCaptureSystemPressureLevelNominal](level-swift.struct/nominal.md) — A level that indicates the system pressure is normal and not under pressure.
- [AVCaptureSystemPressureLevelFair](level-swift.struct/fair.md) — A level that indicates that system pressure is slightly elevated.
- [AVCaptureSystemPressureLevelSerious](level-swift.struct/serious.md) — A level that indicates that system pressure is highly elevated.
- [AVCaptureSystemPressureLevelCritical](level-swift.struct/critical.md) — System pressure is critically elevated.
- [AVCaptureSystemPressureLevelShutdown](level-swift.struct/shutdown.md) — System pressure is beyond critical, so the capture system has shut down.

### Initializers

- [init(rawValue:)](<level-swift.struct/init(rawvalue_).md>) — Creates a system pressure level from its raw string value.

## See Also

### Overall level

- [level](level-swift.property.md) — The overall level of performance constraints on the capture system.
