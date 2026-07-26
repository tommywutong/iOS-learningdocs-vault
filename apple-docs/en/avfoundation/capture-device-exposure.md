---
title: Exposure
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-exposure
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-exposure'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-exposure.json'
content_hash: 'sha256:6c60e75c45f2341a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# Exposure

<sub>API Collection</sub>

Configure the automatic exposure behavior of a camera, or manually control its exposure settings.

## Topics

### Managing the exposure mode

- [- isExposureModeSupported:](<avcapturedevice/isexposuremodesupported(__).md>) — Returns a Boolean value that indicates whether a device supports the specified exposure mode.
- [exposureMode](avcapturedevice/exposuremode-swift.property.md) — The exposure mode for the device.
- [ExposureMode](avcapturedevice/exposuremode-swift.enum.md) — Constants that specify the exposure mode of a capture device.

### Setting an exposure point of interest

- [exposurePointOfInterestSupported](avcapturedevice/isexposurepointofinterestsupported.md) — A Boolean value that indicates whether the device supports a point of interest for exposure.
- [exposurePointOfInterest](avcapturedevice/exposurepointofinterest.md) — The point of interest for exposure.

### Setting an exposure rectangle of interest

- [exposureRectOfInterestSupported](avcapturedevice/isexposurerectofinterestsupported.md) — Whether the device supports exposure rectangles of interest.
- [exposureRectOfInterest](avcapturedevice/exposurerectofinterest.md) — The device’s current exposure rectangle of interest, if it has one.
- [minExposureRectOfInterestSize](avcapturedevice/minexposurerectofinterestsize.md) — The minimum size you may use when specifying a rectangle of interest.
- [- defaultRectForExposurePointOfInterest:](<avcapturedevice/defaultrectforexposurepoint(ofinterest_).md>) — The default rectangle of interest used for a given exposure point of interest.

### Configuring face-driven automatic exposure

- [faceDrivenAutoExposureEnabled](avcapturedevice/isfacedrivenautoexposureenabled.md) — A Boolean value that indicates whether the device has face-driven autoexposure enabled.
- [automaticallyAdjustsFaceDrivenAutoExposureEnabled](avcapturedevice/automaticallyadjustsfacedrivenautoexposureenabled.md) — A Boolean value that indicates whether the device automatically adjusts face-driven autoexposure.

### Monitoring exposure changes

- [adjustingExposure](avcapturedevice/isadjustingexposure.md) — A Boolean value that indicates whether the device is currently adjusting its exposure setting.

### Adjusting exposure compensation

- [exposureTargetOffset](avcapturedevice/exposuretargetoffset.md) — The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [exposureTargetBias](avcapturedevice/exposuretargetbias.md) — The bias to apply to the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](avcapturedevice/minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [maxExposureTargetBias](avcapturedevice/maxexposuretargetbias.md) — The maximum supported exposure bias, in exposure value (EV) units.
- [AVCaptureExposureTargetBiasCurrent](avcapturedevice/currentexposuretargetbias.md) — A special constant that represents the current exposure bias value.
- [- setExposureTargetBias:completionHandler:](<avcapturedevice/setexposuretargetbias(__completionhandler_).md>) — Sets the bias to apply to the target exposure value.

### Configuring exposure manually

- [- setExposureModeCustomWithDuration:ISO:completionHandler:](<avcapturedevice/setexposuremodecustom(duration_iso_completionhandler_).md>) — Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.
- [exposureDuration](avcapturedevice/exposureduration.md) — The length of time over which exposure takes place.
- [ISO](avcapturedevice/iso.md) — The current exposure ISO value.
- [lensAperture](avcapturedevice/lensaperture.md) — The size of the lens diaphragm.
- [activeMaxExposureDuration](avcapturedevice/activemaxexposureduration.md) — The maximum exposure duration, in seconds, defined in the autoexposure algorithm.

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — Releases exclusive control over device hardware properties.
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Formats](capture-device-formats.md) — Configure capture formats and camera frame rates.
- [Focus](capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [White balance](capture-device-white-balance.md) — Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md) — Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
