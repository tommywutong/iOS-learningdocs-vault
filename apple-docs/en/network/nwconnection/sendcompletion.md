---
title: NWConnection.SendCompletion
framework: Network
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/sendcompletion
source_url: 'https://developer.apple.com/documentation/network/nwconnection/sendcompletion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/sendcompletion.json'
content_hash: 'sha256:b09548ed22090248'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# NWConnection.SendCompletion

<sub>Enumeration</sub>

A completion handler that indicates when the connection has finished processing sent content.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
enum SendCompletion
```

## Topics

### Completions

- [NWConnection.SendCompletion.contentProcessed(_:)](<sendcompletion/contentprocessed(__).md>) — Provide a completion handler that’s invoked when the sent data is processed by the stack.
- [NWConnection.SendCompletion.idempotent](sendcompletion/idempotent.md) — Mark the sent data as idempotent—data that can be sent multiple times.

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
