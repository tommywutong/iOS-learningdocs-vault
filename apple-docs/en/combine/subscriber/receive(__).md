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
doc_path: '/documentation/combine/subscriber/receive(_:)'
source_url: 'https://developer.apple.com/documentation/combine/subscriber/receive(_:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber/receive%28_%3A%29.json'
content_hash: 'sha256:3b2ba54cd1f3a7ac'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriber](../subscriber.md)

# receive(_:)

<sub>Instance Method</sub>

Tells the subscriber that the publisher has produced an element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive(_ input: Self.Input) -> Subscribers.Demand
```

## Parameters

- `input` — The published element.

## Return Value

A `Subscribers.Demand` instance indicating how many more elements the subscriber expects to receive.

## See Also

### Receiving elements

- [receive()](<receive().md>) — Tells the subscriber that a publisher of void elements is ready to receive further requests.
