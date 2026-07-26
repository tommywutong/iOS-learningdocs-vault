---
title: 'init(httpCONNECTProxy:tlsOptions:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/proxyconfiguration/init(httpconnectproxy:tlsoptions:)'
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/init(httpconnectproxy:tlsoptions:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/init%28httpconnectproxy%3Atlsoptions%3A%29.json'
content_hash: 'sha256:8ad618371c53411c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# init(httpCONNECTProxy:tlsOptions:)

<sub>Initializer</sub>

Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(httpCONNECTProxy: NWEndpoint, tlsOptions: NWProtocolTLS.Options? = nil)
```

## Parameters

- `httpCONNECTProxy` — A host endpoint identifying the proxy server accessible using HTTP/1.1.

- `tlsOptions` — Optional TLS options to use for a TLS handshake to the relay. If no TLS options are provided, the proxy will be accessed using cleartext HTTP.

## Discussion

These HTTP CONNECT proxies only handle TCP connections. To support UDP proxying, use [init(relayHops:)](<init(relayhops_).md>).

## See Also

### Creating Proxy Configurations

- [init(relayHops:)](<init(relayhops_).md>) — Initializes a proxy configuration with one or two relay hops.
- [RelayHop](relayhop.md) — A single relay server you can chain together with other servers.
- [init(socksv5Proxy:)](<init(socksv5proxy_).md>) — Initializes a SOCKSv5 proxy configuration.
