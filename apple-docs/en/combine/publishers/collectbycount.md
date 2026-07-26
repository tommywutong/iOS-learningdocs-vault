---
title: Publishers.CollectByCount
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/collectbycount
source_url: 'https://developer.apple.com/documentation/combine/publishers/collectbycount'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/collectbycount.json'
content_hash: 'sha256:3099e7e5e5fa168a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.CollectByCount

<sub>Structure</sub>

A publisher that buffers a maximum number of items.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CollectByCount<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a collect by count publisher

- [init(upstream:count:)](<collectbycount/init(upstream_count_).md>) — Creates a publisher that buffers a maximum number of items.

### Declaring supporting types

- [Output](collectbycount/output.md) — The kind of values published by this publisher.
- [Failure](collectbycount/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](collectbycount/upstream.md) — The publisher that this publisher receives elements from.
- [count](collectbycount/count.md) — The maximum number of received elements to buffer before publishing.

### Comparing publishers

- [==(_:_:)](<collectbycount/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](collectbycount/equatable-implementations.md)

## See Also

### Reducing elements

- [Collect](collect.md) — A publisher that buffers items.
- [CollectByTime](collectbytime.md) — A publisher that buffers and periodically publishes its items.
- [TimeGroupingStrategy](timegroupingstrategy.md) — A strategy for collecting received elements.
- [IgnoreOutput](ignoreoutput.md) — A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).
- [Reduce](reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [TryReduce](tryreduce.md) — A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
