---
title: Publishers.TryContainsWhere
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/trycontainswhere
source_url: 'https://developer.apple.com/documentation/combine/publishers/trycontainswhere'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/trycontainswhere.json'
content_hash: 'sha256:b332f66c9a49d975'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryContainsWhere

<sub>Structure</sub>

A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryContainsWhere<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-contains-where publisher

- [init(upstream:predicate:)](<trycontainswhere/init(upstream_predicate_).md>) — Creates a publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.

### Declaring supporting types

- [Output](trycontainswhere/output.md) — The kind of values published by this publisher.
- [Failure](trycontainswhere/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](trycontainswhere/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](trycontainswhere/predicate.md) — The error-throwing closure that determines whether this publisher should emit a Boolean true element.

## See Also

### Applying matching criteria to elements

- [Contains](contains.md) — A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [ContainsWhere](containswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [AllSatisfy](allsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
- [TryAllSatisfy](tryallsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
