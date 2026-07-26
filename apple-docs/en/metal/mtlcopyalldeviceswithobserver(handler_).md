---
title: 'MTLCopyAllDevicesWithObserver(handler:)'
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.13+, Swift 4.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/metal/mtlcopyalldeviceswithobserver(handler:)'
source_url: 'https://developer.apple.com/documentation/metal/mtlcopyalldeviceswithobserver(handler:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcopyalldeviceswithobserver%28handler%3A%29.json'
content_hash: 'sha256:f03959c2a5077e4a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCopyAllDevicesWithObserver(handler:)

<sub>Function</sub>

Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.

<sub>macOS</sub>

```swift
func MTLCopyAllDevicesWithObserver(handler: @escaping (any MTLDevice, MTLDeviceNotificationName) -> Void) -> (devices: [any MTLDevice], observer: NSObject)
```

## Parameters

- `handler` — A notification handler you implement that Metal calls when the system adds or removes a GPU device from the system.

## Return Value

- **`devices`** — An array of [MTLDevice](mtldevice.md) instances
- **`observer`** — An object instance that represents an observer the function creates for you.

## Discussion

Keep a copy of `observer` in your app in case you want to stop receiving notifications. You can stop receiving notifications by passing `observer` to the [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) function.

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_
