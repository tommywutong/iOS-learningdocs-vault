---
title: NWEndpoint.Host
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwendpoint/host
source_url: 'https://developer.apple.com/documentation/network/nwendpoint/host'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint/host.json'
content_hash: 'sha256:cba44752649a3d0b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWEndpoint](../nwendpoint.md)

# NWEndpoint.Host

<sub>Enumeration</sub>

A name or address that identifies a network endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum Host
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Equatable](../../swift/equatable.md), [ExpressibleByExtendedGraphemeClusterLiteral](../../swift/expressiblebyextendedgraphemeclusterliteral.md), [ExpressibleByStringLiteral](../../swift/expressiblebystringliteral.md), [ExpressibleByUnicodeScalarLiteral](../../swift/expressiblebyunicodescalarliteral.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Hosts

- [init(_:)](<host/init(__).md>) — Initializes a host with a string.

### Accessing Host Types

- [NWEndpoint.Host.name(_:_:)](<host/name(____).md>) — A host represented as a name.
- [NWEndpoint.Host.ipv4(_:)](<host/ipv4(__).md>) — A host represented as an IPv4 address.
- [NWEndpoint.Host.ipv6(_:)](<host/ipv6(__).md>) — A host represented as an IPv6 address.

### Requiring Interfaces

- [interface](host/interface.md) — The interface associated with this host, such as the interface scope stored in an IPv6 address.

## See Also

### Host and Ports

- [Port](port.md) — A port number you use along with a host to identify a network endpoint.
