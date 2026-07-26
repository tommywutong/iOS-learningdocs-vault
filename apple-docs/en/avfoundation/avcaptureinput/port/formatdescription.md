---
title: formatDescription
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 4.0+, iPadOS 4.0+, Mac Catalyst 14.0+, macOS 10.7+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/formatdescription
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/formatdescription'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/formatdescription.json'
content_hash: 'sha256:6fd37ff47c8533b5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# formatDescription

<sub>Instance Property</sub>

A description of the port format.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var formatDescription: CMFormatDescription? { get }
```

## Discussion

A format description object describes the format of the media the port currently provides. To observe changes to a port’s format, observe notifications of type [AVCaptureInputPortFormatDescriptionDidChangeNotification](formatdescriptiondidchangenotification.md).

## See Also

### Inspecting an input port

- [enabled](isenabled.md) — A Boolean value that indicates whether the port is in an enabled state.
- [mediaType](mediatype.md) — The media type of the port.
- [sourceDeviceType](sourcedevicetype.md) — The device type of the source camera that provides data to the port.
- [sourceDevicePosition](sourcedeviceposition.md) — The position of the source device providing input through this port.
- [clock](clock.md) — An object that represents the capture device’s clock.
