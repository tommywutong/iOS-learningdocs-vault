---
title: 'receiveMessage(completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/receivemessage(completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/receivemessage(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/receivemessage%28completion%3A%29.json'
content_hash: 'sha256:ad4f3daa5fbb0902'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# receiveMessage(completion:)

<sub>Instance Method</sub>

Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func receiveMessage(completion: @escaping @Sendable (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)
```

## Parameters

- `completion` — A receive completion is invoked exactly once for a call to receive. The completion indicates that the requested content has been received (in which case the content is delivered), or that an error has occurred. The completion delivers the received content, which may be nil if the message is complete or an error occurred, the message context, a flag indicating if the message is complete, and any associated error.

## Discussion

Receiving messages allows you to deal with complete datagrams or application-layer messages without needing to reconstruct a stream.

If you are using UDP, receiving a message will deliver a single datagram.

If you request to receive a message on a protocol that is otherwise an unbounded bytestream, like TCP or TLS, note that this will not deliver any data until the stream is closed by the peer.

In order to use messages on top of a bytestream protocol, add a protocol such as [NWProtocolWebSocket](../nwprotocolwebsocket.md) or a custom [NWProtocolFramer](../nwprotocolframer.md) to your protocol stack.

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
