---
title: 'nw_privacy_context_add_proxy(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_privacy_context_add_proxy(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_privacy_context_add_proxy(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_privacy_context_add_proxy%28_%3A_%3A%29.json'
content_hash: 'sha256:bc2bbd49ad1790b4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_privacy_context_add_proxy(_:_:)

<sub>Function</sub>

Applies a proxy configuration to all connections associated with this context.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_privacy_context_add_proxy(_ privacy_context: nw_privacy_context_t, _ proxy_config: nw_proxy_config_t)
```

## Parameters

- `privacy_context` — A privacy context to modify. This can include the default privacy context.

- `proxy_config` — A proxy configuration object to apply to all connections that use this context.

## Discussion

If set on `NW_DEFAULT_PRIVACY_CONTEXT`, this proxy will additionally apply to other networking APIs used by the calling process.

## See Also

### Configuring Proxies

- [nw_privacy_context_clear_proxies](<nw_privacy_context_clear_proxies(__).md>) — Clears out any proxies added using [nw_privacy_context_add_proxy](<nw_privacy_context_add_proxy(____).md>)
- [nw_proxy_config_t](nw_proxy_config_t.md) — A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.
