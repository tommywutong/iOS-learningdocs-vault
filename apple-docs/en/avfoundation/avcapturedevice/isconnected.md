---
title: isConnected
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+, visionOS 2.1+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isconnected
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isconnected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isconnected.json'
content_hash: 'sha256:c39e2949384c4fe7'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isConnected

<sub>Instance Property</sub>

A Boolean value that indicates whether a device is currently connected to the system and available for use.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var isConnected: Bool { get }
```

## Discussion

When the value of this property is [false](../../swift/false.md) for a particular capture device instance, it doesn’t become [true](../../swift/true.md) again. If the same physical device reconnects, the system represents it as a new capture device instance.

You can key-value observe this property value to monitor when a device is no longer available.

## See Also

### Accessing device state

- [suspended](issuspended.md) — A Boolean value that indicates whether the device is in a suspended state.
- [inUseByAnotherApplication](isinusebyanotherapplication.md) — A Boolean value that indicates whether another app is using the device.
