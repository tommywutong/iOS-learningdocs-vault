---
title: videoZoomFactor
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/videozoomfactor
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/videozoomfactor'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/videozoomfactor.json'
content_hash: 'sha256:3a0154004efbb366'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# videoZoomFactor

<sub>Instance Property</sub>

A value that controls the cropping and enlargement of images captured by the device.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
var videoZoomFactor: CGFloat { get set }
```

## Discussion

This value is a multiplier. For example, a value of `2.0` doubles the size of an image’s subject (and halves the field of view). Allowed values range from `1.0` (full field of view) to the value of the active format’s [videoMaxZoomFactor](format/videomaxzoomfactor.md) property. Setting the value of this property jumps immediately to the new zoom factor. For a smooth transition, use the [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) method.

The device achieves a zoom effect by cropping around the center of the image captured by the sensor. At low zoom factors, the cropped images is equal to or larger than the output size. At higher zoom factors, the device must scale the cropped image up to the output size, resulting in a loss of image quality. The active format’s [videoZoomFactorUpscaleThreshold](format/videozoomfactorupscalethreshold.md) property indicates the factors at which upscaling occurs.

Before changing the value of this property, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Adjusting zoom

- [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) — Begins a smooth transition from the current zoom factor to another.
- [- cancelVideoZoomRamp](<cancelvideozoomramp().md>) — Smoothly ends a zoom transition in progress.
