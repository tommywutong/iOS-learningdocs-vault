---
title: 'request(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscription/request(_:)'
source_url: 'https://developer.apple.com/documentation/combine/subscription/request(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscription/request%28_%3A%29.json'
content_hash: 'sha256:37a548fc76a29590'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscription](../subscription.md)

# request(_:)

<sub>Instance Method</sub>

Tells a publisher that it may send more values to the subscriber.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func request(_ demand: Subscribers.Demand)
```

## See Also

### Requesting elements

- [Demand](../subscribers/demand.md) — A requested number of items, sent to a publisher from a subscriber through the subscription.
