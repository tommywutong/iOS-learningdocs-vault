---
title: fallbackPrimaryConstituentDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/fallbackprimaryconstituentdevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/fallbackprimaryconstituentdevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/fallbackprimaryconstituentdevices.json'
content_hash: 'sha256:7f8af956ed8637f9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# fallbackPrimaryConstituentDevices

<sub>Instance Property</sub>

The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var fallbackPrimaryConstituentDevices: [AVCaptureDevice] { get set }
```

## Discussion

By default, this value contains the array of devices that the [supportedFallbackPrimaryConstituentDevices](supportedfallbackprimaryconstituentdevices.md) property provides. The system throws an exception if you attempt to specify a device other than the ones found in the device array.

This property is key-value observable.

## See Also

### Restricting camera switching

- [- setPrimaryConstituentDeviceSwitchingBehavior:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehavior(__restrictedswitchingbehaviorconditions_).md>) — Sets the switching behavior of the primary constituent device.
- [primaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.property.md) — The switching behavior for the primary constituent device.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditions](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md) — The conditions that restrict the primary constituent device’s switching behavior.
- [activePrimaryConstituentDeviceSwitchingBehavior](activeprimaryconstituentdeviceswitchingbehavior.md) — The switching behavior of the active constituent device.
- [activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md) — The conditions that restrict camera switching behavior for the active primary constituent device.
- [activePrimaryConstituentDevice](activeprimaryconstituent.md) — A virtual device’s active primary constituent device.
- [PrimaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.enum.md) — Constants that control when to allow a virtual device to switch its active primary constituent device.
- [PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.md) — A structure that defines the conditions in which to restrict camera switching.
- [supportedFallbackPrimaryConstituentDevices](supportedfallbackprimaryconstituentdevices.md) — The constituent devices available to select as a fallback for a longer focal length primary constituent device.
