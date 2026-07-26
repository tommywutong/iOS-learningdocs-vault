---
title: builtInTripleCamera
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintriplecamera
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintriplecamera'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/devicetype-swift.struct/builtintriplecamera.json'
content_hash: 'sha256:18b4537a8f38c4bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [AVFoundation](../../../avfoundation.md) · [AVCaptureDevice](../../avcapturedevice.md) · [DeviceType](../devicetype-swift.struct.md)

# builtInTripleCamera

<sub>Type Property</sub>

A built-in camera device type that consists of three cameras of fixed focal length, one ultrawide angle, one wide angle, and one telephoto.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
static let builtInTripleCamera: AVCaptureDevice.DeviceType
```

## Discussion

The built-in triple camera supports the following features:

- Automatic switching from one camera to another when zoom factor, light level, and focus position allow.
- Delivery of photos from constituent devices (ultrawide angle, wide angle, and telephoto cameras) from a single photo capture request.

The built-in triple camera doesn’t support the following features:

- [AVCaptureExposureModeCustom](../exposuremode-swift.enum/custom.md) and manual exposure bracketing.
- Locking focus with a lens position other than [AVCaptureLensPositionCurrent](../currentlensposition.md).
- Locking automatic white balance with device white balance gains other than [AVCaptureWhiteBalanceGainsCurrent](../currentwhitebalancegains.md).

Even when locked, exposure duration, ISO, aperture, white balance gains, or lens position may change when the device switches from one camera to another. However, the overall exposure, white balance, and focus position should be consistent.

> [!note] Note
> You can only discover this device type using an [DiscoverySession](../discoverysession.md) or the [AVCaptureDevice](../../avcapturedevice.md) [+ defaultDeviceWithDeviceType:mediaType:position:](<../default(__for_position_).md>) method.

## See Also

### Cameras

- [AVCaptureDeviceTypeBuiltInWideAngleCamera](builtinwideanglecamera.md) — A built-in wide-angle camera device type.
- [AVCaptureDeviceTypeBuiltInUltraWideCamera](builtinultrawidecamera.md) — A built-in camera device type with a shorter focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInTelephotoCamera](builtintelephotocamera.md) — A built-in camera device type with a longer focal length than a wide-angle camera.
- [AVCaptureDeviceTypeBuiltInDualCamera](builtindualcamera.md) — A built-in camera device type that consists of a wide-angle and telephoto camera.
- [AVCaptureDeviceTypeBuiltInDualWideCamera](builtindualwidecamera.md) — A built-in camera device type that consists of two cameras of fixed focal length, one ultrawide angle and one wide angle.
- [AVCaptureDeviceTypeContinuityCamera](continuitycamera.md) — A Continuity Camera device type.
- [AVCaptureDeviceTypeBuiltInDuoCamera](builtinduocamera.md) — A built-in dual camera device type. _(deprecated)_
