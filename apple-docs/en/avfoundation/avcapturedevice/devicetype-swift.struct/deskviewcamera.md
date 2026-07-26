---
title: deskViewCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [macOS 13.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/deskviewcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/deskviewcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/deskviewcamera.json'
content_hash: 'sha256:f186d51ed200bb2b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# deskViewCamera

<sub>Type Property</sub>

A virtual overhead camera that captures a user’s desk.

<sub>macOS</sub>

```swift
static let deskViewCamera: AVCaptureDevice.DeviceType
```

## Discussion

This device type provides a distortion-corrected cut out from an ultra wide camera that approximates an overhead view of a user’s physical desktop.

You can use this device type with [AVCaptureMultiCamSession](../../avcapturemulticamsession.md).
