---
title: WebSocket Options
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [occ]
beta: false
deprecated: false
doc_path: /documentation/network/websocket-options
source_url: 'https://developer.apple.com/documentation/network/websocket-options'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/websocket-options.json'
content_hash: 'sha256:90bfa6b8d297fdca'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# WebSocket Options

<sub>API Collection</sub>

Configure options for connections that use WebSocket.

## Topics

### Creating WebSocket Connections

- [nw_protocol_copy_ws_definition](<nw_protocol_copy_ws_definition().md>) — Accesses the system definition of the WebSocket protocol.
- [nw_ws_create_options](<nw_ws_create_options(__).md>) — Initializes a default set of WebSocket connection options.
- [nw_ws_version_t](nw_ws_version_t.md) — Supported versions of the WebSocket protocol.
- [nw_ws_options_set_auto_reply_ping](<nw_ws_options_set_auto_reply_ping(____).md>) — Configures the connection to automatically reply to Ping messages instead of delivering them to you.
- [nw_ws_options_set_maximum_message_size](<nw_ws_options_set_maximum_message_size(____).md>) — Sets the maximum allowed message size, in bytes, to be received by the WebSocket connection.

### Configuring Client Handshakes

- [nw_ws_options_add_additional_header](<nw_ws_options_add_additional_header(______).md>) — Adds additional HTTP header fields to be sent by the client during the WebSocket handshake.
- [nw_ws_options_add_subprotocol](<nw_ws_options_add_subprotocol(____).md>) — Adds to the list of supported application protocols that will be presented to a WebSocket server during connection establishment.
- [nw_ws_options_set_skip_handshake](<nw_ws_options_set_skip_handshake(____).md>) — Specifies whether the WebSocket protocol skips its handshake and begins framing data once the underlying connection is established.

### Handling WebSocket Messages

- [nw_protocol_metadata_is_ws](<nw_protocol_metadata_is_ws(__).md>) — Checks whether a metadata object represents a WebSocket message.
- [nw_ws_create_metadata](<nw_ws_create_metadata(__).md>) — Initializes a WebSocket message with a specific type code.
- [nw_ws_metadata_get_opcode](<nw_ws_metadata_get_opcode(__).md>) — Checks the type code on a WebSocket message.
- [nw_ws_opcode_t](nw_ws_opcode_t.md) — Types of messages that you send and receive on a WebSocket connection.
- [nw_ws_metadata_set_close_code](<nw_ws_metadata_set_close_code(____).md>) — Sets a close code on a WebSocket message.
- [nw_ws_metadata_get_close_code](<nw_ws_metadata_get_close_code(__).md>) — Accesses the close code on a WebSocket message.
- [nw_ws_close_code_t](nw_ws_close_code_t.md) — Types of codes used upon closing a WebSocket connection.
- [nw_ws_metadata_set_pong_handler](<nw_ws_metadata_set_pong_handler(______).md>) — Sets a handler on a Ping message to be invoked when the corresponding Pong message is received.
- [nw_ws_pong_handler_t](nw_ws_pong_handler_t.md) — A handler that indicates that a Pong message has been received for a previously sent Ping message, or that an error was encountered.
- [nw_ws_metadata_copy_server_response](<nw_ws_metadata_copy_server_response(__).md>) — Accesses the WebSocket server’s response sent during the handshake.

### Handling Server Handshakes

- [nw_ws_options_set_client_request_handler](<nw_ws_options_set_client_request_handler(______).md>) — Sets a handler to react to as a server to inbound WebSocket client handshakes.
- [nw_ws_client_request_handler_t](nw_ws_client_request_handler_t.md) — A handler that delivers inbound client handshake requests.
- [nw_ws_request_t](nw_ws_request_t.md) — A WebSocket handshake request sent from a client to a server.
- [nw_ws_request_enumerate_subprotocols](<nw_ws_request_enumerate_subprotocols(____).md>) — Enumerates the supported subprotocols in a WebSocket message.
- [nw_ws_subprotocol_enumerator_t](nw_ws_subprotocol_enumerator_t.md) — A block that enumerates the supported subprotocols in a WebSocket client request.
- [nw_ws_request_enumerate_additional_headers](<nw_ws_request_enumerate_additional_headers(____).md>) — Enumerates additional HTTP headers in a WebSocket message.
- [nw_ws_additional_header_enumerator_t](nw_ws_additional_header_enumerator_t.md) — A block that enumerates additional HTTP headers in a WebSocket client request.
- [nw_ws_response_t](nw_ws_response_t.md) — A WebSocket handshake reponse sent from a server to a client.
- [nw_ws_response_create](<nw_ws_response_create(____).md>) — Initializes a WebSocket server response with a status and selected subprotocol.
- [nw_ws_response_status_t](nw_ws_response_status_t.md) — Status values that are sent with a WebSocket server response.
- [nw_ws_response_add_additional_header](<nw_ws_response_add_additional_header(______).md>) — Adds an additional HTTP header to a WebSocket server response.
- [nw_ws_response_get_status](<nw_ws_response_get_status(__).md>) — Accesses the status of a WebSocket server response.
- [nw_ws_response_get_selected_subprotocol](<nw_ws_response_get_selected_subprotocol(__).md>) — Accesses the selected subprotocol in a WebSocket server response.
- [nw_ws_response_enumerate_additional_headers](<nw_ws_response_enumerate_additional_headers(____).md>) — Enumerates the additional HTTP headers in a WebSocket server response.

## See Also

### Network Protocols

- [TCP Options](tcp-options.md) — Configure options for connections that use the Transmission Control Protocol.
- [TLS Options](tls-options.md) — Configure options for connections that use Transport Layer Security.
- [QUIC Options](quic-options.md) — Configure options for connections that use the QUIC transport protocol.
- [UDP Options](udp-options.md) — Configure options for connections that use the User Datagram Protocol.
- [IP Options](ip-options.md) — Configure Internet Protocol options on connections.
- [Framer Protocol Options](framer-protocol-options.md) — Create custom protocols to frame applications messages over a connection.
