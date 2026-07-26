---
title: 'receive(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/subscribers/assign/receive(_:)'
source_url: 'https://developer.apple.com/documentation/combine/subscribers/assign/receive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscribers/assign/receive%28_%3A%29.json'
content_hash: 'sha256:28ab960cb8a59fe5'
translated: false
---

> Navigation: [Technologies](../../../technologies.md) · [Combine](../../../combine.md) · [Subscribers](../../subscribers.md) · [Assign](../assign.md)

# receive(_:)

<sub>Instance Method</sub>

Tells the subscriber that the publisher has produced an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
final func receive(_ value: Input) -> Subscribers.Demand
```

## Discussion

A [Demand](../demand.md) instance indicating how many more elements the subscriber expects to receive.
