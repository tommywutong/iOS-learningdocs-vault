---
title: Publishers.Contains
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/contains
source_url: 'https://developer.apple.com/documentation/combine/publishers/contains'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/contains.json'
content_hash: 'sha256:c82f0e753a10d9bb'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.Contains

<sub>Structure</sub>

A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct Contains<Upstream> where Upstream : Publisher, Upstream.Output : Equatable
```

## Relationships

- **Conforms To**: [Equatable](../../swift/equatable.md), [Publisher](../publisher.md)

## Topics

### Creating a contains Publisher

- [init(upstream:output:)](<contains/init(upstream_output_).md>) — Creates a publisher that emits a Boolean value when it receives a specific element from its upstream publisher.

### Declaring supporting types

- [Output](contains/output-swift.typealias.md) — The kind of values published by this publisher.
- [Failure](contains/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](contains/upstream.md) — The publisher from which this publisher receives elements.
- [output](contains/output-swift.property.md) — The element to match in the upstream publisher.

### Comparing publishers

- [==(_:_:)](<contains/==(____).md>) — Returns a Boolean value that indicates whether two publishers are equivalent.

### Default Implementations

- [Equatable Implementations](contains/equatable-implementations.md)

## See Also

### Applying matching criteria to elements

- [ContainsWhere](containswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [TryContainsWhere](trycontainswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [AllSatisfy](allsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [TryAllSatisfy](tryallsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
