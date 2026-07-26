---
title: Publishers.TryMap
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trymap
source_url: 'https://developer.apple.com/documentation/combine/publishers/trymap'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trymap.json'
content_hash: 'sha256:7217d228b3f64232'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryMap

<sub>Structure</sub>

A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryMap<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-map publisher

- [init(upstream:transform:)](<trymap/init(upstream_transform_).md>) — Creates a publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](trymap/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trymap/upstream.md) — The publisher from which this publisher receives elements.
- [transform](trymap/transform.md) — The error-throwing closure that transforms elements from the upstream publisher.

### Instance Methods

- [map(_:)](<trymap/map(__).md>)
- [tryMap(_:)](<trymap/trymap(__).md>)

## See Also

### Mapping elements

- [Map](map.md) — A publisher that transforms all elements from the upstream publisher with a provided closure.
- [MapError](maperror.md) — A publisher that converts any failure from the upstream publisher into a new error.
- [Scan](scan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [TryScan](tryscan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [SetFailureType](setfailuretype.md) — A publisher that appears to send a specified failure type.
