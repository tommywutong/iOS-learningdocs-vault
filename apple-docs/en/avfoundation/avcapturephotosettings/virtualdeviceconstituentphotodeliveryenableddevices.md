---
title: virtualDeviceConstituentPhotoDeliveryEnabledDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/virtualdeviceconstituentphotodeliveryenableddevices.json'
content_hash: 'sha256:c96689e92d172c60'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# virtualDeviceConstituentPhotoDeliveryEnabledDevices

<sub>Instance Property</sub>

The constituent devices for which the virtual device should deliver photos.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var virtualDeviceConstituentPhotoDeliveryEnabledDevices: [AVCaptureDevice] { get set }
```

## Discussion

You can opt in to constituent-device photo delivery by setting this property to any subset of the devices in the virtual device’s [constituentDevices](../avcapturedevice/constituentdevices.md) array. The framework calls your [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>)callback once for each of the devices you include in the array.

You may only set this property to a non-`nil` array if you’ve set your photo output’s [virtualDeviceConstituentPhotoDeliveryEnabled](../avcapturephotooutput/isvirtualdeviceconstituentphotodeliveryenabled.md) property to [true](../../swift/true.md), and your delegate implements the [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method.

The default value of this property is an empty array.

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [photoQualityPrioritization](photoqualityprioritization.md) — A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [cameraCalibrationDataDeliveryEnabled](iscameracalibrationdatadeliveryenabled.md) — A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [autoContentAwareDistortionCorrectionEnabled](isautocontentawaredistortioncorrectionenabled.md) — A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) — A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
