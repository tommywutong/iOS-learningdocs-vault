---
title: maximumDatagramSize
framework: Network
symbol_kind: property
role: symbol
role_heading: Instance Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/network/nwconnection/maximumdatagramsize
source_url: 'https://developer.apple.com/documentation/network/nwconnection/maximumdatagramsize'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/maximumdatagramsize.json'
content_hash: 'sha256:4a8e6147ac9894b1'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# maximumDatagramSize

<sub>Instance Property</sub>

The maximum size of a datagram message that can be sent on a connection.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final var maximumDatagramSize: Int { get }
```

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [batch(_:)](<batch(__).md>) — Defines a block in which calls to send and receive are processed as a batch to improve performance.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
