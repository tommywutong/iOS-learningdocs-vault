---
title: Publishers.TryRemoveDuplicates
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryremoveduplicates
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryremoveduplicates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryremoveduplicates.json'
content_hash: 'sha256:fca394f7dbb2d96d'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryRemoveDuplicates

<sub>Structure</sub>

A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryRemoveDuplicates<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-remove-duplicates publisher

- [init(upstream:predicate:)](<tryremoveduplicates/init(upstream_predicate_).md>) — Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.

### Inspecting publisher properties

- [upstream](tryremoveduplicates/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](tryremoveduplicates/predicate.md) — An error-throwing closure to evaluate whether two elements are equivalent, for purposes of filtering.

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [CompactMap](compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [TryCompactMap](trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [RemoveDuplicates](removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [ReplaceEmpty](replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
