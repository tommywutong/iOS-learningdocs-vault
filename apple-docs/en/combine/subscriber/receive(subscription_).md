---
title: 'receive(subscription:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscriber/receive(subscription:)'
source_url: 'https://developer.apple.com/documentation/combine/subscriber/receive(subscription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber/receive%28subscription%3A%29.json'
content_hash: 'sha256:e7f8251ad58c4db4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriber](../subscriber.md)

# receive(subscription:)

<sub>Instance Method</sub>

Tells the subscriber that it has successfully subscribed to the publisher and may request items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive(subscription: any Subscription)
```

## Parameters

- `subscription` — A subscription that represents the connection between publisher and subscriber.

## Discussion

Use the received [Subscription](../subscription.md) to request items from the publisher.

## See Also

### Receiving life cycle events

- [receive(completion:)](<receive(completion_).md>) — Tells the subscriber that the publisher has completed publishing, either normally or with an error.
- [Completion](../subscribers/completion.md) — A signal that a publisher doesn’t produce additional elements, either due to normal completion or an error.
