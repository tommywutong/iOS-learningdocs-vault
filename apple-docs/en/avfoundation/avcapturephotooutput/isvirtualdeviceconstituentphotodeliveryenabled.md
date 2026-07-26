---
title: isVirtualDeviceConstituentPhotoDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.json'
content_hash: 'sha256:a9301fd20d742fe6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isVirtualDeviceConstituentPhotoDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVirtualDeviceConstituentPhotoDeliveryEnabled: Bool { get set }
```

## Discussion

You can only set this value to [true](../../swift/true.md) when [virtualDeviceConstituentPhotoDeliverySupported](isvirtualdeviceconstituentphotodeliverysupported.md) is [true](../../swift/true.md).

The default value is [false](../../swift/false.md).

> [!important] Important
> Virtual device constituent photo delivery requires a lengthy reconfiguration of the capture render pipeline, so enable this property prior to starting the capture session.

## See Also

### Configuring virtual device capture

- [virtualDeviceFusionSupported](isvirtualdevicefusionsupported.md) — A Boolean value that indicates whether the device supports virtual device image fusion.
- [virtualDeviceConstituentPhotoDeliverySupported](isvirtualdeviceconstituentphotodeliverysupported.md) — A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.
