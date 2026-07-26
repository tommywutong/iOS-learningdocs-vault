---
title: flashMode
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, macOS 13.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotosettings/flashmode
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotosettings/flashmode'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotosettings/flashmode.json'
content_hash: 'sha256:6652bc04d33cdad5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoSettings](../avcapturephotosettings.md)

# flashMode

<sub>Instance Property</sub>

A setting for whether to fire the flash when capturing photos.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var flashMode: AVCaptureDevice.FlashMode { get set }
```

## Discussion

The default value for this setting is [AVCaptureFlashModeOff](../avcapturedevice/flashmode-swift.enum/off.md).

> [!note] Note
> This setting supersedes the deprecated [AVCaptureDevice](../avcapturedevice.md) [flashMode](../avcapturedevice/flashmode-swift.property.md) property. When using the [AVCapturePhotoOutput](../avcapturephotooutput.md) class, the capture device’s flash mode doesn’t apply—use this property on your photo settings object instead.

Assuming a static scene, using the [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md) setting is equivalent to testing the [AVCapturePhotoOutput](../avcapturephotooutput.md) [isFlashScene](../avcapturephotooutput/isflashscene.md) property (which indicates whether flash is recommended for the scene currently visible to the camera), and then setting the [flashMode](flashmode.md) property of your photo settings output accordingly before requesting a capture. However, the visible scene can change between when you request a capture and when the camera hardware captures an image—the automatic setting ensures that the flash is enabled or disabled appropriately at the moment of capture. When the capture occurs, your [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md) methods receive an [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) object whose [flashEnabled](../avcaptureresolvedphotosettings/isflashenabled.md) property indicates which flash mode was used for that capture.

> [!note] Note
> When the device becomes very hot, the flash becomes temporarily unavailable until the device cools down (see the [AVCaptureDevice](../avcapturedevice.md) [flashAvailable](../avcapturedevice/isflashavailable.md) property). While the flash is unavailable, a photo output’s [supportedFlashModes](../avcapturephotooutput/supportedflashmodes-4u69s.md) property still reports the [AVCaptureFlashModeOn](../avcapturedevice/flashmode-swift.enum/on.md) and [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md) options as available, so you can still enable the flash in your photo settings even when the flash is temporarily unavailable.
>
> When the photo output calls your [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md) methods, check the [flashEnabled](../avcaptureresolvedphotosettings/isflashenabled.md) property of the provided [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md) to verify whether the flash is in use.

When specifying a flash mode, the following requirements apply:

- The specified mode must be present in the photo output’s [supportedFlashModes](../avcapturephotooutput/supportedflashmodes-4u69s.md) array.
- You may not enable image stabilization if the flash mode is [AVCaptureFlashModeOn](../avcapturedevice/flashmode-swift.enum/on.md). (Enabling the flash takes priority over the [autoStillImageStabilizationEnabled](isautostillimagestabilizationenabled.md) setting).

The capture output validates these requirements when you call the [- capturePhotoWithSettings:delegate:](<../avcapturephotooutput/capturephoto(with_delegate_).md>) method. If your settings don’t meet these requirements, that method raises an exception.

## See Also

### Configuring photo settings

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
- [highResolutionPhotoEnabled](ishighresolutionphotoenabled.md) — A Boolean value that specifies whether to capture still images at the highest resolution supported by the active device and format. _(deprecated)_
