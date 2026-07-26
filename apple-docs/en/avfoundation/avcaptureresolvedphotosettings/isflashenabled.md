---
title: isFlashEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/isflashenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isflashenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/isflashenabled.json'
content_hash: 'sha256:007b6d5bebb77f6d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# isFlashEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether the camera flash fires for this capture.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isFlashEnabled: Bool { get }
```

## Discussion

This property corresponds to the [AVCapturePhotoSettings](../avcapturephotosettings.md) property [flashMode](../avcapturephotosettings/flashmode.md).

If you specify a flash mode of [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md) when requesting a capture, the device automatically chooses whether to use the flash based on the scene contents at the moment of capture. Therefore, you don’t know whether the flash will fire until right before the moment of capture. When the photo output calls your [- captureOutput:willBeginCaptureForResolvedSettings:](<../avcapturephotocapturedelegate/photooutput(__willbegincapturefor_).md>) method (or other delegate methods that occur later in the capture process), you can use this property to determine whether a capture uses the flash.

> [!note] Note
> The flash can also become temporarily disabled if the device is too hot. In this case, the flash will not fire even if you specify a flash mode of [AVCaptureFlashModeOn](../avcapturedevice/flashmode-swift.enum/on.md), and the resolved photo settings object passed to your [AVCapturePhotoCaptureDelegate](../avcapturephotocapturedelegate.md) method has a [flashEnabled](isflashenabled.md) value of [false](../../swift/false.md). To detect when the flash is temporarily disabled, key-value observe the [flashAvailable](../avcapturedevice/isflashavailable.md) property.

## See Also

### Examining photo capture settings

- [redEyeReductionEnabled](isredeyereductionenabled.md) — A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.
- [virtualDeviceFusionEnabled](isvirtualdevicefusionenabled.md) — A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [fastCapturePrioritizationEnabled](isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [stillImageStabilizationEnabled](isstillimagestabilizationenabled.md) — A Boolean value indicating whether this capture uses image stabilization. _(deprecated)_
- [dualCameraFusionEnabled](isdualcamerafusionenabled.md) — A Boolean value indicating whether this capture combines image data from a dual camera. _(deprecated)_
