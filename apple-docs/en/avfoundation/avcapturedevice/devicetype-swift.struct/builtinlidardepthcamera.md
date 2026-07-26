---
title: builtInLiDARDepthCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 15.4+, iPadOS 15.4+, Mac Catalyst 15.4+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinlidardepthcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinlidardepthcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtinlidardepthcamera.json'
content_hash: 'sha256:9c48216eaf0c533e'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# builtInLiDARDepthCamera

<sub>Type Property</sub>

A device that consists of two cameras, one LiDAR and one YUV.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let builtInLiDARDepthCamera: AVCaptureDevice.DeviceType
```

## Discussion

The LiDAR camera provides high-quality, high-accuracy depth information by measuring the round trip of an artificial light signal that a laser emits. The device synchronizes and perspective-corrects this data to frames that the YUV camera produces. While the resolution of the depth data and YUV frames may differ, their field of view and aspect ratio always match.

> [!note] Note
> You can only discover devices of this type by using an [DiscoverySession](../discoverysession.md) or by calling the [+ defaultDeviceWithDeviceType:mediaType:position:](<../default(__for_position_).md>) method.

## See Also

### Depth sensing

- [AVCaptureDeviceTypeBuiltInTrueDepthCamera](builtintruedepthcamera.md) — A device that consists of two cameras, one Infrared and one YUV.
