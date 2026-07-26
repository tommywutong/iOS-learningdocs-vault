---
title: 'setPrimaryConstituentDeviceSwitchingBehavior(_:restrictedSwitchingBehaviorConditions:)'
framework: AVFoundation
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: '/documentation/avfoundation/avcapturedevice/setprimaryconstituentdeviceswitchingbehavior(_:restrictedswitchingbehaviorconditions:)'
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/setprimaryconstituentdeviceswitchingbehavior(_:restrictedswitchingbehaviorconditions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/setprimaryconstituentdeviceswitchingbehavior%28_%3Arestrictedswitchingbehaviorconditions%3A%29.json'
content_hash: 'sha256:0ce9812386fff8fa'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# setPrimaryConstituentDeviceSwitchingBehavior(_:restrictedSwitchingBehaviorConditions:)

<sub>Instance Method</sub>

Sets the switching behavior of the primary constituent device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
func setPrimaryConstituentDeviceSwitchingBehavior(_ switchingBehavior: AVCaptureDevice.PrimaryConstituentDeviceSwitchingBehavior, restrictedSwitchingBehaviorConditions: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions)
```

## Parameters

- `switchingBehavior` — The switching behavior to set on the device.

- `restrictedSwitchingBehaviorConditions` — Sets the conditions during which the system restricts switching cameras. Setting the switching behavior to a value other than [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md) requires that you set this argument to an empty option set.

## Discussion

Use this method to configure the camera switching behavior of a capture device. Before calling it, determine if a device supports configuring its device switching behavior by querying the device’s [activePrimaryConstituentDeviceSwitchingBehavior](activeprimaryconstituentdeviceswitchingbehavior.md) property. If the value equals `.unsupported`, attempting to configure its switching behavior results in an error.

```swift
// Exit early if the device doesn't support configuring switching behavior.
guard captureDevice.activePrimaryConstituentDeviceSwitchingBehavior != .unsupported else { return }
captureDevice.setPrimaryConstituentDeviceSwitchingBehavior(.auto, restrictedSwitchingBehaviorConditions: [])
```

When recording using an instance of [AVCaptureMovieFileOutput](../avcapturemoviefileoutput.md), you may override the switching behavior by calling the movie file output’s [- setPrimaryConstituentDeviceSwitchingBehaviorForRecording:restrictedSwitchingBehaviorConditions:](<../avcapturemoviefileoutput/setprimaryconstituentdeviceswitchingbehaviorforrecording(__restrictedswitchingbehaviorconditions_).md>) method.

## See Also

### Restricting camera switching

- [primaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.property.md) — The switching behavior for the primary constituent device.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditions](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md) — The conditions that restrict the primary constituent device’s switching behavior.
- [activePrimaryConstituentDeviceSwitchingBehavior](activeprimaryconstituentdeviceswitchingbehavior.md) — The switching behavior of the active constituent device.
- [activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md) — The conditions that restrict camera switching behavior for the active primary constituent device.
- [activePrimaryConstituentDevice](activeprimaryconstituent.md) — A virtual device’s active primary constituent device.
- [PrimaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.enum.md) — Constants that control when to allow a virtual device to switch its active primary constituent device.
- [PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md) — A structure that defines the conditions in which to restrict camera switching.
- [supportedFallbackPrimaryConstituentDevices](supportedfallbackprimaryconstituentdevices.md) — The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [fallbackPrimaryConstituentDevices](fallbackprimaryconstituentdevices.md) — The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.
