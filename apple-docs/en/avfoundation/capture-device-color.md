---
title: Color
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-color
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-color'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-color.json'
content_hash: 'sha256:14354654cf144016'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# Color

<sub>API Collection</sub>

Manage HDR and color space settings for a device.

## Topics

### Configuring HDR settings

- [automaticallyAdjustsVideoHDREnabled](avcapturedevice/automaticallyadjustsvideohdrenabled.md) — A Boolean value that indicates whether the device automatically manages the state of high dynamic range (HDR) video streaming.
- [videoHDREnabled](avcapturedevice/isvideohdrenabled.md) — A Boolean value that indicates whether the device streams high dynamic range video buffers, also known as extended dynamic range (EDR).

### Enabling global tone mapping

- [globalToneMappingEnabled](avcapturedevice/isglobaltonemappingenabled.md) — A Boolean value that indicates whether the device should use global tone mapping.

### Configuring color space settings

- [activeColorSpace](avcapturedevice/activecolorspace.md) — The currently active color space for capture.
- [AVCaptureColorSpace](avcapturecolorspace.md) — An enumeration of color spaces a device can support.

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — Releases exclusive control over device hardware properties.
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](capture-device-formats.md) — Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md) — Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](capture-device-white-balance.md) — Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Zoom](capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
