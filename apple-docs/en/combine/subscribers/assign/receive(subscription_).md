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
doc_path: '/documentation/combine/subscribers/assign/receive(subscription:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign/receive(subscription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign/receive%28subscription%3A%29.json'
content_hash: 'sha256:734500bc7219e4bd'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Assign](../assign.md)

# receive(subscription:)

<sub>Instance Method</sub>

Tells the subscriber that it has successfully subscribed to the publisher and may request items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func receive(subscription: any Subscription)
```

## Parameters

- `subscription` — A subscription that represents the connection between publisher and subscriber.

## Discussion

Use the received [Subscription](../../subscription.md) to request items from the publisher.

## See Also

### Receiving life cycle events

- [receive(completion:)](<receive(completion_).md>) — Tells the subscriber that the publisher has completed publishing, either normally or with an error.
