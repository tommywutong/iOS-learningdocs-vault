---
title: supportedFallbackPrimaryConstituentDevices
framework: AVFoundation
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/supportedfallbackprimaryconstituentdevices
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/supportedfallbackprimaryconstituentdevices'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/supportedfallbackprimaryconstituentdevices.json'
content_hash: 'sha256:6ca4bad932560048'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# supportedFallbackPrimaryConstituentDevices

<sub>Instance Property</sub>

The constituent devices available to select as a fallback for a longer focal length primary constituent device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
var supportedFallbackPrimaryConstituentDevices: [AVCaptureDevice] { get }
```

## Discussion

The value of this property doesn’t change for a particular virtual device, and is `nil` for nonvirtual devices.

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
- [fallbackPrimaryConstituentDevices](fallbackprimaryconstituentdevices.md) — The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.
