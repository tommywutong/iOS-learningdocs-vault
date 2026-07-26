---
title: 'batch(_:)'
framework: Network
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 12.0+, iPadOS 12.0+, Mac Catalyst 12.0+, macOS 10.14+, tvOS 12.0+, visionOS 1.0+, watchOS 5.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/network/nwconnection/batch(_:)'
source_url: 'https://developer.apple.com/documentation/network/nwconnection/batch(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/network/nwconnection/batch%28_%3A%29.json'
content_hash: 'sha256:d4d5f3bf457b56b6'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Network](../../network.md) · [NWConnection](../nwconnection.md)

# batch(_:)

<sub>Instance Method</sub>

Defines a block in which calls to send and receive are processed as a batch to improve performance.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func batch(_ block: () -> Void)
```

## See Also

### Sending and Receiving Data

- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-5ecuz.md>) — Sends data on a connection.
- [send(content:contentContext:isComplete:completion:)](<send(content_contentcontext_iscomplete_completion_)-3mfmt.md>) — Sends data on a connection using a custom Data type.
- [SendCompletion](sendcompletion.md) — A completion handler that indicates when the connection has finished processing sent content.
- [receive(minimumIncompleteLength:maximumLength:completion:)](<receive(minimumincompletelength_maximumlength_completion_).md>) — Schedules a single receive completion handler, with a range indicating how many bytes the handler can receive at one time.
- [receiveMessage(completion:)](<receivemessage(completion_).md>) — Schedules a single receive completion handler for a complete message, as opposed to a range of bytes.
- [ContentContext](contentcontext.md) — An object that represents a message to send or receive, containing protocol metadata and send properties.
- [maximumDatagramSize](maximumdatagramsize.md) — The maximum size of a datagram message that can be sent on a connection.
