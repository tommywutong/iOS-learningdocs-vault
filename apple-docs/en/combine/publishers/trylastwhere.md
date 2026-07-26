---
title: Publishers.TryLastWhere
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trylastwhere
source_url: 'https://developer.apple.com/documentation/combine/publishers/trylastwhere'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trylastwhere.json'
content_hash: 'sha256:06dba85be3d6a0bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryLastWhere

<sub>Structure</sub>

A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryLastWhere<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-last-where publisher

- [init(upstream:predicate:)](<trylastwhere/init(upstream_predicate_).md>) — Creates a publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.

### Declaring supporting types

- [Output](trylastwhere/output.md) — The kind of values published by this publisher.
- [Failure](trylastwhere/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trylastwhere/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](trylastwhere/predicate.md) — The error-throwing closure that determines whether to publish an element.

## See Also

### Selecting specific elements

- [First](first.md) — A publisher that publishes the first element of a stream, then finishes.
- [FirstWhere](firstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [TryFirstWhere](tryfirstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Last](last.md) — A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [LastWhere](lastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
