---
title: isHighResolutionPhotoEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（16.0 起废弃）, iPadOS 10.0+（16.0 起废弃）, Mac Catalyst 14.0+（16.0 起废弃）, macOS 10.15+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcapturephotosettings/ishighresolutionphotoenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/ishighresolutionphotoenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/ishighresolutionphotoenabled.json'
content_hash: 'sha256:10ac00695131b7ff'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isHighResolutionPhotoEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format.

> [!warning] Deprecated
> Use maxPhotoDimensions instead.

<sub>iOS, iPadOS, Mac Catalyst, macOS</sub>

```swift
var isHighResolutionPhotoEnabled: Bool { get set }
```

## Discussion

When this setting is [false](../../swift/false.md) (the default), a photo capture output delivers images with the dimensions specified by the [formatDescription](../avcapturedevice/format/formatdescription.md) property of the source [AVCaptureDevice](../avcapturedevice.md) object’s active capture format. However, some devices and capture formats allow for still image capture at resolutions higher than their video capture (and streaming photo preview) resolution. To capture the highest possible resolution for still photos (described by the capture format’s [highResolutionStillImageDimensions](../avcapturedevice/format/highresolutionstillimagedimensions.md) property), change this setting to [true](../../swift/true.md).

If any output connected to your capture session enables video stabilization (see the [AVCaptureConnection](../avcaptureconnection.md) [preferredVideoStabilizationMode](../avcaptureconnection/preferredvideostabilizationmode.md) property), captured images may be around 10% smaller than the maximum still image dimensions. (This size change is an effect of video stabilization, which works by cropping and rotating to find the stable region in a moving image). Examine the [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) object provided to your photo capture delegate to find the actual dimensions of each captured photo.

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
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
