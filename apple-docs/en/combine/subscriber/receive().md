---
title: receive()
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/subscriber/receive()
source_url: 'https://developer.apple.com/documentation/combine/subscriber/receive()'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/subscriber/receive%28%29.json'
content_hash: 'sha256:cf5a8f32f111f7a8'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Subscriber](../subscriber.md)

# receive()

<sub>Instance Method</sub>

Tells the subscriber that a publisher of void elements is ready to receive further requests.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive() -> Subscribers.Demand
```

## Return Value

A [Demand](../subscribers/demand.md) instance indicating how many more elements the subscriber expects to receive.

## Discussion

Use `Void` inputs and outputs when you want to signal that an event has occurred, but don’t need to send the event itself.

## See Also

### Receiving elements

- [receive(_:)](<receive(__).md>) — Tells the subscriber that the publisher has produced an element.
