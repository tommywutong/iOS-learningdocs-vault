---
title: sourceDeviceType
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephoto/sourcedevicetype
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephoto/sourcedevicetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephoto/sourcedevicetype.json'
content_hash: 'sha256:1fc9dc1afbef0956'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhoto](../avcapturephoto.md)

# sourceDeviceType

<sub>Instance Property</sub>

The type of device that captured the photo.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var sourceDeviceType: AVCaptureDevice.DeviceType? { get }
```

## Discussion

When you capture dual photos with a [AVCaptureDeviceTypeBuiltInDualCamera](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device and the [dualCameraDualPhotoDeliveryEnabled](../avcapturephotosettings/isdualcameradualphotodeliveryenabled.md) setting, use this property to determine which of the two resulting photo objects is from the [AVCaptureDeviceTypeBuiltInWideAngleCamera](../avcapturedevice/devicetype-swift.struct/builtinwideanglecamera.md) or [AVCaptureDeviceTypeBuiltInTelephotoCamera](../avcapturedevice/devicetype-swift.struct/builtintelephotocamera.md) device.

For all other captures, this property’s value is equal to the [deviceType](../avcapturedevice/devicetype-swift.property.md) property of the capture device to which the photo output is connected.

This property’s value can be `nil` if the [AVCapturePhoto](../avcapturephoto.md) object did not come from an [AVCaptureDevice](../avcapturedevice.md) capture.

## See Also

### Accessing photo metadata

- [depthData](depthdata.md) — Depth or disparity map data captured with the photo.
- [cameraCalibrationData](cameracalibrationdata.md) — Calibration information for the camera device that captured the photo.
- [metadata](metadata.md) — A dictionary of metadata describing the captured image.
- [portraitEffectsMatte](portraiteffectsmatte.md) — The portrait effects matte captured with the photo.
