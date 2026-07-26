---
title: isFollowingExternalSyncDevice
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isfollowingexternalsyncdevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isfollowingexternalsyncdevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isfollowingexternalsyncdevice.json'
content_hash: 'sha256:ec88a8a9417cafc5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isFollowingExternalSyncDevice

<sub>Instance Property</sub>

Whether the device is following an external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isFollowingExternalSyncDevice: Bool { get }
```

## Discussion

See [- followExternalSyncDevice:videoFrameDuration:delegate:](<../avcapturedeviceinput/follow(__videoframeduration_delegate_).md>) for more information on external sync.

## See Also

### Synchronizing with external devices

- [minSupportedExternalSyncFrameDuration](minsupportedexternalsyncframeduration.md) — The minimum frame duration that can be passed as the `videoFrameDuration` when directing your device input to follow an external sync device.
- [videoFrameDurationLocked](isvideoframedurationlocked.md) — Whether the device’s video frame rate (expressed as a duration) is currently locked.
- [minSupportedLockedVideoFrameDuration](minsupportedlockedvideoframeduration.md) — The maximum frame rate (expressed as a minimum duration) that can be set on an input associated with this device.
