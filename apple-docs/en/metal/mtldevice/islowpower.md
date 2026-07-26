---
title: isLowPower
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [Mac Catalyst 13.0+（27.0 起废弃）, macOS 10.11+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevice/islowpower
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/islowpower'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/islowpower.json'
content_hash: 'sha256:8012549008812e26'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# isLowPower

<sub>Instance Property</sub>

A Boolean value that indicates whether the GPU lowers its performance to conserve energy.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>Mac Catalyst, macOS</sub>

```swift
var isLowPower: Bool { get }
```

## Discussion

Some systems contain multiple GPUs that run with different performance and energy characteristics. At runtime, choose a GPU that best matches your performance needs while considering the current state of the system. For example, your app may choose a lower-power GPU if it doesn’t need the best possible performance on a MacBook Pro that’s running on battery power. For more information on discovering and selecting GPUs at runtime, see [Multi-GPU systems](../multi-gpu-systems.md).

> [!note] Note
> Systems with Apple silicon only have one GPU, which removes the need to choose a GPU.

The property is typically [true](../../swift/true.md) for integrated GPUs and [false](../../swift/false.md) for discrete GPUs. However, an Apple silicon GPU on a Mac sets the property to [false](../../swift/false.md) because it doesn’t need to lower its performance to conserve energy.

## See Also

### Identifying a GPU device

- [name](name.md) — The full name of the GPU device.
- [architecture](architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](../mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](registryid.md) — The GPU device’s registry identifier.
- [location](location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](../mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [removable](isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
