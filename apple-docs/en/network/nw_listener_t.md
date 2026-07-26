---
title: nw_listener_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_listener_t
source_url: 'https://developer.apple.com/documentation/network/nw_listener_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_listener_t.json'
content_hash: 'sha256:e3385925c96d95d4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_listener_t

<sub>Type Alias</sub>

An object you use to listen for incoming network connections.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_listener_t = any OS_nw_listener
```

## Topics

### Creating Listeners

- [nw_listener_create](<nw_listener_create(__).md>) — Initializes a network listener, which will select a random port.
- [nw_listener_create_with_port](<nw_listener_create_with_port(____).md>) — Initializes a network listener with a specified local port.
- [nw_listener_create_with_connection](<nw_listener_create_with_connection(____).md>) — Initializes a network listener to receive new streams on a multiplexed connection.
- [nw_listener_set_queue](<nw_listener_set_queue(____).md>) — Sets the queue on which all listener events are delivered.
- [nw_listener_start](<nw_listener_start(__).md>) — Registers for listening for inbound connections.
- [nw_listener_get_port](<nw_listener_get_port(__).md>) — The port on which the listener can accept connections.
- [nw_listener_cancel](<nw_listener_cancel(__).md>) — Stops listening for inbound connections.

### Receiving Connections

- [nw_listener_set_new_connection_handler](<nw_listener_set_new_connection_handler(____).md>) — Sets a handler that receives inbound connections.
- [nw_listener_new_connection_handler_t](nw_listener_new_connection_handler_t.md) — A handler that delivers inbound connections.
- [nw_listener_set_new_connection_limit](<nw_listener_set_new_connection_limit(____).md>) — Resets the number of inbound connections to deliver before rejecting connections.
- [nw_listener_get_new_connection_limit](<nw_listener_get_new_connection_limit(__).md>) — Checks the remaining number of inbound connections to deliver before rejecting connections.
- [NW_LISTENER_INFINITE_CONNECTION_LIMIT](nw_listener_infinite_connection_limit.md) — A static value that indicates that inbound connections should not be limited.

### Advertising Bonjour Services

- [NSBonjourServices](../bundleresources/information-property-list/nsbonjourservices.md) — Bonjour service types browsed by the app.
- [NSLocalNetworkUsageDescription](../bundleresources/information-property-list/nslocalnetworkusagedescription.md) — A message that tells people why the app is requesting access to the local network.
- [nw_listener_set_advertise_descriptor](<nw_listener_set_advertise_descriptor(____).md>) — Sets a Bonjour service that advertises the listener on the local network.
- [nw_advertise_descriptor_t](nw_advertise_descriptor_t.md) — A description used to advertise the Bonjour service that a listener provides.
- [nw_listener_set_advertised_endpoint_changed_handler](<nw_listener_set_advertised_endpoint_changed_handler(____).md>) — Sets a handler that receives updates for the service endpoint being advertised.
- [nw_listener_advertised_endpoint_changed_handler_t](nw_listener_advertised_endpoint_changed_handler_t.md) — A handler that indicates changes to the service endpoints being advertised as they are added and removed.

### Handling State Updates

- [nw_listener_set_state_changed_handler](<nw_listener_set_state_changed_handler(____).md>) — Sets a handler to receive listener state updates.
- [nw_listener_state_changed_handler_t](nw_listener_state_changed_handler_t.md) — A handler that delivers listener state updates with associated errors.
- [nw_listener_state_t](nw_listener_state_t.md) — States indicating whether a listener is able to accept incoming connections.
