---
title: MTLDeviceLocation
framework: Metal
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [macOS 10.15+（27.0 起废弃）]
languages: [swift, occ]
beta: false
deprecated: true
doc_path: /documentation/metal/mtldevicelocation
source_url: 'https://developer.apple.com/documentation/metal/mtldevicelocation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtldevicelocation.json'
content_hash: 'sha256:4b24aaf5b86d701e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLDeviceLocation

<sub>Enumeration</sub>

Indicates the location of the GPU relative to the system it’s connect to.

> [!warning] Deprecated
> Not applicable on Apple Silicon

<sub>macOS</sub>

```swift
enum MTLDeviceLocation
```

## Overview

Check the location of a GPU by checking the [location](mtldevice/location.md) property of its [MTLDevice](mtldevice.md) instance.

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Determining the GPU’s location

- [MTLDeviceLocationBuiltIn](mtldevicelocation/builtin.md) — A location that indicates the GPU is permanently connected to the system internally. _(deprecated)_
- [MTLDeviceLocationSlot](mtldevicelocation/slot.md) — A GPU location that indicates a person connected the GPU to a system’s internal slot. _(deprecated)_
- [MTLDeviceLocationExternal](mtldevicelocation/external.md) — A GPU location that indicates a person connected the GPU to the system with an external interface, such as Thunderbolt. _(deprecated)_
- [MTLDeviceLocationUnspecified](mtldevicelocation/unspecified.md) — A value that indicates the system can’t determine how the GPU connects to it. _(deprecated)_

### Initializers

- [init(rawValue:)](<mtldevicelocation/init(rawvalue_).md>) _(deprecated)_

## See Also

### Identifying a GPU device

- [name](mtldevice/name.md) — The full name of the GPU device.
- [architecture](mtldevice/architecture.md) — The architectural details of the GPU device.
- [MTLArchitecture](mtlarchitecture.md) — A class that contains the architectural details of a GPU device.
- [registryID](mtldevice/registryid.md) — The GPU device’s registry identifier.
- [location](mtldevice/location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [locationNumber](mtldevice/locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](mtldevice/islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](mtldevice/isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](mtldevice/isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](mtldevice/peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](mtldevice/peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](mtldevice/peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
