---
title: photoQualityPrioritization
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/photoqualityprioritization
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/photoqualityprioritization'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/photoqualityprioritization.json'
content_hash: 'sha256:10feac6148bfbe10'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# photoQualityPrioritization

<sub>Instance Property</sub>

A setting that indicates how to prioritize photo quality against speed of photo delivery.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var photoQualityPrioritization: AVCapturePhotoOutput.QualityPrioritization { get set }
```

## Discussion

[AVCapturePhotoOutput](../avcapturephotooutput.md) applies a variety of techniques to improve photo quality, depending on the source device’s [activeFormat](../avcapturedevice/activeformat.md). Some of these techniques — which include reducing noise, preserving detail in low light, and freezing motion — can take significant processing time before the system returns a photo to your delegate callback. This property allows you to specify your preferred quality versus speed of delivery.

The default value of this property is [AVCapturePhotoQualityPrioritizationBalanced](../avcapturephotooutput/qualityprioritization/balanced.md) and indicates that speed and quality are of equal importance to you.

When you need to prioritize speed at the expense of quality, use [AVCapturePhotoQualityPrioritizationSpeed](../avcapturephotooutput/qualityprioritization/speed.md). Use [AVCapturePhotoQualityPrioritizationQuality](../avcapturephotooutput/qualityprioritization/quality.md) to prioritize the best quality at the expense of speed.

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [cameraCalibrationDataDeliveryEnabled](iscameracalibrationdatadeliveryenabled.md) — A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [autoContentAwareDistortionCorrectionEnabled](isautocontentawaredistortioncorrectionenabled.md) — A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) — A Boolean value that specifies whether to use automatic virtual-device image fusion.
- [virtualDeviceConstituentPhotoDeliveryEnabledDevices](virtualdeviceconstituentphotodeliveryenableddevices.md) — The constituent devices for which the virtual device should deliver photos.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
