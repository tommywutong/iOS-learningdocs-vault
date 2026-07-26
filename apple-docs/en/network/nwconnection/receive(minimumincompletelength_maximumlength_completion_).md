---
title: 'receive(minimumIncompleteLength:maximumLength:completion:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/receive(minimumincompletelength:maximumlength:completion:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/receive(minimumincompletelength:maximumlength:completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/receive%28minimumincompletelength%3Amaximumlength%3Acompletion%3A%29.json'
content_hash: 'sha256:61fc6c9f066fbb25'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# receive(minimumIncompleteLength:maximumLength:completion:)

<sub>Instance Method</sub>

Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@preconcurrency final func receive(minimumIncompleteLength: Int, maximumLength: Int, completion: @escaping @Sendable (Data?, NWConnection.ContentContext?, Bool, NWError?) -> Void)
```

## Parameters

- `minimumIncompleteLength` — The minimum length to receive from the connection, until the content is complete.

- `maximumLength` — The maximum length to receive from the connection in a single completion.

- `completion` — A receive completion is invoked exactly once for a call to receive. The completion indicates that the requested content has been received (in which case the content is delivered), or that an error has occurred. The completion delivers the received content, which may be nil if the message is complete or an error occurred, the message context, a flag indicating if the message is complete, and any associated error.

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
