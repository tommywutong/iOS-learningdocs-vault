---
title: MTLArchitecture
framework: Metal
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/metal/mtlarchitecture
source_url: 'https://developer.apple.com/documentation/metal/mtlarchitecture'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/metal/mtlarchitecture.json'
content_hash: 'sha256:1e82e2e4a723f289'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Metal](../metal.md)

# MTLArchitecture

<sub>Class</sub>

A class that contains the architectural details of a GPU device.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS</sub>

```swift
class MTLArchitecture
```

## Relationships

- **Inherits From**: [NSObject](../objectivec/nsobject-swift.class.md)

- **Conforms To**: [CVarArg](../swift/cvararg.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [CustomStringConvertible](../swift/customstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [NSCopying](../foundation/nscopying.md), [NSObjectProtocol](../objectivec/nsobjectprotocol.md)

## Topics

### Inspecting a GPU device’s architecture details

- [name](mtlarchitecture/name.md) — The name of a GPU device’s architecture.

## See Also

### Identifying a GPU device

- [name](mtldevice/name.md) — The full name of the GPU device.
- [architecture](mtldevice/architecture.md) — The architectural details of the GPU device.
- [registryID](mtldevice/registryid.md) — The GPU device’s registry identifier.
- [location](mtldevice/location.md) — The physical location of the GPU relative to the system. _(deprecated)_
- [MTLDeviceLocation](mtldevicelocation.md) — Indicates the location of the GPU relative to the system it’s connect to. _(deprecated)_
- [locationNumber](mtldevice/locationnumber.md) — A specific GPU position based on its general location. _(deprecated)_
- [lowPower](mtldevice/islowpower.md) — A Boolean value that indicates whether the GPU lowers its performance to conserve energy. _(deprecated)_
- [removable](mtldevice/isremovable.md) — A Boolean value that indicates whether the GPU is removable. _(deprecated)_
- [headless](mtldevice/isheadless.md) — A Boolean value that indicates whether a GPU device doesn’t have a connection to a display. _(deprecated)_
- [peerGroupID](mtldevice/peergroupid.md) — The peer group ID the GPU belongs to, if applicable. _(deprecated)_
- [peerCount](mtldevice/peercount.md) — The total number of GPUs in the peer group, if applicable. _(deprecated)_
- [peerIndex](mtldevice/peerindex.md) — The unique identifier for a GPU in a peer group. _(deprecated)_
