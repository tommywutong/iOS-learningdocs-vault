---
title: ProxyConfiguration.RelayHop
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/network/proxyconfiguration/relayhop
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/relayhop'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/relayhop.json'
content_hash: 'sha256:e77ee14d5b9ea6f0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [ProxyConfiguration](../proxyconfiguration.md)

# ProxyConfiguration.RelayHop

<sub>Structure</sub>

A single relay server you can chain together with other servers.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RelayHop
```

## Overview

Relay servers are secure HTTP proxies that allow proxying TCP traffic using the `CONNECT` method and UDP traffic using the `connect-udp` protocol defined in [RFC 9298](https://www.rfc-editor.org/rfc/rfc9298.html).

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../../swift/customdebugstringconvertible.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Creating Relay Hops

- [init(http3RelayEndpoint:http2RelayEndpoint:tlsOptions:additionalHTTPHeaderFields:)](<relayhop/init(http3relayendpoint_http2relayendpoint_tlsoptions_additionalhttpheaderfields_).md>) — Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
- [init(http2RelayEndpoint:tlsOptions:additionalHTTPHeaderFields:)](<relayhop/init(http2relayendpoint_tlsoptions_additionalhttpheaderfields_).md>) — Creates a configuration for a secure relay accessible only using HTTP/2.

## See Also

### Creating Proxy Configurations

- [init(relayHops:)](<init(relayhops_).md>) — Initializes a proxy configuration with one or two relay hops.
- [init(httpCONNECTProxy:tlsOptions:)](<init(httpconnectproxy_tlsoptions_).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [init(socksv5Proxy:)](<init(socksv5proxy_).md>) — Initializes a SOCKSv5 proxy configuration.
