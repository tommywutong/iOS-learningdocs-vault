---
title: peerGroupID
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/peergroupid
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/peergroupid'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/peergroupid.json'
content_hash: 'sha256:ed1d41c17cd3fff6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# peerGroupID

<sub>Instance Property</sub>

The peer group ID the GPU belongs to, if applicable.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var peerGroupID: UInt64 { get }
```

## Discussion

A group ID value of `0` indicates the GPU isn’t in a peer group. Otherwise, the GPU is in a peer group and the value is the group’s ID. All other GPUs in the same peer group have the same group ID.

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
- [removable](isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
