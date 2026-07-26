---
title: nw_ws_close_code_t
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ws_close_code_t
source_url: 'https://developer.apple.com/documentation/network/nw_ws_close_code_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ws_close_code_t.json'
content_hash: 'sha256:fee26fdd859df77e'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ws_close_code_t

<sub>Structure</sub>

Types of codes used upon closing a WebSocket connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct nw_ws_close_code_t
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Defined Close Codes

- [nw_ws_close_code_normal_closure](nw_ws_close_code_normal_closure.md) — A normal closure occurred with no errors.
- [nw_ws_close_code_going_away](nw_ws_close_code_going_away.md) — An endpoint is no longer available, such as when a server is down.
- [nw_ws_close_code_protocol_error](nw_ws_close_code_protocol_error.md) — An endpoint is terminating the connection due to a protocol error.
- [nw_ws_close_code_unsupported_data](nw_ws_close_code_unsupported_data.md) — An endpoint is terminating the connection because it received a type of data it cannot accept.
- [nw_ws_close_code_no_status_received](nw_ws_close_code_no_status_received.md) — This value is reserved for local errors and indicates that no Close code was received.
- [nw_ws_close_code_abnormal_closure](nw_ws_close_code_abnormal_closure.md) — This value is reserved for local errors and indicates that no Close message was received.
- [nw_ws_close_code_invalid_frame_payload_data](nw_ws_close_code_invalid_frame_payload_data.md) — An endpoint is terminating the connection because it received data within a message that was inconsistent with the message type.
- [nw_ws_close_code_policy_violation](nw_ws_close_code_policy_violation.md) — An endpoint is terminating the connection because it received a message that violates its policy.
- [nw_ws_close_code_message_too_big](nw_ws_close_code_message_too_big.md) — An endpoint is terminating the connection because it received a message that is too big for it to process.
- [nw_ws_close_code_mandatory_extension](nw_ws_close_code_mandatory_extension.md) — The WebSocket client expected the server to negotiate one or more extensions that were not negotiated.
- [nw_ws_close_code_internal_server_error](nw_ws_close_code_internal_server_error.md) — The server is terminating the connection because it encountered an unexpected condition that prevented it from fulfilling the request.
- [nw_ws_close_code_tls_handshake](nw_ws_close_code_tls_handshake.md) — This value is reserved for local errors and indicates that the TLS handshake failed.

### Initializers

- [init(_:)](<nw_ws_close_code_t/init(__).md>)
- [init(rawValue:)](<nw_ws_close_code_t/init(rawvalue_).md>)

### Instance Properties

- [rawValue](nw_ws_close_code_t/rawvalue.md)

## See Also

### C Network Structures

- [nw_connection_group_state_t](nw_connection_group_state_t.md) — States that indicate whether you can use a connection group to send and receive messages.
- [nw_browser_state_t](nw_browser_state_t.md) — States indicating whether a browser is able to discover services.
- [nw_connection_state_t](nw_connection_state_t.md) — States indicating whether a connection can be used to send and receive data.
- [nw_data_transfer_report_state_t](nw_data_transfer_report_state_t.md) — States indicating whether a data transfer report is collected yet.
- [nw_endpoint_type_t](nw_endpoint_type_t.md) — The type of a network endpoint, such as a host or a service.
- [nw_error_domain_t](nw_error_domain_t.md) — The error domain for errors used by the Network framework.
- [nw_ethernet_channel_state_t](nw_ethernet_channel_state_t.md) — States indicating whether an Ethernet channel is able to send and receive frames.
- [nw_framer_start_result_t](nw_framer_start_result_t.md) — Results that you send to indicate the disposition of your protocol after the start handler is invoked.
- [nw_interface_type_t](nw_interface_type_t.md) — Types of network interfaces, based on their link layer media types.
- [nw_ip_ecn_flag_t](nw_ip_ecn_flag_t.md) — Flag values for Explicit Congestion Notifications in IP packets.
- [nw_ip_local_address_preference_t](nw_ip_local_address_preference_t.md) — Types of local addresses that can be selected, such as temporary or stable.
- [nw_ip_version_t](nw_ip_version_t.md) — IP versions to require on connections and listeners.
- [nw_listener_state_t](nw_listener_state_t.md) — States indicating whether a listener is able to accept incoming connections.
- [nw_multipath_service_t](nw_multipath_service_t.md) — Modes in which a connection can support multipath protocols.
- [nw_parameters_expired_dns_behavior_t](nw_parameters_expired_dns_behavior_t.md) — Options for configuring how expired DNS answers should be used.
