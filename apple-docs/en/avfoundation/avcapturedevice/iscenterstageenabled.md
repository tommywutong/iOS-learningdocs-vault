---
title: isCenterStageEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/iscenterstageenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscenterstageenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iscenterstageenabled.json'
content_hash: 'sha256:58abf414376c2c0f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isCenterStageEnabled

<sub>Type Property</sub>

A Boolean value that indicates whether a user or an app enabled Center Stage on a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var isCenterStageEnabled: Bool { get set }
```

## Discussion

You can only set this value when Center Stage is under app or cooperative control. Attempting to change the enabled state when the control mode is [AVCaptureCenterStageControlModeUser](centerstagecontrolmode-swift.enum/user.md), results in the system throwing an exception.

> [!note] Note
> When Center Stage is under user or cooperative control, the user may change the feature’s enabled state in Control Center. Key-value observe this property value to monitor these changes.

## See Also

### Configuring Center Stage

- [centerStageActive](iscenterstageactive.md) — A Boolean value that indicates whether Center Stage is active on a device.
- [centerStageRectOfInterest](centerstagerectofinterest.md) — The effective region within the output pixel buffer to perform Center Stage framing.
- [centerStageControlMode](centerstagecontrolmode-swift.type.property.md) — A value that indicates the current mode of Center Stage control.
- [CenterStageControlMode](centerstagecontrolmode-swift.enum.md) — Constants that indicate the current Center Stage control mode.
