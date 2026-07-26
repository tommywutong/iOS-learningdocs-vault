---
title: Publishers.CompactMap
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/compactmap
source_url: 'https://developer.apple.com/documentation/combine/publishers/compactmap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/compactmap.json'
content_hash: 'sha256:c359db287a844d88'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.CompactMap

<sub>Structure</sub>

A publisher that republishes all non-nil results of calling a closure with each received element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct CompactMap<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a compact map publisher

- [init(upstream:transform:)](<compactmap/init(upstream_transform_).md>) — Creates a publisher that republishes all non-`nil` results of calling a closure with each received element.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](compactmap/failure.md) — The kind of errors this publisher might publish.

### Mapping elements

- [map(_:)](<compactmap/map(__).md>)
- [compactMap(_:)](<compactmap/compactmap(__).md>)

### Inspecting publisher properties

- [upstream](compactmap/upstream.md) — The publisher from which this publisher receives elements.
- [transform](compactmap/transform.md) — A closure that receives values from the upstream publisher and returns optional values.

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [TryCompactMap](trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [RemoveDuplicates](removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [TryRemoveDuplicates](tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceEmpty](replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
