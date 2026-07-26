---
title: 'subscribe(_:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/subscribe(_:)-4u8kn'
source_url: 'https://developer.apple.com/documentation/combine/publisher/subscribe(_:)-4u8kn'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/subscribe%28_%3A%29-4u8kn.json'
content_hash: 'sha256:fb1b63eea9ef7486'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# subscribe(_:)

<sub>Instance Method</sub>

Attaches the specified subscriber to this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subscribe<S>(_ subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

## Parameters

- `subscriber` — The subscriber to attach to this publisher. After attaching, the subscriber can start to receive values.

## Discussion

Always call this function instead of [receive(subscriber:)](<receive(subscriber_).md>). Adopters of [Publisher](../publisher.md) must implement [receive(subscriber:)](<receive(subscriber_).md>). The implementation of [subscribe(_:)](<subscribe(__)-4u8kn.md>) provided by [Publisher](../publisher.md) calls through to [receive(subscriber:)](<receive(subscriber_).md>).

## See Also

### Working with subscribers

- [receive(subscriber:)](<receive(subscriber_).md>) — Attaches the specified subscriber to this publisher.
- [subscribe(_:)](<subscribe(__)-3fk20.md>) — Attaches the specified subject to this publisher.
