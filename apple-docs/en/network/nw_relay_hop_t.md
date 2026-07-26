---
title: nw_relay_hop_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_relay_hop_t
source_url: 'https://developer.apple.com/documentation/network/nw_relay_hop_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_relay_hop_t.json'
content_hash: 'sha256:58e4f170b8bd6b48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_relay_hop_t

<sub>Type Alias</sub>

A single relay server you can chain together with other servers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_relay_hop_t = any OS_nw_relay_hop
```

## Discussion

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [RFC 9298](https://www.rfc-editor.org/rfc/rfc9298.html).

## Topics

### Configuring Relay Hops

- [nw_relay_hop_create](<nw_relay_hop_create(______).md>) — Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
- [nw_relay_hop_add_additional_http_header_field](<nw_relay_hop_add_additional_http_header_field(______).md>) — Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.

## See Also

### Creating Proxy Configurations

- [nw_proxy_config_create_relay](<nw_proxy_config_create_relay(____).md>) — Initializes a proxy configuration with one or two relay hops.
- [nw_proxy_config_create_oblivious_http](<nw_proxy_config_create_oblivious_http(________).md>) — Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [nw_proxy_config_create_http_connect](<nw_proxy_config_create_http_connect(____).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [nw_proxy_config_create_socksv5](<nw_proxy_config_create_socksv5(__).md>) — Initializes a SOCKSv5 proxy configuration.
