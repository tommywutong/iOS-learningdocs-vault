---
title: location
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/location
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/location'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/location.json'
content_hash: 'sha256:8e55d313a88be020'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# location

<sub>Instance Property</sub>

The physical location of the GPU relative to the system.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
var location: MTLDeviceLocation { get }
```

## Discussion

The value indicates whether the GPU connects to the system through a built-in connection, an internal card slot, or an external connection.

## See Also

### Identifying a GPU device

- [name](name.md) — The full name of the GPU device.
- [architecture](architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](../mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](registryid.md) — The GPU device’s registry identifier.
- [MTLDeviceLocation](../mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
