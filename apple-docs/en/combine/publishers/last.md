---
title: Publishers.Last
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/last
source_url: 'https://developer.apple.com/documentation/combine/publishers/last'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/last.json'
content_hash: 'sha256:0898e43e1acfb1cf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Last

<sub>Structure</sub>

A publisher that waits until after the stream finishes, and then publishes the last element of the stream.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Last<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a last publisher

- [init(upstream:)](<last/init(upstream_).md>) — Creates a publisher that waits until after the stream finishes and then publishes the last element of the stream.

### Declaring supporting types

- [Output](last/output.md) — The kind of values published by this publisher.
- [Failure](last/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](last/upstream.md) — The publisher from which this publisher receives elements.

### Comparing publishers

- [==(_:_:)](<last/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](last/equatable-implementations.md)

## See Also

### Selecting specific elements

- [First](first.md) — A publisher that publishes the first element of a stream, then finishes.
- [FirstWhere](firstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a predicate closure.
- [TryFirstWhere](tryfirstwhere.md) — A publisher that only publishes the first element of a stream to satisfy a throwing predicate closure.
- [LastWhere](lastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies a predicate closure.
- [TryLastWhere](trylastwhere.md) — A publisher that waits until after the stream finishes and then publishes the last element of the stream that satisfies an error-throwing predicate closure.
- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
