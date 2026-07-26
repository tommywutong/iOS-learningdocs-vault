---
title: Publishers.TryAllSatisfy
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryallsatisfy
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryallsatisfy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryallsatisfy.json'
content_hash: 'sha256:ffad91278e518967'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryAllSatisfy

<sub>Structure</sub>

A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryAllSatisfy<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-all-satisfy publisher

- [init(upstream:predicate:)](<tryallsatisfy/init(upstream_predicate_).md>) — Returns a publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.

### Declaring supporting types

- [Output](tryallsatisfy/output.md) — The kind of values published by this publisher.
- [Failure](tryallsatisfy/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](tryallsatisfy/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](tryallsatisfy/predicate.md) — A closure that evaluates each received element.

## See Also

### Applying matching criteria to elements

- [Contains](contains.md) — A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [ContainsWhere](containswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [TryContainsWhere](trycontainswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [AllSatisfy](allsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.
