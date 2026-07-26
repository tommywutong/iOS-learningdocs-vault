---
title: 'nw_relay_hop_add_additional_http_header_field(_:_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 17.0+, iPadOS 17.0+, Mac Catalyst 17.0+, macOS 14.0+, tvOS 17.0+, visionOS 1.0+, watchOS 10.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_relay_hop_add_additional_http_header_field(_:_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_relay_hop_add_additional_http_header_field(_:_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_relay_hop_add_additional_http_header_field%28_%3A_%3A_%3A%29.json'
content_hash: 'sha256:a8e97a7d0e762e5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_relay_hop_add_additional_http_header_field(_:_:_:)

<sub>Function</sub>

Adds an HTTP header name and value pair to send as part of `CONNECT` requests to the relay.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_relay_hop_add_additional_http_header_field(_ relay_hop: nw_relay_hop_t, _ field_name: UnsafePointer<CChar>, _ field_value: UnsafePointer<CChar>)
```

## Parameters

- `relay_hop` — The relay hop to modify.

- `field_name` — The HTTP header name.

- `field_value` — The HTTP header value.

## See Also

### Configuring Relay Hops

- [nw_relay_hop_create](<nw_relay_hop_create(______).md>) — Creates a configuration for a secure relay accessible using HTTP/3, with an optional HTTP/2 fallback.
