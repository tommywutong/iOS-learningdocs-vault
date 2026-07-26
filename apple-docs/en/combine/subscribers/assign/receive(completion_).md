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
doc_path: '/documentation/combine/subscribers/assign/receive(completion:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign/receive(completion:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign/receive%28completion%3A%29.json'
content_hash: 'sha256:75708113c8a803c8'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Assign](../assign.md)

# receive(completion:)

<sub>Instance Method</sub>

Tells the subscriber that the publisher has completed publishing, either normally or with an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func receive(completion: Subscribers.Completion<Never>)
```

## Parameters

- `completion` — A [Completion](../completion.md) case indicating whether publishing completed normally or with an error.

## See Also

### Receiving life cycle events

- [receive(subscription:)](<receive(subscription_).md>) — Tells the subscriber that it has successfully subscribed to the publisher and may request items.
