---
title: nw_privacy_context_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_privacy_context_t
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_t.json'
content_hash: 'sha256:2836d8f41671995b'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_t

<sub>Type Alias</sub>

An object that defines the privacy requirements for a set of connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_privacy_context_t = any OS_nw_privacy_context
```

## Discussion

Use _NW_DEFAULT_PRIVACY_CONTEXT_ to specify the default shared privacy context that applies to all connections that do not use a custom context.

## Topics

### Configuring Custom Privacy Settings

- [nw_privacy_context_create](<nw_privacy_context_create(__).md>) — Initializes a privacy context with a description string.
- [nw_privacy_context_disable_logging](<nw_privacy_context_disable_logging(__).md>) — Disables system logging of connection activity.
- [nw_privacy_context_flush_cache](<nw_privacy_context_flush_cache(__).md>) — Flushes all cached data, such as TLS session state, created by connections associated with the privacy context.

### Requiring Encrypted DNS

- [nw_privacy_context_require_encrypted_name_resolution](<nw_privacy_context_require_encrypted_name_resolution(______).md>) — Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [nw_resolver_config_t](nw_resolver_config_t.md) — A DNS server configuration that uses TLS or HTTPS.
- [nw_resolver_config_create_https](<nw_resolver_config_create_https(__).md>) — Initializes a DNS-over-HTTPS resolver configuration.
- [nw_resolver_config_create_tls](<nw_resolver_config_create_tls(__).md>) — Initializes a DNS-over-TLS resolver configuration.
- [nw_resolver_config_add_server_address](<nw_resolver_config_add_server_address(____).md>) — Provides a well-known DNS server address to use instead of looking up the address dynamically.

### Configuring Proxies

- [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>) — Applies a proxy configuration to all connections associated with this context.
- [nw_privacy_context_clear_proxies](<nw_privacy_context_clear_proxies(__).md>) — Clears out any proxies added using [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>)
- [nw_proxy_config_t](nw_proxy_config_t.md) — A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

## See Also

### Configuring Privacy Settings

- [nw_parameters_set_privacy_context](<nw_parameters_set_privacy_context(____).md>) — Associates a privacy context with any connections or listeners that use the parameters.
