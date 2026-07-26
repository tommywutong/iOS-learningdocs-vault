---
title: nw_establishment_report_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_establishment_report_t
source_url: 'https://developer.apple.com/documentation/network/nw_establishment_report_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_establishment_report_t.json'
content_hash: 'sha256:f447b5b20bac37ae'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_establishment_report_t

<sub>Type Alias</sub>

A report that provides metrics about how a connection was established.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_establishment_report_t = any OS_nw_establishment_report
```

## Topics

### Inspecting Connection Attempts

- [nw_establishment_report_get_duration_milliseconds](<nw_establishment_report_get_duration_milliseconds(__).md>) — Checks the total duration of the successful connection establishment attempt, from the preparing state to the ready state.
- [nw_establishment_report_get_previous_attempt_count](<nw_establishment_report_get_previous_attempt_count(__).md>) — Checks the number of attempts made before the successful attempt, when the connection moved from the preparing state back to the waiting state.
- [nw_establishment_report_get_attempt_started_after_milliseconds](<nw_establishment_report_get_attempt_started_after_milliseconds(__).md>) — Accesses the time between the call to start and the beginning of the successful connection attempt, in milliseconds.

### Inspecting Resolution

- [nw_establishment_report_enumerate_resolution_reports](<nw_establishment_report_enumerate_resolution_reports(____).md>)
- [nw_report_resolution_report_enumerator_t](nw_report_resolution_report_enumerator_t.md) — Iterates a list of resolution steps, as [nw_resolution_report_t](nw_resolution_report_t.md) objects, performed during connection establishment, in order from first resolved to last resolved.
- [nw_resolution_report_t](nw_resolution_report_t.md) — A description of a single DNS resolution step.
- [nw_resolution_report_get_milliseconds](<nw_resolution_report_get_milliseconds(__).md>) — Accesses the duration of this resolution step, from when the query was issued to when the response was complete.
- [nw_resolution_report_get_source](<nw_resolution_report_get_source(__).md>) — Accesses the source of the DNS response.
- [nw_report_resolution_source_t](nw_report_resolution_source_t.md) — Sources that may provide DNS responses.
- [nw_resolution_report_get_protocol](<nw_resolution_report_get_protocol(__).md>) — Accesses the transport protocol your connection used for DNS resolution.
- [nw_report_resolution_protocol_t](nw_report_resolution_protocol_t.md) — A set of transport protocols connections use for DNS resolution.
- [nw_resolution_report_copy_successful_endpoint](<nw_resolution_report_copy_successful_endpoint(__).md>) — Accesses the resolved endpoint that led to the established connection.
- [nw_resolution_report_copy_preferred_endpoint](<nw_resolution_report_copy_preferred_endpoint(__).md>) — Accesses the resolved endpoint that the connection used for its first connection attempt.
- [nw_resolution_report_get_endpoint_count](<nw_resolution_report_get_endpoint_count(__).md>) — Accesses the number of endpoints resolved in this step.
- [nw_establishment_report_enumerate_resolutions](<nw_establishment_report_enumerate_resolutions(____).md>) — Iterates a list of resolution steps performed during connection establishment, in order from first resolved to last resolved.
- [nw_report_resolution_enumerator_t](nw_report_resolution_enumerator_t.md) — A block used to enumerate resolution steps performed during connection establishment.

### Inspecting Protocol Handshakes

- [nw_establishment_report_enumerate_protocols](<nw_establishment_report_enumerate_protocols(____).md>) — Iterates a list of protocol handshakes in order from first completed to last completed.
- [nw_report_protocol_enumerator_t](nw_report_protocol_enumerator_t.md) — A block used to enumerate protocol handshakes performed during connection establishment.

### Checking for Proxies

- [nw_establishment_report_get_proxy_configured](<nw_establishment_report_get_proxy_configured(__).md>) — Checks whether a proxy was configured on the connection.
- [nw_establishment_report_get_used_proxy](<nw_establishment_report_get_used_proxy(__).md>) — Checks whether the connection used a proxy.
- [nw_establishment_report_copy_proxy_endpoint](<nw_establishment_report_copy_proxy_endpoint(__).md>) — Accesses the endpoint of the proxy the connection used.

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
