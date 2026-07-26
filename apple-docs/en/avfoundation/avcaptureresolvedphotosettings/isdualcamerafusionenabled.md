---
title: isDualCameraFusionEnabled
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.2+（13.0 起废弃）, iPadOS 10.2+（13.0 起废弃）, Mac Catalyst 13.1+（13.1 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/avfoundation/avcaptureresolvedphotosettings/isdualcamerafusionenabled
source_url: 'https://developer.apple.com/documentation/avfoundation/avcaptureresolvedphotosettings/isdualcamerafusionenabled'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcaptureresolvedphotosettings/isdualcamerafusionenabled.json'
content_hash: 'sha256:b34f59827d1c624d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureResolvedPhotoSettings](../avcaptureresolvedphotosettings.md)

# isDualCameraFusionEnabled

<sub>Instance Property</sub>

A Boolean value indicating whether this capture combines image data from a dual camera.

> [!warning] Deprecated
> Use [virtualDeviceFusionEnabled](isvirtualdevicefusionenabled.md) instead.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
var isDualCameraFusionEnabled: Bool { get }
```

## Discussion

This property corresponds to the [AVCapturePhotoSettings](../avcapturephotosettings.md) property [autoDualCameraFusionEnabled](../avcapturephotosettings/isautodualcamerafusionenabled.md).

When this value is [true](../../swift/true.md), a dual-camera device automatically combines samples from both cameras to produce a higher quality image. This property applies only when using the [AVCaptureDeviceTypeBuiltInDualCamera](../avcapturedevice/devicetype-swift.struct/builtindualcamera.md) device type on supported devices.

If you specify automatic image fusion when requesting a capture, the device automatically chooses whether to use image fusion based on the scene conditions at the moment of capture. Therefore, you don’t know whether the system uses image fusion until right before the moment of capture. When the photo output calls your [- captureOutput:willBeginCaptureForResolvedSettings:](<../avcapturephotocapturedelegate/photooutput(__willbegincapturefor_).md>) method (or other delegate methods that occur later in the capture process), you can use this property to determine whether image fusion is active.

## See Also

### Examining photo capture settings

- [flashEnabled](isflashenabled.md) — A Boolean value indicating whether the camera flash fires for this capture.
- [redEyeReductionEnabled](isredeyereductionenabled.md) — A Boolean value indicating whether the camera automatically reduces red-eye when capturing photos.
- [virtualDeviceFusionEnabled](isvirtualdevicefusionenabled.md) — A Boolean value that specifies whether the system automatically uses virtual device image fusion.
- [fastCapturePrioritizationEnabled](isfastcaptureprioritizationenabled.md) — A Boolean value that indicates whether the system uses fast capture prioritization when capturing the photo.
- [contentAwareDistortionCorrectionEnabled](iscontentawaredistortioncorrectionenabled.md) — A Boolean value that indicates whether the system applies content-aware distortion correction when capturing the photo.
- [stillImageStabilizationEnabled](isstillimagestabilizationenabled.md) — A Boolean value indicating whether this capture uses image stabilization. _(deprecated)_
