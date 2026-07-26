---
title: nw_proxy_config_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_proxy_config_t
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_t.json'
content_hash: 'sha256:4fba6ab27383ba48'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_t

<sub>Type Alias</sub>

A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_proxy_config_t = any OS_nw_proxy_config
```

## Topics

### Creating Proxy Configurations

- [nw_proxy_config_create_relay](<nw_proxy_config_create_relay(____).md>) — Initializes a proxy configuration with one or two relay hops.
- [nw_relay_hop_t](nw_relay_hop_t.md) — A single relay server you can chain together with other servers.
- [nw_proxy_config_create_oblivious_http](<nw_proxy_config_create_oblivious_http(________).md>) — Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.
- [nw_proxy_config_create_http_connect](<nw_proxy_config_create_http_connect(____).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [nw_proxy_config_create_socksv5](<nw_proxy_config_create_socksv5(__).md>) — Initializes a SOCKSv5 proxy configuration.

### Customizing Proxy Behavior

- [nw_proxy_config_set_failover_allowed](<nw_proxy_config_set_failover_allowed(____).md>) — Configures whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
- [nw_proxy_config_set_username_and_password](<nw_proxy_config_set_username_and_password(______).md>) — Sets a username and password to use as authentication for a proxy configuration.

### Inspecting Proxies

- [nw_proxy_config_get_failover_allowed](<nw_proxy_config_get_failover_allowed(__).md>) — Checks if a proxy configuration allows failover to non-proxied connections.

## See Also

### Configuring Proxies

- [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>) — Applies a proxy configuration to all connections associated with this context.
- [nw_privacy_context_clear_proxies](<nw_privacy_context_clear_proxies(__).md>) — Clears out any proxies added using [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>)
