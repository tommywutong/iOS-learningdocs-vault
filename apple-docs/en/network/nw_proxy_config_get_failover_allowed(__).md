---
title: 'nw_proxy_config_get_failover_allowed(_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_proxy_config_get_failover_allowed(_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_get_failover_allowed(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_get_failover_allowed%28_%3A%29.json'
content_hash: 'sha256:558764c0d4b2f999'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_get_failover_allowed(_:)

<sub>Function</sub>

Checks if a proxy configuration allows failover to non-proxied connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_proxy_config_get_failover_allowed(_ proxy_config: nw_proxy_config_t) -> Bool
```

## Parameters

- `proxy_config` — The proxy configuration to check.

## Return Value

A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections.
