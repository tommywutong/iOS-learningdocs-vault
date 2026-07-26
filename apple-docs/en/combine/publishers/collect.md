---
title: Publishers.Collect
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collect
source_url: 'https://developer.apple.com/documentation/combine/publishers/collect'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collect.json'
content_hash: 'sha256:5f60f25c0bd47419'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Collect

<sub>Structure</sub>

A publisher that buffers items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Collect<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a collect publisher

- [init(upstream:)](<collect/init(upstream_).md>) — Creates a publisher that buffers items.

### Declaring supporting types

- [Output](collect/output.md) — The kind of values published by this publisher.
- [Failure](collect/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](collect/upstream.md) — The publisher that this publisher receives elements from.

### Comparing publishers

- [==(_:_:)](<collect/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](collect/equatable-implementations.md)

## See Also

### Reducing elements

- [CollectByCount](collectbycount.md) — A publisher that buffers a maximum number of items.
- [CollectByTime](collectbytime.md) — A publisher that buffers and periodically publishes its items.
- [TimeGroupingStrategy](timegroupingstrategy.md) — A strategy for collecting received elements.
- [IgnoreOutput](ignoreoutput.md) — A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Reduce](reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [TryReduce](tryreduce.md) — A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
