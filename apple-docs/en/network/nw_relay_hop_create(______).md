---
title: 'nw_relay_hop_create(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_relay_hop_create(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_relay_hop_create(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_relay_hop_create%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:03e6c222bc738663'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_relay_hop_create(_:_:_:)

<sub>Function</sub>

Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_relay_hop_create(_ http3_relay_endpoint: nw_endpoint_t?, _ http2_relay_endpoint: nw_endpoint_t?, _ relay_tls_options: nw_protocol_options_t?) -> nw_relay_hop_t
```

## Parameters

- `http3_relay_endpoint` — A URL or host endpoint identifying the relay server accessible using HTTP/3.

- `http2_relay_endpoint` — An optional URL or host endpoint identifying the relay server accessible using HTTP/2. This can be the same endpoint as `http3_relay_endpoint`.

- `relay_tls_options` — The TLS options to use for the TLS handshake to the relay.

## Return Value

An initialized relay hop object.

## See Also

### Configuring Relay Hops

- [nw_relay_hop_add_additional_http_header_field](<nw_relay_hop_add_additional_http_header_field(______).md>) — Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.
