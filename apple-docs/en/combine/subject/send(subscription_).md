---
title: 'send(subscription:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subject/send(subscription:)'
source_url: 'https://developer.apple.com/documentation/combine/subject/send(subscription:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subject/send%28subscription%3A%29.json'
content_hash: 'sha256:10e921ad30b370ed'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subject](../subject.md)

# send(subscription:)

<sub>Instance Method</sub>

Sends a subscription to the subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func send(subscription: any Subscription)
```

## Parameters

- `subscription` — The subscription instance through which the subscriber can request elements.

## Discussion

This call provides the [Subject](../subject.md) an opportunity to establish demand for any new upstream subscriptions.

## See Also

### Delivering life cycle events to subscribers

- [send(completion:)](<send(completion_).md>) — Sends a completion signal to the subscriber.
