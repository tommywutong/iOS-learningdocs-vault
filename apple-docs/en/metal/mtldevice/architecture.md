---
title: architecture
framework: Metal
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtldevice/architecture
source_url: 'https://developer.apple.com/documentation/metal/mtldevice/architecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevice/architecture.json'
content_hash: 'sha256:8f65bb19f70d908d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Metal](../../metal.md) · [MTLDevice](../mtldevice.md)

# architecture

<sub>Instance Property</sub>

The architectural details of the GPU device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
var architecture: MTLArchitecture { get }
```

## See Also

### Identifying a GPU device

- [name](name.md) — The full name of the GPU device.
- [MTLArchitecture](../mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](registryid.md) — The GPU device’s registry identifier.
- [location](location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](../mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
