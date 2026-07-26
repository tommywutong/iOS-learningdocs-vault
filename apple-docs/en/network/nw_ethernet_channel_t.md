---
title: nw_ethernet_channel_t
framework: Network
symbol_kind: typealias
role: symbol
role_heading: Type Alias
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 13.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, occ]
beta: false
deprecated: false
doc_path: /documentation/network/nw_ethernet_channel_t
source_url: 'https://developer.apple.com/documentation/network/nw_ethernet_channel_t'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nw_ethernet_channel_t.json'
content_hash: 'sha256:d9747ca905954916'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# nw_ethernet_channel_t

<sub>Type Alias</sub>

An object you use to send and receive custom Ethernet frames.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
typealias nw_ethernet_channel_t = any OS_nw_ethernet_channel
```

## Discussion

Use Ethernet channels to send and receive custom Ethernet frame types over an interface.

Creating Ethernet channels requires the `com.apple.developer.networking.custom-protocol` entitlement.

## Topics

### Managing Ethernet Channels

- [nw_ethernet_channel_create](<nw_ethernet_channel_create(____).md>) — Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [nw_ethernet_channel_set_queue](<nw_ethernet_channel_set_queue(____).md>) — Sets the queue on which all channel events are delivered.
- [nw_ethernet_channel_start](<nw_ethernet_channel_start(__).md>) — Starts the process of registering the channel.
- [nw_ethernet_channel_cancel](<nw_ethernet_channel_cancel(__).md>) — Unregisters the channel from the interface.

### Handling State Updates

- [nw_ethernet_channel_set_state_changed_handler](<nw_ethernet_channel_set_state_changed_handler(____).md>) — Sets a handler to receive channel state updates.
- [nw_ethernet_channel_state_changed_handler_t](nw_ethernet_channel_state_changed_handler_t.md) — A handler that delivers Ethernet channel state updates with associated errors.
- [nw_ethernet_channel_state_t](nw_ethernet_channel_state_t.md) — States indicating whether an Ethernet channel is able to send and receive frames.

### Sending and Receiving Ethernet Frames

- [nw_ethernet_channel_send](<nw_ethernet_channel_send(__________).md>) — Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [nw_ethernet_channel_send_completion_t](nw_ethernet_channel_send_completion_t.md) — A handler that indicates when an Ethernet frame has been sent, or if an error was encountered.
- [nw_ethernet_channel_set_receive_handler](<nw_ethernet_channel_set_receive_handler(____).md>) — Sets a handler to receive inbound Ethernet frames.
- [nw_ethernet_channel_receive_handler_t](nw_ethernet_channel_receive_handler_t.md) — A handler that delivers inbound Ethernet frames.
- [nw_ethernet_address_t](nw_ethernet_address_t.md) — A 48-bit Ethernet address.
