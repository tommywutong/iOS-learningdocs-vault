---
title: NetworkChannel
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 26.0+, iPadOS 26.0+, Mac Catalyst 26.0+, macOS 26.0+, tvOS 26.0+, visionOS 26.0+, watchOS 26.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/networkchannel
source_url: 'https://developer.apple.com/documentation/network/networkchannel'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/networkchannel.json'
content_hash: 'sha256:a70c2b4c81d51ed6'
translated: false
---

> Navigation: [Technologies](../technologies.md) · [Network](../network.md)

# NetworkChannel

<sub>Class</sub>

A base class supporting sending and recieving data through an arbitrary network channel.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class NetworkChannel<ApplicationProtocol> where ApplicationProtocol : NetworkProtocolOptions
```

## Overview

The interface exposed by this type (and any derived classes) is dependent on the generic ApplicationProtocol parameter.

## Relationships

- **Inherited By**: [NetworkConnection](networkconnection.md), [Datagrams](quic/datagrams.md), [Stream](quic/stream.md)

- **Conforms To**: [Copyable](../swift/copyable.md), [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md), [Equatable](../swift/equatable.md), [Escapable](../swift/escapable.md), [Hashable](../swift/hashable.md), [Identifiable](../swift/identifiable.md), [Sendable](../swift/sendable.md), [SendableMetatype](../swift/sendablemetatype.md)

## Topics

### Operators

- [==(_:_:)](<networkchannel/==(____).md>) — Compare two instances of NetworkChannel for equality

### Instance Properties

- [debugDescription](networkchannel/debugdescription.md) — Generate a string representation of NetworkChannel suitable for logging
- [id](networkchannel/id.md) — The stable identity of the entity associated with this instance.
- [maximumDatagramSize](networkchannel/maximumdatagramsize.md) — Retrieve the maximum datagram size that can be sent on the channel. Any datagrams sent should be less than or equal to this size.
- [messages](networkchannel/messages.md) — Receive data from a connection as an async stream.
- [parameters](networkchannel/parameters.md)
- [state](networkchannel/state-swift.property.md) — Access the current state of the connection

### Instance Methods

- [close(code:reason:metadata:)](<networkchannel/close(code_reason_metadata_).md>) — Send a WebSocket close frame on a connection.
- [dataTransferReport()](<networkchannel/datatransferreport().md>) — Start a data transfer report on a connection. The report begins capturing data when the connection moves to the .ready state, or when the report is created (whichever occurs last). This method will start the connection if it isn’t already started.
- [establishmentReport()](<networkchannel/establishmentreport().md>) — Asynchronously request the establishment report for this connection. If called prior to the connection being in the .ready state, this method will wait until the connection becomes ready and then deliver the report. This method will start the connection if it isn’t already started.
- [metadata(definition:)](<networkchannel/metadata(definition_).md>) — Access connection-wide protocol metadata on the connection. This allows access to state for protocols like TCP and TLS that have long-term state.
- [onBetterPathUpdate(_:)](<networkchannel/onbetterpathupdate(__).md>) — A better path being available indicates that the system thinks there is a preferred path or interface to use, compared to the one this connection is actively using. As an example, the connection is established over an expensive cellular interface and an unmetered Wi-Fi interface is now available. _(beta)_
- [onPathUpdate(_:)](<networkchannel/onpathupdate(__).md>) — Set a closure to be called when the connection’s path has changed, which may be called multiple times until the connection is cancelled. _(beta)_
- [onViabilityUpdate(_:)](<networkchannel/onviabilityupdate(__).md>) — Set a closure to be called when the connection’s viability changes, which may be called multiple times until the connection is cancelled. _(beta)_
- [ping(_:metadata:)](<networkchannel/ping(__metadata_).md>) — Send a ping frame on a connection.
- [pong(_:metadata:)](<networkchannel/pong(__metadata_).md>) — Send a pong frame on a connection.
- [receive()](<networkchannel/receive()-3a115.md>) — Receive data from a connection.
- [receive()](<networkchannel/receive()-3atum.md>) — Receive data from a connection.
- [receive()](<networkchannel/receive()-5p11z.md>) — Receive an object from a connection.
- [receive()](<networkchannel/receive()-86md7.md>) — Receive data from a connection.
- [receive()](<networkchannel/receive()-8jbul.md>) — Receive data on a connection.
- [receive(as:)](<networkchannel/receive(as_).md>) — Receive data from a connection as a fixed width integer.
- [receive(atLeast:atMost:)](<networkchannel/receive(atleast_atmost_).md>) — Receive data from a connection
- [receive(exactly:)](<networkchannel/receive(exactly_).md>) — Receive data from a connection.
- [send(_:endOfStream:metadata:)](<networkchannel/send(__endofstream_metadata_)-4f2l0.md>) — Send fixed width integer on a connection. This may be called before the connection is ready, in which case the send will be enqueued until the connection is ready to send.
- [send(_:endOfStream:metadata:)](<networkchannel/send(__endofstream_metadata_)-79bb6.md>) — Send data on a connection.
- [send(_:lastMessage:metadata:other:)](<networkchannel/send(__lastmessage_metadata_other_).md>) — Send data on a connection.
- [send(_:metadata:)](<networkchannel/send(__metadata_)-3r1av.md>) — Send binary frame on a WebSocket connection.
- [send(_:metadata:)](<networkchannel/send(__metadata_)-42nkz.md>) — Send data on a UDP connection.
- [send(_:metadata:)](<networkchannel/send(__metadata_)-4rxt1.md>) — Send data on a connection.
- [send(_:metadata:)](<networkchannel/send(__metadata_)-5ec48.md>) — Send a text frame on a WebSocket connection.
- [send(_:type:lastMessage:metadata:)](<networkchannel/send(__type_lastmessage_metadata_).md>) — Send data on a connection.
- [sendIdempotent(_:endOfStream:metadata:)](<networkchannel/sendidempotent(__endofstream_metadata_)-4bo5u.md>) — Send data idempotently on a connection.
- [sendIdempotent(_:endOfStream:metadata:)](<networkchannel/sendidempotent(__endofstream_metadata_)-6cko0.md>) — Send data idempotently on a connection.
- [sendIdempotent(_:metadata:)](<networkchannel/sendidempotent(__metadata_)-37eiq.md>) — Send an idempotent text frame on a WebSocket connection.
- [sendIdempotent(_:metadata:)](<networkchannel/sendidempotent(__metadata_)-6tubc.md>) — Send an idempotent binary frame on a WebSocket connection.
- [sendIdempotent(_:type:lastMessage:metadata:)](<networkchannel/sendidempotent(__type_lastmessage_metadata_).md>) — Send idempotent data on a connection.
- [startReceive(_:)](<networkchannel/startreceive(__).md>) — Receive partial data from a connection.
- [startSend(_:metadata:handler:)](<networkchannel/startsend(__metadata_handler_)-15tt3.md>) — Send partial text on a connection.
- [startSend(_:metadata:handler:)](<networkchannel/startsend(__metadata_handler_)-5xhjv.md>) — Send partial binary data on a connection.

### Enumerations

- [State](networkchannel/state-swift.enum.md)
