---
title: nw_path_status_t
framework: Network
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_path_status_t
source_url: 'https://developer.apple.com/documentation/network/nw_path_status_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_path_status_t.json'
content_hash: 'sha256:1cc6e6388f8a2e84'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_path_status_t

<sub>Structure</sub>

Status values indicating whether a path can be used by connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct nw_path_status_t
```

## Relationships

- **Conforms To**: [BitwiseCopyable](../swift/bitwisecopyable.md), [Equatable](../swift/equatable.md), [Hashable](../swift/hashable.md), [RawRepresentable](../swift/rawrepresentable.md), [Sendable](../swift/sendable.md)

## Topics

### Status Values

- [nw_path_status_invalid](nw_path_status_invalid.md) — The path is not valid.
- [nw_path_status_unsatisfied](nw_path_status_unsatisfied.md) — The path is not available for use.
- [nw_path_status_satisfied](nw_path_status_satisfied.md) — The path is available to establish connections and send data.
- [nw_path_status_satisfiable](nw_path_status_satisfiable.md) — The path is not currently available, but establishing a new connection may activate the path.

### Initializers

- [init(_:)](<nw_path_status_t/init(__).md>)
- [init(rawValue:)](<nw_path_status_t/init(rawvalue_).md>)

### Instance Properties

- [rawValue](nw_path_status_t/rawvalue.md)

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
