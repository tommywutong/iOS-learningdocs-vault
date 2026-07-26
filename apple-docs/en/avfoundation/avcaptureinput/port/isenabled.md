---
title: isEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/isenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/isenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/isenabled.json'
content_hash: 'sha256:cac6e30079526796'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# isEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the port is in an enabled state.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var isEnabled: Bool { get set }
```

## Discussion

Ports are in an enabled state by default. If you want to capture only a subset of the media streams provided by a capture input, use this property to selectively disable streams.

## See Also

### Inspecting an input port

- [mediaType](mediatype.md) — The media type of the port.
- [formatDescription](formatdescription.md) — A description of the port format.
- [sourceDeviceType](sourcedevicetype.md) — The device type of the source camera that provides data to the port.
- [sourceDevicePosition](sourcedeviceposition.md) — The position of the source device providing input through this port.
- [clock](clock.md) — An object that represents the capture device’s clock.
