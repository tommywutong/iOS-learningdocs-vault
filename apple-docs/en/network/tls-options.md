---
title: TLS Options
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/tls-options
source_url: 'https://developer.apple.com/documentation/network/tls-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tls-options.json'
content_hash: 'sha256:a884cbf88e5f90f8'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# TLS Options

<sub>API Collection</sub>

Configure options for connections that use Transport Layer Security.

## Topics

### Creating TLS Connections

- [nw_protocol_copy_tls_definition](<nw_protocol_copy_tls_definition().md>) — Accesses the system definition of the Transport Layer Security protocol.
- [nw_tls_create_options](<nw_tls_create_options().md>) — Initializes a default set of TLS connection options.
- [nw_tls_copy_sec_protocol_options](<nw_tls_copy_sec_protocol_options(__).md>) — Accesses the handshake security options TLS will use.

### Inspecting TLS State

- [nw_protocol_metadata_is_tls](<nw_protocol_metadata_is_tls(__).md>) — Checks whether a metadata object contains TLS connection state.
- [nw_tls_copy_sec_protocol_metadata](<nw_tls_copy_sec_protocol_metadata(__).md>) — Accesses the result of the TLS handshake.

## See Also

### Network Protocols

- [TCP Options](tcp-options.md) — Configure options for connections that use the Transmission Control Protocol.
- [QUIC Options](quic-options.md) — Configure options for connections that use the QUIC transport protocol.
- [UDP Options](udp-options.md) — Configure options for connections that use the User Datagram Protocol.
- [IP Options](ip-options.md) — Configure Internet Protocol options on connections.
- [WebSocket Options](websocket-options.md) — Configure options for connections that use WebSocket.
- [Framer Protocol Options](framer-protocol-options.md) — Create custom protocols to frame applications messages over a connection.
