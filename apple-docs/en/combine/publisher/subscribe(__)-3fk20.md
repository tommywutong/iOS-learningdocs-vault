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
doc_path: '/documentation/combine/publisher/subscribe(_:)-3fk20'
source_url: 'https://developer.apple.com/documentation/combine/publisher/subscribe(_:)-3fk20'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publisher/subscribe%28_%3A%29-3fk20.json'
content_hash: 'sha256:0e3c8ad5dc6875e9'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publisher](../publisher.md)

# subscribe(_:)

<sub>Instance Method</sub>

Attaches the specified subject to this publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
func subscribe<S>(_ subject: S) -> AnyCancellable where S : Subject, Self.Failure == S.Failure, Self.Output == S.Output
```

## Parameters

- `subject` — The subject to attach to this publisher.

## See Also

### Working with subscribers

- [receive(subscriber:)](<receive(subscriber_).md>) — Attaches the specified subscriber to this publisher.
- [subscribe(_:)](<subscribe(__)-4u8kn.md>) — Attaches the specified subscriber to this publisher.
