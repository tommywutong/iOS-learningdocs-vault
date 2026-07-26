---
title: 'setDynamicAspectRatio(_:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setdynamicaspectratio(_:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setdynamicaspectratio(_:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setdynamicaspectratio%28_%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:b78aa93cd0517051'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setDynamicAspectRatio(_:completionHandler:)

<sub>Instance Method</sub>

Updates the dynamic aspect ratio of the device.

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setDynamicAspectRatio(_ dynamicAspectRatio: AVCaptureDevice.AspectRatio, completionHandler handler: (@Sendable (CMTime, (any Error)?) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst</sub>

```swift
func setDynamicAspectRatio(_ dynamicAspectRatio: AVCaptureDevice.AspectRatio) async throws -> CMTime
```

## Parameters

- `dynamicAspectRatio` — The new [AspectRatio](aspectratio.md) the device should output.

- `handler` — A block called by the device when `dynamicAspectRatio` is set to the value specified. If you call [- setDynamicAspectRatio:completionHandler:](<setdynamicaspectratio(__completionhandler_).md>) multiple times, the completion handlers are called in FIFO order. The block receives a timestamp which matches that of the first buffer to which all settings have been applied. Note that the timestamp is synchronized to the device clock, and thus must be converted to the [synchronizationClock](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered via an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md). You may pass `nil` for the `handler` parameter if you do not need to know when the operation completes.

## Discussion

This is the only way of setting [dynamicAspectRatio](dynamicaspectratio.md). This method throws an `NSInvalidArgumentException` if `dynamicAspectRatio` is not a supported aspect ratio found in the device’s activeFormat’s [supportedDynamicAspectRatios](format/supporteddynamicaspectratios.md). This method throws an `NSGenericException` if you call it without first obtaining exclusive access to the device using [- lockForConfiguration:](<lockforconfiguration().md>).

## See Also

### Configuring dynamic aspect ratio

- [AspectRatio](aspectratio.md) — String constants describing the different video aspect ratios you can configure for a particular device.
- [dynamicAspectRatio](dynamicaspectratio.md) — A key-value observable property indicating the current aspect ratio for a device.
- [dynamicDimensions](dynamicdimensions.md) — A key-value observable property describing the output dimensions of the video buffer based on the device’s dynamic aspect ratio.
