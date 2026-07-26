---
title: Publishers.TryFilter
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryfilter
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryfilter'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryfilter.json'
content_hash: 'sha256:c79f37f90908cf44'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryFilter

<sub>Structure</sub>

A publisher that republishes all elements that match a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryFilter<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-filter publisher

- [init(upstream:isIncluded:)](<tryfilter/init(upstream_isincluded_).md>) — Creates a publisher that republishes all elements that match a provided error-throwing closure.

### Filtering elements

- [filter(_:)](<tryfilter/filter(__).md>)
- [tryFilter(_:)](<tryfilter/tryfilter(__).md>)

### Declaring supporting types

- [Output](tryfilter/output.md) — The kind of values published by this publisher.
- [Failure](tryfilter/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](tryfilter/upstream.md) — The publisher from which this publisher receives elements.
- [isIncluded](tryfilter/isincluded.md) — An error-throwing closure that indicates whether this filter should republish an element.

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [CompactMap](compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [TryCompactMap](trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [RemoveDuplicates](removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [TryRemoveDuplicates](tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceEmpty](replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
