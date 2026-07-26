---
title: Publishers.Comparison
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/comparison
source_url: 'https://developer.apple.com/documentation/combine/publishers/comparison'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/comparison.json'
content_hash: 'sha256:10786d9fef8502fc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Comparison

<sub>Structure</sub>

A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Comparison<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a comparison publisher

- [init(upstream:areInIncreasingOrder:)](<comparison/init(upstream_areinincreasingorder_).md>) — Creates a publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item.

### Declaring supporting types

- [Output](comparison/output.md) — The kind of values published by this publisher.
- [Failure](comparison/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](comparison/upstream.md) — The publisher from which this publisher receives its elements.
- [areInIncreasingOrder](comparison/areinincreasingorder.md) — A closure that receives two elements and returns true if they are in increasing order.

## See Also

### Applying mathematical operations on elements

- [Count](count.md) — A publisher that publishes the number of elements received from the upstream publisher.
- [TryComparison](trycomparison.md) — A publisher that republishes items from another publisher only if each new item is in increasing order from the previously-published item, and fails if the ordering logic throws an error.
