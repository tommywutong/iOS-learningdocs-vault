---
title: Publishers.Count
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/count
source_url: 'https://developer.apple.com/documentation/combine/publishers/count'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/count.json'
content_hash: 'sha256:ee54a6200d42fadf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Count

<sub>Structure</sub>

A publisher that publishes the number of elements received from the upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Count<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a count Publisher

- [init(upstream:)](<count/init(upstream_).md>) — Creates a publisher that publishes the number of elements received from the upstream publisher.

### Declaring supporting types

- [Output](count/output.md) — The kind of values published by this publisher.
- [Failure](count/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](count/upstream.md) — The publisher from which this publisher receives elements.

### Comparing publishers

- [==(_:_:)](<count/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent. /// - Parameters:

### Default Implementations

- [Equatable Implementations](count/equatable-implementations.md)

## See Also

### Applying mathematical operations on elements

- [Comparison](comparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
- [TryComparison](trycomparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.
