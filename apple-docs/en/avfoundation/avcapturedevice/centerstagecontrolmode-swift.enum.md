---
title: AVCaptureDevice.CenterStageControlMode
framework: AVFoundation
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum.json'
content_hash: 'sha256:8c5f2e4a5fac8b12'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.CenterStageControlMode

<sub>Enumeration</sub>

Constants that indicate the current Center Stage control mode.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
enum CenterStageControlMode
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Control modes

- [AVCaptureCenterStageControlModeUser](centerstagecontrolmode-swift.enum/user.md) — The user controls Center Stage.
- [AVCaptureCenterStageControlModeApp](centerstagecontrolmode-swift.enum/app.md) — The app controls Center Stage.
- [AVCaptureCenterStageControlModeCooperative](centerstagecontrolmode-swift.enum/cooperative.md) — A user and app cooperatively share control of Center Stage.

### Initializers

- [init(rawValue:)](<centerstagecontrolmode-swift.enum/init(rawvalue_).md>)

## See Also

### Configuring Center Stage

- [centerStageActive](iscenterstageactive.md) — A Boolean value that indicates whether Center Stage is active on a device.
- [centerStageEnabled](iscenterstageenabled.md) — A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [centerStageRectOfInterest](centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [centerStageControlMode](centerstagecontrolmode-swift.type.property.md) — A value that indicates the current mode of Center Stage control.
