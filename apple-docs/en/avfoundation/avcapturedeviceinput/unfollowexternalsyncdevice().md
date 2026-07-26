---
title: unfollowExternalSyncDevice()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/unfollowexternalsyncdevice()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/unfollowexternalsyncdevice()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/unfollowexternalsyncdevice%28%29.json'
content_hash: 'sha256:e4a46e0db17208c9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# unfollowExternalSyncDevice()

<sub>Instance Method</sub>

Discontinues external sync.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func unfollowExternalSyncDevice()
```

## Discussion

This method stops your input from syncing to the external sync device you specified in [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>).

## See Also

### Synchronizing with external devices

- [externalSyncSupported](isexternalsyncsupported.md) — Indicates whether the device input supports being configured to follow an external sync device.
- [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>) — Configures the the device input to follow an external sync device at the given frame duration.
- [activeExternalSyncVideoFrameDuration](activeexternalsyncvideoframeduration.md) — The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [externalSyncDevice](externalsyncdevice.md) — The external sync device currently being followed by this input.
