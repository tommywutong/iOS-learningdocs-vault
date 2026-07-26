---
title: nw_parameters_create()
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_create()
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_create()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_create%28%29.json'
content_hash: 'sha256:c2a1d51c7e095274'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_create()

<sub>Function</sub>

Initializes parameters for connections, listeners, and browsers with no protocols specified.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_create() -> nw_parameters_t
```

## See Also

### Creating Parameters

- [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) — Initializes parameters for TLS or TCP connections and listeners.
- [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) — Initializes parameters for DTLS or UDP connections and listeners.
- [nw_parameters_create_quic](<nw_parameters_create_quic(__).md>) — Initializes parameters for QUIC connections and listeners.
- [nw_parameters_configure_protocol_block_t](nw_parameters_configure_protocol_block_t.md) — A block to configure protocol options during the creation of a parameters object.
- [nw_parameters_create_custom_ip](<nw_parameters_create_custom_ip(____).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [nw_parameters_copy](<nw_parameters_copy(__).md>) — Peforms a deep copy of a parameters object.
