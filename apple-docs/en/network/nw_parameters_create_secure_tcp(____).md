---
title: 'nw_parameters_create_secure_tcp(_:_:)'
framework: Network
symbol_kind: func
role: symbol
role_heading: Function
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.1+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: '/documentation/network/nw_parameters_create_secure_tcp(_:_:)'
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_create_secure_tcp(_:_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_create_secure_tcp%28_%3A_%3A%29.json'
content_hash: 'sha256:85967c3d0c216f1a'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_create_secure_tcp(_:_:)

<sub>Function</sub>

Initializes parameters for TLS or TCP connections and listeners.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func nw_parameters_create_secure_tcp(_ configure_tls: @escaping nw_parameters_configure_protocol_block_t, _ configure_tcp: @escaping nw_parameters_configure_protocol_block_t) -> nw_parameters_t
```

## Discussion

This function allows you to either use the default configurations for TLS and TCP, or use customized protocol options. If you want to use the default configuration, pass NW_PARAMETERS_DEFAULT_CONFIGURATION. If you want to customize the options for a protocol, pass a block to modify the options.

If you need to disable TLS, pass NW_PARAMETERS_DISABLE_PROTOCOL.

## See Also

### Creating Parameters

- [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) — Initializes parameters for DTLS or UDP connections and listeners.
- [nw_parameters_create_quic](<nw_parameters_create_quic(__).md>) — Initializes parameters for QUIC connections and listeners.
- [nw_parameters_configure_protocol_block_t](nw_parameters_configure_protocol_block_t.md) — A block to configure protocol options during the creation of a parameters object.
- [nw_parameters_create](<nw_parameters_create().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [nw_parameters_create_custom_ip](<nw_parameters_create_custom_ip(____).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [nw_parameters_copy](<nw_parameters_copy(__).md>) — Peforms a deep copy of a parameters object.
