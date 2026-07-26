---
title: isSuspended
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/issuspended
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/issuspended'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/issuspended.json'
content_hash: 'sha256:6b4dd41ab5dd8033'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isSuspended

<sub>Instance Property</sub>

A Boolean value that indicates whether the device is in a suspended state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isSuspended: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Accessing device state

- [connected](isconnected.md) — A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [inUseByAnotherApplication](isinusebyanotherapplication.md) — A Boolean value that indicates whether another app is using the device.
