---
title: 'receive(completion:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscriber/receive(completion:)'
source_url: 'https://developer.apple.com/documentation/combine/subscriber/receive(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber/receive%28completion%3A%29.json'
content_hash: 'sha256:56a7ba4746a7ffba'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriber](../subscriber.md)

# receive(completion:)

<sub>Instance Method</sub>

Tells the subscriber that the publisher has completed publishing, either normally or with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive(completion: Subscribers.Completion<Self.Failure>)
```

## Parameters

- `completion` — A [Completion](../subscribers/completion.md) case indicating whether publishing completed normally or with an error.

## See Also

### Receiving life cycle events

- [receive(subscription:)](<receive(subscription_).md>) — Tells the subscriber that it has successfully subscribed to the publisher and may request items.
- [Completion](../subscribers/completion.md) — A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.
