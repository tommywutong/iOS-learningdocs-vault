---
title: Zoom
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-zoom
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-zoom'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-zoom.json'
content_hash: 'sha256:50b1464c5e2ba9e1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# Zoom

<sub>API Collection</sub>

Configure device zooming behavior and inspect hardware capabilities.

## Topics

### Adjusting zoom

- [videoZoomFactor](avcapturedevice/videozoomfactor.md) — A value that controls the cropping and enlargement of images captured by the device.
- [- rampToVideoZoomFactor:withRate:](<avcapturedevice/ramp(tovideozoomfactor_withrate_).md>) — Begins a smooth transition from the current zoom factor to another.
- [- cancelVideoZoomRamp](<avcapturedevice/cancelvideozoomramp().md>) — Smoothly ends a zoom transition in progress.

### Observing zoom

- [rampingVideoZoom](avcapturedevice/isrampingvideozoom.md) — A Boolean value that indicates whether a zoom transition is in progress.

### Inspecting zoom factors

- [minAvailableVideoZoomFactor](avcapturedevice/minavailablevideozoomfactor.md) — The minimum zoom factor allowed in the current capture configuration.
- [maxAvailableVideoZoomFactor](avcapturedevice/maxavailablevideozoomfactor.md) — The maximum zoom factor allowed in the current capture configuration.
- [virtualDeviceSwitchOverVideoZoomFactors](avcapturedevice/virtualdeviceswitchovervideozoomfactors.md) — An array of video zoom factors at or above which a virtual device, such as the dual camera, may switch to its next constituent device.
- [dualCameraSwitchOverVideoZoomFactor](avcapturedevice/dualcameraswitchovervideozoomfactor.md) — The video zoom factor at which a dual camera device can automatically switch between cameras. _(deprecated)_
- [displayVideoZoomFactorMultiplier](avcapturedevice/displayvideozoomfactormultiplier.md) — A video zoom factor multiplier to use when displaying zoom information in a user interface.

### Enabling geometric distortion correction

- [geometricDistortionCorrectionSupported](avcapturedevice/isgeometricdistortioncorrectionsupported.md) — A Boolean value that indicates whether this device supports geometric distortion correction.
- [geometricDistortionCorrectionEnabled](avcapturedevice/isgeometricdistortioncorrectionenabled.md) — A Boolean value that indicates whether geometric distortion correction is enabled for this device.

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
- [Color](capture-device-color.md) — Manage HDR and color space settings for a device.
