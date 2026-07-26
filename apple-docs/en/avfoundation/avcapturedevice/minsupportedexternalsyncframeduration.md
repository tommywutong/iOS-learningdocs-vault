---
title: minSupportedExternalSyncFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minsupportedexternalsyncframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minsupportedexternalsyncframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minsupportedexternalsyncframeduration.json'
content_hash: 'sha256:ce4c5ce3caaf47e3'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minSupportedExternalSyncFrameDuration

<sub>Instance Property</sub>

The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minSupportedExternalSyncFrameDuration: CMTime { get }
```

## Discussion

Use this property as the minimum allowable frame duration to pass to `AVCaptureDeviceInput/follow:externalSyncDevice:videoFrameDuration:delegate:` when you want to follow an external sync device. This property returns `kCMTimeInvalid` when the device’s’ current configuration does not support external sync device following.

## See Also

### Synchronizing with external devices

- [followingExternalSyncDevice](isfollowingexternalsyncdevice.md) — Whether the device is following an external sync device.
- [videoFrameDurationLocked](isvideoframedurationlocked.md) — Whether the device’s video frame rate (expressed as a duration) is currently locked.
- [minSupportedLockedVideoFrameDuration](minsupportedlockedvideoframeduration.md) — The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.
