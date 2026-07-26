---
title: 'send(content:contentContext:isComplete:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/send(content:contentcontext:iscomplete:completion:)-3mfmt'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/send(content:contentcontext:iscomplete:completion:)-3mfmt'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/send%28content%3Acontentcontext%3Aiscomplete%3Acompletion%3A%29-3mfmt.json'
content_hash: 'sha256:033c483f43965da0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# send(content:contentContext:isComplete:completion:)

<sub>Instance Method</sub>

Sends data on a connection using a custom Data type.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func send<Content>(content: Content?, contentContext: NWConnection.ContentContext = .defaultMessage, isComplete: Bool = true, completion: NWConnection.SendCompletion) where Content : DataProtocol
```

## Parameters

- `content` — The data to send on the connection. May be nil if this send marks its context as complete, such as by sending [finalMessage](contentcontext/finalmessage.md) as the context and marking the send complete to send a write-close.

- `contentContext` — The context associated with the content, which represents a logical message to be sent on the connection. All content sent within a single context will be sent as an in-order unit, up until the point that the context is marked complete. Once a context is marked complete, it may be re-used as a new logical message. Protocols like TCP that cannot send multiple independent messages at once (serial bytestreams) will only start processing a new context once the prior context has been marked complete. Defaults to [defaultMessage](contentcontext/defaultmessage.md).

- `isComplete` — A flag indicating if the caller’s sending context (logical message) is now complete. Until a context is marked complete, content sent for other contexts may not be sent immediately (if the protocol requires sending bytes serially, like TCP). For datagram protocols, like UDP, this flag indicates that the content represents a complete datagram. When sending using streaming protocols like TCP, this flag can be used to mark the end of a single message on the stream, of which there may be many. However, it can also indicate that the connection should send a “write close” (a TCP FIN) if the sending context is the final context on the connection. Specifically, to send a “write close”, pass [finalMessage](contentcontext/finalmessage.md) or [defaultStream](contentcontext/defaultstream.md) for the context (or create a custom context and set [isFinal](contentcontext/isfinal.md)), and mark the send as complete.

- `completion` — A completion handler ([NWConnection.SendCompletion.contentProcessed(_:)](<sendcompletion/contentprocessed(__).md>)) to notify the caller when content has been processed by the connection, or a marker that this data is idempotent ([NWConnection.SendCompletion.idempotent](sendcompletion/idempotent.md)) and may be sent multiple times as fast open data if [allowFastOpen](../nwparameters/allowfastopen.md) is set.

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
