---
title: allowFailover
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/proxyconfiguration/allowfailover
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/allowfailover'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/allowfailover.json'
content_hash: 'sha256:34525239ecfc96a5'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# allowFailover

<sub>Instance Property</sub>

A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var allowFailover: Bool { get set }
```

## See Also

### Customizing Proxy Behavior

- [applyCredential(username:password:)](<applycredential(username_password_).md>) — Sets a username and password to use as authentication for a proxy configuration.
