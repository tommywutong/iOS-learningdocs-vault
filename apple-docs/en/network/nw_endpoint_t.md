---
title: nw_endpoint_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_endpoint_t
source_url: 'https://developer.apple.com/documentation/network/nw_endpoint_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_endpoint_t.json'
content_hash: 'sha256:3220aa8c47031f80'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_endpoint_t

<sub>Type Alias</sub>

A local or remote endpoint in a network connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_endpoint_t = any OS_nw_endpoint
```

## Topics

### Endpoint Types

- [nw_endpoint_type_t](nw_endpoint_type_t.md) — The type of a network endpoint, such as a host or a service.
- [nw_endpoint_get_type](<nw_endpoint_get_type(__).md>) — Accesses the type of a endpoint.

### Host Endpoints

- [nw_endpoint_create_host](<nw_endpoint_create_host(____).md>) — Creates a network endpoint with a hostname and port, where the hostname may be interpreted as an IP address.
- [nw_endpoint_get_hostname](<nw_endpoint_get_hostname(__).md>) — Accesses the hostname stored in an endpoint.
- [nw_endpoint_get_port](<nw_endpoint_get_port(__).md>) — Accesses the port stored in an endpoint, in host-byte order.
- [nw_endpoint_copy_port_string](<nw_endpoint_copy_port_string(__).md>) — Copies the port of an endpoint as a string.

### Address Endpoints

- [nw_endpoint_create_address](<nw_endpoint_create_address(__).md>) — Creates a network endpoint with an address structure.
- [nw_endpoint_get_address](<nw_endpoint_get_address(__).md>) — Accesses the address structure stored in an address endpoint.
- [nw_endpoint_copy_address_string](<nw_endpoint_copy_address_string(__).md>) — Copies the address of an endpoint as a string.
- [nw_endpoint_copy_port_string](<nw_endpoint_copy_port_string(__).md>) — Copies the port of an endpoint as a string.

### Bonjour Service Endpoints

- [nw_endpoint_create_bonjour_service](<nw_endpoint_create_bonjour_service(______).md>) — Creates a network endpoint with a Bonjour service name, type, and domain.
- [nw_endpoint_get_bonjour_service_name](<nw_endpoint_get_bonjour_service_name(__).md>) — Accesses the Bonjour service name stored in an endpoint.
- [nw_endpoint_get_bonjour_service_type](<nw_endpoint_get_bonjour_service_type(__).md>) — Accesses the Bonjour service type stored in an endpoint.
- [nw_endpoint_get_bonjour_service_domain](<nw_endpoint_get_bonjour_service_domain(__).md>) — Accesses the Bonjour service domain stored in an endpoint.

### URL Endpoints

- [nw_endpoint_create_url](<nw_endpoint_create_url(__).md>) — Creates a network endpoint with a URL string.
- [nw_endpoint_get_url](<nw_endpoint_get_url(__).md>) — Accesses the URL string stored in an endpoint.
