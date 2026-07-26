---
title: empty
framework: Combine
symbol_kind: property
role: symbol
role_heading: Type Property
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscriptions/empty
source_url: 'https://developer.apple.com/documentation/combine/subscriptions/empty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriptions/empty.json'
content_hash: 'sha256:88048f2c2ee4dcf0'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriptions](../subscriptions.md)

# empty

<sub>Type Property</sub>

Returns the “empty” subscription.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
static var empty: any Subscription { get }
```

## Discussion

Use the empty subscription when you need a [Subscription](../subscription.md) that ignores requests and cancellation.
