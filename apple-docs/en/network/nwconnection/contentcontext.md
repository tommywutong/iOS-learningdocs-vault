---
title: NWConnection.ContentContext
framework: Network
symbol_kind: class
role: symbol
role_heading: Class
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/contentcontext
source_url: 'https://developer.apple.com/documentation/network/nwconnection/contentcontext'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/contentcontext.json'
content_hash: 'sha256:c42490985d2b9b64'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# NWConnection.ContentContext

<sub>Class</sub>

An object that represents a message to send or receive, containing protocol metadata and send properties.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
class ContentContext
```

## Overview

For sending, you should use [defaultMessage](contentcontext/defaultmessage.md) unless there is a reason to override some values.

You can pass [finalMessage](contentcontext/finalmessage.md) to mark the final message in a connection. Once this context is used for sending, and the send is marked as complete, no more data can be sent on the connection.

If you are using a protocol that expects message content, like WebSocket or a custom framer, create a custom context and set metadata using [protocolMetadata](contentcontext/protocolmetadata.md).

## Relationships

- **Inherited By**: [Message](../nwconnectiongroup/message.md)

- **Conforms To**: [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Using Constant Send Contexts

- [defaultMessage](contentcontext/defaultmessage.md) — A static context representing a message with default properties.
- [finalMessage](contentcontext/finalmessage.md) — A static context that’s marked as the final message in a connection.
- [defaultStream](contentcontext/defaultstream.md) — A static context representing the total stream of bytes on a connection.

### Creating Custom Send Contexts

- [init(identifier:expiration:priority:isFinal:antecedent:metadata:)](<contentcontext/init(identifier_expiration_priority_isfinal_antecedent_metadata_).md>) — Initializes a custom message context.
- [identifier](contentcontext/identifier.md) — The identifier of the message, used for debugging.
- [protocolMetadata](contentcontext/protocolmetadata.md) — An array of protocol metadata used to configure per-message or per-packet properties.
- [NWProtocolMetadata](../nwprotocolmetadata.md) — The abstract superclass for specifying metadata about a network protocol.
- [antecedent](contentcontext/antecedent.md) — An optional message context that must be sent before the context you are sending.
- [expirationMilliseconds](contentcontext/expirationmilliseconds.md) — A number of milliseconds after which sending the data associated with this context must begin, otherwise the data is discarded.
- [relativePriority](contentcontext/relativepriority.md) — A relative value of priority used to reorder contexts when sending.

### Inspecting Receive Contexts

- [isFinal](contentcontext/isfinal.md) — A Boolean indicating whether this context represents the final message being sent or received.
- [protocolMetadata(definition:)](<contentcontext/protocolmetadata(definition_).md>) — Retreives the metadata associated with a specific protocol.

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
