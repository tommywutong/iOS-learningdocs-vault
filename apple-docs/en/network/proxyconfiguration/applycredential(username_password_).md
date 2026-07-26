---
title: 'applyCredential(username:password:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/proxyconfiguration/applycredential(username:password:)'
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/applycredential(username:password:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/applycredential%28username%3Apassword%3A%29.json'
content_hash: 'sha256:a9791446e124110f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# applyCredential(username:password:)

<sub>Instance Method</sub>

Sets a username and password to use as authentication for a proxy configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func applyCredential(username: String, password: String)
```

## Parameters

- `username` — A proxy authentication username.

- `password` — A proxy authentication password.

## See Also

### Customizing Proxy Behavior

- [allowFailover](allowfailover.md) — A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
