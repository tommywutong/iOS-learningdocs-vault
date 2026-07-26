---
title: 'setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues:handler:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues:handler:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked(whitebalancetemperatureandtintvalues:handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setwhitebalancemodelocked%28whitebalancetemperatureandtintvalues%3Ahandler%3A%29.json'
content_hash: 'sha256:a3a05231145cc1b0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues:handler:)

<sub>Instance Method</sub>

Sets white balance to locked mode with explicit temperature and tint values.

<sub>iOS, iPadOS, Mac Catalyst, tvOS</sub>

```swift
func setWhiteBalanceModeLocked(whiteBalanceTemperatureAndTintValues: AVCaptureDevice.WhiteBalanceTemperatureAndTintValues, handler: ((CMTime) -> Void)? = nil)
```

## Parameters

- `whiteBalanceTemperatureAndTintValues` — The white balance temperature and tint values, as computed from [- temperatureAndTintValuesForDeviceWhiteBalanceGains:](<temperatureandtintvalues(for_).md>) method, [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) presets or manual input.

- `handler` — A block to be called when white balance values have been set to the values specified and [whiteBalanceMode](whitebalancemode-swift.property.md) is set to `AVCaptureWhiteBalanceModeLocked`. If [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceTemperatureAndTintValues:completionHandler:](<setwhitebalancemodelocked(whitebalancetemperatureandtintvalues_handler_).md>) is called multiple times, the completion handlers are called in FIFO order. The block receives a timestamp which matches that of the first buffer to which all settings have been applied. Note that the timestamp is synchronized to the device clock, and thus must be converted to the [synchronizationClock](../avcapturesession/synchronizationclock.md) prior to comparison with the timestamps of buffers delivered via an [AVCaptureVideoDataOutput](../avcapturevideodataoutput.md). This parameter may be `nil` if synchronization is not required.

## Discussion

This method takes a [WhiteBalanceTemperatureAndTintValues](whitebalancetemperatureandtintvalues.md) struct and applies the appropriate [WhiteBalanceGains](whitebalancegains.md). This method throws an `NSRangeException` if any of the values are set to an unsupported level. This method throws an `NSGenericException` if called without first obtaining exclusive access to the device using [- lockForConfiguration:](<lockforconfiguration().md>).

## See Also

### Setting white balance manually

- [lockingWhiteBalanceWithCustomDeviceGainsSupported](islockingwhitebalancewithcustomdevicegainssupported.md) — A Boolean value that indicates whether the device supports locking white balance to specific gain values.
- [- setWhiteBalanceModeLockedWithDeviceWhiteBalanceGains:completionHandler:](<setwhitebalancemodelocked(with_completionhandler_).md>) — Sets the white balance to locked mode with the specified white balance gains.
