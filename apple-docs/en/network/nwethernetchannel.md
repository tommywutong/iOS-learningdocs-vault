---
title: NWEthernetChannel
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [macOS 10.15+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwethernetchannel
source_url: 'https://developer.apple.com/documentation/network/nwethernetchannel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwethernetchannel.json'
content_hash: 'sha256:ef8ede98b8bcabb4'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWEthernetChannel

<sub>Class</sub>

An object you use to send and receive custom Ethernet frames.

<sub>macOS</sub>

```swift
final class NWEthernetChannel
```

## Overview

Use Ethernet channels to send and receive custom Ethernet frame types over an interface.

Creating Ethernet channels requires the `com.apple.developer.networking.custom-protocol` entitlement.

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Managing Ethernet Channels

- [init(on:etherType:)](<nwethernetchannel/init(on_ethertype_).md>) — Initializes an Ethernet channel on a specific interface with a custom Ethernet type.
- [start(queue:)](<nwethernetchannel/start(queue_).md>) — Starts the process of registering the channel, and sets the queue on which all channel events are delivered.
- [cancel()](<nwethernetchannel/cancel().md>) — Unregisters the channel from the interface.

### Handling State Updates

- [state](nwethernetchannel/state-swift.property.md) — The current state of the channel.
- [State](nwethernetchannel/state-swift.enum.md) — States indicating whether an Ethernet channel is able to send and receive frames.
- [stateUpdateHandler](nwethernetchannel/stateupdatehandler.md) — A handler that delivers channel state updates.

### Sending and Receiving Ethernet Frames

- [send(content:to:vlanTag:completion:)](<nwethernetchannel/send(content_to_vlantag_completion_).md>) — Sends a single Ethernet frame over a channel to a specific Ethernet address.
- [receiveHandler](nwethernetchannel/receivehandler.md) — A handler that delivers inbound Ethernet frames.
- [EthernetAddress](nwethernetchannel/ethernetaddress.md) — A 48-bit Ethernet address.

### Inspecting Ethernet Channels

- [etherType](nwethernetchannel/ethertype.md) — The custom Ethernet type with which the channel was initialized.
- [interface](nwethernetchannel/interface.md) — The interface with which the channel was initialized.
- [queue](nwethernetchannel/queue.md) — The queue on which channel events will be delivered.

### Initializers

- [init(on:etherType:parameters:)](<nwethernetchannel/init(on_ethertype_parameters_).md>)

### Instance Properties

- [maximumPayloadSize](nwethernetchannel/maximumpayloadsize.md)

## See Also

### Connections and Listeners

- [NWConnection](nwconnection.md) — A bidirectional data connection between a local endpoint and a remote endpoint.
- [NWListener](nwlistener.md) — An object you use to listen for incoming network connections.
- [NWBrowser](nwbrowser.md) — An object you use to browse for available network services.
- [NWConnectionGroup](nwconnectiongroup.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
