---
title: 'nw_privacy_context_require_encrypted_name_resolution(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 14.0+, iPadOS 14.0+, Mac Catalyst 14.0+, macOS 11.0+, tvOS 14.0+, visionOS 1.0+, watchOS 7.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_privacy_context_require_encrypted_name_resolution(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_require_encrypted_name_resolution(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_require_encrypted_name_resolution%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:abaa0a7d491c6fbf'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_require_encrypted_name_resolution(_:_:_:)

<sub>Function</sub>

Requires that any DNS name resolution for connections associated with this context use encrypted transports, such as TLS or HTTPS.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_privacy_context_require_encrypted_name_resolution(_ privacy_context: nw_privacy_context_t, _ require_encrypted_name_resolution: Bool, _ fallback_resolver_config: nw_resolver_config_t?)
```

## See Also

### Requiring Encrypted DNS

- [nw_resolver_config_t](nw_resolver_config_t.md) — A DNS server configuration that uses TLS or HTTPS.
- [nw_resolver_config_create_https](<nw_resolver_config_create_https(__).md>) — Initializes a DNS-over-HTTPS resolver configuration.
- [nw_resolver_config_create_tls](<nw_resolver_config_create_tls(__).md>) — Initializes a DNS-over-TLS resolver configuration.
- [nw_resolver_config_add_server_address](<nw_resolver_config_add_server_address(____).md>) — Provides a well-known DNS server address to use instead of looking up the address dynamically.
