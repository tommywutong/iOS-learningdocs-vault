---
title: isStillImageStabilizationEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+（13.0 起废弃）, iPadOS 10.0+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）, tvOS 10.0+（13.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/isstillimagestabilizationenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isstillimagestabilizationenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/isstillimagestabilizationenabled.json'
content_hash: 'sha256:98af623a03a01a31'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# isStillImageStabilizationEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether this capture uses image stabilization.

> [!warning] Deprecated
> Use [photoProcessingTimeRange](photoprocessingtimerange.md) instead.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var isStillImageStabilizationEnabled: Bool { get }
```

## Discussion

This property corresponds to the [AVCapturePhotoSettings](../avcapturephotosettings.md) property [autoStillImageStabilizationEnabled](../avcapturephotosettings/isautostillimagestabilizationenabled.md).

When this value is [true](../../swift/true.md), the device automatically applies stabilization in low-light conditions to counteract hand shake. Automatic stabilization always includes digital image stabilization, and may also include optical lens stabilization, based on the current device.

If you specify automatic stabilization when requesting a capture, the device automatically chooses whether to use image stabilization based on the scene contents at the moment of capture. Therefore, you don’t know whether the system uses stabilization until right before the moment of capture. When the photo output calls your [- captureOutput:willBeginCaptureForResolvedSettings:](<../avcapturephotocapturedelegate/photooutput(__willbegincapturefor_).md>) method (or other delegate methods that occur later in the capture process), you can use this property to determine whether stabilization is active.

## See Also

### Examining photo capture settings

- [flashEnabled](isflashenabled.md) — A Boolean value indicating whether the camera flash fires for this capture.
- [redEyeReductionEnabled](isredeyereductionenabled.md) — A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.
- [virtualDeviceFusionEnabled](isvirtualdevicefusionenabled.md) — A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [fastCapturePrioritizationEnabled](isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [dualCameraFusionEnabled](isdualcamerafusionenabled.md) — A Boolean value indicating whether this capture combines image data from a dual camera. _(deprecated)_
