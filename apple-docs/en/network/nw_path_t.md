---
title: nw_path_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_path_t
source_url: 'https://developer.apple.com/documentation/network/nw_path_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_path_t.json'
content_hash: 'sha256:bb6fe5980d339e4e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_path_t

<sub>Type Alias</sub>

An object that contains information about the properties of the network that a connection uses, or that are available to your app.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_path_t = any OS_nw_path
```

## Topics

### Checking Path Availability

- [nw_path_get_status](<nw_path_get_status(__).md>) — Checks whether a path can be used by connections.
- [nw_path_status_t](nw_path_status_t.md) — Status values indicating whether a path can be used by connections.

### Inspecting Interfaces

- [nw_path_uses_interface_type](<nw_path_uses_interface_type(____).md>) — Checks if connections using the path may send traffic over a specific interface type.
- [nw_path_enumerate_interfaces](<nw_path_enumerate_interfaces(____).md>) — Enumerates the list of all interfaces available to the path, in order of preference.
- [nw_path_enumerate_interfaces_block_t](nw_path_enumerate_interfaces_block_t.md) — A block that enumerates the interfaces available to a path.
- [nw_path_enumerate_gateways](<nw_path_enumerate_gateways(____).md>) — Enumerates the list of gateways configured on the interfaces available to a path.
- [nw_path_enumerate_gateways_block_t](nw_path_enumerate_gateways_block_t.md) — A block that enumerates the gateways configured on the interfaces available to a path.

### Checking Path Capabilities

- [nw_path_has_ipv4](<nw_path_has_ipv4(__).md>) — Checks whether the path can route IPv4 traffic.
- [nw_path_has_ipv6](<nw_path_has_ipv6(__).md>) — Checks whether the path can route IPv6 traffic.
- [nw_path_has_dns](<nw_path_has_dns(__).md>) — Checks whether the path has a DNS server configured.
- [nw_path_is_constrained](<nw_path_is_constrained(__).md>) — Checks whether the path uses an interface in Low Data Mode.
- [nw_path_is_expensive](<nw_path_is_expensive(__).md>) — Checks whether the path uses an interface that is considered expensive, such as Cellular or a Personal Hotspot.

### Comparing Paths

- [nw_path_is_equal](<nw_path_is_equal(____).md>) — Compares if two paths are identical.

### Inspecting Connected Paths

- [nw_path_copy_effective_local_endpoint](<nw_path_copy_effective_local_endpoint(__).md>) — Accesses the local endpoint in use by a connection’s network path.
- [nw_path_copy_effective_remote_endpoint](<nw_path_copy_effective_remote_endpoint(__).md>) — Accesses the remote endpoint in use by a connection’s network path.
