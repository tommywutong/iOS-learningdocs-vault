---
title: AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions
framework: AVFoundation
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 15.0+, iPadOS 15.0+, Mac Catalyst 15.0+, macOS 12.0+, tvOS 17.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct
source_url: 'https://developer.apple.com/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/avfoundation/avcapturedevice/primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct.json'
content_hash: 'sha256:6cb046cc1fa5d9e4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [AVFoundation](../../avfoundation.md) · [AVCaptureDevice](../avcapturedevice.md)

# AVCaptureDevice.PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions

<sub>Structure</sub>

A structure that defines the conditions in which to restrict camera switching.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS</sub>

```swift
struct PrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions
```

## Overview

Use these constants to control the conditions that allow fallback camera selection when you set the value of the [primaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.property.md) property to [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md).

When triggered by one or more enabled conditions, fallback camera switching waits for exposure and focus to stabilize before deciding which camera to use as the primary constituent device.

Whenever [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionVideoZoomChanged](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md) isn’t included in the restricted switching behavior conditions, [AVCapturePrimaryConstituentDeviceSwitchingBehaviorRestricted](primaryconstituentdeviceswitchingbehavior-swift.enum/restricted.md) still allows camera selection when a change in video zoom factor makes a camera eligible or ineligible for selection as the [activePrimaryConstituentDevice](activeprimaryconstituent.md).

When the video zoom factor decreases to below the switch-over zoom factor of the active primary constituent device, the system selects a different camera to satisfy the requested zoom factor.

When the video zoom factor increases and crosses a camera’s switch-over zoom factor, this camera becomes eligible to set as the [activePrimaryConstituentDevice](activeprimaryconstituent.md). If exposure and focus allow, this camera then becomes the new active primary constituent device. Similar to the [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionVideoZoomChanged](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md) this also waits for exposure and focus to stabilize. Otherwise the [activePrimaryConstituentDevice](activeprimaryconstituent.md) remains unchanged.

## Relationships

- **Conforms To**: [BitwiseCopyable](../../swift/bitwisecopyable.md), [Equatable](../../swift/equatable.md), [ExpressibleByArrayLiteral](../../swift/expressiblebyarrayliteral.md), [OptionSet](../../swift/optionset.md), [RawRepresentable](../../swift/rawrepresentable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md), [SetAlgebra](../../swift/setalgebra.md)

## Topics

### Switching behavior conditions

- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionExposureModeChanged](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/exposuremodechanged.md) — Restrict switching to a fallback camera only when the device’s exposure mode changes.
- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionFocusModeChanged](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/focusmodechanged.md) — Restrict switching to a fallback camera only when the device’s focus mode changes.
- [AVCapturePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditionVideoZoomChanged](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/videozoomchanged.md) — Restrict switching to a fallback camera only when the device’s video zoom changes.

### Initializers

- [init(rawValue:)](<primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.struct/init(rawvalue_).md>) — Creates a switching behavior condition with an unsigned integer value.

## See Also

### Restricting camera switching

- [- setPrimaryConstituentDeviceSwitchingBehavior:restrictedSwitchingBehaviorConditions:](<setprimaryconstituentdeviceswitchingbehavior(__restrictedswitchingbehaviorconditions_).md>) — Sets the switching behavior of the primary constituent device.
- [primaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.property.md) — The switching behavior for the primary constituent device.
- [primaryConstituentDeviceRestrictedSwitchingBehaviorConditions](primaryconstituentdevicerestrictedswitchingbehaviorconditions-swift.property.md) — The conditions that restrict the primary constituent device’s switching behavior.
- [activePrimaryConstituentDeviceSwitchingBehavior](activeprimaryconstituentdeviceswitchingbehavior.md) — The switching behavior of the active constituent device.
- [activePrimaryConstituentDeviceRestrictedSwitchingBehaviorConditions](activeprimaryconstituentdevicerestrictedswitchingbehaviorconditions.md) — The conditions that restrict camera switching behavior for the active primary constituent device.
- [activePrimaryConstituentDevice](activeprimaryconstituent.md) — A virtual device’s active primary constituent device.
- [PrimaryConstituentDeviceSwitchingBehavior](primaryconstituentdeviceswitchingbehavior-swift.enum.md) — Constants that control when to allow a virtual device to switch its active primary constituent device.
- [supportedFallbackPrimaryConstituentDevices](supportedfallbackprimaryconstituentdevices.md) — The constituent devices available to select as a fallback for a longer focal length primary constituent device.
- [fallbackPrimaryConstituentDevices](fallbackprimaryconstituentdevices.md) — The fallback devices to use when a constituent device with a longer focal length becomes limited by its light sensitivity or minimum focus distance.
