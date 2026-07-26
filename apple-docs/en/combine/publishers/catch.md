---
title: Publishers.Catch
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/catch
source_url: 'https://developer.apple.com/documentation/combine/publishers/catch'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/catch.json'
content_hash: 'sha256:52cc185d85670a4f'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Catch

<sub>Structure</sub>

A publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Catch<Upstream, NewPublisher> where Upstream : Publisher, NewPublisher : Publisher, Upstream.Output == NewPublisher.Output
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a catch publisher

- [init(upstream:handler:)](<catch/init(upstream_handler_).md>) — Creates a publisher that handles errors from an upstream publisher by replacing the failed publisher with another publisher.

### Declaring supporting types

- [Output](catch/output.md) — The kind of values published by this publisher.
- [Failure](catch/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](catch/upstream.md) — The publisher from which this publisher receives its elements.
- [handler](catch/handler.md) — A closure that accepts the upstream failure as input and returns a publisher to replace the upstream publisher.

## See Also

### Convenience publishers

- [Sequence](sequence.md) — A publisher that publishes a given sequence of elements.
