---
title: linkedDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.7+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/linkeddevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/linkeddevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/linkeddevices.json'
content_hash: 'sha256:f252134d3abcb021'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# linkedDevices

<sub>Instance Property</sub>

An array of capture devices that are physically linked to a device.

<sub>macOS</sub>

```swift
var linkedDevices: [AVCaptureDevice] { get }
```

## Discussion

For an external iSight camera, the array contains an [AVCaptureDevice](../avcapturedevice.md) instance that represents the external iSight microphone.
