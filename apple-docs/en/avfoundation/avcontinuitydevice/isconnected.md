---
title: isConnected
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcontinuitydevice/isconnected
source_url: 'https://developer.apple.com/documentation/avfoundation/avcontinuitydevice/isconnected'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcontinuitydevice/isconnected.json'
content_hash: 'sha256:76789b65588c976c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVContinuityDevice](../avcontinuitydevice.md)

# isConnected

<sub>Instance Property</sub>

A Boolean value that indicates whether you can use the continuity device because it’s connected to the system.

<sub>tvOS</sub>

```swift
var isConnected: Bool { get }
```

## Discussion

The value of the property can change from [true](../../swift/true.md) to [false](../../swift/false.md), but not the reverse. Instead, the system creates a new [AVContinuityDevice](../avcontinuitydevice.md) instance when the same physical device reconnects to the system.
