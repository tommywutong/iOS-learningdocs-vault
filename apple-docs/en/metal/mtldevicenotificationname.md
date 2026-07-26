---
title: MTLDeviceNotificationName
framework: Metal
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicenotificationname
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationname'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationname.json'
content_hash: 'sha256:c596ea81faa2e1c6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDeviceNotificationName

<sub>Structure</sub>

A notification that represents a change to a GPU device in the system.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
struct MTLDeviceNotificationName
```

## Relationships

- **Conforms To**: [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating a notification name

- [MTLDeviceWasAddedNotification](mtldevicenotificationname/wasadded.md) — A notification that Metal sends to observers when the system adds a GPU device. _(deprecated)_
- [MTLDeviceRemovalRequestedNotification](mtldevicenotificationname/removalrequested.md) — A notification that Metal sends to observers when a person requests to remove a GPU device from the system. _(deprecated)_
- [MTLDeviceWasRemovedNotification](mtldevicenotificationname/wasremoved.md) — A notification that Metal sends to observers when the system removes a GPU device. _(deprecated)_
- [init(rawValue:)](<mtldevicenotificationname/init(rawvalue_).md>) — Creates a Metal device notification name from a string. _(deprecated)_

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
