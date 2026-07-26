---
title: AVCaptureDevice.CenterStageControlMode.user
framework: AVFoundation
symbol_kind: case
role: symbol
role_heading: Case
platforms: [iOS 14.5+, iPadOS 14.5+, Mac Catalyst 14.5+, macOS 12.3+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/user
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/user'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/centerstagecontrolmode-swift.enum/user.json'
content_hash: 'sha256:49737372d2779166'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [CenterStageControlMode](../centerstagecontrolmode-swift.enum.md)

# AVCaptureDevice.CenterStageControlMode.user

<sub>Case</sub>

The user controls Center Stage.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
case user
```

## Discussion

In this mode, the user has exclusive control of Center Stage through Control Center. The system throws an exception in this mode if an app attempts to programmatically change the enabled state of Center Stage.

## See Also

### Control modes

- [AVCaptureCenterStageControlModeApp](app.md) — The app controls Center Stage.
- [AVCaptureCenterStageControlModeCooperative](cooperative.md) — A user and app cooperatively share control of Center Stage.
