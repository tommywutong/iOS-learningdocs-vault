---
title: Network Data Types
framework: Network
symbol_kind: article
role: collectionGroup
role_heading: API Collection
platforms: []
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/network-data-types
source_url: 'https://developer.apple.com/documentation/network/network-data-types'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/network-data-types.json'
content_hash: 'sha256:5585d1a2cc55da93'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# Network Data Types

<sub>API Collection</sub>

## Topics

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
- [nw_connection_receive_completion_t](nw_connection_receive_completion_t.md) — A completion handler that indicates when content has been received by the connection, or that an error was encountered.
- [nw_connection_send_completion_t](nw_connection_send_completion_t.md) — A completion handler that indicates when the connection has finished processing sent content.
- [nw_connection_state_changed_handler_t](nw_connection_state_changed_handler_t.md) — A handler that delivers connection state updates with associated errors.
- [nw_connection_t](nw_connection_t.md) — A bidirectional data connection between a local endpoint and a remote endpoint.
- [nw_content_context_t](nw_content_context_t.md) — A representation of a message to send or receive, containing protocol metadata and send properties.
- [nw_data_transfer_report_collect_block_t](nw_data_transfer_report_collect_block_t.md) — A block that is delivered when a data transfer report is fully collected.
- [nw_data_transfer_report_t](nw_data_transfer_report_t.md) — A report that provides metrics about data being sent and received on a connection.
- [nw_endpoint_t](nw_endpoint_t.md) — A local or remote endpoint in a network connection.
- [nw_error_t](nw_error_t.md) — The errors returned by the Network framework.
- [nw_establishment_report_access_block_t](nw_establishment_report_access_block_t.md) — A block that delivers a connection’s establishment report when it’s in the ready state.
- [nw_establishment_report_t](nw_establishment_report_t.md) — A report that provides metrics about how a connection was established.
- [nw_ethernet_address_t](nw_ethernet_address_t.md) — A 48-bit Ethernet address.
- [nw_ethernet_channel_receive_handler_t](nw_ethernet_channel_receive_handler_t.md) — A handler that delivers inbound Ethernet frames.
- [nw_ethernet_channel_send_completion_t](nw_ethernet_channel_send_completion_t.md) — A handler that indicates when an Ethernet frame has been sent, or if an error was encountered.
- [nw_ethernet_channel_state_changed_handler_t](nw_ethernet_channel_state_changed_handler_t.md) — A handler that delivers Ethernet channel state updates with associated errors.
- [nw_ethernet_channel_t](nw_ethernet_channel_t.md) — An object you use to send and receive custom Ethernet frames.
- [nw_framer_block_t](nw_framer_block_t.md) — A block to be invoked asynchronously on your framer protocol’s scheduling context.
- [nw_framer_cleanup_handler_t](nw_framer_cleanup_handler_t.md) — A handler that tells your protocol to clean up all allocations before being deallocated.
- [nw_framer_input_handler_t](nw_framer_input_handler_t.md) — A handler that notifies your protocol that new inbound data is available to parse.
- [nw_framer_message_dispose_value_t](nw_framer_message_dispose_value_t.md) — A handler that’s invoked when your custom value needs to be released due to a message being released or the value being replaced.
- [nw_framer_message_t](nw_framer_message_t.md) — A message for a custom protocol, in which you can store arbitrary key-value pairs.
- [nw_framer_output_handler_t](nw_framer_output_handler_t.md) — A handler that notifies your protocol about a new outbound message.
- [nw_framer_parse_completion_t](nw_framer_parse_completion_t.md) — A handler that examines a range of data being sent or received.
- [nw_framer_start_handler_t](nw_framer_start_handler_t.md) — A handler that represents the entry point into your custom protocol.
- [nw_framer_stop_handler_t](nw_framer_stop_handler_t.md) — A handler that requests that your protocol send any final messages to close the connection.
- [nw_framer_t](nw_framer_t.md) — An object that represents a single instance of your custom protocol running in a connection.
- [nw_framer_wakeup_handler_t](nw_framer_wakeup_handler_t.md) — A handler that delivers a scheduled wakeup event.
- [nw_group_descriptor_enumerate_endpoints_block_t](nw_group_descriptor_enumerate_endpoints_block_t.md) — A handler that lists all endpoints added to the group descriptor.
- [nw_group_descriptor_t](nw_group_descriptor_t.md) — A type that defines a group of endpoints with which you can communicate, such as a multicast group.
- [nw_interface_t](nw_interface_t.md) — An interface that a network connection uses to send and receive data.
- [nw_listener_advertised_endpoint_changed_handler_t](nw_listener_advertised_endpoint_changed_handler_t.md) — A handler that indicates changes to the service endpoints being advertised as they are added and removed.
- [nw_listener_new_connection_group_handler_t](nw_listener_new_connection_group_handler_t.md)
- [nw_listener_new_connection_handler_t](nw_listener_new_connection_handler_t.md) — A handler that delivers inbound connections.
- [nw_listener_state_changed_handler_t](nw_listener_state_changed_handler_t.md) — A handler that delivers listener state updates with associated errors.
- [nw_listener_t](nw_listener_t.md) — An object you use to listen for incoming network connections.
- [nw_object_t](nw_object_t.md) — The generic type for objects in the Network framework.
- [nw_path_enumerate_gateways_block_t](nw_path_enumerate_gateways_block_t.md) — A block that enumerates the gateways configured on the interfaces available to a path.
- [nw_path_enumerate_interfaces_block_t](nw_path_enumerate_interfaces_block_t.md) — A block that enumerates the interfaces available to a path.
- [nw_path_monitor_cancel_handler_t](nw_path_monitor_cancel_handler_t.md) — A handler that indicates when a monitor has been cancelled.
- [nw_path_monitor_t](nw_path_monitor_t.md) — An observer that you use to monitor and react to network changes.
- [nw_path_monitor_update_handler_t](nw_path_monitor_update_handler_t.md) — A handler that delivers network path updates.
- [nw_path_t](nw_path_t.md) — An object that contains information about the properties of the network that a connection uses, or that are available to your app.
- [nw_protocol_metadata_t](nw_protocol_metadata_t.md) — The abstract superclass for specifying metadata about a network protocol.
- [nw_proxy_domain_enumerator_t](nw_proxy_domain_enumerator_t.md)
- [nw_report_protocol_enumerator_t](nw_report_protocol_enumerator_t.md) — A block used to enumerate protocol handshakes performed during connection establishment.
- [nw_report_resolution_enumerator_t](nw_report_resolution_enumerator_t.md) — A block used to enumerate resolution steps performed during connection establishment.
- [nw_report_resolution_report_enumerator_t](nw_report_resolution_report_enumerator_t.md) — Iterates a list of resolution steps, as [nw_resolution_report_t](nw_resolution_report_t.md) objects, performed during connection establishment, in order from first resolved to last resolved.
- [nw_resolution_report_t](nw_resolution_report_t.md) — A description of a single DNS resolution step.
- [nw_txt_record_access_bytes_t](nw_txt_record_access_bytes_t.md) — A block that provides access to the raw bytes of a TXT record.
- [nw_txt_record_access_key_t](nw_txt_record_access_key_t.md) — A block that returns a value in a TXT record dictionary.
- [nw_txt_record_applier_t](nw_txt_record_applier_t.md) — A block that iterates over values and keys in a TXT record dictionary.
- [nw_txt_record_t](nw_txt_record_t.md) — A dictionary representing a TXT record in a DNS packet.
- [nw_ws_additional_header_enumerator_t](nw_ws_additional_header_enumerator_t.md) — A block that enumerates additional HTTP headers in a WebSocket client request.
- [nw_ws_client_request_handler_t](nw_ws_client_request_handler_t.md) — A handler that delivers inbound client handshake requests.
- [nw_ws_pong_handler_t](nw_ws_pong_handler_t.md) — A handler that indicates that a Pong message has been received for a previously sent Ping message, or that an error was encountered.
- [nw_ws_request_t](nw_ws_request_t.md) — A WebSocket handshake request sent from a client to a server.
- [nw_ws_response_t](nw_ws_response_t.md) — A WebSocket handshake reponse sent from a server to a client.
- [nw_ws_subprotocol_enumerator_t](nw_ws_subprotocol_enumerator_t.md) — A block that enumerates the supported subprotocols in a WebSocket client request.

## See Also

### Reference

- [Network Constants](network-constants.md) — Access Network framework constants used in C.
- [Network Functions](network-functions.md) — Access Network framework functions used in C.
