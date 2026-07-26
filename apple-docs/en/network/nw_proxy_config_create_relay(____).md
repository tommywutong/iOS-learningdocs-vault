---
title: 'nw_proxy_config_create_relay(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_proxy_config_create_relay(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_create_relay(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_create_relay%28_%3A_%3A%29.json'
content_hash: 'sha256:1f847193dcf9e977'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_create_relay(_:_:)

<sub>Function</sub>

Initializes a proxy configuration with one or two relay hops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_proxy_config_create_relay(_ first_hop: nw_relay_hop_t, _ second_hop: nw_relay_hop_t?) -> nw_proxy_config_t
```

## Parameters

- `first_hop` — A relay hop, which is either the first of two hops, or the only hop.

- `second_hop` — An optional second relay hop.

## Return Value

An initialized proxy configuration object.

## See Also

### Creating Proxy Configurations

- [nw_relay_hop_t](nw_relay_hop_t.md) — A single relay server you can chain together with other servers.
- [nw_proxy_config_create_oblivious_http](<nw_proxy_config_create_oblivious_http(________).md>) — Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [nw_proxy_config_create_http_connect](<nw_proxy_config_create_http_connect(____).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [nw_proxy_config_create_socksv5](<nw_proxy_config_create_socksv5(__).md>) — Initializes a SOCKSv5 proxy configuration.
