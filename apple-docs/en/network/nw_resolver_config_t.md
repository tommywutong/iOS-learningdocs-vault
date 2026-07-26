---
title: nw_resolver_config_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_resolver_config_t
source_url: 'https://developer.apple.com/documentation/network/nw_resolver_config_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_resolver_config_t.json'
content_hash: 'sha256:f9ea5462553e58be'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_resolver_config_t

<sub>Type Alias</sub>

A DNS server configuration that uses TLS or HTTPS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_resolver_config_t = any OS_nw_resolver_config
```

## See Also

### Requiring Encrypted DNS

- [nw_privacy_context_require_encrypted_name_resolution](<nw_privacy_context_require_encrypted_name_resolution(______).md>) — Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.
- [nw_resolver_config_create_https](<nw_resolver_config_create_https(__).md>) — Initializes a DNS-over-HTTPS resolver configuration.
- [nw_resolver_config_create_tls](<nw_resolver_config_create_tls(__).md>) — Initializes a DNS-over-TLS resolver configuration.
- [nw_resolver_config_add_server_address](<nw_resolver_config_add_server_address(____).md>) — Provides a well-known DNS server address to use instead of looking up the address dynamically.
