---
title: 'MTLRemoveDeviceObserver(_:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: '/documentation/metal/mtlremovedeviceobserver(_:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlremovedeviceobserver(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlremovedeviceobserver%28_%3A%29.json'
content_hash: 'sha256:8a8a5bf16633b747'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLRemoveDeviceObserver(_:)

<sub>Function</sub>

Removes a registered observer of device notifications.

> [!warning] Deprecated
> Device notifications are not applicable on Apple Silicon

<sub>macOS</sub>

```swift
func MTLRemoveDeviceObserver(_ observer: any NSObjectProtocol)
```

## Parameters

- `observer` — An object instance that represents the observer the [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) function creates.

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLCopyAllDevicesWithObserver(handler:)](<mtlcopyalldeviceswithobserver(handler_).md>) — Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_
