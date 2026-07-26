---
title: 'init(socksv5Proxy:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/proxyconfiguration/init(socksv5proxy:)'
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/init(socksv5proxy:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/init%28socksv5proxy%3A%29.json'
content_hash: 'sha256:72d073d27789539f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# init(socksv5Proxy:)

<sub>Initializer</sub>

Initializes a SOCKSv5 proxy configuration.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(socksv5Proxy: NWEndpoint)
```

## Parameters

- `socksv5Proxy` — A host endpoint identifying the SOCKS proxy server.

## See Also

### Creating Proxy Configurations

- [init(relayHops:)](<init(relayhops_).md>) — Initializes a proxy configuration with one or two relay hops.
- [RelayHop](relayhop.md) — A single relay server you can chain together with other servers.
- [init(httpCONNECTProxy:tlsOptions:)](<init(httpconnectproxy_tlsoptions_).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
