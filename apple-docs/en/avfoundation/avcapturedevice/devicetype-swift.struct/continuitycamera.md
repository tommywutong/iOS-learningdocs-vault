---
title: continuityCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/continuitycamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/continuitycamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/continuitycamera.json'
content_hash: 'sha256:c550057c5f149a6b'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# continuityCamera

<sub>Type Property</sub>

A Continuity Camera device type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
static let continuityCamera: AVCaptureDevice.DeviceType
```

## Discussion

You discover devices of this type using an [DiscoverySession](../discoverysession.md) of by calling the device’s [+ defaultDeviceWithDeviceType:mediaType:position:](<../default(__for_position_).md>) method.

## See Also

### Cameras

- [AVCaptureDeviceTypeBuiltInWideAngleCamera](builtinwideanglecamera.md) — A built-in wide-angle camera device type.
- [AVCaptureDeviceTypeBuiltInUltraWideCamera](builtinultrawidecamera.md) — A built-in camera device type with a shorter focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInTelephotoCamera](builtintelephotocamera.md) — A built-in camera device type with a longer focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInDualCamera](builtindualcamera.md) — A built-in camera device type that consists of a wide-angle and telephoto camera.
- [AVCaptureDeviceTypeBuiltInDualWideCamera](builtindualwidecamera.md) — A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [AVCaptureDeviceTypeBuiltInTripleCamera](builtintriplecamera.md) — A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [AVCaptureDeviceTypeBuiltInDuoCamera](builtinduocamera.md) — A built-in dual camera device type. _(deprecated)_
