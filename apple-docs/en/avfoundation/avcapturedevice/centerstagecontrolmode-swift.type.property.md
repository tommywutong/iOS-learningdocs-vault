---
title: centerStageControlMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.type.property
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.type.property'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.type.property.json'
content_hash: 'sha256:1075d850f93275a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# centerStageControlMode

<sub>Type Property</sub>

A value that indicates the current mode of Center Stage control.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var centerStageControlMode: AVCaptureDevice.CenterStageControlMode { get set }
```

## Discussion

See Control Modes for details on choosing an appropriate control mode.

## See Also

### Configuring Center Stage

- [centerStageActive](iscenterstageactive.md) — A Boolean value that indicates whether Center Stage is active on a device.
- [centerStageEnabled](iscenterstageenabled.md) — A Boolean value that indicates whether a user or an app enabled Center Stage on a device.
- [centerStageRectOfInterest](centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [CenterStageControlMode](centerstagecontrolmode-swift.enum.md) — Constants that indicate the current Center Stage control mode.
