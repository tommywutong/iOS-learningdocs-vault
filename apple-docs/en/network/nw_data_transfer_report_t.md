---
title: nw_data_transfer_report_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_data_transfer_report_t
source_url: 'https://developer.apple.com/documentation/network/nw_data_transfer_report_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_data_transfer_report_t.json'
content_hash: 'sha256:b9012cd1a6be68c5'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_data_transfer_report_t

<sub>Type Alias</sub>

A report that provides metrics about data being sent and received on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_data_transfer_report_t = any OS_nw_data_transfer_report
```

## Topics

### Collecting Reports

- [nw_data_transfer_report_collect](<nw_data_transfer_report_collect(______).md>) — Stops an outstanding data transfer report and calculates the results.
- [nw_data_transfer_report_collect_block_t](nw_data_transfer_report_collect_block_t.md) — A block that is delivered when a data transfer report is fully collected.
- [nw_data_transfer_report_get_state](<nw_data_transfer_report_get_state(__).md>) — Checks whether a data transfer report is collected.
- [nw_data_transfer_report_state_t](nw_data_transfer_report_state_t.md) — States indicating whether a data transfer report is collected yet.

### Identifying Paths

- [nw_data_transfer_report_get_path_count](<nw_data_transfer_report_get_path_count(__).md>) — Checks the number of valid paths in the report.
- [nw_data_transfer_report_get_duration_milliseconds](<nw_data_transfer_report_get_duration_milliseconds(__).md>) — Checks the duration of the data transfer report, from when it was started to when it was collected.
- [nw_data_transfer_report_copy_path_interface](<nw_data_transfer_report_copy_path_interface(____).md>) — Accesses the network interface the path used.

### Inspecting Application Metrics

- [nw_data_transfer_report_get_received_application_byte_count](<nw_data_transfer_report_get_received_application_byte_count(____).md>) — Accesses the number of bytes the connection delivered.
- [nw_data_transfer_report_get_sent_application_byte_count](<nw_data_transfer_report_get_sent_application_byte_count(____).md>) — Accesses the number of bytes sent on the connection.

### Inspecting Transport Metrics

- [nw_data_transfer_report_get_received_transport_byte_count](<nw_data_transfer_report_get_received_transport_byte_count(____).md>) — Accesses the number of bytes the transport protocol delivered.
- [nw_data_transfer_report_get_received_transport_duplicate_byte_count](<nw_data_transfer_report_get_received_transport_duplicate_byte_count(____).md>) — Accesses the number of duplicated bytes the transport protocol detected.
- [nw_data_transfer_report_get_received_transport_out_of_order_byte_count](<nw_data_transfer_report_get_received_transport_out_of_order_byte_count(____).md>) — Accesses the number of bytes the transport protocol received out of order.
- [nw_data_transfer_report_get_sent_transport_byte_count](<nw_data_transfer_report_get_sent_transport_byte_count(____).md>) — Accesses the number of bytes sent into the transport protocol.
- [nw_data_transfer_report_get_sent_transport_retransmitted_byte_count](<nw_data_transfer_report_get_sent_transport_retransmitted_byte_count(____).md>) — Accesses the number of bytes the transport protocol retransmitted.
- [nw_data_transfer_report_get_transport_smoothed_rtt_milliseconds](<nw_data_transfer_report_get_transport_smoothed_rtt_milliseconds(____).md>) — Accesses the smoothed round-trip time the transport protocol measured, in milliseconds.
- [nw_data_transfer_report_get_transport_minimum_rtt_milliseconds](<nw_data_transfer_report_get_transport_minimum_rtt_milliseconds(____).md>) — Accesses the minimum round-trip time the transport protocol measured, in milliseconds.
- [nw_data_transfer_report_get_transport_rtt_variance](<nw_data_transfer_report_get_transport_rtt_variance(____).md>) — Accesses the variance of the round-trip time the transport protocol measured.

### Inspecting Packet Metrics

- [nw_data_transfer_report_get_received_ip_packet_count](<nw_data_transfer_report_get_received_ip_packet_count(____).md>) — Accesses the number of IP packets the connection received.
- [nw_data_transfer_report_get_sent_ip_packet_count](<nw_data_transfer_report_get_sent_ip_packet_count(____).md>) — Accesses the number of IP packets the connection sent.

## See Also

### Data Types

- [nw_advertise_descriptor_t](nw_advertise_descriptor_t.md) — A description used to advertise the Bonjour service that a listener provides.
- [nw_browse_descriptor_t](nw_browse_descriptor_t.md) — A service description used to discover Bonjour services.
- [nw_browse_result_change_t](nw_browse_result_change_t.md) — Flags describing ways in which discovered services can change between specific results.
- [nw_browse_result_enumerate_interface_t](nw_browse_result_enumerate_interface_t.md) — A handler that enumerates the interfaces associated with a discovered service.
- [nw_browse_result_t](nw_browse_result_t.md) — A discovered service and metadata about the service.
- [nw_browser_browse_results_changed_handler_t](nw_browser_browse_results_changed_handler_t.md) — A handler that delivers updates about discovered services.
- [nw_browser_state_changed_handler_t](nw_browser_state_changed_handler_t.md) — A handler that delivers browser state updates with associated errors.
- [nw_browser_t](nw_browser_t.md) — An object you use to browse for available network services.
- [nw_connection_boolean_event_handler_t](nw_connection_boolean_event_handler_t.md) — A handler that receives Boolean state updates from a connection, such as viability and better path state.
- [nw_connection_group_new_connection_handler_t](nw_connection_group_new_connection_handler_t.md)
- [nw_connection_group_receive_handler_t](nw_connection_group_receive_handler_t.md) — A handler that receives inbound messages from members of the group.
- [nw_connection_group_send_completion_t](nw_connection_group_send_completion_t.md) — A completion to notify you when data has been processed and sent.
- [nw_connection_group_state_changed_handler_t](nw_connection_group_state_changed_handler_t.md) — A handler that receives connection group state updates.
- [nw_connection_group_t](nw_connection_group_t.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [nw_connection_path_event_handler_t](nw_connection_path_event_handler_t.md) — A handler that delivers network path updates.
