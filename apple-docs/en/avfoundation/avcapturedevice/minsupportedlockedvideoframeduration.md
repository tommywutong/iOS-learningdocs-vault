---
title: minSupportedLockedVideoFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minsupportedlockedvideoframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minsupportedlockedvideoframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minsupportedlockedvideoframeduration.json'
content_hash: 'sha256:ee7a2e96932339b2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minSupportedLockedVideoFrameDuration

<sub>Instance Property</sub>

The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minSupportedLockedVideoFrameDuration: CMTime { get }
```

## Discussion

`kCMTimeInvalid` is returned when the device or its current configuration does not support locked frame rate. Use [activeLockedVideoFrameDuration](../avcapturedeviceinput/activelockedvideoframeduration.md) to set the locked frame rate on the input.

## See Also

### Synchronizing with external devices

- [followingExternalSyncDevice](isfollowingexternalsyncdevice.md) — Whether the device is following an external sync device.
- [minSupportedExternalSyncFrameDuration](minsupportedexternalsyncframeduration.md) — The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [videoFrameDurationLocked](isvideoframedurationlocked.md) — Whether the device’s video frame rate (expressed as a duration) is currently locked.
