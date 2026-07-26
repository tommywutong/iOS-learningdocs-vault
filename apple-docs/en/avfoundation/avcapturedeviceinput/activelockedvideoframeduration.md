---
title: activeLockedVideoFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/activelockedvideoframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/activelockedvideoframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/activelockedvideoframeduration.json'
content_hash: 'sha256:18ec4cc791086f22'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# activeLockedVideoFrameDuration

<sub>Instance Property</sub>

The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var activeLockedVideoFrameDuration: CMTime { get set }
```

## Discussion

Set this property to run the receiver’s associated [AVCaptureDevice](../avcapturedevice.md) at precisely your provided frame rate (expressed as a duration). Query [minSupportedLockedVideoFrameDuration](../avcapturedevice/minsupportedlockedvideoframeduration.md) to find the minimum value supported by this [AVCaptureDeviceInput](../avcapturedeviceinput.md). In order to disable locked video frame duration, set this property to `kCMTimeInvalid`. This property resets itself to `kCMTimeInvalid` when the receiver’s attached [activeFormat](../avcapturedevice/activeformat.md) changes. When you set this property, its value is also reflected in the receiver’s [activeVideoMinFrameDuration](../avcapturedevice/activevideominframeduration.md) and [activeVideoMaxFrameDuration](../avcapturedevice/activevideomaxframeduration.md).

> [!note] Note
> Locked frame duration availability may change depending on the device configuration. For example, locked frame duration is unsupported when [autoVideoFrameRateEnabled](../avcapturedevice/isautovideoframerateenabled.md) or [spatialVideoCaptureEnabled](../avcapturemoviefileoutput/isspatialvideocaptureenabled.md) is set to `true`.

> [!note] Note
> Only one [AVCaptureDeviceInput](../avcapturedeviceinput.md) added to an [AVCaptureMultiCamSession](../avcapturemulticamsession.md) can follow an external sync device or run at a locked frame duration.

> [!note] Note
> Setting this property may cause a lengthy reconfiguration of the receiver, similar to setting [activeFormat](../avcapturedevice/activeformat.md) or [sessionPreset](../avcapturesession/sessionpreset.md).

> [!note] Note
> When using this property, set the exposure duration with [- setExposureModeCustomWithDuration:ISO:completionHandler:](<../avcapturedevice/setexposuremodecustom(duration_iso_completionhandler_).md>) to one half the frame duration (or less) to maintain full dynamic range.

> [!important] Important
> If you set this property to a valid value while the receiver’s [minSupportedLockedVideoFrameDuration](../avcapturedevice/minsupportedlockedvideoframeduration.md) is `kCMTimeInvalid`, it throws an `NSInvalidArgumentException`.

> [!important] Important
> If you set this property while the receiver’s  [lockedVideoFrameDurationSupported](islockedvideoframedurationsupported.md) property returns `false`, it throws an `NSInvalidArgumentException`.

## See Also

### Locking frame duration

- [lockedVideoFrameDurationSupported](islockedvideoframedurationsupported.md) — Indicates whether the device input supports locked frame durations.
