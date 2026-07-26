---
title: 'nw_proxy_config_set_username_and_password(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_proxy_config_set_username_and_password(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_set_username_and_password(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_set_username_and_password%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:42bda7eb30110538'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_set_username_and_password(_:_:_:)

<sub>Function</sub>

Sets a username and password to use as authentication for a proxy configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_proxy_config_set_username_and_password(_ proxy_config: nw_proxy_config_t, _ username: UnsafePointer<CChar>, _ password: UnsafePointer<CChar>?)
```

## Parameters

- `proxy_config` — The proxy configuration to modify.

- `username` — A proxy authentication username.

- `password` — A proxy authentication password.

## See Also

### Customizing Proxy Behavior

- [nw_proxy_config_set_failover_allowed](<nw_proxy_config_set_failover_allowed(____).md>) — Configures whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
