---
title: 'nw_proxy_config_set_failover_allowed(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_proxy_config_set_failover_allowed(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_set_failover_allowed(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_set_failover_allowed%28_%3A_%3A%29.json'
content_hash: 'sha256:d50b6f6f1430858d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_set_failover_allowed(_:_:)

<sub>Function</sub>

Configures whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_proxy_config_set_failover_allowed(_ proxy_config: nw_proxy_config_t, _ failover_allowed: Bool)
```

## Parameters

- `proxy_config` — The proxy configuration to modify.

- `failover_allowed` — A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections.

## See Also

### Customizing Proxy Behavior

- [nw_proxy_config_set_username_and_password](<nw_proxy_config_set_username_and_password(______).md>) — Sets a username and password to use as authentication for a proxy configuration.
