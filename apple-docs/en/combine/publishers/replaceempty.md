---
title: Publishers.ReplaceEmpty
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/replaceempty
source_url: 'https://developer.apple.com/documentation/combine/publishers/replaceempty'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/replaceempty.json'
content_hash: 'sha256:4e9d531ed6853a4a'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.ReplaceEmpty

<sub>Structure</sub>

A publisher that replaces an empty stream with a provided element.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct ReplaceEmpty<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a replace empty publisher

- [init(upstream:output:)](<replaceempty/init(upstream_output_).md>) — Creates a publisher that replaces an empty stream with a provided element.

### Declaring supporting types

- [Output](replaceempty/output-swift.typealias.md) — The kind of values published by this publisher.
- [Output](replaceempty/output-swift.typealias.md) — The kind of values published by this publisher.
- [Failure](replaceempty/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](replaceempty/upstream.md) — The publisher from which this publisher receives elements.
- [output](replaceempty/output-swift.property.md) — The element to deliver when the upstream publisher finishes without delivering any elements.
- [output](replaceempty/output-swift.property.md) — The element to deliver when the upstream publisher finishes without delivering any elements.

### Comparing publishers

- [==(_:_:)](<replaceempty/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](replaceempty/equatable-implementations.md)

## See Also

### Filtering elements

- [Filter](filter.md) — A publisher that republishes all elements that match a provided closure.
- [TryFilter](tryfilter.md) — A publisher that republishes all elements that match a provided error-throwing closure.
- [CompactMap](compactmap.md) — A publisher that republishes all non-nil results of calling a closure with each received element.
- [TryCompactMap](trycompactmap.md) — A publisher that republishes all non-nil results of calling an error-throwing closure with each received element.
- [RemoveDuplicates](removeduplicates.md) — A publisher that publishes only elements that don’t match the previous element.
- [TryRemoveDuplicates](tryremoveduplicates.md) — A publisher that publishes only elements that don’t match the previous element, as evaluated by a provided error-throwing closure.
- [ReplaceError](replaceerror.md) — A publisher that replaces any errors in the stream with a provided element.
