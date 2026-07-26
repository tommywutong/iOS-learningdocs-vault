---
title: Publishers.FlatMap
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/flatmap
source_url: 'https://developer.apple.com/documentation/combine/publishers/flatmap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/flatmap.json'
content_hash: 'sha256:ded869c3809d6348'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.FlatMap

<sub>Structure</sub>

A publisher that transforms elements from an upstream publisher into a new publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct FlatMap<NewPublisher, Upstream> where NewPublisher : Publisher, Upstream : Publisher, NewPublisher.Failure == Upstream.Failure
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a flat map Publisher

- [init(upstream:maxPublishers:transform:)](<flatmap/init(upstream_maxpublishers_transform_).md>) — Creates a publisher that transforms elements from an upstream publisher into a new publisher.

### Declaring supporting types

- [Output](flatmap/output.md) — The kind of values published by this publisher.
- [Failure](flatmap/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](flatmap/upstream.md) — The publisher from which this publisher receives elements.
- [maxPublishers](flatmap/maxpublishers.md) — The maximum number of concurrent publisher subscriptions
- [transform](flatmap/transform.md) — A closure that takes an element as a parameter and returns a publisher that produces elements of that type.

## See Also

### Republishing elements by subscribing to new publishers

- [SwitchToLatest](switchtolatest.md) — A publisher that flattens nested publishers.
