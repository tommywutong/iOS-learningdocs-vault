---
title: Publishers.TryScan
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/tryscan
source_url: 'https://developer.apple.com/documentation/combine/publishers/tryscan'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/tryscan.json'
content_hash: 'sha256:d7d06e0a2ff2f274'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.TryScan

<sub>Structure</sub>

A publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct TryScan<Upstream, Output> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Creating a try-scan publisher

- [init(upstream:initialResult:nextPartialResult:)](<tryscan/init(upstream_initialresult_nextpartialresult_).md>) — Creates a publisher that transforms elements from the upstream publisher by providing the current element to a failable closure along with the last value returned by the closure.

### Declaring supporting types

- [Output](output.md) — A publisher that publishes elements specified by a range in the sequence of published elements.
- [Failure](tryscan/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](tryscan/upstream.md) — The publisher that this publisher receives elements from.
- [initialResult](tryscan/initialresult.md) — The previous result returned by the `nextPartialResult` closure.
- [nextPartialResult](tryscan/nextpartialresult.md) — An error-throwing closure that takes as its arguments the previous value returned by the closure and the next element emitted from the upstream publisher.

## See Also

### Mapping elements

- [Map](map.md) — A publisher that transforms all elements from the upstream publisher with a provided closure.
- [TryMap](trymap.md) — A publisher that transforms all elements from the upstream publisher with a provided error-throwing closure.
- [MapError](maperror.md) — A publisher that converts any failure from the upstream publisher into a new error.
- [Scan](scan.md) — A publisher that transforms elements from the upstream publisher by providing the current element to a closure along with the last value returned by the closure.
- [SetFailureType](setfailuretype.md) — A publisher that appears to send a specified failure type.
