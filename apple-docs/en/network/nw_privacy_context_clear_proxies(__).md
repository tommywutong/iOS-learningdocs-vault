---
title: 'nw_privacy_context_clear_proxies(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_privacy_context_clear_proxies(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_clear_proxies(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_clear_proxies%28_%3A%29.json'
content_hash: 'sha256:9087731d2af24ba2'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_clear_proxies(_:)

<sub>Function</sub>

Clears out any proxies added using [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>)

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_privacy_context_clear_proxies(_ privacy_context: nw_privacy_context_t)
```

## Parameters

- `privacy_context` — A privacy context to modify. This can include the default privacy context.

## See Also

### Configuring Proxies

- [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>) — Applies a proxy configuration to all connections associated with this context.
- [nw_proxy_config_t](nw_proxy_config_t.md) — A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
