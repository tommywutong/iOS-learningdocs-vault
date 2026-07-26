---
title: 'nw_proxy_config_create_oblivious_http(_:_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_proxy_config_create_oblivious_http(_:_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_proxy_config_create_oblivious_http(_:_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_proxy_config_create_oblivious_http%28_%3A_%3A_%3A_%3A%29.json'
content_hash: 'sha256:fbe3a862f63256b7'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_proxy_config_create_oblivious_http(_:_:_:_:)

<sub>Function</sub>

Initializes an Oblivious HTTP proxy configuration using a relay and a gateway.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_proxy_config_create_oblivious_http(_ relay: nw_relay_hop_t, _ relay_resource_path: UnsafePointer<CChar>, _ gateway_key_config: UnsafePointer<UInt8>, _ gateway_key_config_length: Int) -> nw_proxy_config_t
```

## Parameters

- `relay` — The Oblivious HTTP relay hop.

- `relay_resource_path` — The HTTP path to use for requests to the Oblivious HTTP relay that will forward requests to the gateway.

- `gateway_key_config` — The [key configuration](https://www.ietf.org/archive/id/draft-ietf-ohai-ohttp-08.html#name-key-configuration-encoding) for the Oblivious HTTP gateway.

- `gateway_key_config_length` — The length of the key configuration buffer in `gateway_key_config.`

## Return Value

An initialized proxy configuration object.

## Discussion

[Oblivious HTTP](https://www.ietf.org/archive/id/draft-ietf-ohai-ohttp-08.html) provides per-message encryption to a gateway through a relay.

## See Also

### Creating Proxy Configurations

- [nw_proxy_config_create_relay](<nw_proxy_config_create_relay(____).md>) — Initializes a proxy configuration with one or two relay hops.
- [nw_relay_hop_t](nw_relay_hop_t.md) — A single relay server you can chain together with other servers.
- [nw_proxy_config_create_http_connect](<nw_proxy_config_create_http_connect(____).md>) — Initializes a legacy HTTP CONNECT configuration for a proxy server accessible using HTTP/1.1.
- [nw_proxy_config_create_socksv5](<nw_proxy_config_create_socksv5(__).md>) — Initializes a SOCKSv5 proxy configuration.
