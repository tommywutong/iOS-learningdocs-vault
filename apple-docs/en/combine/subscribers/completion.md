---
title: Subscribers.Completion
framework: Combine
symbol_kind: enum
role: symbol
role_heading: Enumeration
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscribers/completion
source_url: 'https://developer.apple.com/documentation/combine/subscribers/completion'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/completion.json'
content_hash: 'sha256:2cf7dcbd27df5278'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscribers](../subscribers.md)

# Subscribers.Completion

<sub>Enumeration</sub>

A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
@frozen enum Completion<Failure> where Failure : Error
```

## Relationships

- **Conforms To**: [Copyable](../../swift/copyable.md), [Decodable](../../swift/decodable.md), [Encodable](../../swift/encodable.md), [Equatable](../../swift/equatable.md), [Escapable](../../swift/escapable.md), [Hashable](../../swift/hashable.md), [Sendable](../../swift/sendable.md), [SendableMetatype](../../swift/sendablemetatype.md)

## Topics

### Completion states

- [Subscribers.Completion.finished](completion/finished.md) — The publisher finished normally.
- [Subscribers.Completion.failure(_:)](<completion/failure(__).md>) — The publisher stopped publishing due to the indicated error.

## See Also

### Receiving life cycle events

- [receive(subscription:)](<../subscriber/receive(subscription_).md>) — Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [receive(completion:)](<../subscriber/receive(completion_).md>) — Tells the subscriber that the publisher has completed publishing, either normally or with an error.
