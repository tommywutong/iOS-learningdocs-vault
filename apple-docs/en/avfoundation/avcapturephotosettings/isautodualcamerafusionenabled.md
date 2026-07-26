---
title: isAutoDualCameraFusionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+（13.0 起废弃）, iPadOS 10.2+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotosettings/isautodualcamerafusionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautodualcamerafusionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isautodualcamerafusionenabled.json'
content_hash: 'sha256:fb53eadfec5a6433'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isAutoDualCameraFusionEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether captures automatically combine data from a dual camera device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isAutoDualCameraFusionEnabled: Bool { get set }
```

## Discussion

The default setting is [true](../../swift/true.md), unless you are capturing a RAW photo. (By definition, RAW photos are unprocessed, and image fusion involves processing the captured image).

When you enable this setting, a dual-camera device automatically combines samples from both cameras to produce a higher quality image. This property applies only when using the [AVCaptureDeviceTypeBuiltInDualCamera](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device type on supported devices.

> [!tip] Tip
> Image processing, including dual camera fusion, increases capture time. To capture photos at the highest possible speed (like in the built-in Camera app’s burst mode), set the [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) and [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) properties to [false](../../swift/false.md) and the [flashMode](flashmode.md) property to [AVCaptureFlashModeOff](../avcapturedevice/flashmode-swift.enum/off.md).

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [photoQualityPrioritization](photoqualityprioritization.md) — A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [cameraCalibrationDataDeliveryEnabled](iscameracalibrationdatadeliveryenabled.md) — A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [autoContentAwareDistortionCorrectionEnabled](isautocontentawaredistortioncorrectionenabled.md) — A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) — A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [virtualDeviceConstituentPhotoDeliveryEnabledDevices](virtualdeviceconstituentphotodeliveryenableddevices.md) — The constituent devices for which the virtual device should deliver photos.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
