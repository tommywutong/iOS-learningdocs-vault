---
title: Publishers.AllSatisfy
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/allsatisfy
source_url: 'https://developer.apple.com/documentation/combine/publishers/allsatisfy'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/allsatisfy.json'
content_hash: 'sha256:db670e8a9de988bc'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.AllSatisfy

<sub>Structure</sub>

A publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct AllSatisfy<Upstream> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating an all satisfy publisher

- [init(upstream:predicate:)](<allsatisfy/init(upstream_predicate_).md>) — Creates a publisher that publishes a single Boolean value that indicates whether all received elements pass a given predicate.

### Declaring supporting types

- [Output](allsatisfy/output.md) — The kind of values published by this publisher.
- [Failure](allsatisfy/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](allsatisfy/upstream.md) — The publisher from which this publisher receives elements.
- [predicate](allsatisfy/predicate.md) — A closure that evaluates each received element.

## See Also

### Applying matching criteria to elements

- [Contains](contains.md) — A publisher that emits a Boolean value when it receives a specific element from its upstream publisher.
- [ContainsWhere](containswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the predicate closure.
- [TryContainsWhere](trycontainswhere.md) — A publisher that emits a Boolean value upon receiving an element that satisfies the throwing predicate closure.
- [TryAllSatisfy](tryallsatisfy.md) — A publisher that publishes a single Boolean value that indicates whether all received elements pass a given error-throwing predicate.
