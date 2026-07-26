---
title: MTLCopyAllDevicesWithObserver
framework: Metal
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.13+（27.0 起废弃）]
languages: [occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtlcopyalldeviceswithobserver
source_url: 'https://developer.apple.com/documentation/metal/mtlcopyalldeviceswithobserver'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlcopyalldeviceswithobserver.json'
content_hash: 'sha256:e64e4ab0f5e4c8f1'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLCopyAllDevicesWithObserver

<sub>Function</sub>

Returns an array of all the Metal GPU devices in the system and registers a notification handler that Metal calls when the device list changes.

<sub>Mac Catalyst, macOS</sub>

```objc
extern NSArray<id<MTLDevice>> *MTLCopyAllDevicesWithObserver(id<NSObject>*observer, MTLDeviceNotificationHandler handler);
```

## Parameters

- `observer` — A pointer to an object instance the method sets to a new observer — which Metal retains — before returning.

- `handler` — A notification handler you implement that Metal calls when the system adds or removes a GPU device from the system.

## Discussion

Keep a copy of `observer` in your app after this function returns in case you want to stop receiving notifications. You can stop receiving notifications by passing `observer` to the [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) function.

## See Also

### Locating GPUs

- [Finding multiple GPUs on an Intel-based Mac](finding-multiple-gpus-on-an-intel-based-mac.md) — Locate, identify, and choose suitable GPUs for your app.
- [Getting the GPU that drives a view’s display](getting-the-gpu-that-drives-a-views-display.md) — Keep up to date with the optimal device for your display.
- [MTLCopyAllDevices](<mtlcopyalldevices().md>) — Returns an array of all the Metal device instances in the system.
- [MTLRemoveDeviceObserver](<mtlremovedeviceobserver(__).md>) — Removes a registered observer of device notifications. _(deprecated)_
- [CGDirectDisplayCopyCurrentMetalDevice(_:)](<../coregraphics/cgdirectdisplaycopycurrentmetaldevice(__).md>) — Returns the GPU device instance that’s currently driving a display.
- [MTLDeviceNotificationHandler](mtldevicenotificationhandler.md) — A Swift closure or an Objective-C block that Metal calls when the system adds or removes a GPU device. _(deprecated)_
- [MTLDeviceNotificationName](mtldevicenotificationname.md) — A notification that represents a change to a GPU device in the system. _(deprecated)_
