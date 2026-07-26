---
title: photoSettingsForSceneMonitoring
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 10.0+, iPadOS 10.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturephotooutput/photosettingsforscenemonitoring
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturephotooutput/photosettingsforscenemonitoring'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturephotooutput/photosettingsforscenemonitoring.json'
content_hash: 'sha256:8cd6e49e02025cb9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCapturePhotoOutput](../avcapturephotooutput.md)

# photoSettingsForSceneMonitoring

<sub>Instance Property</sub>

A photo settings object that controls how the photo output detects and handles automatic flash and stabilization modes.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
@NSCopying var photoSettingsForSceneMonitoring: AVCapturePhotoSettings? { get set }
```

## Discussion

Set the [flashMode](../avcapturephotosettings/flashmode.md) and [autoStillImageStabilizationEnabled](../avcapturephotosettings/isautostillimagestabilizationenabled.md) properties of this photo settings object to influence the values of the photo output’s scene monitoring properties ([isFlashScene](isflashscene.md) and [isStillImageStabilizationScene](isstillimagestabilizationscene.md)). For example, if you set the [flashMode](../avcapturephotosettings/flashmode.md) property of this photo settings object to [AVCaptureFlashModeOff](../avcapturedevice/flashmode-swift.enum/off.md), the photo output’s [isFlashScene](isflashscene.md) property reports [false](../../swift/false.md) regardless of lighting conditions in the visible scene. If you set this photo settings object’s [flashMode](../avcapturephotosettings/flashmode.md) property to [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md) or [AVCaptureFlashModeOn](../avcapturedevice/flashmode-swift.enum/on.md), the photo output’s [isFlashScene](isflashscene.md) property reverts to its default behavior of returning [true](../../swift/true.md) or [false](../../swift/false.md) based on the visible light level.

> [!note] Note
> There is some overlap in the light level ranges that benefit from still image stabilization and flash. If this photo settings object indicates that the scene should be monitored for both still image stabilization and flash, still image stabilization takes precedence, and the [isFlashScene](isflashscene.md) property becomes [true](../../swift/true.md) at lower overall light levels.

The default value is an [AVCapturePhotoSettings](../avcapturephotosettings.md) object with the following settings:

- [flashMode](../avcapturephotosettings/flashmode.md): [AVCaptureFlashModeAuto](../avcapturedevice/flashmode-swift.enum/auto.md)
- [autoStillImageStabilizationEnabled](../avcapturephotosettings/isautostillimagestabilizationenabled.md): [true](../../swift/true.md)

The photo output ignores all other properties of this photo settings object. To control other photo settings when requesting capture, create a photo settings object to pass to the [- capturePhotoWithSettings:delegate:](<capturephoto(with_delegate_).md>) method.

## See Also

### Monitoring the visible scene

- [isFlashScene](isflashscene.md) — A Boolean value indicating whether the scene currently being previewed by the camera warrants use of the flash.
