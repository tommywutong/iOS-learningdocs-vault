---
title: NWEndpoint
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwendpoint
source_url: 'https://developer.apple.com/documentation/network/nwendpoint'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwendpoint.json'
content_hash: 'sha256:d339738a74e5acd5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWEndpoint

<sub>Enumeration</sub>

A local or remote endpoint in a network connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum NWEndpoint
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Endpoint Types

- [NWEndpoint.hostPort(host:port:)](<nwendpoint/hostport(host_port_).md>) — An endpoint represented as a host and port, with the host including both names and addresses.
- [NWEndpoint.service(name:type:domain:interface:)](<nwendpoint/service(name_type_domain_interface_).md>) — An endpoint represented as a Bonjour service.
- [NWEndpoint.url(_:)](<nwendpoint/url(__).md>) — An endpoint represented as a URL, with host and port values inferred from the URL.
- [NWEndpoint.unix(path:)](<nwendpoint/unix(path_).md>) — An endpoint represented as a UNIX domain path.

### Host and Ports

- [Host](nwendpoint/host.md) — A name or address that identifies a network endpoint.
- [Port](nwendpoint/port.md) — A port number you use along with a host to identify a network endpoint.

### Internet Addresses

- [IPAddress](ipaddress.md) — An abstract protocol you use to interact with IP addresses.
- [IPv4Address](ipv4address.md) — A structure containing an IPv4 address.
- [IPv6Address](ipv6address.md) — A structure containing an IPv6 address.

### Endpoint Properties

- [interface](nwendpoint/interface.md) — The optional interface associated with this endpoint, such as the interface on which it was discovered.

### Enumeration Cases

- [NWEndpoint.opaque(_:)](<nwendpoint/opaque(__).md>)

### Initializers

- [init(copying:newPort:)](<nwendpoint/init(copying_newport_).md>) — Creates a new `NWEndpoint` by copying an existing endpoint and specifying a new port.

### Instance Properties

- [txtRecord](nwendpoint/txtrecord.md)
- [wifiAware](nwendpoint/wifiaware.md) — Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

### Instance Methods

- [wifiAware(port:)](<nwendpoint/wifiaware(port_).md>) — Get an `WAEndpoint` that can connect to this `NWEndpoint`’s remote device over Wi-Fi Aware on the specified port, or `nil` if the `NWEndpoint` is not compatible with Wi-Fi Aware.

## See Also

### Essentials

- [NWParameters](nwparameters.md) — An object that stores the protocols to use for connections, options for sending data, and network path constraints.
