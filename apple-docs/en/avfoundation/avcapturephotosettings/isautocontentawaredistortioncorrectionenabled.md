---
title: isAutoContentAwareDistortionCorrectionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 14.1+, iPadOS 14.1+, Mac Catalyst 14.1+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isautocontentawaredistortioncorrectionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautocontentawaredistortioncorrectionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isautocontentawaredistortioncorrectionenabled.json'
content_hash: 'sha256:ff225c3c260956a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isAutoContentAwareDistortionCorrectionEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isAutoContentAwareDistortionCorrectionEnabled: Bool { get set }
```

## Discussion

The default value is [false](../../swift/false.md). Enabling this setting introduces a small amount of latency when processing the photo request.

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [photoQualityPrioritization](photoqualityprioritization.md) — A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [cameraCalibrationDataDeliveryEnabled](iscameracalibrationdatadeliveryenabled.md) — A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) — A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [virtualDeviceConstituentPhotoDeliveryEnabledDevices](virtualdeviceconstituentphotodeliveryenableddevices.md) — The constituent devices for which the virtual device should deliver photos.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
