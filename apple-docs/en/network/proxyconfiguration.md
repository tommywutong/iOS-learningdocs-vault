---
title: ProxyConfiguration
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/proxyconfiguration
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration.json'
content_hash: 'sha256:deae35fd42ceef52'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# ProxyConfiguration

<sub>Structure</sub>

A proxy configuration for Relays, Oblivious HTTP, HTTP CONNECT, or SOCKSv5.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ProxyConfiguration
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Proxy Configurations

- [init(relayHops:)](<proxyconfiguration/init(relayhops_).md>) — Initializes a proxy configuration with one or two relay hops.
- [RelayHop](proxyconfiguration/relayhop.md) — A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy:tlsOptions:)](<proxyconfiguration/init(httpconnectproxy_tlsoptions_).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy:)](<proxyconfiguration/init(socksv5proxy_).md>) — Initializes a SOCKSv5 proxy configuration.

### Customizing Proxy Behavior

- [allowFailover](proxyconfiguration/allowfailover.md) — A Boolean that indicates whether or not a proxy configuration allows failover to non-proxied connections. Failover isn’t allowed by default.
- [applyCredential(username:password:)](<proxyconfiguration/applycredential(username_password_).md>) — Sets a username and password to use as authentication for a proxy configuration.

### Initializers

- [init(obliviousHTTPRelay:relayResourcePath:gatewayKeyConfig:matchDomains:)](<proxyconfiguration/init(oblivioushttprelay_relayresourcepath_gatewaykeyconfig_matchdomains_).md>)

### Instance Properties

- [excludedDomains](proxyconfiguration/excludeddomains.md)
- [matchDomains](proxyconfiguration/matchdomains.md)

## See Also

### Configuring Proxies

- [proxyConfigurations](nwparameters/privacycontext/proxyconfigurations.md) — Applies proxy configurations for all connections associated with this context.
