---
title: NWConnection
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection
source_url: 'https://developer.apple.com/documentation/network/nwconnection'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection.json'
content_hash: 'sha256:afbe0b59a0af66c9'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NWConnection

<sub>Class</sub>

A bidirectional data connection between a local endpoint and a remote endpoint.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final class NWConnection
```

## Relationships

- **Conforms To**: [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Creating Connections

- [init(host:port:using:)](<nwconnection/init(host_port_using_).md>) — Initializes a new connection to a host and port.
- [init(to:using:)](<nwconnection/init(to_using_).md>) — Initializes a new connection to a remote endpoint.
- [start(queue:)](<nwconnection/start(queue_).md>) — Starts establishing a connection, and sets the queue on which to deliver all connection events.
- [restart()](<nwconnection/restart().md>) — Restarts a connection that is in the waiting state.

### Handling State Updates

- [state](nwconnection/state-swift.property.md) — The current state of the connection.
- [State](nwconnection/state-swift.enum.md) — States indicating whether a connection can be used to send and receive data.
- [stateUpdateHandler](nwconnection/stateupdatehandler.md) — A handler that receives connection state updates.

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<nwconnection/send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<nwconnection/send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](nwconnection/sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<nwconnection/receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<nwconnection/receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<nwconnection/batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](nwconnection/contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](nwconnection/maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.

### Canceling Connections

- [cancel()](<nwconnection/cancel().md>) — Cancels the connection and gracefully disconnects any established network protocols.
- [forceCancel()](<nwconnection/forcecancel().md>) — Cancels the connection and immediately disconnects any established network protocols.
- [cancelCurrentEndpoint()](<nwconnection/cancelcurrentendpoint().md>) — Causes the current endpoint to be rejected, allowing the connection to try another resolved address.

### Handling Path Updates

- [currentPath](nwconnection/currentpath.md) — The network path the connection is using.
- [pathUpdateHandler](nwconnection/pathupdatehandler.md) — A handler that receives network path updates.
- [viabilityUpdateHandler](nwconnection/viabilityupdatehandler.md) — A handler that receives updates when data can be sent and received.
- [betterPathUpdateHandler](nwconnection/betterpathupdatehandler.md) — A handler that receives updates when an alternative network path is preferred over the current path.

### Collecting Connection Metrics

- [Collecting Network Connection Metrics](collecting-network-connection-metrics.md) — Use reports to understand how DNS and protocol handshakes impact connection establishment.
- [requestEstablishmentReport(queue:completion:)](<nwconnection/requestestablishmentreport(queue_completion_).md>) — Requests a copy of the connection’s establishment report once the connection is in the ready state.
- [EstablishmentReport](nwconnection/establishmentreport.md) — A report that provides metrics about the establishment of a connection.
- [startDataTransferReport()](<nwconnection/startdatatransferreport().md>) — Begins a new data transfer report, which can later be collected.
- [PendingDataTransferReport](nwconnection/pendingdatatransferreport.md) — An outstanding data transfer report that has yet to be collected.
- [DataTransferReport](nwconnection/datatransferreport.md) — A report that provides metrics about data being sent and received on a connection.

### Inspecting Connections

- [metadata(definition:)](<nwconnection/metadata(definition_).md>) — Retrieves the connection-wide metadata for a specific protocol.
- [NWProtocolMetadata](nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [endpoint](nwconnection/endpoint.md) — The remote endpoint with which the connection was initialized.
- [parameters](nwconnection/parameters.md) — The parameters with which the connection was initialized.
- [queue](nwconnection/queue.md) — The queue on which connection events are delivered.

### Initializers

- [init(from:to:using:)](<nwconnection/init(from_to_using_).md>)
- [init(message:)](<nwconnection/init(message_).md>)

### Instance Methods

- [receiveDiscontiguous(minimumIncompleteLength:maximumLength:completion:)](<nwconnection/receivediscontiguous(minimumincompletelength_maximumlength_completion_).md>)
- [receiveMessageDiscontiguous(completion:)](<nwconnection/receivemessagediscontiguous(completion_).md>)

## See Also

### Connections and Listeners

- [NWListener](nwlistener.md) — An object you use to listen for incoming network connections.
- [NWBrowser](nwbrowser.md) — An object you use to browse for available network services.
- [NWConnectionGroup](nwconnectiongroup.md) — An object you use to communicate with a group of endpoints, such as an IP multicast group on a local network.
- [NWEthernetChannel](nwethernetchannel.md) — An object you use to send and receive custom Ethernet frames.
