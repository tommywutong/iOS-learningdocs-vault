---
title: QUIC Options
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/quic-options
source_url: 'https://developer.apple.com/documentation/network/quic-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/quic-options.json'
content_hash: 'sha256:ded156d11a2b3f5d'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# QUIC Options

<sub>API Collection</sub>

Configure options for connections that use the QUIC transport protocol.

## Topics

### Creating QUIC Connections

- [nw_protocol_copy_quic_definition](<nw_protocol_copy_quic_definition().md>) — Accesses the system definition of the QUIC transport protocol.
- [nw_quic_create_options](<nw_quic_create_options().md>) — Initializes a default set of QUIC connection options.
- [nw_protocol_options_is_quic](<nw_protocol_options_is_quic(__).md>) — Checks whether an options object uses the QUIC protocol.

### Customizing Connection Options

- [nw_quic_add_tls_application_protocol](<nw_quic_add_tls_application_protocol(____).md>) — Adds a supported Application-Layer Protocol Negotiation value.
- [nw_quic_set_idle_timeout](<nw_quic_set_idle_timeout(____).md>) — Sets the idle timeout for the QUIC connection, in milliseconds.
- [nw_quic_get_idle_timeout](<nw_quic_get_idle_timeout(__).md>) — Accesses the idle timeout for the QUIC connection, in milliseconds.
- [nw_quic_set_initial_max_data](<nw_quic_set_initial_max_data(____).md>) — Sets a QUIC connection’s initial maximum data transport parameter.
- [nw_quic_get_initial_max_data](<nw_quic_get_initial_max_data(__).md>) — Accesses a QUIC connection’s initial maximum data transport parameter.
- [nw_quic_set_initial_max_stream_data_bidirectional_local](<nw_quic_set_initial_max_stream_data_bidirectional_local(____).md>) — Sets a QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [nw_quic_get_initial_max_stream_data_bidirectional_local](<nw_quic_get_initial_max_stream_data_bidirectional_local(__).md>) — Accesses a QUIC connection’s initial maximum stream data limit for locally-initiated bidirectional streams.
- [nw_quic_set_initial_max_stream_data_bidirectional_remote](<nw_quic_set_initial_max_stream_data_bidirectional_remote(____).md>) — Sets a QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [nw_quic_get_initial_max_stream_data_bidirectional_remote](<nw_quic_get_initial_max_stream_data_bidirectional_remote(__).md>) — Accesses a QUIC connection’s initial maximum stream data limit for remote-initiated bidirectional streams.
- [nw_quic_set_initial_max_stream_data_unidirectional](<nw_quic_set_initial_max_stream_data_unidirectional(____).md>) — Sets a QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [nw_quic_get_initial_max_stream_data_unidirectional](<nw_quic_get_initial_max_stream_data_unidirectional(__).md>) — Accesses a QUIC connection’s initial maximum stream data limit for unidirectional streams.
- [nw_quic_set_initial_max_streams_bidirectional](<nw_quic_set_initial_max_streams_bidirectional(____).md>) — Sets a QUIC connection’s initial maximum number of bidirectional streams.
- [nw_quic_get_initial_max_streams_bidirectional](<nw_quic_get_initial_max_streams_bidirectional(__).md>) — Accesses a QUIC connection’s initial maximum number of bidirectional streams.
- [nw_quic_set_initial_max_streams_unidirectional](<nw_quic_set_initial_max_streams_unidirectional(____).md>) — Sets a QUIC connection’s initial maximum number of unidirectional streams.
- [nw_quic_get_initial_max_streams_unidirectional](<nw_quic_get_initial_max_streams_unidirectional(__).md>) — Accesses a QUIC connection’s initial maximum number of unidirectional streams.
- [nw_quic_set_max_datagram_frame_size](<nw_quic_set_max_datagram_frame_size(____).md>) — Sets a QUIC connection’s maximum DATAGRAM frame size.
- [nw_quic_get_max_datagram_frame_size](<nw_quic_get_max_datagram_frame_size(__).md>) — Accesses a QUIC connection’s maximum DATAGRAM frame size.
- [nw_quic_set_max_udp_payload_size](<nw_quic_set_max_udp_payload_size(____).md>) — Sets the maximum length of a QUIC packet that can be received on a connection, in bytes.
- [nw_quic_get_max_udp_payload_size](<nw_quic_get_max_udp_payload_size(__).md>) — Accesses the maximum length of a QUIC packet that can be received on a connection, in bytes.
- [nw_quic_copy_sec_protocol_options](<nw_quic_copy_sec_protocol_options(__).md>) — Accesses the handshake security options QUIC will use.

