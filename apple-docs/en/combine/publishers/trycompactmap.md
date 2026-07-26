---
title: Publishers.TryCompactMap
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycompactmap
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycompactmap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycompactmap.json'
content_hash: 'sha256:d30d5fa3d410ee9c'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryCompactMap

<sub>Structure</sub>

A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryCompactMap<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-compact-map Publisher

- [init(upstream:transform:)](<trycompactmap/init(upstream_transform_).md>)

### Mapping elements

- [compactMap(_:)](<trycompactmap/compactmap(__).md>)

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](trycompactmap/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trycompactmap/upstream.md) — The publisher from which this publisher receives elements.
- [transform](trycompactmap/transform.md) — An error-throwing closure that receives values from the upstream publisher and returns optional values.

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [CompactMap](compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [RemoveDuplicates](removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [TryRemoveDuplicates](tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceEmpty](replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
