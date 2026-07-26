---
title: AVCaptureDevice.CenterStageControlMode.cooperative
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/cooperative
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/cooperative'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/cooperative.json'
content_hash: 'sha256:f282dd946924d4cf'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [CenterStageControlMode](../centerstagecontrolmode-swift.enum.md)

# AVCaptureDevice.CenterStageControlMode.cooperative

<sub>Case</sub>

A user and app cooperatively share control of Center Stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case cooperative
```

## Discussion

In this mode, it’s your app’s responsibilitiy to honor user intent and make center stage active when they request. Because the user can change the enabled state through Control Center, key-value observe the [centerStageEnabled](../iscenterstageenabled.md) property value and update your app state appropriately.

## See Also

### Control modes

- [AVCaptureCenterStageControlModeUser](user.md) — The user controls Center Stage.
- [AVCaptureCenterStageControlModeApp](app.md) — The app controls Center Stage.
