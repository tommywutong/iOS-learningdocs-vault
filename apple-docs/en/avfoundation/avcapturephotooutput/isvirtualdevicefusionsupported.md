---
title: isVirtualDeviceFusionSupported
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/isvirtualdevicefusionsupported
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/isvirtualdevicefusionsupported'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/isvirtualdevicefusionsupported.json'
content_hash: 'sha256:c90710a9e89bdafb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# isVirtualDeviceFusionSupported

<sub>Instance Property</sub>

A Boolean value that indicates whether the device supports virtual device image fusion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isVirtualDeviceFusionSupported: Bool { get }
```

## Discussion

When using a virtual capture device, the system can fuse the images from its constituent cameras to improve image quality.

If the current configuration doesn’t support virtual device fusion, your capture requests always resolve [virtualDeviceFusionEnabled](../avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md) to [false](../../swift/false.md).

This property is key-value observable.

## See Also

### Configuring virtual device capture

- [virtualDeviceConstituentPhotoDeliverySupported](isvirtualdeviceconstituentphotodeliverysupported.md) — A Boolean value that indicates whether the photo output configuration supports delivery of photos from constituent cameras of a virtual device.
- [virtualDeviceConstituentPhotoDeliveryEnabled](isvirtualdeviceconstituentphotodeliveryenabled.md) — A Boolean value that indicates whether the photo output delivers photos from constituent cameras of a virtual device.
