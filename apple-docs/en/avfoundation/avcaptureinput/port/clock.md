---
title: clock
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, macOS 10.9+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/clock
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/clock'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/clock.json'
content_hash: 'sha256:4117c912bb1aa44e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# clock

<sub>Instance Property</sub>

An object that represents the capture device’s clock.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var clock: CMClock? { get }
```

## Discussion

The value of this property is readonly and may not reflect the actual clock in the capture device.

## See Also

### Inspecting an input port

- [enabled](isenabled.md) — A Boolean value that indicates whether the port is in an enabled state.
- [mediaType](mediatype.md) — The media type of the port.
- [formatDescription](formatdescription.md) — A description of the port format.
- [sourceDeviceType](sourcedevicetype.md) — The device type of the source camera that provides data to the port.
- [sourceDevicePosition](sourcedeviceposition.md) — The position of the source device providing input through this port.
