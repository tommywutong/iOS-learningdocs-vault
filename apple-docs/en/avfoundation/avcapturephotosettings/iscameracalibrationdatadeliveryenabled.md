---
title: isCameraCalibrationDataDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+, iPadOS 11.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/iscameracalibrationdatadeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/iscameracalibrationdatadeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/iscameracalibrationdatadeliveryenabled.json'
content_hash: 'sha256:674291db6ca74d24'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isCameraCalibrationDataDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether a dual photo capture also delivers camera calibration data.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isCameraCalibrationDataDeliveryEnabled: Bool { get set }
```

## Discussion

When this setting is [false](../../swift/false.md) (the default), and the [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) setting is [true](../../swift/true.md), dual photo capture doesn’t deliver additional data.

If you change this setting to [true](../../swift/true.md), the [AVCapturePhoto](../avcapturephoto.md) results from a dual photo capture include [AVCameraCalibrationData](../avcameracalibrationdata.md) objects that describe the imaging parameters for each camera. This data can be useful for performing computer vision tasks on the resulting images.

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [photoQualityPrioritization](photoqualityprioritization.md) — A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [autoContentAwareDistortionCorrectionEnabled](isautocontentawaredistortioncorrectionenabled.md) — A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) — A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [virtualDeviceConstituentPhotoDeliveryEnabledDevices](virtualdeviceconstituentphotodeliveryenableddevices.md) — The constituent devices for which the virtual device should deliver photos.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
