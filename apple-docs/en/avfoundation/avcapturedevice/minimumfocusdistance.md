---
title: minimumFocusDistance
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/minimumfocusdistance
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/minimumfocusdistance'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/minimumfocusdistance.json'
content_hash: 'sha256:2de24b8666eb475e'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# minimumFocusDistance

<sub>Instance Property</sub>

The capture device’s minimum focus distance in millimeters.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var minimumFocusDistance: Int { get }
```

## Discussion

For virtual cameras, like [AVCaptureDeviceTypeBuiltInDualCamera](devicetype-swift.struct/builtindualcamera.md) or [AVCaptureDeviceTypeBuiltInTripleCamera](devicetype-swift.struct/builtintriplecamera.md), this value represents the smallest minimum focus distance of the autofocus-capable cameras that it sources.

This value is `-1` if the distance is unknown.
