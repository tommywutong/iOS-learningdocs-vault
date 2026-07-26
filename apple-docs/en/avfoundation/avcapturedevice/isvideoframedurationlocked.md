---
title: isVideoFrameDurationLocked
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isvideoframedurationlocked
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isvideoframedurationlocked'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isvideoframedurationlocked.json'
content_hash: 'sha256:60e3b65445bf2a1f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isVideoFrameDurationLocked

<sub>Instance Property</sub>

Whether the device’s video frame rate (expressed as a duration) is currently locked.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isVideoFrameDurationLocked: Bool { get }
```

## Discussion

Returns `true` when an [AVCaptureDeviceInput](../avcapturedeviceinput.md) associated with the device has its [activeLockedVideoFrameDuration](../avcapturedeviceinput/activelockedvideoframeduration.md) property set to something other than `kCMTimeInvalid`. See [activeLockedVideoFrameDuration](../avcapturedeviceinput/activelockedvideoframeduration.md) for more information on video frame duration locking.

## See Also

### Synchronizing with external devices

- [followingExternalSyncDevice](isfollowingexternalsyncdevice.md) — Whether the device is following an external sync device.
- [minSupportedExternalSyncFrameDuration](minsupportedexternalsyncframeduration.md) — The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [minSupportedLockedVideoFrameDuration](minsupportedlockedvideoframeduration.md) — The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.
