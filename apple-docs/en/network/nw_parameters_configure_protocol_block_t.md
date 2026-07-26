---
title: nw_parameters_configure_protocol_block_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_parameters_configure_protocol_block_t
source_url: 'https://developer.apple.com/documentation/network/nw_parameters_configure_protocol_block_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_parameters_configure_protocol_block_t.json'
content_hash: 'sha256:7ec4812050f5d238'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_parameters_configure_protocol_block_t

<sub>Type Alias</sub>

A block to configure protocol options during the creation of a parameters object.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_parameters_configure_protocol_block_t = (nw_protocol_options_t) -> Void
```

## Discussion

Passing in a block allows you to customize how a protocol will behave in a connection.

If you want to use the default configuration for a protocol, pass NW_PARAMETERS_DEFAULT_CONFIGURATION.

If you want to disable a protocol (such as TLS), pass NW_PARAMETERS_DISABLE_PROTOCOL. Not all protocols can be disabled.

## See Also

### Creating Parameters

- [nw_parameters_create_secure_tcp](<nw_parameters_create_secure_tcp(____).md>) — Initializes parameters for TLS or TCP connections and listeners.
- [nw_parameters_create_secure_udp](<nw_parameters_create_secure_udp(____).md>) — Initializes parameters for DTLS or UDP connections and listeners.
- [nw_parameters_create_quic](<nw_parameters_create_quic(__).md>) — Initializes parameters for QUIC connections and listeners.
- [nw_parameters_create](<nw_parameters_create().md>) — Initializes parameters for connections, listeners, and browsers with no protocols specified.
- [nw_parameters_create_custom_ip](<nw_parameters_create_custom_ip(____).md>) — Initializes parameters for connections and listeners using a custom IP protocol.
- [nw_parameters_copy](<nw_parameters_copy(__).md>) — Peforms a deep copy of a parameters object.
