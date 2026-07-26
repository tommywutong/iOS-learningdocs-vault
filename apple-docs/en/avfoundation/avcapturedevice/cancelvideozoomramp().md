---
title: cancelVideoZoomRamp()
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 7.0+, iPadOS 7.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/cancelvideozoomramp()
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/cancelvideozoomramp()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/cancelvideozoomramp%28%29.json'
content_hash: 'sha256:cd760c3596e5d866'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# cancelVideoZoomRamp()

<sub>Instance Method</sub>

Smoothly ends a zoom transition in progress.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func cancelVideoZoomRamp()
```

## Discussion

Calling this method is equivalent to calling [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) with a rate of zero. If a zoom transition is in progress, the transition slows to a stop (instead of stopping abruptly).

Before calling this method, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. If you don’t, calling this method raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Adjusting zoom

- [videoZoomFactor](videozoomfactor.md) — A value that controls the cropping and enlargement of images captured by the device.
- [- rampToVideoZoomFactor:withRate:](<ramp(tovideozoomfactor_withrate_).md>) — Begins a smooth transition from the current zoom factor to another.
