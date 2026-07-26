---
title: 'nw_resolver_config_create_tls(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_resolver_config_create_tls(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_resolver_config_create_tls(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_resolver_config_create_tls%28_%3A%29.json'
content_hash: 'sha256:4eecda623a599546'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_resolver_config_create_tls(_:)

<sub>Function</sub>

Initializes a DNS-over-TLS resolver configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_resolver_config_create_tls(_ server_endpoint: nw_endpoint_t) -> nw_resolver_config_t
```

## Parameters

- `server_endpoint` — The hostname of the provided endpoint will be used to validate the TLS certificate of the server. See [RFC 7858](https://tools.ietf.org/html/rfc7858) for more details.

## See Also

### Requiring Encrypted DNS

- [nw_privacy_context_require_encrypted_name_resolution](<nw_privacy_context_require_encrypted_name_resolution(______).md>) — Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [nw_resolver_config_t](nw_resolver_config_t.md) — A DNS server configuration that uses TLS or HTTPS.
- [nw_resolver_config_create_https](<nw_resolver_config_create_https(__).md>) — Initializes a DNS-over-HTTPS resolver configuration.
- [nw_resolver_config_add_server_address](<nw_resolver_config_add_server_address(____).md>) — Provides a well-known DNS server address to use instead of looking up the address dynamically.
