---
title: isLockedVideoFrameDurationSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedeviceinput/islockedvideoframedurationsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/islockedvideoframedurationsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/islockedvideoframedurationsupported.json'
content_hash: 'sha256:8eac2ab08933f5d7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# isLockedVideoFrameDurationSupported

<sub>Instance Property</sub>

Indicates whether the device input supports locked frame durations.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isLockedVideoFrameDurationSupported: Bool { get }
```

## Discussion

See [activeLockedVideoFrameDuration](activelockedvideoframeduration.md) for more information on video frame duration locking.

## See Also

### Locking frame duration

- [activeLockedVideoFrameDuration](activelockedvideoframeduration.md) — The receiver’s locked frame duration (the reciprocal of its frame rate). Setting this property guarantees the intra-frame duration delivered by the device input is precisely the frame duration you request.
