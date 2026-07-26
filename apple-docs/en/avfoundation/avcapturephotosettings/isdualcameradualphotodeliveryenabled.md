---
title: isDualCameraDualPhotoDeliveryEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 11.0+（13.0 起废弃）, iPadOS 11.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotosettings/isdualcameradualphotodeliveryenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isdualcameradualphotodeliveryenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isdualcameradualphotodeliveryenabled.json'
content_hash: 'sha256:de027f7b10b2beb2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isDualCameraDualPhotoDeliveryEnabled

<sub>Instance Property</sub>

A Boolean value that determines whether a dual camera device delivers images from both cameras.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDualCameraDualPhotoDeliveryEnabled: Bool { get set }
```

## Discussion

When this property is [false](../../swift/false.md) (the default), and the photo output is configured with a capture device of the [AVCaptureDeviceTypeBuiltInDualCamera](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) type, the photo output delivers a single main photo image for each capture. (The device determines how to produce that image from one or both cameras).

If you change this setting to [true](../../swift/true.md), your delegate’s [- captureOutput:didFinishProcessingPhoto:error:](<../avcapturephotocapturedelegate/photooutput(__didfinishprocessingphoto_error_).md>) method fires at least twice for each main image—once for the telephoto image and again for the wide-angle image. Setting this property to true when not using a dual-camera device raises an exception.

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
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
