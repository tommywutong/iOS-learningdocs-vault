---
title: companionDeskViewCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 16.0+, iPadOS 16.0+, Mac Catalyst 16.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/companiondeskviewcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/companiondeskviewcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/companiondeskviewcamera.json'
content_hash: 'sha256:b568149ce05badce'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# companionDeskViewCamera

<sub>Instance Property</sub>

A Desk View camera associated with a device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var companionDeskViewCamera: AVCaptureDevice? { get }
```

## Discussion

The value provides an Desk View camera for a device, if one exists, that derives its framing from the device’s ultra wide camera. When multiple Continuity Camera devices are available on the system, use this property to a relate a particular instance with its associated Desk View device.

## See Also

### Supporting Continuity Camera

- [systemPreferredCamera](systempreferredcamera.md) — A camera the system prefers to use for video and photo capture.
- [userPreferredCamera](userpreferredcamera.md) — A camera the user prefers to use for video and photo capture.
- [continuityCamera](iscontinuitycamera.md) — A Boolean value that indicates whether the device is a Continuity Camera.
