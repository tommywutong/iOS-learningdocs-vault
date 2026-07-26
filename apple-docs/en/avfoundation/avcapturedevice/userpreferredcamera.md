---
title: userPreferredCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/userpreferredcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/userpreferredcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/userpreferredcamera.json'
content_hash: 'sha256:95873a799d355330'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# userPreferredCamera

<sub>Type Property</sub>

A camera the user prefers to use for video and photo capture.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
class var userPreferredCamera: AVCaptureDevice? { get set }
```

## Discussion

In addition to being a [systemPreferredCamera](systempreferredcamera.md), you can designate a device as a user-preferred camera. Setting a value for this property allows an app to persist its preference across app launches and system reboots. The system internally maintains a short history of devices, so if a user’s most recently preferred camera isn’t currently connected, it still reports the next best choice.

This property always returns a device that’s present. If no camera is available, this value is `nil`.

> [!note] Note
> Setting the value to `nil` has no effect.

## See Also

### Supporting Continuity Camera

- [systemPreferredCamera](systempreferredcamera.md) — A camera the system prefers to use for video and photo capture.
- [continuityCamera](iscontinuitycamera.md) — A Boolean value that indicates whether the device is a Continuity Camera.
- [companionDeskViewCamera](companiondeskviewcamera.md) — A Desk View camera associated with a device.
