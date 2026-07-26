---
title: 'ramp(toVideoZoomFactor:withRate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/ramp(tovideozoomfactor:withrate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/ramp(tovideozoomfactor:withrate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/ramp%28tovideozoomfactor%3Awithrate%3A%29.json'
content_hash: 'sha256:3e0c3a41255de10c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# ramp(toVideoZoomFactor:withRate:)

<sub>Instance Method</sub>

Begins a smooth transition from the current zoom factor to another.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func ramp(toVideoZoomFactor factor: CGFloat, withRate rate: Float)
```

## Parameters

- `factor` — The new magnification factor.

- `rate` — The rate at which to transition to the new magnification factor, specified in powers of two per second.

## Discussion

Allowed values for `factor` range from `1.0` (full field of view) to the [videoMaxZoomFactor](format/videomaxzoomfactor.md) specified by the active capture format.

During a ramp, the zoom factor changes at an exponential rate, but this yields a visually linear transition. The `rate` parameter controls the speed of this transition independent of direction; for example, a value of `1.0` causes zoom factor to double every second if zooming in (that’s, if the specified `factor` is greater than the current [videoZoomFactor](videozoomfactor.md)) or halve every second if zooming out.

Before calling this method, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. If you don’t, calling this method raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Adjusting zoom

- [videoZoomFactor](videozoomfactor.md) — A value that controls the cropping and enlargement of images captured by the device.
- [- cancelVideoZoomRamp](<cancelvideozoomramp().md>) — Smoothly ends a zoom transition in progress.
