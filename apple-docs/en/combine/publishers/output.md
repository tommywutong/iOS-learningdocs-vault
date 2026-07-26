---
title: Publishers.Output
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift, swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/output
source_url: 'https://developer.apple.com/documentation/combine/publishers/output'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/output.json'
content_hash: 'sha256:9e51073140a637a4'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Output

<sub>Structure</sub>

A publisher that publishes elements specified by a range in the sequence of published elements.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Output<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating an output publisher

- [init(upstream:range:)](<output/init(upstream_range_).md>) — Creates a publisher that publishes elements specified by a range.

### Declaring supporting types

- [Output](output/output.md) — The kind of values published by this publisher.
- [Failure](output/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](output/upstream.md) — The publisher from which this publisher receives its elements.
- [range](output/range.md) — The range of elements to publish.

### Comparing publishers

- [==(_:_:)](<output/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](output/equatable-implementations.md)

## See Also

### Selecting specific elements

- [First](first.md) — A publisher that publishes the first element of a stream, then finishes.
- [FirstWhere](firstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [TryFirstWhere](tryfirstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [Last](last.md) — A publisher that waits until after the stream finishes, and then publishes the last element of the stream.
- [LastWhere](lastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [TryLastWhere](trylastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
