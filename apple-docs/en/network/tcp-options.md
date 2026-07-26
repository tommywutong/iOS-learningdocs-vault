---
title: TCP Options
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/tcp-options
source_url: 'https://developer.apple.com/documentation/network/tcp-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/tcp-options.json'
content_hash: 'sha256:44ab537ab71b97d9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# TCP Options

<sub>API Collection</sub>

Configure options for connections that use the Transmission Control Protocol.

## Topics

### Creating TCP Connections

- [nw_protocol_copy_tcp_definition](<nw_protocol_copy_tcp_definition().md>) — Accesses the system definition of the Transport Control Protocol.
- [nw_tcp_create_options](<nw_tcp_create_options().md>) — Initializes a default set of TCP connection options.

### Customizing TCP Options

- [nw_tcp_options_set_enable_fast_open](<nw_tcp_options_set_enable_fast_open(____).md>) — Enables TCP Fast Open on a connection.
- [nw_tcp_options_set_maximum_segment_size](<nw_tcp_options_set_maximum_segment_size(____).md>) — Sets TCP’s maximum segment size in bytes.
- [nw_tcp_options_set_no_delay](<nw_tcp_options_set_no_delay(____).md>) — Disables Nagle’s algorithm for TCP.
- [nw_tcp_options_set_no_options](<nw_tcp_options_set_no_options(____).md>) — Sets TCP into no-options mode.
- [nw_tcp_options_set_no_push](<nw_tcp_options_set_no_push(____).md>) — Sets TCP into no-push mode.
- [nw_tcp_options_set_retransmit_fin_drop](<nw_tcp_options_set_retransmit_fin_drop(____).md>) — Causes TCP to drop its connection after not receiving an ACK after a FIN.
- [nw_tcp_options_set_disable_ack_stretching](<nw_tcp_options_set_disable_ack_stretching(____).md>) — Disables TCP acknowledgment stretching.
- [nw_tcp_options_set_disable_ecn](<nw_tcp_options_set_disable_ecn(____).md>) — Disables negotiation of Explicit Congestion Notification markings.

### Configuring Keepalives

- [nw_tcp_options_set_enable_keepalive](<nw_tcp_options_set_enable_keepalive(____).md>) — Enables TCP keepalives.
- [nw_tcp_options_set_keepalive_idle_time](<nw_tcp_options_set_keepalive_idle_time(____).md>) — Sets the number of seconds of idleness that TCP waits before sending keepalive probes.
- [nw_tcp_options_set_keepalive_count](<nw_tcp_options_set_keepalive_count(____).md>) — Sets the number of keepalive probes that TCP sends before terminating the connection.
- [nw_tcp_options_set_keepalive_interval](<nw_tcp_options_set_keepalive_interval(____).md>) — Sets the number of seconds that TCP waits between sending keepalive probes.

### Setting Timeouts

- [nw_tcp_options_set_connection_timeout](<nw_tcp_options_set_connection_timeout(____).md>) — Sets the number of seconds that TCP waits before timing out its handshake.
- [nw_tcp_options_set_retransmit_connection_drop_time](<nw_tcp_options_set_retransmit_connection_drop_time(____).md>) — Sets the number of seconds that TCP waits between retransmission attempts.
- [nw_tcp_options_set_persist_timeout](<nw_tcp_options_set_persist_timeout(____).md>) — Sets the TCP persist timeout in seconds, as defined by RFC 6429.

### Inspecting TCP State

- [nw_protocol_metadata_is_tcp](<nw_protocol_metadata_is_tcp(__).md>) — Checks whether a metadata object contains TCP connection state.
- [nw_tcp_get_available_send_buffer](<nw_tcp_get_available_send_buffer(__).md>) — Accesses the number of available bytes in the TCP send buffer.
- [nw_tcp_get_available_receive_buffer](<nw_tcp_get_available_receive_buffer(__).md>) — Accesses the number of available bytes in the TCP receive buffer.

## See Also

### Network Protocols

- [TLS Options](tls-options.md) — Configure options for connections that use Transport Layer Security.
- [QUIC Options](quic-options.md) — Configure options for connections that use the QUIC transport protocol.
- [UDP Options](udp-options.md) — Configure options for connections that use the User Datagram Protocol.
- [IP Options](ip-options.md) — Configure Internet Protocol options on connections.
- [WebSocket Options](websocket-options.md) — Configure options for connections that use WebSocket.
- [Framer Protocol Options](framer-protocol-options.md) — Create custom protocols to frame applications messages over a connection.
