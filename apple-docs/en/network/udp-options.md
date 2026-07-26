---
title: UDP Options
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/udp-options
source_url: 'https://developer.apple.com/documentation/network/udp-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/udp-options.json'
content_hash: 'sha256:09ed8c58d4fedbf3'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# UDP Options

<sub>API Collection</sub>

Configure options for connections that use the User Datagram Protocol.

## Topics

### Creating UDP Connections

- [nw_protocol_copy_udp_definition](<nw_protocol_copy_udp_definition().md>) — Accesses the system definition of the User Datagram Protocol.
- [nw_udp_create_options](<nw_udp_create_options().md>) — Initializes a default set of UDP connection options.

### Customizing UDP Connections

- [nw_udp_options_set_prefer_no_checksum](<nw_udp_options_set_prefer_no_checksum(____).md>) — Configures the connection to not send UDP checksums.

### Sending UDP Messages

- [nw_protocol_metadata_is_udp](<nw_protocol_metadata_is_udp(__).md>) — Checks whether a metadata object represents a UDP datagram.
- [nw_udp_create_metadata](<nw_udp_create_metadata().md>) — Initializes a default UDP message.

## See Also

### Network Protocols

- [TCP Options](tcp-options.md) — Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](tls-options.md) — Configure options for connections that use Transport Layer Security.
- [QUIC Options](quic-options.md) — Configure options for connections that use the QUIC transport protocol.
- [IP Options](ip-options.md) — Configure Internet Protocol options on connections.
- [WebSocket Options](websocket-options.md) — Configure options for connections that use WebSocket.
- [Framer Protocol Options](framer-protocol-options.md) — Create custom protocols to frame applications messages over a connection.
