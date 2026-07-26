---
title: isAutoStillImageStabilizationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotosettings/isautostillimagestabilizationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautostillimagestabilizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isautostillimagestabilizationenabled.json'
content_hash: 'sha256:dece6ebeec22c5bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isAutoStillImageStabilizationEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether captures use automatic image stabilization.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isAutoStillImageStabilizationEnabled: Bool { get set }
```

## Discussion

The default setting is [true](../../swift/true.md), unless you are capturing a RAW photo (By definition, RAW photos are unprocessed, and image stabilization involves processing the captured image).

When you enable this setting, the device automatically applies stabilization in low-light conditions to counteract hand shake. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device.

Automatic image stabilization is not compatible with the [AVCaptureFlashModeOn](../avcapturedevice/flashmode-swift.enum/on.md) setting. If you explicitly enable the flash, the photo output ignores your image stabilization setting, and the [stillImageStabilizationEnabled](../avcaptureresolvedphotosettings/isstillimagestabilizationenabled.md) property of the [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) object provided to your photo capture delegate is always [false](../../swift/false.md).

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
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
