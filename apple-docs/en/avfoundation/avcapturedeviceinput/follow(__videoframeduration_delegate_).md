---
title: 'follow(_:videoFrameDuration:delegate:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedeviceinput/follow(_:videoframeduration:delegate:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedeviceinput/follow(_:videoframeduration:delegate:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedeviceinput/follow%28_%3Avideoframeduration%3Adelegate%3A%29.json'
content_hash: 'sha256:391fe4e78c787dae'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDeviceInput](../avcapturedeviceinput.md)

# follow(_:videoFrameDuration:delegate:)

<sub>Instance Method</sub>

Configures the the device input to follow an external sync device at the given frame duration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func follow(_ externalSyncDevice: AVExternalSyncDevice, videoFrameDuration frameDuration: CMTime, delegate: (any AVExternalSyncDeviceDelegate)?)
```

## Parameters

- `externalSyncDevice` — The [AVExternalSyncDevice](../avexternalsyncdevice.md) hardware to follow.

- `delegate` — The delegate to notify when the connection status changes, or an error occurs.

## Discussion

Call this method to direct your [AVCaptureDeviceInput](../avcapturedeviceinput.md) to follow the external sync pulse from a sync device at the given frame duration.

Your provided `videoFrameDuration` value must match the sync pulse duration of the external sync device. If it does not, the request times out, the external sync device’s status returns to `AVExternalSyncDeviceStatusReady`, and your session stops running, posting a [AVCaptureSessionRuntimeErrorNotification](../avcapturesession/runtimeerrornotification.md) with `AVErrorFollowExternalSyncDeviceTimedOut`.

The ability to follow an external sync device may change depending on the device configuration. For example, [- followExternalSyncDevice:videoFrameDuration:delegate:](<follow(__videoframeduration_delegate_).md>) cannot be used when [autoVideoFrameRateEnabled](../avcapturedevice/isautovideoframerateenabled.md) is `true`.

To stop following an external pulse, call [- unfollowExternalSyncDevice](<unfollowexternalsyncdevice().md>). External sync device following is also disabled when your device’s [Format](../avcapturedevice/format.md) changes.

Your provided delegate’s [- externalSyncDeviceStatusDidChange:](<../avexternalsyncdevicedelegate/externalsyncdevicestatusdidchange(__).md>) method is called with a status of `AVExternalSyncDeviceStatusReady` if the external pulse signal is not close enough to the provided `videoFrameDuration` for successful calibration.

Once your [status](../avexternalsyncdevice/status.md) changes to `AVExternalSyncDeviceStatusActiveSync`, your input’s  `AVCaptureInput/activeExternalSyncVideoFrameDuration` property reports the up-to-date frame duration. `AVCaptureInput/activeExternalSyncVideoFrameDuration` is also reflected in the [activeVideoMinFrameDuration](../avcapturedevice/activevideominframeduration.md) and [activeVideoMaxFrameDuration](../avcapturedevice/activevideomaxframeduration.md) of your input’s associated device.

> [!note] Note
> Calling this method may cause a lengthy reconfiguration of the receiver, similar to setting a new active format or [sessionPreset](../avcapturesession/sessionpreset.md).

> [!note] Note
> When using this property, set the exposure duration with [- setExposureModeCustomWithDuration:ISO:completionHandler:](<../avcapturedevice/setexposuremodecustom(duration_iso_completionhandler_).md>) to one half the frame duration (or less) to maintain full dynamic range.

> [!important] Important
> Calling this method throws an `NSInvalidArgumentException` if [externalSyncSupported](isexternalsyncsupported.md) returns `false`.

> [!important] Important
> The provided external sync device’s `status` must be `AVExternalSyncDeviceStatusReady` when you call this method, otherwise an `NSInvalidArgumentException` is thrown.

## See Also

### Synchronizing with external devices

- [externalSyncSupported](isexternalsyncsupported.md) — Indicates whether the device input supports being configured to follow an external sync device.
- [- unfollowExternalSyncDevice](<unfollowexternalsyncdevice().md>) — Discontinues external sync.
- [activeExternalSyncVideoFrameDuration](activeexternalsyncvideoframeduration.md) — The receiver’s external sync frame duration (the reciprocal of its frame rate) when being driven by an external sync device.
- [externalSyncDevice](externalsyncdevice.md) — The external sync device currently being followed by this input.
