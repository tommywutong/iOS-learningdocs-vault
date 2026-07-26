---
title: Publishers.RemoveDuplicates
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/removeduplicates
source_url: 'https://developer.apple.com/documentation/combine/publishers/removeduplicates'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/removeduplicates.json'
content_hash: 'sha256:42fc5c263f4e411b'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.RemoveDuplicates

<sub>Structure</sub>

A publisher that publishes only elements that don’t match the previous element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct RemoveDuplicates<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a remove duplicates publisher

- [init(upstream:predicate:)](<removeduplicates/init(upstream_predicate_).md>) — Creates a publisher that publishes only elements that don’t match the previous element, as evaluated by a provided closure.

### Declaring supporting types

- [Output](removeduplicates/output.md) — The kind of values published by this publisher.
- [Failure](removeduplicates/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](removeduplicates/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](removeduplicates/predicate.md) — The predicate closure used to evaluate whether two elements are duplicates.

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [CompactMap](compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [TryCompactMap](trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [TryRemoveDuplicates](tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceEmpty](replaceempty.md) — A publisher that replaces an empty stream with a provided element.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
