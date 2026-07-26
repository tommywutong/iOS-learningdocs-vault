---
title: externalSyncDevice
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/externalsyncdevice
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/externalsyncdevice'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/externalsyncdevice.json'
content_hash: 'sha256:74c0754183509bcf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# externalSyncDevice

<sub>Instance Property</sub>

The external sync device currently being followed by this input.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var externalSyncDevice: AVExternalSyncDevice? { get }
```

## Discussion

This readonly property returns the [AVExternalSyncDevice](../avexternalsyncdevice.md) instance you provided in [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>). This property returns `nil` when an external sync device is disconnected or fails to calibrate.

## See Also

### Synchronizing with external devices

- [externalSyncSupported](isexternalsyncsupported.md) — Indicates whether the device input supports being configured to follow an external sync device.
- [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>) — Configures the the device input to follow an external sync device at the given frame duration.
- [- unfollowExternalSyncDevice](<unfollowexternalsyncdevice().md>) — Discontinues external sync.
- [activeExternalSyncVideoFrameDuration](activeexternalsyncvideoframeduration.md) — The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
