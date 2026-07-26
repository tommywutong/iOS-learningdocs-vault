---
title: Publishers.IgnoreOutput
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/ignoreoutput
source_url: 'https://developer.apple.com/documentation/combine/publishers/ignoreoutput'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/ignoreoutput.json'
content_hash: 'sha256:c09c45a2fa8ea1d2'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.IgnoreOutput

<sub>Structure</sub>

A publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finished or failed).

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct IgnoreOutput<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating an ignore output publisher

- [init(upstream:)](<ignoreoutput/init(upstream_).md>) — Creates a publisher that ignores all upstream elements, but passes along the upstream publisher’s completion state (finish or failed).

### Declaring supporting types

- [Output](ignoreoutput/output.md) — The kind of values published by this publisher.
- [Failure](ignoreoutput/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](ignoreoutput/upstream.md) — The publisher from which this publisher receives elements.

### Comparing publishers

- [==(_:_:)](<ignoreoutput/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](ignoreoutput/equatable-implementations.md)

## See Also

### Reducing elements

- [Collect](collect.md) — A publisher that buffers items.
- [CollectByCount](collectbycount.md) — A publisher that buffers a maximum number of items.
- [CollectByTime](collectbytime.md) — A publisher that buffers and periodically publishes its items.
- [TimeGroupingStrategy](timegroupingstrategy.md) — A strategy for collecting received elements.
- [Reduce](reduce.md) — A publisher that applies a closure to all received elements and produces an accumulated value when the upstream publisher finishes.
- [TryReduce](tryreduce.md) — A publisher that applies an error-throwing closure to all received elements and produces an accumulated value when the upstream publisher finishes.
