---
title: 'receive(subscriber:)'
framework: Combine
symbol_kind: method
role: symbol
role_heading: Instance Method
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: '/documentation/combine/publisher/receive(subscriber:)'
source_url: 'https://developer.apple.com/documentation/combine/publisher/receive(subscriber:)'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/receive%28subscriber%3A%29.json'
content_hash: 'sha256:1e5a97dd85cd5420'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# receive(subscriber:)

<sub>Instance Method</sub>

Attaches the specified subscriber to this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func receive<S>(subscriber: S) where S : Subscriber, Self.Failure == S.Failure, Self.Output == S.Input
```

## Parameters

- `subscriber` — The subscriber to attach to this [Publisher](../publisher.md), after which it can receive values.

## Discussion

Implementations of [Publisher](../publisher.md) must implement this method.

The provided implementation of [subscribe(_:)](<subscribe(__)-4u8kn.md>)calls this method.

## See Also

### Working with subscribers

- [subscribe(_:)](<subscribe(__)-4u8kn.md>) — Attaches the specified subscriber to this publisher.
- [subscribe(_:)](<subscribe(__)-3fk20.md>) — Attaches the specified subject to this publisher.
