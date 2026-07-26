---
title: 'init(http2RelayEndpoint:tlsOptions:additionalHTTPHeaderFields:)'
framework: Network
symbol_kind: init
role: symbol
role_heading: Initializer
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: '/documentation/network/proxyconfiguration/relayhop/init(http2relayendpoint:tlsoptions:additionalhttpheaderfields:)'
source_url: 'https://developer.apple.com/documentation/network/proxyconfiguration/relayhop/init(http2relayendpoint:tlsoptions:additionalhttpheaderfields:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/proxyconfiguration/relayhop/init%28http2relayendpoint%3Atlsoptions%3Aadditionalhttpheaderfields%3A%29.json'
content_hash: 'sha256:70b7f92e6741e965'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Network](../../../network.md) · [ProxyConfiguration](../../proxyconfiguration.md) · [RelayHop](../relayhop.md)

# init(http2RelayEndpoint:tlsOptions:additionalHTTPHeaderFields:)

<sub>Initializer</sub>

Creates a configuration for a secure relay accessible only using HTTP/2.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
init(http2RelayEndpoint: NWEndpoint, tlsOptions: NWProtocolTLS.Options = .init(), additionalHTTPHeaderFields: [String : String] = [:])
```

## Parameters

- `http2RelayEndpoint` — A URL or host endpoint identifying the relay server accessible using HTTP/2.

- `tlsOptions` — The TLS options to use for the TLS handshake to the relay.

- `additionalHTTPHeaderFields` — A dictionary of additional HTTP headers to send as part of `CONNECT` requests to the relay.

## See Also

### Creating Relay Hops

- [init(http3RelayEndpoint:http2RelayEndpoint:tlsOptions:additionalHTTPHeaderFields:)](<init(http3relayendpoint_http2relayendpoint_tlsoptions_additionalhttpheaderfields_).md>) — Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
