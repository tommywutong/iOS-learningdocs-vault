---
title: NWInterface
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwinterface
source_url: 'https://developer.apple.com/documentation/network/nwinterface'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwinterface.json'
content_hash: 'sha256:11a0689456b41830'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWInterface

<sub>Structure</sub>

An interface that a network connection uses to send and receive data.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct NWInterface
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Inspecting Interfaces

- [type](nwinterface/type.md) — The type of the interface, such as Wi-Fi or loopback.
- [InterfaceType](nwinterface/interfacetype.md) — Types of network interfaces, based on their link layer media types.
- [name](nwinterface/name.md) — The name of the interface.
- [index](nwinterface/index.md) — The system interface index associated with the interface.

### Enumerations

- [RadioType](nwinterface/radiotype.md)

## See Also

### Paths and Interfaces

- [NWPath](nwpath.md) — An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [NWPathMonitor](nwpathmonitor.md) — An observer that you use to monitor and react to network changes.
