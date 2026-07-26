---
title: builtInDualCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 10.2+, iPadOS 10.2+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtindualcamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtindualcamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtindualcamera.json'
content_hash: 'sha256:042fea4c9bc5c258'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# builtInDualCamera

<sub>Type Property</sub>

A built-in camera device type that consists of a wide-angle and telephoto camera.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let builtInDualCamera: AVCaptureDevice.DeviceType
```

## Discussion

This device type supports the following features:

- Automatic switching from one camera to the other when the zoom factor, light level, and focus position allow.
- Higher-quality zoom for still captures by fusing images from both cameras.
- Depth data delivery by measuring the disparity of matched features between the wide and telephoto cameras.
- Delivery of photos from constituent devices (wide and telephoto cameras) from a single photo capture request.

It doesn’t support the features below:

- Setting a [AVCaptureExposureModeCustom](../exposuremode-swift.enum/custom.md) exposure mode or manual exposure bracketing.
- Locking focus with a lens position to a value other than [AVCaptureLensPositionCurrent](../currentlensposition.md).
- Locking automatic white balance with device white balance gains other than [AVCaptureWhiteBalanceGainsCurrent](../currentwhitebalancegains.md).

Even when locked, exposure duration, ISO, aperture, white balance gains, or lens position may change when the device switches from one camera to the other. The overall exposure, white balance, and focus position however should be consistent.

You can only retrieve devices of this type using an [DiscoverySession](../discoverysession.md) or by calling [+ defaultDeviceWithDeviceType:mediaType:position:](<../default(__for_position_).md>).

## See Also

### Cameras

- [AVCaptureDeviceTypeBuiltInWideAngleCamera](builtinwideanglecamera.md) — A built-in wide-angle camera device type.
- [AVCaptureDeviceTypeBuiltInUltraWideCamera](builtinultrawidecamera.md) — A built-in camera device type with a shorter focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInTelephotoCamera](builtintelephotocamera.md) — A built-in camera device type with a longer focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInDualWideCamera](builtindualwidecamera.md) — A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [AVCaptureDeviceTypeBuiltInTripleCamera](builtintriplecamera.md) — A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.
- [AVCaptureDeviceTypeContinuityCamera](continuitycamera.md) — A Continuity Camera device type.
- [AVCaptureDeviceTypeBuiltInDuoCamera](builtinduocamera.md) — A built-in dual camera device type. _(deprecated)_
