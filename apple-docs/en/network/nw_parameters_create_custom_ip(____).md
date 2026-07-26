---
title: 'nw_parameters_create_custom_ip(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [macOS 10.15+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_create_custom_ip(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_create_custom_ip(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_create_custom_ip%28_%3A_%3A%29.json'
content_hash: 'sha256:9b26a4b3bc8e417f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_create_custom_ip(_:_:)

<sub>Function</sub>

Initializes parameters for connections and listeners using a custom IP protocol.

<sub>macOS</sub>

```swift
func nw_parameters_create_custom_ip(_ custom_ip_protocol_number: UInt8, _ configure_ip: @escaping nw_parameters_configure_protocol_block_t) -> nw_parameters_t
```

## Discussion

Creating custom IP protocol connections requires the “com.apple.developer.networking.custom-protocol” entitlement.

## See Also

### Creating Parameters

- [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) — Initializes parameters for TLS or TCP connections and listeners.
- [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) — Initializes parameters for DTLS or UDP connections and listeners.
- [nw_parameters_create_quic](<nw_parameters_create_quic(__).md>) — Initializes parameters for QUIC connections and listeners.
- [nw_parameters_configure_protocol_block_t](nw_parameters_configure_protocol_block_t.md) — A block to configure protocol options during the creation of a parameters object.
- [nw_parameters_create](<nw_parameters_create().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [nw_parameters_copy](<nw_parameters_copy(__).md>) — Peforms a deep copy of a parameters object.
