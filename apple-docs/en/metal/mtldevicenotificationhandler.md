---
title: MTLDeviceNotificationHandler
framework: Metal
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicenotificationhandler
source_url: 'https://developer.apple.com/documentation/metal/mtldevicenotificationhandler'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicenotificationhandler.json'
content_hash: 'sha256:dcad53905fc664aa'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDeviceNotificationHandler

<sub>Type Alias</sub>

A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
typealias MTLDeviceNotificationHandler = @Sendable (any MTLDevice, MTLDeviceNotificationName) -> Void
```

## Parameters

- `device` — An [MTLDevice](mtldevice.md) that represents the GPU that’s sending the notification.

- `notifyName` — A notification that represents a change to a GPU device in the system.

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_
