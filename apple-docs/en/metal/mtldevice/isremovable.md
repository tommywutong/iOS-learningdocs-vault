---
title: isRemovable
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.13+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/isremovable
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/isremovable'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/isremovable.json'
content_hash: 'sha256:a7ce5c3179a85e9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# isRemovable

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU is removable.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>Mac Catalyst, macOS</sub>

```swift
var isRemovable: Bool { get }
```

## Discussion

You can respond to GPU removal notifications by registering with the [MTLCopyAllDevicesWithObserver(handler:)](<../mtlcopyalldeviceswithobserver(handler_).md>) function in Swift, or the [MTLCopyAllDevicesWithObserver](../mtlcopyalldeviceswithobserver.md) function in Objective-C, and responding to the [MTLDeviceRemovalRequestedNotification](../mtldevicenotificationname/removalrequested.md) and [MTLDeviceWasRemovedNotification](../mtldevicenotificationname/wasremoved.md) device notification names.

> [!important] Important
> If a person removes a GPU without warning, [MTLDevice](../mtldevice.md) APIs may fail even before your app receives a [MTLDeviceWasRemovedNotification](../mtldevicenotificationname/wasremoved.md) notification.

## See Also

### Identifying a GPU device

- [name](name.md) — The full name of the GPU device.
- [architecture](architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](../mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](registryid.md) — The GPU device’s registry identifier.
- [location](location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](../mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
