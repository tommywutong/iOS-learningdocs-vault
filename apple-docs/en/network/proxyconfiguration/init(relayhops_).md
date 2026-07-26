---
title: 'init(relayHops:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/proxyconfiguration/init(relayhops:)'
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/init(relayhops:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/init%28relayhops%3A%29.json'
content_hash: 'sha256:a5de4fbc00ce243d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# init(relayHops:)

<sub>Initializer</sub>

Initializes a proxy configuration with one or two relay hops.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(relayHops: [ProxyConfiguration.RelayHop])
```

## Parameters

- `relayHops` — An array of relay hops, which must contain either one or two hops.

## See Also

### Creating Proxy Configurations

- [RelayHop](relayhop.md) — A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy:tlsOptions:)](<init(httpconnectproxy_tlsoptions_).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy:)](<init(socksv5proxy_).md>) — Initializes a SOCKSv5 proxy configuration.
