---
title: nw_ws_close_code_policy_violation
framework: Network
symbol_kind: var
role: symbol
role_heading: Global Variable
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ws_close_code_policy_violation
source_url: 'https://developer.apple.com/documentation/network/nw_ws_close_code_policy_violation'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ws_close_code_policy_violation.json'
content_hash: 'sha256:2a2e067b09d73cc9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ws_close_code_policy_violation

<sub>Global Variable</sub>

An endpoint is terminating the connection because it received a message that violates its policy.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
var nw_ws_close_code_policy_violation: nw_ws_close_code_t { get }
```

## See Also

### Defined Close Codes

- [nw_ws_close_code_normal_closure](nw_ws_close_code_normal_closure.md) — A normal closure occurred with no errors.
- [nw_ws_close_code_going_away](nw_ws_close_code_going_away.md) — An endpoint is no longer available, such as when a server is down.
- [nw_ws_close_code_protocol_error](nw_ws_close_code_protocol_error.md) — An endpoint is terminating the connection due to a protocol error.
- [nw_ws_close_code_unsupported_data](nw_ws_close_code_unsupported_data.md) — An endpoint is terminating the connection because it received a type of data it cannot accept.
- [nw_ws_close_code_no_status_received](nw_ws_close_code_no_status_received.md) — This value is reserved for local errors and indicates that no Close code was received.
- [nw_ws_close_code_abnormal_closure](nw_ws_close_code_abnormal_closure.md) — This value is reserved for local errors and indicates that no Close message was received.
- [nw_ws_close_code_invalid_frame_payload_data](nw_ws_close_code_invalid_frame_payload_data.md) — An endpoint is terminating the connection because it received data within a message that was inconsistent with the message type.
- [nw_ws_close_code_message_too_big](nw_ws_close_code_message_too_big.md) — An endpoint is terminating the connection because it received a message that is too big for it to process.
- [nw_ws_close_code_mandatory_extension](nw_ws_close_code_mandatory_extension.md) — The WebSocket client expected the server to negotiate one or more extensions that were not negotiated.
- [nw_ws_close_code_internal_server_error](nw_ws_close_code_internal_server_error.md) — The server is terminating the connection because it encountered an unexpected condition that prevented it from fulfilling the request.
- [nw_ws_close_code_tls_handshake](nw_ws_close_code_tls_handshake.md) — This value is reserved for local errors and indicates that the TLS handshake failed.
