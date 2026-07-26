---
title: activeExternalSyncVideoFrameDuration
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/activeexternalsyncvideoframeduration
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/activeexternalsyncvideoframeduration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/activeexternalsyncvideoframeduration.json'
content_hash: 'sha256:78ae9acbe2049003'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# activeExternalSyncVideoFrameDuration

<sub>Instance Property</sub>

The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var activeExternalSyncVideoFrameDuration: CMTime { get }
```

## Discussion

Set up your input to follow an external sync device by calling [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>).

> [!note] Note
> The value of this readonly property is `kCMTimeInvalid` unless the [AVExternalSyncDevice](../avexternalsyncdevice.md) is actively driving the [AVCaptureDeviceInput](../avcapturedeviceinput.md). This is reflected by the [status](../avexternalsyncdevice/status.md) being either `AVExternalSyncDeviceStatusActiveSync` or `AVExternalSyncDeviceStatusFreeRunSync`.

## See Also

### Synchronizing with external devices

- [externalSyncSupported](isexternalsyncsupported.md) — Indicates whether the device input supports being configured to follow an external sync device.
- [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>) — Configures the the device input to follow an external sync device at the given frame duration.
- [- unfollowExternalSyncDevice](<unfollowexternalsyncdevice().md>) — Discontinues external sync.
- [externalSyncDevice](externalsyncdevice.md) — The external sync device currently being followed by this input.
