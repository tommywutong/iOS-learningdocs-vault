---
title: nw_connection_group_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_connection_group_t
source_url: 'https://developer.apple.com/documentation/network/nw_connection_group_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_connection_group_t.json'
content_hash: 'sha256:fc02970457e1f60f'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_connection_group_t

<sub>Type Alias</sub>

An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_connection_group_t = any OS_nw_connection_group
```

## Topics

### Establishing Group Connectivity

- [nw_connection_group_create](<nw_connection_group_create(____).md>) — Initializes a new connection group with a group identifier.
- [nw_group_descriptor_create_multicast](<nw_group_descriptor_create_multicast(__).md>) — Creates group descriptor you use to join an IP multicast group on a local network.
- [nw_group_descriptor_t](nw_group_descriptor_t.md) — A type that defines a group of endpoints with which you can communicate, such as a multicast group.
- [nw_group_descriptor_add_endpoint](<nw_group_descriptor_add_endpoint(____).md>) — Adds a multicast address endpoint you specify to define an extra IP multicast group to join.
- [nw_group_descriptor_enumerate_endpoints](<nw_group_descriptor_enumerate_endpoints(____).md>) — Sets a handler to list all endpoints added to the group descriptor.
- [nw_group_descriptor_enumerate_endpoints_block_t](nw_group_descriptor_enumerate_endpoints_block_t.md) — A handler that lists all endpoints added to the group descriptor.
- [nw_connection_group_set_queue](<nw_connection_group_set_queue(____).md>) — Sets the queue on which you handle connection group events.
- [nw_connection_group_start](<nw_connection_group_start(__).md>) — Joins the group and registers to receive messages.

### Sending and Receiving Group Messages

- [nw_connection_group_set_receive_handler](<nw_connection_group_set_receive_handler(________).md>) — Sets a handler that receives inbound messages from members of the group.
- [nw_connection_group_receive_handler_t](nw_connection_group_receive_handler_t.md) — A handler that receives inbound messages from members of the group.
- [nw_connection_group_copy_remote_endpoint_for_message](<nw_connection_group_copy_remote_endpoint_for_message(____).md>) — Accesses the endpoint that originates the message you receive.
- [nw_connection_group_copy_local_endpoint_for_message](<nw_connection_group_copy_local_endpoint_for_message(____).md>) — Accesses the local address and port you use to receive the message.
- [nw_connection_group_copy_path_for_message](<nw_connection_group_copy_path_for_message(____).md>) — Accesses the network path on which you receive the message.
- [nw_connection_group_reply](<nw_connection_group_reply(________).md>) — Sends a reply to the specific endpoint that originates a group message you receive.
- [nw_connection_group_extract_connection_for_message](<nw_connection_group_extract_connection_for_message(____).md>) — Converts a message you receive from an endpoint into a connection object that you use for long-term communication with that endpoint.
- [nw_connection_group_send_message](<nw_connection_group_send_message(__________).md>) — Sends data to the entire group, or to a specific member of the group.
- [nw_connection_group_send_completion_t](nw_connection_group_send_completion_t.md) — A completion to notify you when data has been processed and sent.

### Managing Groups

- [nw_connection_group_set_state_changed_handler](<nw_connection_group_set_state_changed_handler(____).md>) — Sets a handler that receives connection group state updates.
- [nw_connection_group_state_changed_handler_t](nw_connection_group_state_changed_handler_t.md) — A handler that receives connection group state updates.
- [nw_connection_group_state_t](nw_connection_group_state_t.md) — States that indicate whether you can use a connection group to send and receive messages.
- [nw_connection_group_cancel](<nw_connection_group_cancel(__).md>) — Cancels the connection group object and leaves the network group.

### Inspecting Groups

- [nw_connection_group_copy_descriptor](<nw_connection_group_copy_descriptor(__).md>) — Accesses the descriptor of the group you use to initialize the connection group.
- [nw_connection_group_copy_parameters](<nw_connection_group_copy_parameters(__).md>) — Accesses the parameters with which you initialize the connection group.
