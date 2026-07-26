---
title: NWInterface.InterfaceType
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwinterface/interfacetype
source_url: 'https://developer.apple.com/documentation/network/nwinterface/interfacetype'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwinterface/interfacetype.json'
content_hash: 'sha256:7349424adf72ea16'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWInterface](../nwinterface.md)

# NWInterface.InterfaceType

<sub>Enumeration</sub>

Types of network interfaces, based on their link layer media types.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum InterfaceType
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Interface Types

- [NWInterface.InterfaceType.wifi](interfacetype/wifi.md) — The network interface type used for communication over Wi-Fi networks.
- [NWInterface.InterfaceType.cellular](interfacetype/cellular.md) — The network interface type used for communication over cellular networks.
- [NWInterface.InterfaceType.wiredEthernet](interfacetype/wiredethernet.md) — The network interface type used for communication over wired Ethernet networks.
- [NWInterface.InterfaceType.loopback](interfacetype/loopback.md) — The network interface type used for communication over local loopback networks.
- [NWInterface.InterfaceType.other](interfacetype/other.md) — The network interface type used for communication over virtual networks or networks of unknown types.

## See Also

### Inspecting Interfaces

- [type](type.md) — The type of the interface, such as Wi-Fi or loopback.
- [name](name.md) — The name of the interface.
- [index](index.md) — The system interface index associated with the interface.
