---
title: isContinuityCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/iscontinuitycamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/iscontinuitycamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/iscontinuitycamera.json'
content_hash: 'sha256:bfff8f23e8e8a64c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isContinuityCamera

<sub>Instance Property</sub>

A Boolean value that indicates whether the device is a Continuity Camera.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isContinuityCamera: Bool { get }
```

## Discussion

Continuity Camera enables you to use the rear camera system of iPhone as an external webcam in macOS.

## See Also

### Supporting Continuity Camera

- [systemPreferredCamera](systempreferredcamera.md) — A camera the system prefers to use for video and photo capture.
- [userPreferredCamera](userpreferredcamera.md) — A camera the user prefers to use for video and photo capture.
- [companionDeskViewCamera](companiondeskviewcamera.md) — A Desk View camera associated with a device.
