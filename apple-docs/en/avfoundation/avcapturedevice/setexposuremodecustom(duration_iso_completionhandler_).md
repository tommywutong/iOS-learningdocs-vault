---
title: 'setExposureModeCustom(duration:iso:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuremodecustom(duration:iso:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setexposuremodecustom%28duration%3Aiso%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:d5ebfcc502a322cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setExposureModeCustom(duration:iso:completionHandler:)

<sub>Instance Method</sub>

Sets the exposure mode to a custom state, and locks exposure duration and ISO at explicit values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setExposureModeCustom(duration: CMTime, iso ISO: Float, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setExposureModeCustom(duration: CMTime, iso ISO: Float) async -> CMTime
```

## Parameters

- `duration` — The exposure duration. Pass a value of [AVCaptureExposureDurationCurrent](currentexposureduration.md) to leave the current exposure duration unchanged. Changes made to the exposure duration may result in changes to [activeVideoMinFrameDuration](activevideominframeduration.md) or [activeVideoMaxFrameDuration](activevideomaxframeduration.md).

- `ISO` — The exposure ISO value. Pass a value of [AVCaptureISOCurrent](currentiso.md) to leave the current ISO unchanged.

- `handler` — A callback the system invokes when the adjustment to the exposure duration and ISO is complete. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [synchronizationClock](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## Discussion

This method throws an exception if you set the exposure duration or ISO values to an unsupported level

Before changing exposure mode, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

When using [AVCapturePhotoOutput](../avcapturephotooutput.md) to capture photos, the [photoQualityPrioritization](../avcapturephotosettings/photoqualityprioritization.md) property of [AVCapturePhotoSettings](../avcapturephotosettings.md) defaults to [AVCapturePhotoQualityPrioritizationBalanced](../avcapturephotooutput/qualityprioritization/balanced.md), which allows photo capture to temporarily override the capture device’s exposure duration and ISO if the scene is dark enough to require multi-image fusion to improve quality. To ensure that the system honors the device exposure duration and ISO values while in [AVCaptureExposureModeCustom](exposuremode-swift.enum/custom.md) or [AVCaptureExposureModeLocked](exposuremode-swift.enum/locked.md) mode, you must photo quality prioritization to [AVCapturePhotoQualityPrioritizationSpeed](../avcapturephotooutput/qualityprioritization/speed.md).

## Topics

### Exposure constants

- [AVCaptureExposureDurationCurrent](currentexposureduration.md) — A special constant representing the current exposure duration setting.
- [AVCaptureISOCurrent](currentiso.md) — A constant to indicate not to specify a new ISO value, and instead set it to its current value.

## See Also

### Configuring exposure manually

- [exposureDuration](exposureduration.md) — The length of time over which exposure takes place.
- [ISO](iso.md) — The current exposure ISO value.
- [lensAperture](lensaperture.md) — The size of the lens diaphragm.
- [activeMaxExposureDuration](activemaxexposureduration.md) — The maximum exposure duration, in seconds, defined in the autoexposure algorithm.
