---
title: Publishers.MapKeyPath3
framework: Combine
symbol_kind: struct
role: symbol
role_heading: Structure
platforms: [iOS 13.0+, iPadOS 13.0+, Mac Catalyst 13.0+, macOS 10.15+, tvOS 13.0+, visionOS 1.0+, watchOS 6.0+]
languages: [swift]
beta: false
deprecated: false
doc_path: /documentation/combine/publishers/mapkeypath3
source_url: 'https://developer.apple.com/documentation/combine/publishers/mapkeypath3'
doc_json: 'https://developer.apple.com/tutorials/data/documentation/combine/publishers/mapkeypath3.json'
content_hash: 'sha256:6229adf6b6d12ecd'
translated: false
---

> Navigation: [Technologies](../../technologies.md) · [Combine](../../combine.md) · [Publishers](../publishers.md)

# Publishers.MapKeyPath3

<sub>Structure</sub>

A publisher that publishes the values of three key paths as a tuple.

<sub>iOS, iPadOS, Mac Catalyst, macOS, tvOS, visionOS, watchOS</sub>

```swift
struct MapKeyPath3<Upstream, Output0, Output1, Output2> where Upstream : Publisher
```

## Relationships

- **Conforms To**: [Publisher](../publisher.md)

## Topics

### Declaring supporting types

- [Output](mapkeypath3/output.md) — The kind of values published by this publisher.
- [Failure](mapkeypath3/failure.md) — The kind of errors this publisher might publish.

### Inspecting publisher properties

- [upstream](mapkeypath3/upstream.md) — The publisher from which this publisher receives elements.
- [keyPath0](mapkeypath3/keypath0.md) — The key path of a property to publish.
- [keyPath1](mapkeypath3/keypath1.md) — The key path of a second property to publish.
- [keyPath2](mapkeypath3/keypath2.md) — The key path of a third property to publish.

## See Also

### Identifying properties with key paths

- [MapKeyPath](mapkeypath.md) — A publisher that publishes the value of a key path.
- [MapKeyPath2](mapkeypath2.md) — A publisher that publishes the values of two key paths as a tuple.
