---
title: builtInTelephotoCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintelephotocamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintelephotocamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintelephotocamera.json'
content_hash: 'sha256:1c1cee53fa7fb63a'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# builtInTelephotoCamera

<sub>Type Property</sub>

A built-in camera device type with a longer focal length than a wide-angle camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let builtInTelephotoCamera: AVCaptureDevice.DeviceType
```

## Discussion

You can only discover this device type using an [DiscoverySession](../discoverysession.md).

## See Also

### Cameras

- [AVCaptureDeviceTypeBuiltInWideAngleCamera](builtinwideanglecamera.md) — A built-in wide-angle camera device type.
- [AVCaptureDeviceTypeBuiltInUltraWideCamera](builtinultrawidecamera.md) — A built-in camera device type with a shorter focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInDualCamera](builtindualcamera.md) — A built-in camera device type that consists of a wide-angle and telephoto camera.
- [AVCaptureDeviceTypeBuiltInDualWideCamera](builtindualwidecamera.md) — A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [AVCaptureDeviceTypeBuiltInTripleCamera](builtintriplecamera.md) — A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [AVCaptureDeviceTypeContinuityCamera](continuitycamera.md) — A Continuity Camera device type.
- [AVCaptureDeviceTypeBuiltInDuoCamera](builtinduocamera.md) — A built-in dual camera device type. _(deprecated)_
