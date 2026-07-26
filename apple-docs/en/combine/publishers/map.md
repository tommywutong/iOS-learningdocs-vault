---
title: Publishers.Map
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/map
source_url: 'https://developer.apple.com/documentation/combine/publishers/map'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/map.json'
content_hash: 'sha256:0e34b6e1646754bf'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Map

<sub>Structure</sub>

A publisher that transforms all elements from the upstream publisher with a provided closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Map<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a map publisher

- [init(upstream:transform:)](<map/init(upstream_transform_).md>) — Creates a publisher that transforms all elements from the upstream publisher with a provided closure.

### Mapping elements

- [map(_:)](<map/map(__).md>)
- [tryMap(_:)](<map/trymap(__).md>)

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](map/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](map/upstream.md) — The publisher from which this publisher receives elements.
- [transform](map/transform.md) — The closure that transforms elements from the upstream publisher.

## See Also

### Mapping elements

- [TryMap](trymap.md) — A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [MapError](maperror.md) — A publisher that converts any failure from the upstream publisher into a new error.
- [Scan](scan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [TryScan](tryscan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.
- [SetFailureType](setfailuretype.md) — A publisher that appears to send a specified failure type.
