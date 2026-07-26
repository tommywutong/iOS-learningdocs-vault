---
title: 'send(completion:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subject/send(completion:)'
source_url: 'https://developer.apple.com/documentation/combine/subject/send(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subject/send%28completion%3A%29.json'
content_hash: 'sha256:5eb6d6698f12934f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subject](../subject.md)

# send(completion:)

<sub>Instance Method</sub>

Sends a completion signal to the subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send(completion: Subscribers.Completion<Self.Failure>)
```

## Parameters

- `completion` — A `Completion` instance which indicates whether publishing has finished normally or failed with an error.

## See Also

### Delivering life cycle events to subscribers

- [send(subscription:)](<send(subscription_).md>) — Sends a subscription to the subscriber.
