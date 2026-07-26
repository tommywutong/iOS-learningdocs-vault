---
title: 'setWhiteBalanceModeLocked(with:completionHandler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 8.0+, iPadOS 8.0+, Mac Catalyst 14.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(with:completionhandler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(with:completionhandler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked%28with%3Acompletionhandler%3A%29.json'
content_hash: 'sha256:58ca12f030006d1c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setWhiteBalanceModeLocked(with:completionHandler:)

<sub>Instance Method</sub>

Sets the white balance to locked mode with the specified white balance gains.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setWhiteBalanceModeLocked(with whiteBalanceGains: AVCaptureDevice.WhiteBalanceGains, completionHandler handler: (@Sendable (CMTime) -> Void)? = nil)
```

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setWhiteBalanceModeLocked(with whiteBalanceGains: AVCaptureDevice.WhiteBalanceGains) async -> CMTime
```

## Parameters

- `whiteBalanceGains` — The white balance gains to set. Pass a value of [AVCaptureWhiteBalanceGainsCurrent](currentwhitebalancegains.md) to leave the current white balance unchanged.

- `handler` — A callback the system invokes when the adjustment to the white balance is complete and the [whiteBalanceMode](whitebalancemode-swift.property.md) set to a locked state. If you call this method multiple times, the system calls the completion handlers in FIFO order. The system passes a time value that matches that of the first buffer to which its applied all settings. It synchronizes the timestamp to the device clock, and you must convert the timestamp to the [synchronizationClock](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered through an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md). You can pass `nil` for this parameter if you don’t require this information.

## Discussion

Each channel in the white balance gains structure supports values between `1.0` and [maxWhiteBalanceGain](maxwhitebalancegain.md). Setting a channel value outside this range generates an exception.

The system normalizes gain values to the minimum channel value to avoid brightness changes (for example, `R:2 G:2 B:4` normalizes to `R:1 G:1 B:2`).

Before changing the value the white balance gains, you must call [- lockForConfiguration:](<lockforconfiguration().md>) to acquire exclusive access to the device’s configuration properties. Otherwise, setting the value of this property raises an exception. When you finish configuring the device, call [- unlockForConfiguration](<unlockforconfiguration().md>) to release the lock and allow other devices to configure the settings.

## Topics

### White balance constants

- [AVCaptureWhiteBalanceGainsCurrent](currentwhitebalancegains.md) — A special constant representing the current white balance setting.

## See Also

### Setting white balance manually

- [lockingWhiteBalanceWithCustomDeviceGainsSupported](islockingwhitebalancewithcustomdevicegainssupported.md) — A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:](<setwhitebalancemodelocked(whitebalancetemperatureandtintvalues_handler_).md>) — Sets white balance to locked mode with explicit temperature and tint values.
