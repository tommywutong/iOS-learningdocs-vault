---
title: isInUseByAnotherApplication
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 14.0+, macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/isinusebyanotherapplication
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/isinusebyanotherapplication'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/isinusebyanotherapplication.json'
content_hash: 'sha256:883cbf29bb87a321'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# isInUseByAnotherApplication

<sub>Instance Property</sub>

A Boolean value that indicates whether another app is using the device.

<sub>Mac Catalyst, macOS</sub>

```swift
var isInUseByAnotherApplication: Bool { get }
```

## Discussion

This property is key-value observable.

## See Also

### Accessing device state

- [connected](isconnected.md) — A Boolean value that indicates whether a device is currently connected to the system and available for use.
- [suspended](issuspended.md) — A Boolean value that indicates whether the device is in a suspended state.
