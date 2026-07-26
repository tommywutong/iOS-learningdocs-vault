---
title: isVirtualDeviceConstituentPhotoDeliverySupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliverysupported.json'
content_hash: 'sha256:6ae00d34b5757693'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isVirtualDeviceConstituentPhotoDeliverySupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVirtualDeviceConstituentPhotoDeliverySupported: Bool { get }
```

## Discussion

The system only supports virtual device constituent photo delivery for certain capture session presets and capture device formats.

When switching cameras or formats, this property may change. When this property changes from [true](../../swift/true.md) to [false](../../swift/false.md), [virtualDeviceConstituentPhotoDeliveryEnabled](isvirtualdeviceconstituentphotodeliveryenabled.md) also reverts to [false](../../swift/false.md).

This property is key-value observable.

## See Also

### Configuring virtual device capture

- [virtualDeviceFusionSupported](isvirtualdevicefusionsupported.md) — A Boolean value that indicates whether the device supports virtual device image fusion.
- [virtualDeviceConstituentPhotoDeliveryEnabled](isvirtualdeviceconstituentphotodeliveryenabled.md) — A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.
