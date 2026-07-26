---
title: unlockForConfiguration()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/unlockforconfiguration()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/unlockforconfiguration()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/unlockforconfiguration%28%29.json'
content_hash: 'sha256:f25f62b881e7917b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# unlockForConfiguration()

<sub>Instance Method</sub>

Releases exclusive control over device hardware properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
func unlockForConfiguration()
```

## Discussion

If you’ve previously locked a device by calling [- lockForConfiguration:](<lockforconfiguration().md>), call this method when your app no longer requires preventing device properties from changing automatically.

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [subjectAreaChangeMonitoringEnabled](issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [AVCaptureDeviceSubjectAreaDidChangeNotification](subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](../capture-device-formats.md) — Configure capture formats and camera frame rates.
- [Focus](../capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](../capture-device-exposure.md) — Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](../capture-device-white-balance.md) — Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](../capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Color](../capture-device-color.md) — Manage HDR and color space settings for a device.
- [Zoom](../capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
