---
title: sourceDeviceType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureinput/port/sourcedevicetype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureinput/port/sourcedevicetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureinput/port/sourcedevicetype.json'
content_hash: 'sha256:d9c0210bdf2df161'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureInput](../../avcaptureinput.md) · [Port](../port.md)

# sourceDeviceType

<sub>Instance Property</sub>

The device type of the source camera that provides data to the port.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sourceDeviceType: AVCaptureDevice.DeviceType? { get }
```

## Discussion

All ports contained in an input’s [ports](../ports.md) property have the same source device type, which each equal to the [deviceType](../../avcapturedevice/devicetype-swift.property.md) property of the input’s device.

When working with virtual devices such as the [AVCaptureDeviceTypeBuiltInDualCamera](../../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) in an [AVCaptureMultiCamSession](../../avcapturemulticamsession.md), it’s possible to stream media from the virtual device’s constituent device streams by discovering and connecting hidden ports. In the case of the [AVCaptureDeviceTypeBuiltInDualCamera](../../avcapturedevice/devicetype-swift.struct/builtindualcamera.md), its constituent devices are the wide-angle and telephoto cameras.

By calling [- portsWithMediaType:sourceDeviceType:sourceDevicePosition:](<../../avcapturedeviceinput/ports(for_sourcedevicetype_sourcedeviceposition_).md>):, you may discover ports originating from one or more of the virtual device’s constituent devices and then make connections using those ports. Constituent device ports are never present in their owning virtual device input’s ports array.

## See Also

### Inspecting an input port

- [enabled](isenabled.md) — A Boolean value that indicates whether the port is in an enabled state.
- [mediaType](mediatype.md) — The media type of the port.
- [formatDescription](formatdescription.md) — A description of the port format.
- [sourceDevicePosition](sourcedeviceposition.md) — The position of the source device providing input through this port.
- [clock](clock.md) — An object that represents the capture device’s clock.
