---
title: builtInTrueDepthCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 11.1+, iPadOS 11.1+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintruedepthcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintruedepthcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintruedepthcamera.json'
content_hash: 'sha256:0098b517009c2bab'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# builtInTrueDepthCamera

<sub>Type Property</sub>

A device that consists of two cameras, one Infrared and one YUV.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let builtInTrueDepthCamera: AVCaptureDevice.DeviceType
```

## Discussion

The infrared camera provides high-quality depth information that’s synchronized and perspective corrected to the frame the YUV camera produces. While the resolution of the depth data and YUV frames may differ, their field of view and aspect ratio always match.

> [!important] Important
> To obtain a device of this type, use the [+ defaultDeviceWithDeviceType:mediaType:position:](<../default(__for_position_).md>) method or the [DiscoverySession](../discoverysession.md) class. Other methods don’t discover devices of this type.

## See Also

### Depth sensing

- [AVCaptureDeviceTypeBuiltInLiDARDepthCamera](builtinlidardepthcamera.md) — A device that consists of two cameras, one LiDAR and one YUV.
