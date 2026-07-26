---
title: Formats
framework: AVFoundation
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/capture-device-formats
source_url: 'https://developer.apple.com/documentation/avfoundation/capture-device-formats'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/capture-device-formats.json'
content_hash: 'sha256:8b8253bb943e4768'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [AVFoundation](../avfoundation.md) · [Capture setup](capture-setup.md) · [AVCaptureDevice](avcapturedevice.md)

# Formats

<sub>API Collection</sub>

Configure capture formats and camera frame rates.

## Overview

The following code example illustrates how to select an iOS device’s highest possible frame rate:

```swift
func configureCameraForHighestFrameRate(device: AVCaptureDevice) {
    
    var bestFormat: AVCaptureDevice.Format?
    var bestFrameRateRange: AVFrameRateRange?

    for format in device.formats {
        for range in format.videoSupportedFrameRateRanges {
            if range.maxFrameRate > bestFrameRateRange?.maxFrameRate ?? 0 {
                bestFormat = format
                bestFrameRateRange = range
            }
        }
    }
    
    if let bestFormat = bestFormat, 
       let bestFrameRateRange = bestFrameRateRange {
        do {
            try device.lockForConfiguration()
            
            // Set the device's active format.
            device.activeFormat = bestFormat
            
            // Set the device's min/max frame duration.
            let duration = bestFrameRateRange.minFrameDuration
            device.activeVideoMinFrameDuration = duration
            device.activeVideoMaxFrameDuration = duration
            
            device.unlockForConfiguration()
        } catch {
            // Handle error.
        }
    }
}
```

Most common configurations of capture settings are available through the [AVCaptureSession](avcapturesession.md) object and its available presets. However, on iOS devices, some specialized options (such as high frame rate) require directly setting a capture format on an [AVCaptureDevice](avcapturedevice.md) instance.

> [!note] Note
> In iOS, directly configuring a capture device’s [activeFormat](avcapturedevice/activeformat.md) property changes the capture session’s preset to [AVCaptureSessionPresetInputPriority](avcapturesession/preset/inputpriority.md). Upon making this change, the capture session no longer automatically configures the capture format when you call the [- startRunning](<avcapturesession/startrunning().md>) method or call the [- commitConfiguration](<avcapturesession/commitconfiguration().md>) method after changing the session topology.
>
> In macOS, a capture session can still automatically configure the capture format after you make changes. To prevent automatic changes to the capture format in macOS, follow the advice listed under the [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) method.

## Topics

### Configuring capture formats

- [formats](avcapturedevice/formats.md) — The capture formats a device supports.
- [activeFormat](avcapturedevice/activeformat.md) — The capture format in use by the device.
- [activeDepthDataFormat](avcapturedevice/activedepthdataformat.md) — The currently active depth data format of the capture device.
- [Format](avcapturedevice/format.md) — A class that defines media formats and capture settings that capture devices support.

### Configuring frame durations

- [activeVideoMinFrameDuration](avcapturedevice/activevideominframeduration.md) — The currently active minimum frame duration.
- [activeVideoMaxFrameDuration](avcapturedevice/activevideomaxframeduration.md) — The currently active maximum frame duration.
- [activeDepthDataMinFrameDuration](avcapturedevice/activedepthdataminframeduration.md) — The minimum frame duration of depth data.

## See Also

### Configuring camera hardware

- [- lockForConfiguration:](<avcapturedevice/lockforconfiguration().md>) — Requests exclusive access to configure device hardware properties.
- [- unlockForConfiguration](<avcapturedevice/unlockforconfiguration().md>) — Releases exclusive control over device hardware properties.
- [subjectAreaChangeMonitoringEnabled](avcapturedevice/issubjectareachangemonitoringenabled.md) — A Boolean value that indicates whether the device monitors the subject area for changes.
- [AVCaptureDeviceSubjectAreaDidChangeNotification](avcapturedevice/subjectareadidchangenotification.md) — A notification the system posts when a capture device detects a substantial change to the video subject area.
- [Focus](capture-device-focus.md) — Configure the automatic focus behavior of a camera, or manually set its lens position.
- [Exposure](capture-device-exposure.md) — Configure the automatic exposure behavior of a camera, or manually control its exposure settings.
- [White balance](capture-device-white-balance.md) — Configure the automatic white balance behavior of a camera, or manually control white balance settings.
- [Lighting](capture-device-lighting.md) — Configure the device flash, torch, and low light settings.
- [Color](capture-device-color.md) — Manage HDR and color space settings for a device.
- [Zoom](capture-device-zoom.md) — Configure device zooming behavior and inspect hardware capabilities.
