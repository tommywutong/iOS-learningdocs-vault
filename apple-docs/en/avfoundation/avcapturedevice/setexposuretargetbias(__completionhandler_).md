---
title: 'setExposureTargetBias(_:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setexposuretargetbias(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setexposuretargetbias(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setexposuretargetbias%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:76e98e4696db8143'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setExposureTargetBias(_:completionHandler:)

<sub>Instance Method</sub>

Sets the bias to apply to the target exposure value.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setExposureTargetBias(_ bias: Float, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setExposureTargetBias(_ bias: Float) async -> CMTime
```

## Parameters

- `bias` — The bias to apply to the exposure target value.

- `handler` — A callback the system invokes when the adjustment to the exposure target bias is complete. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [synchronizationClock](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## Discussion

Before changing the value the lens position, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## See Also

### Adjusting exposure compensation

- [exposureTargetOffset](exposuretargetoffset.md) — The metered exposure level’s offset from the target exposure value, in exposure value (EV) units.
- [exposureTargetBias](exposuretargetbias.md) — The bias to apply to the target exposure value, in exposure value (EV) units.
- [minExposureTargetBias](minexposuretargetbias.md) — The minimum supported exposure bias, in exposure value (EV) units.
- [maxExposureTargetBias](maxexposuretargetbias.md) — The maximum supported exposure bias, in exposure value (EV) units.
- [AVCaptureExposureTargetBiasCurrent](currentexposuretargetbias.md) — A special constant that represents the current exposure bias value.