### Customizing Stream Options

- [nw_quic_set_stream_is_unidirectional](<nw_quic_set_stream_is_unidirectional(____).md>) — Configures a QUIC stream as unidirectional, instead of bidirectional.
- [nw_quic_get_stream_is_unidirectional](<nw_quic_get_stream_is_unidirectional(__).md>) — Checks if a QUIC stream is unidirectional, instead of bidirectional.
- [nw_quic_set_stream_is_datagram](<nw_quic_set_stream_is_datagram(____).md>) — Configures a QUIC stream as a datagram flow, instead of a byte stream.
- [nw_quic_get_stream_is_datagram](<nw_quic_get_stream_is_datagram(__).md>) — Checks if a QUIC stream is a datagram flow, instead of a byte stream.

### Inspecting Connection State

- [nw_protocol_metadata_is_quic](<nw_protocol_metadata_is_quic(__).md>) — Checks whether a metadata object contains QUIC connection state.
- [nw_quic_set_local_max_streams_bidirectional](<nw_quic_set_local_max_streams_bidirectional(____).md>) — Sets the maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [nw_quic_get_local_max_streams_bidirectional](<nw_quic_get_local_max_streams_bidirectional(__).md>) — Accesses the maximum number of bidirectional streams that the peer can create on a QUIC connection.
- [nw_quic_set_local_max_streams_unidirectional](<nw_quic_set_local_max_streams_unidirectional(____).md>) — Sets the maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [nw_quic_get_local_max_streams_unidirectional](<nw_quic_get_local_max_streams_unidirectional(__).md>) — Accesses the maximum number of unidirectional streams that the peer can create on a QUIC connection.
- [nw_quic_get_remote_max_streams_bidirectional](<nw_quic_get_remote_max_streams_bidirectional(__).md>) — Accesses the maximum number of bidirectional streams advertised by peer that the connection is allowed to create.
- [nw_quic_get_remote_max_streams_unidirectional](<nw_quic_get_remote_max_streams_unidirectional(__).md>) — Accesses the maximum number of unidirectional streams advertised by peer that the connection is allowed to create.
- [nw_quic_get_remote_idle_timeout](<nw_quic_get_remote_idle_timeout(__).md>) — Accesses the idle timeout value from the peer’s transport parameters, in milliseconds.
- [nw_quic_copy_sec_protocol_metadata](<nw_quic_copy_sec_protocol_metadata(__).md>) — Accesses the result of the QUIC handshake.

### Inspecting Stream State

- [nw_quic_get_stream_id](<nw_quic_get_stream_id(__).md>) — Accesses the QUIC stream identifier.
- [nw_quic_get_stream_type](<nw_quic_get_stream_type(__).md>) — Accesses the stream type of the QUIC stream.
- [nw_quic_get_stream_usable_datagram_frame_size](<nw_quic_get_stream_usable_datagram_frame_size(__).md>) — Accesses the maximum usable size of a datagram frame on a QUIC datagram flow.

### Handling Errors

- [nw_quic_set_application_error](<nw_quic_set_application_error(______).md>) — Sets the QUIC application error code to send for the connection.
- [nw_quic_get_application_error](<nw_quic_get_application_error(__).md>) — Accesses the QUIC application error code received from the peer.
- [nw_quic_get_application_error_reason](<nw_quic_get_application_error_reason(__).md>) — Accesses the QUIC application error reason received from the peer.
- [nw_quic_set_stream_application_error](<nw_quic_set_stream_application_error(____).md>) — Sets the QUIC application error code to send for the stream.
- [nw_quic_get_stream_application_error](<nw_quic_get_stream_application_error(__).md>) — Accesses the QUIC application error code received from the peer for the stream.

### Configuring Keepalives

- [nw_quic_set_keepalive_interval](<nw_quic_set_keepalive_interval(____).md>) — Sets the keepalive interval for the QUIC connection, in seconds.
- [nw_quic_get_keepalive_interval](<nw_quic_get_keepalive_interval(__).md>) — Accesses the keepalive interval for the QUIC connection, in seconds.

## See Also

### Network Protocols

- [TCP Options](tcp-options.md) — Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](tls-options.md) — Configure options for connections that use Transport Layer Security.
- [UDP Options](udp-options.md) — Configure options for connections that use the User Datagram Protocol.
- [IP Options](ip-options.md) — Configure Internet Protocol options on connections.
- [WebSocket Options](websocket-options.md) — Configure options for connections that use WebSocket.
- [Framer Protocol Options](framer-protocol-options.md) — Create custom protocols to frame applications messages over a connection.
