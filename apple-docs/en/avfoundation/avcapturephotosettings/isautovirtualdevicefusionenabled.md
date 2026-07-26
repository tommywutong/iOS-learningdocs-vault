---
title: isAutoVirtualDeviceFusionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/isautovirtualdevicefusionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/isautovirtualdevicefusionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/isautovirtualdevicefusionenabled.json'
content_hash: 'sha256:5280ae981fac3d94'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# isAutoVirtualDeviceFusionEnabled

<sub>Instance Property</sub>

A Boolean value that specifies whether to use automatic virtual-device image fusion.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isAutoVirtualDeviceFusionEnabled: Bool { get set }
```

## Discussion

When [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) and [virtualDeviceFusionSupported](../avcapturephotooutput/isvirtualdevicefusionsupported.md) are true, the framework may fuse constituent camera images of a virtual device to improve still image quality, depending on the current zoom factor, light levels, and focus position. You can determine whether virtual device fusion is enabled for a particular capture request by inspecting the [virtualDeviceFusionEnabled](../avcaptureresolvedphotosettings/isvirtualdevicefusionenabled.md) property of [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md).

The default value for this property is true, unless you’re capturing a RAW photo or a bracket using [AVCapturePhotoBracketSettings](../avcapturephotobracketsettings.md).

> [!note] Note
> When using the deprecated [AVCaptureStillImageOutput](../avcapturestillimageoutput.md) interface with a virtual device, [autoVirtualDeviceFusionEnabled](isautovirtualdevicefusionenabled.md) is always enabled, if supported.

## See Also

### Configuring photo settings

- [flashMode](flashmode.md) — A setting for whether to fire the flash when capturing photos.
- [autoRedEyeReductionEnabled](isautoredeyereductionenabled.md) — A Boolean value that indicates whether to use auto red-eye reduction on flash captures.
- [maxPhotoDimensions](maxphotodimensions.md) — The maximum resolution of the photo to capture.
- [photoQualityPrioritization](photoqualityprioritization.md) — A setting that indicates how to prioritize photo quality against speed of photo delivery.
- [cameraCalibrationDataDeliveryEnabled](iscameracalibrationdatadeliveryenabled.md) — A Boolean value that determines whether a dual photo capture also delivers camera calibration data.
- [autoContentAwareDistortionCorrectionEnabled](isautocontentawaredistortioncorrectionenabled.md) — A Boolean value that specifies whether the photo output, at its discretion, uses content-aware distortion correction on this photo request.
- [virtualDeviceConstituentPhotoDeliveryEnabledDevices](virtualdeviceconstituentphotodeliveryenableddevices.md) — The constituent devices for which the virtual device should deliver photos.
- [dualCameraDualPhotoDeliveryEnabled](isdualcameradualphotodeliveryenabled.md) — A Boolean value that determines whether a dual camera device delivers images from both cameras. _(deprecated)_
- [autoDualCameraFusionEnabled](isautodualcamerafusionenabled.md) — A Boolean value that specifies whether captures automatically combine data from a dual camera device. _(deprecated)_
- [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) — A Boolean value that specifies whether captures use automatic image stabilization. _(deprecated)_
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
