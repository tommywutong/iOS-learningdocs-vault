---
title: locationNumber
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/locationnumber
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/locationnumber'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/locationnumber.json'
content_hash: 'sha256:b8c88e539754cdbb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# locationNumber

<sub>Instance Property</sub>

A specific GPU position based on its general location.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var locationNumber: Int { get }
```

## Discussion

The meaning of the location number depends on a device’s [location](location.md) property:

- For [MTLDeviceLocationBuiltIn](../mtldevicelocation/builtin.md), the location number is `0` for low-power GPUs (see [lowPower](islowpower.md)) and `1` for other GPUs.
- For [MTLDeviceLocationSlot](../mtldevicelocation/slot.md), the location number represents the slot.
- For [MTLDeviceLocationExternal](../mtldevicelocation/external.md), the location number represents the Thunderbolt port.

> [!note] Note
> It’s possible for multiple devices to share the same location and number. For example, a card in a slot may have multiple GPUs, or a person may connect multiple eGPUs to the same Thunderbolt port.

## See Also

### Identifying a GPU device

- [name](name.md) — The full name of the GPU device.
- [architecture](architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](../mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](registryid.md) — The GPU device’s registry identifier.
- [location](location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](../mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [lowPower](islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
