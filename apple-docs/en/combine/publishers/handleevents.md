---
title: Publishers.HandleEvents
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/handleevents
source_url: 'https://developer.apple.com/documentation/combine/publishers/handleevents'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/handleevents.json'
content_hash: 'sha256:abde90e44a0f3f5f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.HandleEvents

<sub>Structure</sub>

A publisher that performs the specified closures when publisher events occur.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct HandleEvents<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating an event-handling publisher

- [init(upstream:receiveSubscription:receiveOutput:receiveCompletion:receiveCancel:receiveRequest:)](<handleevents/init(upstream_receivesubscription_receiveoutput_receivecompletion_receivecancel_receiverequest_).md>) — Creates a publisher that performs the specified closures when publisher events occur.

### Declaring supporting types

- [Output](handleevents/output.md) — The kind of values published by this publisher.
- [Failure](handleevents/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](handleevents/upstream.md) — The publisher from which this publisher receives elements.
- [receiveSubscription](handleevents/receivesubscription.md) — A closure that executes when the publisher receives the subscription from the upstream publisher.
- [receiveOutput](handleevents/receiveoutput.md) — A closure that executes when the publisher receives a value from the upstream publisher.
- [receiveCompletion](handleevents/receivecompletion.md) — A closure that executes when the upstream publisher finishes normally or terminates with an error.
- [receiveCancel](handleevents/receivecancel.md) — A closure that executes when the downstream receiver cancels publishing.
- [receiveRequest](handleevents/receiverequest.md) — A closure that executes when the publisher receives a request for more elements.

## See Also

### Debugging

- [Breakpoint](breakpoint.md) — A publisher that raises a debugger signal when a provided closure needs to stop the process in the debugger.
- [Print](print.md) — A publisher that prints log messages for all publishing events, optionally prefixed with a given string.
