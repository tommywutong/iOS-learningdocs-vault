---
title: Publishers.TryComparison
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycomparison
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycomparison'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycomparison.json'
content_hash: 'sha256:f8a2867503d19015'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryComparison

<sub>Structure</sub>

A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryComparison<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-comparison publisher

- [init(upstream:areInIncreasingOrder:)](<trycomparison/init(upstream_areinincreasingorder_).md>) — Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.

### Declaring supporting types

- [Output](trycomparison/output.md) — The kind of values published by this publisher.
- [Failure](trycomparison/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trycomparison/upstream.md) — The publisher from which this publisher receives its elements.
- [areInIncreasingOrder](trycomparison/areinincreasingorder.md) — A closure that receives two elements and returns true if they are in increasing order.

## See Also

### Applying mathematical operations on elements

- [Count](count.md) — A publisher that publishes the number of elements received from the upstream publisher.
- [Comparison](comparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.
