---
title: subjectAreaDidChangeNotification
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 5.0+, iPadOS 5.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/subjectareadidchangenotification
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/subjectareadidchangenotification'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/subjectareadidchangenotification.json'
content_hash: 'sha256:b48b445c4dd3bcf7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# subjectAreaDidChangeNotification

<sub>Type Property</sub>

A notification the system posts when a capture device detects a substantial change to the video subject area.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
class let subjectAreaDidChangeNotification: NSNotification.Name
```

## Discussion

The system posts this notification only if the device’s [subjectAreaChangeMonitoringEnabled](issubjectareachangemonitoringenabled.md) property value is [true](../../swift/true.md).

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [- unlockForConfiguration](<unlockforconfiguration().md>) — Releases exclusive control over device hardware properties.
- [subjectAreaChangeMonitoringEnabled](issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [Formats](../capture-device-formats.md) — Configure capture formats and camera frame rates.
- [Focus](../capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](../capture-device-exposure.md) — Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](../capture-device-white-balance.md) — Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](../capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Color](../capture-device-color.md) — Manage HDR and color space settings for a device.
- [Zoom](../capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
